import os

def find_dot4_folders(start_path):
    dot4_paths = []

    for root, dirs, files in os.walk(start_path):
        if ".4" in dirs:
            dot4_path = os.path.join(root, ".4")
            dot4_paths.append(dot4_path)

            # Prevent scanning inside the .4 folder itself
            dirs.remove(".4")

    return dot4_paths


def read_see_me(dot4_path):
    see_me_file = os.path.join(dot4_path, "see-me.txt")

    if os.path.exists(see_me_file):
        with open(see_me_file, "r", encoding="utf-8") as f:
            return f.read()

    return None


if __name__ == "__main__":
    start_dir = os.getcwd()

    print(f"Scanning for .4 folders in: {start_dir}\n")

    folders = find_dot4_folders(start_dir)

    if not folders:
        print("No .4 folders found.")
    else:
        for path in folders:
            print(f"Found: {path}")

            content = read_see_me(path)
            if content:
                print("  see-me.txt:")
                print("  ----------------")
                print(content.strip())
                print("  ----------------\n")
            else:
                print("  (no see-me.txt)\n")