from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
Sky()

blocks = []

# Terrain Gen
for x in range(20):
    for z in range(20):
        block = Button(
            model='cube',
            texture='grass.png',
            color=color.white,
            position=(x, 0, z),
            parent=scene,
            origin_y=0.5
        )
        blocks.append(block)

# Put Blocks
def input(key):
    for block in blocks:
        if block.hovered:
            if key == 'left mouse down':
                blocks.remove(block)
                destroy(block)

            elif key == 'right mouse down':
                new_block = Button(
                    model='cube',
                    texture='grass.png',
                    color=color.white,
                    position=block.position + mouse.normal,
                    parent=scene,
                    origin_y=0.5
                )
                blocks.append(new_block)

app.run()
