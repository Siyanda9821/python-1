# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]

# # Task (map or filter)
# # Number letter in the name
# # [4, 8, 11, 15, 10, 4]

# length = map(lambda x: len(x), avengers)
# print(list(length))


# # Find longer names more the 10 letters name and stored in a new list

# # Output
# # ["Black widow", "Captain america"]

# res = filter(lambda x: len(x) > 10, avengers)
# print(list(res))


# # Task 1.3

# # Find the passed student's names (pass criteria >= 40)

# # Output
# # ["Lillian Ellis", "Debra Beard",  "Nettie Hancock" ]

scores = [
    {
        "marks": 32,
        "name": "Yvette Merritt",
    },
    {
        "marks": 57,
        "name": "Lillian Ellis",
    },
    {
        "marks": 22,
        "name": "Mccall Carter",
    },
    {
        "marks": 21,
        "name": "Pate Collier",
    },
    {
        "marks": 91,
        "name": "Debra Beard",
    },
    {
        "marks": 75,
        "name": "Nettie Hancock",
    },
    {
        "marks": 20,
        "name": "Hatfield Hodge",
    },
]

# mark = filter(lambda x: x["marks"] >= 40, scores)
# names_ = list(map(lambda x: x["name"], mark))

# print(list(names_))


# # ## Task 1.4
# # Find the topper

# # Clue:
# # Use sorted()

# # Output
# # Debra Beard

new = sorted(scores, reverse=True, key=lambda X: X["marks"])
print(new[0]["name"])
