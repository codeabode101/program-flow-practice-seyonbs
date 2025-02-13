mystical_creature = input("what do you see?(owl/troll/fairy)")
name = input("what is your name")
health = input("what is your health")
if mystical_creature == "owl":
    print(name,"gets wise advice,health +10")
elif mystical_creature == "troll":
    print("Roar!",name,"loses 25 health") 
elif mystical_creature == "fairy":
    print(name,"dances with fairies!health +20") 
print(f"{name}'s current health:{health}")        