word = input("Enter a noun: ")
if word.endswith(("s", "x", "z", "ch", "sh")):
    plural = word + "es"
elif word.endswith("y") and word[-2].lower() not in "aeiou":
    plural = word[:-1] + "ies"
else:
    plural = word + "s"
print("Plural Form:", plural)



Output :
Enter a noun: edith
Plural Form: ediths
