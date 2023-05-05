import zipfile

def create_zip_file(file_objects, output_path):

    """
    This function can be used by any function which wants to return multiple files.

    The function accepts file objects and creates a single zip file for the same.
    """
    with zipfile.ZipFile(output_path, 'w') as zip_file:
        for file_obj in file_objects:
            filename = file_obj.name
            zip_file.write(filename, arcname=filename)
