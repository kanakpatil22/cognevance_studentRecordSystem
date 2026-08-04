# Student Record Management System

A menu-driven Python application to manage student records using file handling and core programming concepts. This project is submitted as part of Cognevance Technologies' Python Programming - Level 1 (Easy) project.

## Project Overview

This application allows users to add, view, update, delete, and search student records, along with generating a basic performance report (average marks, topper, pass/fail count). All data is stored persistently in a JSON file, so records remain saved even after the program is closed.

## Features

- Add new student records (Roll No, Name, Marks)
- View all student records in a formatted table
- Update existing student details
- Delete a student record (with confirmation)
- Search for a student by Roll No
- Generate a performance report (average marks, topper, pass/fail count)
- Input validation and exception handling (empty fields, invalid marks, duplicate roll numbers, etc.)

## Modules Used

- `os` – to check if the data file exists
- `json` – to read and write student data in JSON format

Both are built-in Python modules; no external installation is required.

## Project Structure