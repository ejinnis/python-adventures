# Python Adventures
A text-based adventure game for Computer Science class. Co-created by Elwood Innis, Lakshay Sharma and Erik Easter.

## Note on the metadata "API"
Systems like HP, inventory, dice, invalid options, and the game over screen are all pre-made in functions in the infrastucture code section of main.py. I'm calling this an API but it's really not. It's just functions. To list from inv() or hp() you must pass it a few options:

inv() requires char. id, list/edit, slot, item, qty
hp() requires char.id, list/edit, hp to add/remove
Dice requires the winReq, e.g. you must roll more than 10 to survive.
