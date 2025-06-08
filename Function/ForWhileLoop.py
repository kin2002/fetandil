"""
For and While Loops
"""

my_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

x=0
while x<3:
    x += 1
    for i in my_list:
        if i == "Tuesday":
            print("_________")
        if i == "Thursday":
            print("_________")
            continue
        print(i)

