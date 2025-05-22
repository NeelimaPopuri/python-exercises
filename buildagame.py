name = input("Hey type your Name!! ")
print("Hello " + name + " Welcome to the gaming zone")

should_we_play = input("Do you wanna play this game(yes/no)? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play the game..")
    direction = input("Do you wanna turn Left/right? ").lower()

    if direction == "right":
        print("Oops! When Nothing went right.. maybe you should've picked left! Game over, but thanks for playing!!")
    elif direction == "left":
        choose = input(
            "You found the ladder and reached the Intermodal terminal. Do you wanna choose seaport/aero ? ")
        if choose == "seaport":
            print(
                "Oopsie! So sorry.. you picked a sinking ship goes glub glub!!--but thanks for Playing!!.. ")
        else:
            print("You won the game!! You've come so far!!....")
    else:
        print(" Sorry not a valid direction. You die.")
else:
    print("We are not playing.")
