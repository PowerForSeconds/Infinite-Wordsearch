import random, os
os.system("cls")

def clearscreen():
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            pass
        
location = [0, 0]

characters = ["A",
              "B",
              "C",
              "D",
              "E",
              "F",
              "G",
              "H",
              "I",
              "J",
              "K",
              "L",
              "M",
              "N",
              "O",
              "P",
              "Q",
              "R",
              "S",
              "T",
              "U",
              "V",
              "W",
              "X",
              "Y",
              "Z"]

while True:
    clearscreen()
    for y in range(10):
        for x in range(10):
            seed = round(((location[0] + x + 0.1) / (location[1] + y + 0.1)) * 93452647) * 7691524
            random.seed(seed)
            print(characters[random.randint(0, 25)], end="")
        print()
