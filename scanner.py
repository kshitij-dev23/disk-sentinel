import os 

def scan_directory(path):

    if not os.path.exists(path):
        return None
    
    if not os.path.isdir(path):
        return None
    
    #continue normally

    files= os.walk(path)
    file_count=0
    folder_count=0

    for item in files:
        full_path= os.path.join(path,item)
        if os.path.isfile(full_path):
            file_count+=1
        if os.path.isdir(full_path):
            folder_count+=1

    largest_size = -1
    largest_file = None
    size_gb = 0

    for root, dirs, files in os.walk(path, onerror=lambda e: None):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(full_path)
            except PermissionError:
                continue

            if file_size > largest_size:
                largest_size = file_size
                largest_file = full_path
                    
        if largest_size > 0:
            size_gb = largest_size / (1024**3)

    return file_count, folder_count, largest_file, size_gb