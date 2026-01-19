"""
/helpers/validator.py: input validation helper functions.
"""

from datetime import datetime

# ALLOWABLE VALUES FOR PRIORITIES AND STATUSES
ALLOWED_PRIORITIES = {"Low", "Medium", "High"}
ALLOWED_STATUSES = {"Pending", "In progress", "Completed"}


def clean_text(value):
    """
    cleans string input first.
    """
    if not value:
        return None
    return value.strip()


def parse_date(date_str):
    """
    Parse date string in YYYY-MM-DD format,and then return date object or None.
    """
    if not date_str:
        return None

    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")


def validate_priority(priority):
    """
    function to validate task priority.
    """
    if priority not in ALLOWED_PRIORITIES:
        raise ValueError("Priority must be Low, Medium, or High")
    return priority


def validate_status(status):
    """
    function to validate task status.
    """
    if status not in ALLOWED_STATUSES:
        raise ValueError("Status must be Pending, In Progress, or Completed")
    return status
