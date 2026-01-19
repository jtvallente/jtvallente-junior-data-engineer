# Task Management App (CLI)

A simple command-line task manager built with Python and MySQL.

## Features
- Add, list, update, complete, and delete tasks
- Filter and sort tasks
- Persistent storage using MySQL
- Thread-safe DB writes (mutex lock in TaskManager)

## Requirements
- Python 3.x
- MySQL Server
- Python packages: mysql-connector-python, python-dotenv

## Setup

1) Install dependencies
pip install -r requirements.txt

2) Create a .env file in the project root (same folder as main.py)
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=root_password
DB_NAME=task_manager
DB_PORT=3306

3) Create database + table
Open MySQL and run:
SOURCE database_provider/schema.sql;

## Run the App
From the project root:
python3 main.py

## Notes
- Author: James Lourence T. Vallente