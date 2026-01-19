-- /database_provider/db_schema.sql: This is the database schema of the task management app
-- create a database if it is not created yet (i.e. fresh start)

CREATE DATABASE IF NOT EXISTS task_manager;
USE task_manager;

-- TASKS MANAGER TABLE 
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR (256) NOT NULL,
    task_desc TEXT,
    due_date DATE,
    task_priority ENUM('Low', 'Medium', 'High') DEFAULT 'Low',
    task_status ENUM('Pending', 'In progress', 'Completed') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

)