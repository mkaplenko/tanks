from pygame import constants

from battlecity import Direction
from battlecity.tank import Tank


class Player(Tank):
    def move(self, keys):
        if not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vy = 0
        elif keys[constants.K_UP] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = -self.model.SPEED
            self.direction = Direction.UP
            self.animation = self.model.animations[self.direction]
            self.animation.play()
        elif keys[constants.K_DOWN] and not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vy = self.model.SPEED
            self.direction = Direction.DOWN
            self.animation = self.model.animations[self.direction]
            self.animation.play()

        if not keys[constants.K_LEFT] and not keys[constants.K_RIGHT]:
            self.vx = 0
        elif keys[constants.K_LEFT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = -self.model.SPEED
            self.direction = Direction.LEFT
            self.animation = self.model.animations[self.direction]
            self.animation.play()
        elif keys[constants.K_RIGHT] and not keys[constants.K_UP] and not keys[constants.K_DOWN]:
            self.vx = self.model.SPEED
            self.direction = Direction.RIGHT
            self.animation = self.model.animations[self.direction]
            self.animation.play()

        if not keys[constants.K_UP] and not keys[constants.K_DOWN] and not keys[constants.K_LEFT] \
                and not keys[constants.K_RIGHT]:
            self.animation.pause()
