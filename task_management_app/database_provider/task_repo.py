"""
/database_provider/task_repo.py: handles all database queries for all tasks (CRUD)
"""

from database_provider.db_connection import connection_estab


class TaskRepo:
    """
    Repository for tasks table using CRUD operations.
    """

    def fetch_tasks(self):
        """
        list of dict rows from the tasks table.
        """
        conn = connection_estab()
        if not conn:
            return []

        try:
            cur = conn.cursor(dictionary=True)
            cur.execute("""
                SELECT id, title, task_desc, due_date, task_priority, task_status, created_at
                FROM tasks
                ORDER BY created_at DESC
            """)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    def insert_task(self, task):
        """
        insert a task row and return the inserted id.
        """
        conn = connection_estab()
        if not conn:
            return None

        try:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO tasks (title, task_desc, due_date, task_priority, task_status)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                task.title,
                task.task_desc,
                task.due_date,
                task.task_priority,
                task.task_status
            ))
            conn.commit()
            return cur.lastrowid
        finally:
            cur.close()
            conn.close()

    def update_task(self, task_id, fields):
        """
        This will update a task by id using dict.Only updte the allowed collumn
        """
        allowed = {"title", "task_desc", "due_date", "task_priority", "task_status"}
        set_parts = []
        values = []

        for k, v in fields.items():
            if k in allowed:
                set_parts.append(f"{k}=%s")
                values.append(v)

        if not set_parts:
            return False

        values.append(task_id)
        sql = f"UPDATE tasks SET {', '.join(set_parts)} WHERE id=%s"

        conn = connection_estab()
        if not conn:
            return False

        try:
            cur = conn.cursor()
            cur.execute(sql, tuple(values))
            conn.commit()
            return cur.rowcount > 0
        finally:
            cur.close()
            conn.close()

    def delete_task(self, task_id):
        """
        deletee a task row by id.
        """
        conn = connection_estab()
        if not conn:
            return False

        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            cur.close()
            conn.close()