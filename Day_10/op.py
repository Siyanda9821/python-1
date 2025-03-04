# price = 200


# def ff():
#     # print(price)
#     price = 100
#     print(price)


# print(ff())


def f1():
    def f2():
        return "Hi"

    return f2()


print(f1())


add1 = lambda n1, n2: (n1 + n2)

print(add1(2, 4))
