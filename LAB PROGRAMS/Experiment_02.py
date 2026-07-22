string = input("Enter the String : ")
state = "q0"
for ch in string:
    if state == "q0":
        if ch == "a":
            state = "q1"
        else :
            state = "q0"

    elif state == "q1":
        if ch == "a":
            state = "q1"
        else:
            state = "q2"
    elif state == "q2":
        if ch == "a":
            state = "q1"
        else:
            state = "q0"

if state == "q2":
    print("Accepted : String Ends with ab")
else:
    print("Rejected")


Output:
Enter the String : aaabaab
Accepted : String Ends with ab
