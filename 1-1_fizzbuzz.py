# 1-1 fizzbuzz
# If you reverse the order of the ifs, you can eliminate
# some `and` logic.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:  
        print("fizzbuzz")
    elif i % 3 == 0:  # only executes if the above condition wasn't hit
        print("fizz")
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

