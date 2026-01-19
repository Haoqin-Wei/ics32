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

def list_one_dir(the_path: Path, recursive: bool):
    list_dict = the_path.iterdir()
    files = []
    dirs = []
    for items in list_dict:
        if items.is_file():
            files.append(items)
        elif items.is_dir():
            dirs.append(items)
            
        for i in files:
                print(str(i))
        for p in dirs:
                print(str(p))
            
    if recursive:
        for d in dirs:
            list_one_dir(d, True)
    
    else:
         print("ERROR: Unknown command")
        


def list_dict():
    dict = Path.iterdir()
    print(dict)





if __name__ == "__main__":
    main()