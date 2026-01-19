from pathlib import Path

def main():
    while True:
        user_input = input().strip()

        shit = user_input.split()
        command = shit[0]

        if command == "Q":
            break
        elif command == "L":
            print("Got L command")
        else:
            print("ERROR: Unknown command")
        


def list_dict():
    dict = Path.iterdir()
    print(dict)





if __name__ == "__main__":
    main()