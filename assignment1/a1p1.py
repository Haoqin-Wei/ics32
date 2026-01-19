from pathlib import Path

def main():
    while True:
        user_input = input().strip()
        shit = user_input.split()

        if len(shit) == 0:
            continue

        command = shit[0]

        if command == "Q":
            break
        elif command == "L":
            print("Got L command")
            if len(shit) < 2:
                print("missing directory!")
                continue

            the_path = Path(shit[1])

            if not the_path.exists():
                print("ERROR: Directory does not exist")
                continue

            if not the_path.is_dir():
                print("ERROR: Not a directory")
                continue

            recursive = ("-r" in shit)
            files_only = ("-f" in shit)

            list_one_dir(the_path, recursive, files_only)

        else:
            print("ERROR: Unknown command")

def list_one_dir(the_path: Path, recursive: bool, files_only: bool):
    list_dict = the_path.iterdir()
    files = []
    dirs = []

    for items in list_dict:
        if items.is_file():
            files.append(items)
        elif items.is_dir():
            dirs.append(items)
            
    for f in files:
        print(str(f))

    if not files_only:
        for d in dirs:
            print(str(d))

            
    if recursive:
        for d in dirs:
            list_one_dir(d, True, files_only)


if __name__ == "__main__":
    main()