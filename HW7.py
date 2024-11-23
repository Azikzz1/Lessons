users = [
    ("Олег", 35),
    ("Егор", 33),
    ("Игорь", 32)
]

def get_user(index):
    if 1 <= index <= len(users):
        name, age = users[index - 1]
        print(f"{name} {age}")
    else:
        print("Неверный индекс")


get_user(2)
