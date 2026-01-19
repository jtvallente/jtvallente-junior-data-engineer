"""
/models/task.py: This store the model that represents a single task entity.
"""

from datetime import datetime

"""
Creating task object that represents a task record based on the DB schema.
"""
class Task:
    def __init__(
        self,
        title,
        task_desc=None,
        due_date=None,
        task_priority="Low",
        task_status="Pending",
        id=None,
        created_at=None
    ):
        if not title or not title.strip():
            raise ValueError("Error. Title cannot be empty. Please try again")

        self.id = id
        self.title = title.strip()
        self.task_desc = task_desc.strip() if task_desc else None
        self.due_date = due_date
        self.task_priority = task_priority
        self.task_status = task_status
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        """
        retrns a dict using db column names.
        """
        return {
            "id": self.id,
            "title": self.title,
            "task_desc": self.task_desc,
            "due_date": self.due_date,
            "task_priority": self.task_priority,
            "task_status": self.task_status,
            "created_at": self.created_at
        }

    def __str__(self):
        return (
            f"[{self.id}] {self.title} | "
            f"Priority: {self.task_priority} | "
            f"Status: {self.task_status} | "
            f"Due: {self.due_date}"
        )
