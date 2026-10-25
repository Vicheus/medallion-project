from ...settings import MINIO_HOSTS
from .settings import MEDIA_EXTENSIONS_FILE_TYPES
import uuid

import os


def media(dataset_code_name, filename, document_id, description=""):
    def get_file_type_based_on_extension(extension):
        file_type = MEDIA_EXTENSIONS_FILE_TYPES.get(extension)
        if file_type is None:
            print(f"""File type not found for extension: {extension}""")
        return file_type

    def get_file_extension(path):
        _, file_extension = os.path.splitext(path)
        if not file_extension:
            print(f"""File extension not found for file: {path}""")
        return file_extension.strip()

    if (not filename) or (not dataset_code_name) or (not document_id):
        return None

    file_extension = get_file_extension(filename)
    file_type = get_file_type_based_on_extension(file_extension)
    if (file_extension is None) or (file_type is None):
        print(
            f"""file extension {file_extension} or file type {file_type} is empty for: {filename}"""
        )
        return

    file_id = uuid.uuid4()
    formatted_filename = {
        "file_name": f"""{file_type}_{file_id}{file_extension}""",
        "raw_file_name": filename,
        "file_type": file_type,
        "url": f"""http://{MINIO_HOSTS}/{dataset_code_name}/{document_id}/{file_type}_{file_id}{file_extension}""",
        "description": description,
        "ds_internal_id": document_id,
    }
    if not formatted_filename:
        return

    return formatted_filename
