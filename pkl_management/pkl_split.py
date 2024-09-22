def split_file(file_path, chunk_size=50 * 1024 * 1024):
    with open(file_path, 'rb') as f:
        chunk_number = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            with open(f"{file_path}.part{chunk_number}", 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_number += 1