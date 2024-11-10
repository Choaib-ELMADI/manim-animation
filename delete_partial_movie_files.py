import os
import shutil


def delete_partial_movie_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "partial_movie_files" in dirnames:
            folder_to_delete = os.path.join(dirpath, "partial_movie_files")
            try:
                shutil.rmtree(folder_to_delete)
                print(f"Deleted: {folder_to_delete}")
            except Exception as e:
                print(f"Error deleting {folder_to_delete}: {e}")


root_directory = "C:\\Manim"

delete_partial_movie_files(root_directory)
