# 📚 Student Task Manager

A simple command-line **Student Task Manager built with Python** to help students manage their assignments and daily tasks.

This project was created to practice working with **functions, loops, lists, file handling, indexing, conditions, and user input** in a real project.

## ✨ Features

* ➕ **Add Tasks** — Add one or multiple tasks.
* 📋 **View Tasks** — View all saved tasks.
* 🗑️ **Delete Tasks** — Remove a task from the task list.
* ✅ **Mark as Completed** — Mark a task as completed.
* ⭐ **Set Priority** — Set a priority for a task.
* 📅 **Due Date** — Add a due date to each task.
* 🔍 **Search Tasks** — Search for a particular assignment or task.
* 💾 **File Storage** — Tasks are saved in a text file so they remain available after the program closes.

## 🛠️ Technologies Used

* **Python**
* File Handling
* Lists
* Loops
* Functions
* Conditional Statements
* String Methods
* `enumerate()`
* `os` module

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository.
3. Open the project folder in your terminal or VS Code.
4. Run the Python file.

```bash
python task_manager.py
```

The program will display a menu:

```text
Student Task Manager

1. Add_task
2. View_task
3. Delete task
4. Completed task
5. Set_priority
6. Due Date
7. Search_task
```

Choose an option by entering its number.

## 📁 File Storage

The application uses `task.txt` to store tasks.

Example:

```text
Complete CS301 assignment - Due: 5 October
Study Python - Completed
Practice Python - High
```

## 🎯 What I Learned

While building this project, I practiced:

* Reading and writing files
* Working with lists created from file data
* Using indexes to update specific tasks
* Using `enumerate()` to work with task numbers
* Searching using the `in` operator
* Updating existing data
* Using flags such as `found`
* Using loops to process multiple tasks
* Breaking a larger program into separate functions

## 🚀 Future Improvements

Possible improvements for future versions:

* Add a graphical user interface (GUI)
* Add automatic overdue-task detection
* Validate priority input (`Low`, `Medium`, `High`)
* Add better date validation
* Store tasks in a structured format such as JSON
* Add task IDs
* Improve error handling for invalid menu choices and task numbers

## 📌 Project Status

**Completed as a Python practice project.**

More features and improvements may be added as I continue learning Python.
