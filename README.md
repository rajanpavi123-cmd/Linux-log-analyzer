# Linux Log Analyzer (Python)

A simple Python tool that analyzes Linux log files and detects error messages for basic system troubleshooting.

## Features
- Reads Linux log files
- Detects error patterns using regular expressions
- Helps identify system issues quickly

## Technologies Used
- Python
- Regular Expressions (re module)
- Linux log files

## How to Run

1. Create a sample log file:

sample.log

Example log content:

INFO System started
WARNING Disk space low
ERROR Failed to start service

2. Run the script:

python log_analyzer.py

The script will display lines that contain errors.

## Use Case
This project demonstrates basic log analysis, which is commonly used in Linux system administration and backend troubleshooting.
