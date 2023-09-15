import re
file = open("password.txt", "r")
passwords_array = [line.rstrip() for line in file]
password_policy = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]|[_]).{8,}$"

for password in passwords_array:
    try:
        match = re.search(password_policy, password)
        print(match[0])
    except:
        pass

