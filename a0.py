#this is for assignment 0
#testing git functionality
string_1 = "+-+"
string_2 = "| |"
string_3 = "-+"

num = int(input("Enter a number: "))

for i in range(num):
    for j in range(num - 1):
        print(string_1)
        print(string_2)