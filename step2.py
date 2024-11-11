import pew


pew.init()
world = pew.Pix.from_iter([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 2, 1, 2, 1, 1, 1],
    [1, 1, 2, 1, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 2, 3, 2],
    [1, 3, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
])
x = 0
y = 0
blink = True
delay = 1/6
end = False


while not end:
    world.pixel(x, y, 3 if blink else 0)
    pew.show(world)
    pew.tick(delay)
    blink = not blink
