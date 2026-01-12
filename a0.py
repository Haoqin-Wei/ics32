#this is for assignment 0
#testing git functionality
#Haoqin Wei

def block(num: int) -> str:
    if num == 0:
        return ""
    list1 = ["+-+", "| |", "+-+"]
    for i in range(1, num):
        space = "  " * i
        list1[-1] = list1[-1] + "-+"
        list1.append(f"{space}| |")
        list1.append(f"{space}+-+")

    return "\n".join(list1)
def main():
    n = int(input())
    print(block(n))

if __name__ == "__main__":
    main()