import os

def scan_directory(path):

    if not os.path.exists(path):
        return None

    if not os.path.isdir(path):
        return None

    file_count = 0
    folder_count = 0
    largest_size = -1
    largest_file = None

    for root, dirs, files in os.walk(path, onerror=lambda e: None):
        folder_count += len(dirs)
        file_count += len(files)

        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
            except PermissionError:
                continue

            if size > largest_size:
                largest_size = size
                largest_file = full_path

    size_gb = largest_size / (1024**3) if largest_size > 0 else 0

    return file_count, folder_count, largest_file, size_gb