import random
def end(enemy_health,your_health):
    if your_health > 0:
        print("  ")
        print("You slay the Enemy")
        print('Пошли')
    else:
        print("  ")
        print("You were slain...")
        print('Перезапустите игру')
        time.sleep(1000)

def your_first():
    enemy_health = 20
    your_health =20
    while your_health > 0 and enemy_health > 0:
        your_damage = random.choice(range(7,13))
        enemy_health -= your_damage
        if enemy_health <= 0:
            enemy_health = 0
            print(" ")
            print("You dealt " + str(your_damage) + " damage!")
            print("Enemy health:" + str(enemy_health))
            end(enemy_health,your_health)
        else:
            print(" ")
            print("You dealt " + str(your_damage) + " damage!")
            print("Enemy health:" + str(enemy_health))
            enemy_damage = random.choice(range(9, 21))
            your_health -= enemy_damage
            if your_health <= 0:
                your_health = 0
                print("  ")
                print("Enemy dealt " + str(enemy_damage) + " damage!")
                print("Your health:" + str(your_health))
                end(enemy_health,your_health)
            else:
                print("  ")
                print("Enemy dealt " + str(enemy_damage) + " damage!")
                print("Your health:" + str(your_health))
def enemy_first():
    enemy_health = 20
    your_health =20
    while your_health > 0 and enemy_health > 0:
     enemy_damage = random.choice(range(9, 21))
    your_health -= enemy_damage
    if your_health <= 0:
        your_health = 0
        print("  ")
        print("Ork dealt " + str(enemy_damage) + " damage!")
        print("Your health:" + str(your_health))
        end(enemy_health,your_health)
    else:
        print(" ")
        print("Enemy dealt " + str(enemy_damage) + " damage!")
        print("Your health:" + str(your_health))
        your_damage = random.choice(range(7,13))
        enemy_health -= your_damage
        if enemy_health <= 0:
            print(" ")
            print("You dealt " + str(your_damage) + " damage!")
            print("Enemy health:" + str(enemy_health))
            end(enemy_health,your_health)
        else:
            print("  ")
            print("You dealt " + str(your_damage) + " damage!")
            print("Enemy health:" + str(enemy_health))

print("(+)~~~~~~~~~~~~~~~(+)")
print(" | Damage:         | ")
print(" | 7-12            | ")
print(" | Speed:          | ")
print(" | 6/10            | ")
print(" | Critical Chance:| ")
print(" | 64%             | ")
print("(+)~~~~~~~~~~~~~~~(+)")
print("  ")
print("You encountered an Enemy")
enemy = "Enemy"
print("  ")
print("(+)~~~~~~~~~~~~~~~(+)")
print(" |Enemy |  Health: 20| ")
print(" |-----------------| ")
print(" |Damage:      9-20| ")
print(" |-----------------| ")
print(" |Speed:       2/10| ")
print(" |-----------------| ")
print(" |Crit Chance:  13%| ")
print("(+)~~~~~~~~~~~~~~~(+)")
print("You engage the Enemy in a battle!")
your_crit = (1, 65)
enemy_crits = (1, 13)
your_speed = 6
ork_speed = 2
if ork_speed >= your_speed:
    print("The " + enemy + " is faster, it attacks first!")
    enemy_first()
else:
    print("You're faster and get to attack first!")
    your_first()

