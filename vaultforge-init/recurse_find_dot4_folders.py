import os

def find_dot4_folders(start_path):
    dot4_paths = []

    for root, dirs, files in os.walk(start_path):
        if ".4" in dirs:
            dot4_path = os.path.join(root, ".4")
            dot4_paths.append(dot4_path)

            # stop os.walk from going inside this .4 folder
            dirs.remove(".4")

    return dot4_paths