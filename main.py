# deal with numbers using loop

print("\n== Counting numbers using loop ==")
print("1.Count number from zero up to user-input number")
print("2.Count number from user-input start and finish point")
print("3.Count number from user-input start and finish point with step how to count it")
print("4.Display word/s, character by character")
print("E - Exit")
choice = input("Option: ")

while choice != "E" and choice != "e":
    if choice == "1":
        st = int(input("\ninput a number to stop the counting: "))
        for i in range(st):
            print(i+1)
    elif choice == "2":
        sr = int(input("\ninput a number to start the counting: "))
        fh = int(input("input a number to finish the counting: "))
        for i in range(sr,fh+1):                                    # plus one to include the last number
            print(i)
    elif choice == "3":
        strt = int(input("\ninput a number to start the counting: "))
        fnh = int(input("input a number to finish the counting: "))
        step = int(input("input a step of how the counting should be counted: "))
        for i in range(strt,fnh+1,step):                            # plus one to inlude the finish point if possible
            print(i)
    elif choice == "4":
        word = input("\ninput word/s to be displayed one by one: ")
        for i in word:
            print(i)
    else:
        print("Invalid input")

    print("\n== Counting numbers using loop ==")
    print("1.Count number from zero up to user-input number")
    print("2.Count number from user-input start and finish point")
    print("3.Count number from user-input start and finish point with step how to count it")
    print("4.Display word/s, character by character")
    print("E - Exit")
    choice = input("Option: ")


if choice == "E" or choice == "e":
    print("Exit Program\nHave a good day")