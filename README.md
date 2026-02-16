# Disk Sentinel

Disk Sentinel is a lightweight Python CLI tool that analyzes directory usage.

It scans a given path and reports:
- Total number of folders
- Total number of files
- Largest file in the directory (recursive)
- Size of the largest file (in GB)

---

## 🚀 Features

- Recursive directory scanning using `os.walk`
- Permission-safe file handling
- Cross-platform path support
- Command-line interface using `argparse`
- Clean modular structure (scanner logic separated from CLI)

---

## 🛠 Requirements

- Python 3.8+
- No external dependencies

---

## ▶️ Usage

Run from project root:

```bash
python main.py <path>

---

## 📊 Example Output

```bash
python main.py .

--- Disk Sentinel Report ---
Folders: 15
Files: 102
Largest file: C:/Users/Kshitiz Mishra/Downloads/movie.mp4
Size (GB): 1.532

---

## Help

You can view CLI options using:

```bash
python main.py --help

usage: disk-sentinel [-h] path

Disk Sentinel - Analyze directory usage and detect largest files.

positional arguments:
  path        Path to the directory to scan

optional arguments:
  -h, --help  show this help message and exit

---

## 🎯 Purpose

Disk Sentinel was built to practice file system traversal, CLI tool design, and modular Python architecture.

The goal is to build and gradually improve a real-world utility tool rather than isolated practice scripts.

---

## 🧩 Technical Concepts Used

- os.walk for recursive directory traversal
- argparse for CLI interface
- Modular program design
- Exception handling (PermissionError)
- Path normalization for cross-platform compatibility

---

## 🗺 Roadmap

### Version 1.0
- Basic recursive scanning
- Largest file detection
- CLI interface

### Planned Enhancements
- Total directory size calculation
- Top N largest files
- File extension summary
- JSON export mode
- Packaging as installable CLI tool

---

## 👤 Author

Kshitiz Mishra  
B.S. Electronic Systems Student  
Interested in systems programming and cybersecurity tooling

---

⭐ If you find this useful, feel free to fork or improve it.