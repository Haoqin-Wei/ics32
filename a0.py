#this is for assignment 0
#testing git functionality
#Haoqin Wei

def block(num: int) -> str:
    if num == 0:
        return ""
    rows = ["+-+", "| |", "+-+"]
    result = []

def main():
    n = int(input("Enter the number of blocks: "))
    print(block(n))

if __name__ == "__main__":
    main()