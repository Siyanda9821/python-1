# # control flow

# number_ = 10
# if number_ <= 2:
#     print("use a bike")
# else:
#     print("car")
# #

name_1 = input("Please enter your name: ")
height_1 = input("Please enter your height: ")

name_2 = input("Please enter your name: ")
height_2 = input("Please enter your height: ")
difference = abs(float(height_1) - float(height_2))

if height_1 > height_2:
    print(name_1, name_2)
    print(height_1 + "cm", height_2 + "cm")
    print(name_1, "is taller than ", name_2, " by ", difference)
elif height_2 > height_1:
    print(name_2, name_1)
    print(height_2 + "cm", height_1 + "cm")
    print(name_2, "is taller than ", name_1, " by ", difference)

else:
    print("They are the same height")
