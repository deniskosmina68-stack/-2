users = {
    "Taras": {
        "password": "1234",
        "grades": [12, 10, 8, 11, 4, 3]
    },
    "Denis": {
        "password": "qwerty",
        "grades": [9, 7, 12, 5, 3]
    },
    "Ivan": {
        "password": "1111",
        "grades": [6, 8, 4, 10, 12]
    },
    "Petro": {
        "password": "2222",
        "grades": [5, 7, 2, 11, 4]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("Задовільних оцінок (5-12):", satisfactory)
    print("Незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("Неправильний логін або пароль!")