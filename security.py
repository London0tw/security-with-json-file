import json
import random
import main
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


token = os.getenv("TOKEN")


def security_system():
    choose = input("Log / Reg: ").lower()
    if choose != "log" and choose != "reg":
        security_system()
        return
    name = input("Write your username: ")
    password = input("Write your password: ")
    if choose == "log":
        log(name=name, password=password)
    elif choose == "reg":
        if not check_username(name):
            security_system()
            return
        if not check_password(password):
            security_system()
            return
        password2 = input("Write your password again: ")
        if password2 != password:
            print("Пароли не совпадают!")
            security_system()
            return
        person_token = input("Write token: ")
        if person_token == token:
            reg(name=name, password=password)
        else:
            print("Wrong token!")
            security_system()


def reg(name, password):
    with open("data.json", "r") as f:
        data = json.load(f)
    ids = data["all_data"]
    while True:
        person_id = random.randint(100000000, 1000000000)
        for x in ids:
            if x == str(person_id):
                continue
        break
    data["name + pass"][str(person_id)] = {"name": name, "pass": password}
    data["all_id"].append(str(person_id))
    if not check_username(name):
        return
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("You have been registered!")
    main.main_prog(person_id=str(person_id))


def log(name, password):
    with open("data.json", "r") as f:
        data = json.load(f)
    ids = data["all_data"]
    for x in ids:
        if data["name + pass"][x]["name"] == name and data["name + pass"][x]["pass"] == password:
            print("You are logged in!")
            main.main_prog(person_id=str(x))
            return
    print("Wrong username or password")
    security_system()


def check_username(username):
    with open("data.json", "r") as f:
        data = json.load(f)
    ids = data["all_data"]
    a = 0
    b = 0
    c = 0
    for x in ids:
        if data["name + pass"][x]["name"] == username:
            a += 1
    if a == 1:
        b += 1
        print(f"Username {username} is not avaliable!!")
    if len(username) < 4:
        b += 1
        print("Your username too short!")
    for x in username:
        if x.lower() in "qwertyuiopasdfghjklzxcvbnm1234567890!-_":
            c += 1
    if c != len(username):
        b += 1
        print('Username must have "a-z" "1-9" "!" only!')
    if b == 0:
        return True


def check_password(password):
    a = 0
    b = 0
    c = 0
    if len(password) < 4:
        b += 1
        print("Your password too short!")
    for x in password:
        if x.lower() in "qwertyuiopasdfghjklzxcvbnm":
            a += 1
        elif x.lower() in "1234567890":
            c += 1
    if a == 0 or c == 0:
        b += 1
        print("Password must contain a-z 1-9!")
    if b == 0:
        return True
