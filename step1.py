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
delay = 1/6
end = False


while not end:
    pew.show(world)
    pew.tick(delay)
