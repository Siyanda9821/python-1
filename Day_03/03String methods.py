name = "John Wick"

print(name[0])

# if print(name.find("e")) == -1:
#     {print("It doesn't exists")}

print(f"{name[-4]}{name[-3]}{name[-2]}{name[-1]}")
print(name[slice(5, 9)])


# Slice operator
print(name[slice(5, 9)])

print(
    name[
        slice(
            5,
        )
    ]
)


print(name[5:9])


print(name.lower())


catchphrase = "  i am Groot   "
print(catchphrase.upper())
print(catchphrase.lower())
print(catchphrase.capitalize())
print(catchphrase.title())
print(catchphrase.swapcase())


quote = "wit*h greate power comes greate responsibility"

print(quote.strip("*"))

print(quote)


quote1 = "Dream is not something you see in sleep, Dream is something that does not let you sleep"

print(quote1.count("Dream"))


print(quote1.replace("Dream", "🛌☁️"))  # type: ignore

print(quote1.find("m"))  # type: ignore
