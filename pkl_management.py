import os

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


def reassemble_file(file_path, output_path):
    with open(output_path, 'wb') as output_file:
        chunk_number = 0
        while True:
            chunk_file_path = f"{file_path}.part{chunk_number}"
            if not os.path.exists(chunk_file_path):
                break
            with open(chunk_file_path, 'rb') as chunk_file:
                output_file.write(chunk_file.read())
            chunk_number += 1

#split_file('similarity.pkl')