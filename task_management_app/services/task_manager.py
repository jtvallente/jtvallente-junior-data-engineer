"""
/services/task_manager.py: TaskManager service. Handles business logic for tasks (DB persistence). Uses a mutex lock for thread-safe write operations.
"""

from models.task import Task
import threading
from helpers.validator import (
    clean_text,
    parse_date,
    validate_priority,
    validate_status
)


class TaskManager:

    def __init__(self, repo):
        if repo is None:
            raise ValueError("repo is required for DB mode")
        self.repo = repo
        self.lock = threading.Lock()

    def add_task(self, title, task_desc, due_date, task_priority, task_status):
        """
        Add a new task to DB and returns the created Task object.
        """
        title = clean_text(title)
        task_desc = clean_text(task_desc)

        if not title:
            raise ValueError("Error: Title cannot be empty")

        due_date = parse_date(due_date) if due_date else None
        task_priority = validate_priority(task_priority)
        task_status = validate_status(task_status)

        t = Task(
            id=None,
            title=title,
            task_desc=task_desc,
            due_date=due_date,
            task_priority=task_priority,
            task_status=task_status
        )

        with self.lock:
            new_id = self.repo.insert_task(t)

        if not new_id:
            raise Exception("Failed to insert task into database")

        #fetch the inserted task so created_at is accurate 
        return self.get_task(new_id)

    def list_tasks(self, status=None, priority=None, due_date=None, sort_by=None):
        """
        list tasks from db with filters and sorting. 
        """
        rows = self.repo.fetch_tasks()
        tasks = [self._row_to_task(r) for r in rows]

        if status:
            status = validate_status(status)
            tasks = [t for t in tasks if t.task_status == status]

        if priority:
            priority = validate_priority(priority)
            tasks = [t for t in tasks if t.task_priority == priority]

        if due_date:
            d = parse_date(due_date)
            tasks = [t for t in tasks if t.due_date == d]

        if sort_by:
            if sort_by == "due_date":
                tasks.sort(key=lambda x: (x.due_date is None, x.due_date))
            elif sort_by == "priority":
                order = {"Low": 1, "Medium": 2, "High": 3}
                tasks.sort(key=lambda x: order.get(x.task_priority, 0), reverse=True)
            elif sort_by == "status":
                order = {"Pending": 1, "In progress": 2, "Completed": 3}
                tasks.sort(key=lambda x: order.get(x.task_status, 0))
            elif sort_by == "created_at":
                tasks.sort(key=lambda x: x.created_at)

        return tasks

    def get_task(self, task_id):
        """
        get a single task from db --> fetch all then find.
        """
        rows = self.repo.fetch_tasks()
        for r in rows:
            if r["id"] == task_id:
                return self._row_to_task(r)
        return None

    def update_task(
        self,
        task_id,
        title=None,
        task_desc=None,
        due_date=None,
        task_priority=None,
        task_status=None
    ):
        """
        update a task in db and returns updated Task, or None if not found.
        """
        old = self.get_task(task_id)
        if not old:
            return None

        fields = {}

        if title is not None:
            title = clean_text(title)
            if not title:
                raise ValueError("Erro: Title cannot be empty")
            fields["title"] = title

        if task_desc is not None:
            fields["task_desc"] = clean_text(task_desc)

        if due_date is not None:
            fields["due_date"] = parse_date(due_date) if due_date else None

        if task_priority is not None:
            fields["task_priority"] = validate_priority(task_priority)

        if task_status is not None:
            fields["task_status"] = validate_status(task_status)

        if not fields:
            return old  #no updates added

        with self.lock:
            ok = self.repo.update_task(task_id, fields)

        if not ok:
            raise Exception("Failed to update task in database")

        return self.get_task(task_id)

    def complete_task(self, task_id):
        """
        Marks a task as Completed.
        """
        return self.update_task(task_id, task_status="Completed")

    def delete_task(self, task_id):
        """
        delete a task from DB; return True if deleted, False if not found
        """
        existing = self.get_task(task_id)
        if not existing:
            return False

        with self.lock:
            return bool(self.repo.delete_task(task_id))

    def _row_to_task(self, row):
        """
        Converts a DB row dict into a Task object (from Task class).
        """
        return Task(
            id=row["id"],
            title=row["title"],
            task_desc=row.get("task_desc"),
            due_date=row.get("due_date"),
            task_priority=row.get("task_priority"),
            task_status=row.get("task_status"),
            created_at=row.get("created_at")
        )