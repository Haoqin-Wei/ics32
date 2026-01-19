from pathlib import Path

def main():
    while True:
        user_input = input().strip()

        if user_input == "Q":
            break

def dict():
    dict = Path.iterdir()
    print(dict)





if __name__ == "__main__":
    main()