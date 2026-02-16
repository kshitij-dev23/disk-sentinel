import argparse
import os
import sys
from scanner import scan_directory


def main():
    parser = argparse.ArgumentParser(
        prog="disk-sentinel",
        description="Disk Sentinel - Analyze directory usage and detect largest files."
    )

    parser.add_argument(
        "path",
        type=str,
        help="Path to the directory to scan"
    )

    args = parser.parse_args()

    # Normalize path (important for Windows + spaces + Unicode)
    path = os.path.abspath(os.path.expanduser(args.path))

    result = scan_directory(path)

    if result is None:
        print("Invalid directory path.")
        sys.exit(1)

    file_count, folder_count, largest_file, size_gb = result

    print("\n--- Disk Sentinel Report ---")
    print(f"Folders: {folder_count}")
    print(f"Files: {file_count}")

    if largest_file:
        print(f"Largest file: {largest_file}")
        print(f"Size (GB): {round(size_gb, 3)}")
    else:
        print("No files found.")


if __name__ == "__main__":
    main()