command = ""
while "true":
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
