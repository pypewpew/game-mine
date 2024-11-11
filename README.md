# Mine

## Rules

This is a simple digging and rock pushing game. The player controls a miner,
represented by a blinking pixel.

![Miner in a tunnel](mine1.png)

They can move up/down/left/right, digging a tunnel (represented with black
pixels). They can't dig through rocks (represented as red pixels), but they can
hold the rock if they stand below it, and they can push the rock left and right
if there is empty space on the other side.

![Miner holding a rock](mine2.png)

Unsupported rocks fall down. The objective of the game is to collect all treasures, represented as yellow pixels.

![Miner collecting treasure](mine3.png)

If at any point a falling rock hits the miner, it stuns them, and the game is over.

![Miner hit by a rock](mine4.png)

If two rocks stand on top of each other, they can be held in place by dirt or the miner.

![Miner holding a rock sideways](mine5.png)

However, if there is empty space next to the rocks, the top rock will slip to the side and fall down.

![Rock slipping to the side](mine6.png)

## Code
