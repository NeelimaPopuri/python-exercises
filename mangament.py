names = []
ages = []
emails = []

for i in range(3):
    print(i+1, "Input")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Emails: ")

    names.append(name)
    ages.append(age)
    emails.append(email)

print(names, ages, emails)
