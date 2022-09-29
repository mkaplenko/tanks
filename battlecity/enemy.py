from battlecity import Direction
from battlecity.tank import Tank, TankModel


class EnemyAI:
    def __init__(self, tank: 'Enemy'):
        self.tank = tank

    def move(self):
        self.tank.direction = Direction.LEFT
        self.tank.animation = self.tank.model.animations[self.tank.direction]
        self.tank.vx = -1
        self.tank.vy = 0
        self.tank.animation.play()


class Enemy(Tank):
    def __init__(self, x: int, y: int, direction: Direction, model: TankModel):
        super(Enemy, self).__init__(x, y, direction, model)
        self.ai = EnemyAI(self)

    def move(self):
        self.ai.move()

    def update(self):
        self.move()
        super(Enemy, self).update()
