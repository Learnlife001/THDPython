import tkinter as tk
from abc import ABC, abstractmethod
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CANVAS_BG = "black"

SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 10

INVADER_ROWS = 4
INVADER_COLS = 8
INVADER_SPACING = 50
INVADER_SPEED = 3


#

# --- UTILITY FUNCTION ---

def check_collision(canvas, item_a_id, item_b_id):
    coords_a = canvas.coords(item_a_id)
    coords_b = canvas.coords(item_b_id)

    # in case where an item might have already been deleted
    if not coords_a or not coords_b:
        return False

    x_overlap = coords_a[0] < coords_b[2] and coords_a[2] > coords_b[0]
    y_overlap = coords_a[1] < coords_b[3] and coords_a[3] > coords_b[1]

    return x_overlap and y_overlap


# --- SPACESHIP HIERARCHY ---

class Spaceship(ABC):
    """
    Abstract Base Class for Defender and Invader
    """

    def __init__(self, canvas, x, y, width, height, color, speed=1, health=1):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.health = health

        self.id = self.canvas.create_rectangle(
            x, y, x + width, y + height, fill=color
        )

        self.bullets = []

    def move_left(self):
        self.canvas.move(self.id, -self.speed, 0)

    def move_right(self):
        self.canvas.move(self.id, self.speed, 0)

    @abstractmethod
    def shoot(self):
        pass

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()

        # Remove inactive bullets
        self.bullets = [b for b in self.bullets if b.active]


class Defender(Spaceship):
    """Defender"""

    def __init__(self, canvas, x, y, width, height, color, speed=1):
        super().__init__(canvas, x, y, width, height, color, speed)
        self.health = 3

    def move_left(self):
        if self.canvas.coords(self.id)[0] > 0:
            print("Moving left!")
            self.canvas.move(self.id, -self.speed, 0)

    def move_right(self):
        if self.canvas.coords(self.id)[2] < CANVAS_WIDTH:
            print("Moving right!")
            self.canvas.move(self.id, self.speed, 0)

    def shoot(self):
        coords = self.canvas.coords(self.id)
        center_x = (coords[0] + coords[2]) // 2
        top_y = coords[1]
        print("Firing!")
        new_bullet = BasicBullet(
            self.canvas, center_x, top_y, 4, 8, color="white", speed=10, damage=1)

        self.bullets.append(new_bullet)


class Invader(Spaceship):
    """Invader"""

    def __init__(self, canvas, x, y, width, height, color, speed=1):
        super().__init__(canvas, x, y, width, height, color, speed)
        self.health = 1

    def move(self, x, y):
        self.canvas.move(self.id, x, y)

    def get_coords(self):
        if self.canvas.coords(self.id):
            return self.canvas.coords(self.id)
        else:
            return None

    def shoot(self):
        pass


# --- BULLET HIERARCHY ---

class Bullet(ABC):
    """
    Abstract Base Class for all Bullet types
    """

    def __init__(self, canvas, x, y, width, height, color, speed, damage):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.damage = damage
        self.active = True

        # Draw Bullet
        self.id = self.canvas.create_rectangle(
            x, y, x + width, y - height, fill=color
        )

    @abstractmethod
    def move(self):
        pass


class BasicBullet(Bullet):
    """
    Concrete implementation of a player-fired bullet
    """

    def move(self):
        if not self.active:
            return
        self.canvas.move(self.id, 0, -self.speed)
        if self.canvas.coords(self.id)[1] < 0:
            self.active = False
            self.canvas.delete(self.id)


class Gameapp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH,
                                height=CANVAS_HEIGHT, bg=CANVAS_BG)
        self.root.resizable(width=False, height=False)
        self.root.title("Space Invaders (THD Prog 1)")
        self.canvas.pack()

        self.keys_pressed = {"Left": False, "Right": False}

        self.player = Defender(self.canvas, CANVAS_WIDTH // 2, CANVAS_HEIGHT - 50, SPACESHIP_WIDTH, SPACESHIP_HEIGHT,
                               "red", 10)
        self.root.bind('<KeyPress-Left>',
                       lambda event: self.set_key_state('Left', True))
        self.root.bind('<KeyRelease-Left>',
                       lambda event: self.set_key_state('Left', False))
        self.root.bind('<KeyPress-Right>',
                       lambda event: self.set_key_state('Right', True))
        self.root.bind('<KeyRelease-Right>',
                       lambda event: self.set_key_state('Right', False))
        self.root.bind('<space>', lambda e: self.player.shoot())

        self.invaders = []
        # Central state for group movement (1=Right, -1=Left)
        self.invader_direction = 1
        self.spawn_invaders()

        self.game_loop()

    def set_key_state(self, key, state):
        self.keys_pressed[key] = state

    def player_movement(self):
        if self.keys_pressed['Left']:
            self.player.move_left()
        if self.keys_pressed['Right']:
            self.player.move_right()

    def spawn_invaders(self):
        for row in range(INVADER_ROWS):
            for col in range(INVADER_COLS):
                x = col * INVADER_SPACING + 100
                y = row * INVADER_SPACING + 50

                invader = Invader(self.canvas, x, y,
                                  SPACESHIP_WIDTH, SPACESHIP_HEIGHT,
                                  "green", INVADER_SPEED)

                self.invaders.append(invader)
                print(self.invaders)

    def update_invader_movement(self):
        print("update_invader_movement")
        # in case no invaders left
        if not self.invaders:
            print("No invaders found")
            return

        # for finding the left and right most invaders.
        min_x = CANVAS_WIDTH
        max_x = 0

        for invader in self.invaders:
            coords = invader.get_coords()
            if coords:
                min_x = min(min_x, coords[0])  # Find smallest x1 (left edge)
                max_x = max(max_x, coords[2])  # Find largest x2 (right edge)

        change_direction = False

        # for screen border collision
        # moving right and rightmost hit the border.
        if self.invader_direction == 1 and max_x >= CANVAS_WIDTH:
            change_direction = True
        # moving left and leftmost hit the border.
        elif self.invader_direction == -1 and min_x <= 0:
            change_direction = True

        # movement
        if change_direction:
            print("here1")  # checking #dont forget to delete this!
            # Reverse direction
            self.invader_direction *= -1

            # Move all invaders down
            drop_distance = INVADER_SPACING / 4
            for invader in self.invaders:
                invader.move(0, drop_distance)
        else:
            # keep moving horizontally
            x = INVADER_SPEED * self.invader_direction
            for invader in self.invaders:
                invader.move(x, 0)

    def check_bullet_collisions(self):
        for bullet in self.player.bullets[:]:
            if not bullet.active:
                continue

            for invader in self.invaders[:]:
                if check_collision(self.canvas, bullet.id, invader.id):
                    bullet.active = False
                    self.canvas.delete(bullet.id)

                    self.invaders.remove(invader)  # Remove object from list
                    # Remove graphic from canvas
                    self.canvas.delete(invader.id)
                    # move to the next player bullet.
                    break

    def game_loop(self):
        self.player_movement()
        self.player.update_bullets()
        self.update_invader_movement()
        self.check_bullet_collisions()
        self.root.after(30, self.game_loop)


if __name__ == "__main__":
    root = tk.Tk()
    gameapp = Gameapp(root)
    root.mainloop()
