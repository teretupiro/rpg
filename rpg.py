import time
import random


hello=input('Press \'Enter\' to start ')


feelings=input('\"Как ты себя чувствуешь?\" ')

feelings= input ('Ваше действие: хорошо-1 , плохо-2 ')
if feelings=='1':
    input('Это хорошо ')

#while enemy_hp >=0:


 #dps_player=random.randint(1,50)
 #dps_enemy=random.randint(1,25)
 #dfns_player=3
 #dfns_enemy=1




 #print("Вы нанесли урон гоблину",dps_player,'У него осталось',enemy_hp - dps_player + dfns_enemy,
       #"Вам нанесли урон",dps_enemy,'У вас осталось',player_hp - dps_enemy + dfns_player)
 #time.sleep(4)


 #print ('win')
def exit ():
    exit()




print('О!Монстр! ')
#monsters=input('Ваше действие: атака-1, защита-2  '  )
#if monsters== '1':
 #print('Вы убили монстра ' )
#elif monsters== '2':
 #   print('Вы зашитились' )
#else:
   #  print('Dead ')
    # print('Перезапустите игру ')
    # time.sleep(1000)

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
    enemy_health = 25
    your_health =50
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
print(" |Enemy |  Health: 25| ")
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


print('Перед вами появился город')
city=input('Ваше действие: войти-1 , не входить-2 ')
if city=='1':

 print('┈┈┈┈▅┈┈▕▀┈┈┈┈┈┈')
 print('┈┈┈▕┈┈┈╱╲▕▀┈┈┈┈')
 print('┈┈┈╱╲┈┈▏▕╱╲┈┈┈┈')
 print('┈┈┈▏▕╱╲▏▎▏▕╱╲┈▃')
 print('┈╱╲▏▎▅▂▅▂▏▎▏▎▏▏')
 print('▂▏▎▏▕╭┳┳╮▏┊▏▕╱╲')
 print('▏▏┊▏▎┃┊┊┃▏▎▏▎▏▕')
 print('▇▆▅▃▂┻┻┻┻▂▃▅▆▇▉')
 time.sleep(3)
elif city == '2':
 print('Ну пошли тогда')
 time.sleep(10)
print('Бандиты напали на вас ')

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
    enemy_health = 25
    your_health =50
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
print(" |Enemy |  Health: 25| ")
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



print('Вы видели как власти забирают последние деньги у торгвца')
money= input(' Ваши действия: вступиться -1 не вступаться-2  ')
if money =='1':
 print('Вас упекли в тюрьму ')
 jail = input('Попробывать сбежать-1 Отсидеть срок-2 ')
 if jail == '1':
     print('Вы сбежали ')
 elif jail == '2':
     time.slep(20)
     print('Вы вышли из тюрьмы ')



elif money=='2':
 print('Вы прошли мимо')




print('Нам надо зайти в магазин')
shop = input('Ваше действие: войти-1 ')
if shop=='1':

     print('Добро пожаловть в магазин Мечи и топоры')
     time.sleep(1)
     print('Вот мой асортимент товаров ')
     time.sleep(2)
     print('меч ,топор ,маг.палочка')
sword=input('Ваше действие: купить меч-1 , купить топор-2 , купить маг.палочку-3 ')
if sword =='1':
 print('Вы купили меч ')

 print("(+)~~~~~~~~~~~~~~~(+)")
 print(" | Damage:         | ")
 print(" | 7-15            | ")
 print(" | Speed:          | ")
 print(" | 7/10            | ")
 print(" | Critical Chance:| ")
 print(" | 64%             | ")
 print("(+)~~~~~~~~~~~~~~~(+)")
 print("  ")

elif sword=='2':
  print('Вы купили топор ')

  print("(+)~~~~~~~~~~~~~~~(+)")
  print(" | Damage:         | ")
  print(" | 7-20           | ")
  print(" | Speed:          | ")
  print(" | 3/10            | ")
  print(" | Critical Chance:| ")
  print(" | 64%             | ")
  print("(+)~~~~~~~~~~~~~~~(+)")
  print("  ")

elif sword=='3':
 print('Вы купили маг.палочку')

 print("(+)~~~~~~~~~~~~~~~(+)")
 print(" | Damage:         | ")
 print(" | 7-12            | ")
 print(" | Speed:          | ")
 print(" | 6/10            | ")
 print(" | Critical Chance:| ")
 print(" | 70%             | ")
 print("(+)~~~~~~~~~~~~~~~(+)")
 print("  ")

else:
   print('Пошли' )
time.sleep(10)
print('Нам надо купить лошадь')
horse = input('купить белую кобылу-1 купить черную кобылу-2  не покупать-Enter ')
if horse=='1':
    print('Вы купили белую лошадь')
elif horse =='2':
    print('Вы купили черную лошадь')
else:
    print('Пошли ')

    
print('')


