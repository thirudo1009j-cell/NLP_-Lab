import re
text = input("Enter the text : ")
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
phone = re.search(r'\b\d{10}\b', text)
if email:
    print("Email Found : ", email.group())
if phone:
    print("Phone number Found :", phone.group())



Output :
Enter the text : My email is siddarthagalla@gmail.com and my phone number is 8555066377
Email Found :  siddarthagalla@gmail.com
Phone number Found : 8555066377
