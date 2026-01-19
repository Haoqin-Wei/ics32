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

            the_path = shit[1]

            if not the_path.exists():
                print("ERROR: Directory does not exist")
                continue

            print(the_path)
    
        else:
            print("ERROR: Unknown command")
        


def list_dict():
    dict = Path.iterdir()
    print(dict)





if __name__ == "__main__":
    main()