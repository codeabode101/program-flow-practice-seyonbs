name = input("what is your warrior name?")
town = input("where does yor adventure begin? misty vale/stonehaven?")

health = input("what is your health?")
print(type(health))
print(f"{name} enters {town} tavern,ready for adventure")
if health == 100:
    print(name,"is at full health!let's roll dice")
else:
    print(name,"should visit alchemist")           