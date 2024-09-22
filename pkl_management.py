import os


def reassemble_file(file_path, output_path):
    with open(output_path, 'wb') as output_file:
        chunk_number = 0
        while True:
            chunk_file_path = f"{file_path}.part{chunk_number}"
            if not os.path.exists(chunk_file_path):
                break
            with open(chunk_file_path, 'rb') as chunk_file:
                chunk_data = chunk_file.read()
                output_file.write(chunk_data)
                print(f"Reassembled {chunk_file_path} ({len(chunk_data)} bytes)")
            chunk_number += 1
        print(f"Reassembly complete. Total chunks: {chunk_number}")