from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
player = FirstPersonController()
player.cursor.visible = False
Sky()
camera.fov = 75
camera.clip_plane_far = 1000

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

crosshair = Entity(
    parent=camera.ui,
    model='quad',
    color=color.gray,
    scale=(0.003, 0.03),
    position=(0, 0)
)
crosshair2 = Entity(
    parent=camera.ui,
    model='quad',
    color=color.gray,
    scale=(0.03, 0.003),
    position=(0, 0)
)

# Put Blocks
def input(key):
    for block in blocks:
        if block.hovered:
            if key == 'escape':
                application.quit()

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

def update():
    if player.y < -20:
        application.quit()

app.run()
