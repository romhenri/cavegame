from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
player.cursor.visible = False
Sky()
camera.fov = 90
camera.clip_plane_far = 1000

blocks = []

active_block = 'assets/grass.png'

# Terrain Gen
# Y = 0
for x in range(20):
    for z in range(20):
        block = Button(
            model='cube',
            texture='assets/grass.png',
            color=color.white,
            position=(x, 0, z),
            parent=scene,
            origin_y=0.5
        )
        blocks.append(block)
#Y < 0
for y in [-1, -2]:
    for x in range(20):
        for z in range(20):
            block = Button(
                model='cube',
                texture='assets/stone.png',
                color=color.white,
                position=(x, y, z),
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

def input(key):
    global active_block

    if key == '1':
        active_block = 'assets/grass.png'
        print("Bloco ativo: Grama")

    elif key == '2':
        active_block = 'assets/stone.png'
        print("Bloco ativo: Pedra")

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
                    texture=active_block,
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
