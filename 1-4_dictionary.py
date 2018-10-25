# 1-4 dictionary

demo_dict = {}
id_input = input("Enter ID: ")
demo_dict["ID"] = id_input
a = 0
while True:
    sex_input = input("M or F? ").upper()
    a += 1
    if sex_input == "M" or sex_input == "F":
        demo_dict["Sex"] = sex_input
        break
    elif a >= 3:
        demo_dict["Sex"] = "Unknown"
        print("You will never hold a data entry job with an attitude like that.")
        break
b = 0
while True:
    age_input = input("Age? ")
    b += 1
    if age_input.isnumeric():
        demo_dict["Age"] = age_input
        break
    elif b >= 3:
        demo_dict["Age"] = "Unknown"
        print("If you didn't know his age you should have just guessed.")
        break
print("\n")
for i in demo_dict:
    print(i + ": " + demo_dict[i])


# Python code often idiomatically uses the "beg forgiveness" approach 
# rather than the "ask permission" approach. So you'll see try/except used 
# instead of guarding "if" conditions

# try:
#     age = int(age_input) # raises exception if not numeric
#     demo_dict["Age"] = age
# except ValueError:
#     print("I was expecting a number. Try again.")
