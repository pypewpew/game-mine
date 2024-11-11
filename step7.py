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
    world.pixel(x, y, 4)
    buttons = pew.keys()
    while pew.keys():
        pew.tick(delay)
    dx = 0
    dy = 0
    if buttons & pew.K_UP:
        dy = -1
    elif buttons & pew.K_DOWN:
        dy = 1
    elif buttons & pew.K_LEFT:
        dx = -1
    elif buttons & pew.K_RIGHT:
        dx = 1
    if (0 <= x + dx <= 7 and 0 <= y + dy <= 7 and
            world.pixel(x + dx, y + dy) != 2):
        world.pixel(x, y, 0)
        x += dx
        y += dy
        world.pixel(x, y, 4)
    elif (dy == 0 and 1 <= x + dx <= 6 and
            world.pixel(x + 2 * dx, y + 2 * dy) == 0):
        world.pixel(x, y, 0)
        x += dx
        y += dy
        world.pixel(x, y, 4)
        world.pixel(x + dx, y + dy, 2)
    gems = 0
    for row in range(7, -1, -1):
        for col in range(8):
            if world.pixel(col, row) == 3:
                gems += 1
            elif world.pixel(col, row) == 2:
                if world.pixel(col, row + 1) == 0:
                    world.pixel(col, row, 0)
                    world.pixel(col, row + 1, 2)
                    if world.pixel(col, row + 2) == 4:
                        end = True
                elif world.pixel(col, row + 1) in {2, 3}:
                    if (world.pixel(col + 1, row) == 0 and
                       world.pixel(col + 1, row + 1) == 0):
                            world.pixel(col, row, 0)
                            world.pixel(col + 1, row, 2)
                    elif (world.pixel(col - 1, row) == 0 and
                       world.pixel(col - 1, row + 1) == 0):
                            world.pixel(col, row, 0)
                            world.pixel(col - 1, row, 2)
    if gems == 0:
        end = True
    world.pixel(x, y, 3 if blink else 0)
    pew.show(world)
    pew.tick(delay)
    blink = not blink

import supervisor
supervisor.reload()
