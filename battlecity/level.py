import os

from battlecity import all_sprites, tank_blocks, bullet_blocks, forests
from battlecity.block import Block, Wall, ArmoredWall, Forest, Sea
from battlecity.config import DATA_DIR


class Level:
    def __init__(self, level_num: int = 1):
        self.level_num = level_num

    def render_map(self):
        with open(os.path.join(DATA_DIR, self.filename)) as fd:
            map_data = fd.readlines()

            cords = 0, 0
            for row in map_data:
                for el in row:
                    if el == Block.WALL:
                        bl = Wall(*cords)
                        all_sprites.add(bl)
                        tank_blocks.add(bl)
                        bullet_blocks.add(bl)
                    elif el == Block.ARM_WALL:
                        bl = ArmoredWall(*cords)
                        all_sprites.add(bl)
                        tank_blocks.add(bl)
                        bullet_blocks.add(bl)
                    elif el == Block.FOREST:
                        bl = Forest(*cords)
                        forests.add(bl)
                    elif el == Block.SEA:
                        bl = Sea(*cords)
                        all_sprites.add(bl)
                        tank_blocks.add(bl)

                    cords = cords[0] + Block.SIZE[0], cords[1]
                cords = 0, cords[1] + Block.SIZE[1]

    @property
    def filename(self):
        return f'level-{self.level_num}.map'
