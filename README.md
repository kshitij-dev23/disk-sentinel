# 🛡 Disk Sentinel

Disk Sentinel is a lightweight Python CLI tool that analyzes a directory and provides:

- Total number of folders  
- Total number of files  
- Detection of the largest file  
- Size of the largest file (in GB)  

It is designed to be simple, fast, and dependency-free.

---

## 🚀 Features

- Recursive directory scanning using `os.walk`
- Largest file detection
- Graceful handling of permission errors
- Windows path normalization support
- CLI interface using `argparse`
- No external dependencies

---

## 🧰 Requirements

- Python 3.8+
- No third-party libraries required

---

## 📦 Project Structure

```
disk-sentinel/
│
├── main.py        # CLI entry point
├── scanner.py     # Core scanning logic
├── formatter.py   # (Optional future formatting module)
├── README.md
└── LICENSE
```

---

## ▶ Usage

Run from the project root directory:

```bash
python main.py <path>
```

### Example

```bash
python main.py "C:\Users\Kshitiz Mishra\Downloads"
```

---

## 📊 Example Output

```bash
python main.py .
```

```
--- Disk Sentinel Report ---
Folders: 15
Files: 102
Largest file: C:/Users/Kshitiz Mishra/Downloads/movie.mp4
Size (GB): 1.532
```

---

## ❓ Help

To view CLI options:

```bash
python main.py --help
```

Example output:

```
usage: disk-sentinel [-h] path

Disk Sentinel - Analyze directory usage and detect largest files.

positional arguments:
  path        Path to the directory to scan

optional arguments:
  -h, --help  show this help message and exit
```

---

## 🧠 How It Works

1. Validates directory path
2. Recursively walks through folders using `os.walk`
3. Counts files and directories
4. Tracks largest file by comparing file sizes
5. Handles permission errors safely

---

## ⚠ Error Handling

- Invalid paths return a safe error message
- Non-directory paths are rejected
- Permission errors are skipped automatically

---

## 🛠 Future Improvements

- Add size summary per subdirectory
- Add top N largest files
- Add export to JSON/CSV
- Add colored terminal output
- Package as installable CLI tool

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

Kshitiz Mishra  
Python Developer | Cybersecurity Enthusiast

---

⭐ If you found this project useful, consider starring the repository.