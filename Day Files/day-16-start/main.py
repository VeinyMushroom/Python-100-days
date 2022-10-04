# import another_module
# print(another_module.another_variable)
#

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.hideturtle()
# timmy.color("#3d7364")
#
# for x in range(3):
#     timmy.forward(100)
#     timmy.lt(120)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", ])
# table.add_column("Pokemon Type", ["Electric", "Water", "Fire", ])
# table.align = "l"
#
# print(table)

list = []
prime = 0
not_prime = 0

num = int(input("Prime or not?: "))
for x in range(2, num):
    list.append(x)

for x in list:
    if num == 2:
        print("Prime")
    elif num % x == 0:
        not_prime = 1
    else:
        prime = 1

if not_prime == 1:
    print("Not prime")
elif prime == 1:
    print("Prime")

