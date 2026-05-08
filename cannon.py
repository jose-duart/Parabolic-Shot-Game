from random import randrange
from turtle import (
    clear, goto, dot, update, setup,
    hideturtle, up, tracer, onscreenclick, ontimer, done
)
from freegames import vector
BALL_SPEED_FACTOR = 3
TARGET_SPEED = 1.5
GRAVITY = 0.75
TIMER_MS = 50
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / BALL_SPEED_FACTOR
        speed.y = (y + 200) / BALL_SPEED_FACTOR
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200
def draw():
    clear()
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    update()
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
    for target in targets:
        target.x -= TARGET_SPEED
    if inside(ball):
        speed.y -= GRAVITY
        ball.move(speed)
    remaining = []
    for target in targets:
        if abs(target - ball) <= 13:
            continue
        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)
        remaining.append(target)
    targets.clear()
    targets.extend(remaining)
    draw()
    ontimer(move, TIMER_MS)
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

