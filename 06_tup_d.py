a = [1, 22, 48, 16, "Bill"]
b = ["monday", True, "test"]
c = a+b
c = tuple(c)
# print(type(c))
# c = tuple(a+b)
# print(c[-1])

c = "Bill", 28, "Admin"
# print(type(c))

name, age, role = c
# print(name)
# print(age)
# print(role)


def get_user():
    name = "Tom"
    age = 22
    is_married = False
    return name, age, is_married


user = get_user()
print(user[0])              # Tom
print(user[1])              # 22
print(user[2])              # False

table = [
    {
        "vendor": "Samsung",
        "model": "S1",
        "price": 12000
    },
    {
        "vendor": "Nokia",
        "model": "SX5",
        "price": 15300
    },
    {
        "vendor": "Apple",
        "model": "I5",
        "price": 25000
    },
    {
        "vendor": "Samsung",
        "model": "S1",
        "price": 12000
    },
    {
        "vendor": "Sony",
        "model": "SX3",
        "price": 15000
    }
]
for item in table:
    print(item["vendor"], "\n")
    print(item["model"], "\n")
    print(item["price"], "\n")
    print("------------------")
