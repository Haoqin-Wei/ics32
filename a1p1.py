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

            name_filter = None
            ext_filter = None

            if "-s" in shit:
                i = shit.index("-s")
                if i + 1 >= len(shit):
                    print("ERROR: Missing filename for -s")
                    continue
                name_filter = shit[i + 1]
                files_only = True

            if "-e" in shit:
                i = shit.index("-e")
                if i + 1 >= len(shit):
                    print("ERROR: Missing extension for -e")
                    continue
                ext_filter = shit[i + 1].lstrip(".")
                files_only = True

            list_one_dir(the_path, recursive, files_only, name_filter, ext_filter)

        else:
            print("ERROR: Unknown command")

def list_one_dir(the_path: Path, recursive: bool, files_only: bool, name_filter, ext_filter):
    list_dict = the_path.iterdir()
    files = []
    dirs = []

    for items in list_dict:
        if items.is_file():
            files.append(items)
        elif items.is_dir():
            dirs.append(items)
    
    files.sort(key=lambda p: p.name)
    dirs.sort(key=lambda p: p.name)
         
    for f in files:
        if name_filter is not None and f.name != name_filter:
            continue
        if ext_filter is not None and f.suffix.lower() != ("." + ext_filter.lower()):
            continue
        print(str(f))

    if not files_only:
        for d in dirs:
            print(str(d))

    if recursive:
        for d in dirs:
            list_one_dir(d, True, files_only, name_filter, ext_filter)

if __name__ == "__main__":
    main()