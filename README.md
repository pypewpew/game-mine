# Mine

## Rules

This is a simple digging and rock pushing game. The player controls a miner,
represented by a blinking pixel.

![mine1.png](Miner in a tunnel)

They can move up/down/left/right, digging a tunnel (represented with black
pixels). They can't dig through rocks (represented as red pixels), but they can
hold the rock if they stand below it, and they can push the rock left and right
if there is empty space on the other side.

![mine2.png](Miner holding a rock)

Unsupported rocks fall down. The objective of the game is to collect all treasures, represented as yellow pixels.

![mine3.png](Miner collecting treasure)

If at any point a falling rock hits the miner, it stuns them, and the game is over.

![mine4.png](Miner hit by a rock)

If two rocks stand on top of each other, they can be held in place by dirt or the miner.

![mine5.png](Miner holding a rock sideways)

However, if there is empty space next to the rocks, the top rock will slip to the side and fall down.

![mine6.png](Rock slipping to the side)

## Code
