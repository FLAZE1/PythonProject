from turtle import*
#пересечение-внутри
#обьединение- все
# m=20
# tracer(False)
# # forward()
# # left()
# # right()
# # back()
# # up(Поднимает перо)
# # down(Опускает)
# # goto(Координаты перемещения черепахи)
# # tracer(False) - рисунок без анимации
# # update() - обновление рисунка
# # done() - оставить на экране
# # screensize()-размер экрана
#
# screensize(5000,5000)
# left(90)
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(18*m)
#     right(90)
# up()
# forward(5*m)
# right(90)
# forward(7*m)
# left(90)
# down()
# for i in range(2):
#     forward(10*m)
#     right(90)
#     forward(7*m)
#     right(90)
#
# up()
# for x in range(7,15):
#     for y in range(11,16):
#         goto(x*m,y*m)
#         dot(3,'red')
#
#
#
#
# update()
# done()
#
# print(19*11+5*8)


# m=20
# tracer(False)
# screensize(5000,5000)
# left(90)
# for i in range(2):
#     forward(13*m)
#     right(90)
#     forward(20*m)
#     right(90)
# up()
# forward(8*m)
# right(90)
# back(3*m)
# left(90)
# down()
# for i in range(2):
#     forward(16*m)
#     right(90)
#     forward(8*m)
#     right(90)
# up()
#
# for x in range(-3,21):
#     for y in range(0,25):
#         goto(x*m,y*m)
#         dot(3,'red')
#
# print(14*21+17*9-36)
#
#
# update()
# done()


m=10
tracer(False)
screensize(5000,5000)
left(90)

for i in range(3):
    forward(7*m)
    right(90)
    forward(12*m)
    right(90)

up()

forward(4*m)
right(90)
forward(6*m)
left(90)

down()

for i in range(4):
    forward(83*m)
    right(90)
    forward(77*m)
    right(90)
up()

for x in range(-71,13):
    for y in range(-80,8):
        goto(x*m,y*m)
        dot(3,'red')




update()
done()