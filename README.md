cyoa-game
=========

My attempt into learning to code in Python, with a "Choose your own adventure" game program.
This has influence taken from Nethack, and choose your own adventure game books, this is only a learning exercise. 
Constructive criticsm welcomed, as this is primarily to improve my knowledge, including any style changes (as trying to keep to the PEP8 system). Please bear in mind this is a work in progress.

####Progress:####
- [x] Randomly generated maps, with random amounts of rooms, which have random sizes and positions.
- [x] Doors have been added on horizontal walls these are (currently) indicated by red squares.
- [x] Add doors to the vertical walls (currently) indicated by green squares
- [x] Prevent character from walking through the walls

####To do:####
- [ ] Add some sort of game element to it, whether it's creatures
- [ ] Clean up code some more (constantly trying to do this)

####Known bugs/defects####
- [x] Occasionally the game can't render a room as get's itself stuck in the generation loop (or so I suspect).
 * Sorted by preventing the loop iterate too many times, which can lead to number of rooms being low
