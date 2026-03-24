import tkinter as tk

WIDTH = 500
HEIGHT = 450
SPACESHIP_WIDTH = 45
SPACESHIP_HEIGHT = 25
SPACESHIP_Y = HEIGHT - 60
SPACESHIP_SPEED = 35

INVADER_WIDTH = 25
INVADER_HEIGHT = 18
INVADER_GAP_X = 6
INVADER_GAP_Y = 10
INVADER_ROWS = 4
INVADER_COLS = 7

BULLET_WIDTH = 4
BULLET_HEIGHT = 10
BULLET_SPEED = -12

ENEMY_MOVE_X = 5
ENEMY_DROP_Y = 1
GAME_TICK = 60


def boxes_overlap(b1, b2):
    if not b1 or not b2:
        return False
    x1a, y1a, x2a, y2a = b1
    x1b, y1b, x2b, y2b = b2
    return (x1a < x2b) and (x2a > x1b) and (y1a < y2b) and (y2a > y1b)


class Spaceship:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(
            x, y, x + SPACESHIP_WIDTH, y + SPACESHIP_HEIGHT, fill="blue"
        )

    def move(self, dx):
        coords = self.canvas.coords(self.id)
        if not coords:
            return
        x1, y1, x2, y2 = coords
        if x1 + dx < 0:
            dx = -x1
        if x2 + dx > WIDTH:
            dx = WIDTH - x2
        if dx != 0:
            self.canvas.move(self.id, dx, 0)

    def shoot(self):
        coords = self.canvas.coords(self.id)
        if not coords:
            return None
        x1, y1, x2, y2 = coords
        bx = (x1 + x2) / 2
        by = y1 - BULLET_HEIGHT
        bullet_id = self.canvas.create_rectangle(
            bx - BULLET_WIDTH/2, by - BULLET_HEIGHT/2,
            bx + BULLET_WIDTH/2, by + BULLET_HEIGHT/2,
            fill="red"
        )
        return Bullet(self.canvas, bullet_id)


class Bullet:
    def __init__(self, canvas, id):
        self.canvas = canvas
        self.id = id

    def move(self):
        self.canvas.move(self.id, 0, BULLET_SPEED)

    def bbox(self):
        return self.canvas.bbox(self.id)

    def remove(self):
        self.canvas.delete(self.id)


class Invader:
    def __init__(self, canvas, x, y, color="purple"):
        self.canvas = canvas
        self.id = canvas.create_rectangle(
            x, y, x + INVADER_WIDTH, y + INVADER_HEIGHT, fill=color
        )

    def move(self, dx, dy):
        self.canvas.move(self.id, dx, dy)

    def bbox(self):
        return self.canvas.bbox(self.id)

    def remove(self):
        self.canvas.delete(self.id)


class GameApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")
        self.canvas.pack()

        self.restart_button = None  # will hold the restart button widget

        self.setup_game()
        root.bind("<Left>", self.on_left)
        root.bind("<Right>", self.on_right)
        root.bind("<space>", self.on_shoot)
        self.game_loop()

    def setup_game(self):
        # initialize / reset game state
        self.canvas.delete("all")
        start_x = (WIDTH - SPACESHIP_WIDTH) / 2
        self.player = Spaceship(self.canvas, start_x, SPACESHIP_Y)

        self.bullets = []
        self.invaders = []
        self.enemy_dx = ENEMY_MOVE_X
        self.running = True

        top_margin = 40
        for row in range(INVADER_ROWS):
            y = top_margin + row * (INVADER_HEIGHT + INVADER_GAP_Y)
            for col in range(INVADER_COLS):
                x = 20 + col * (INVADER_WIDTH + INVADER_GAP_X)
                inv = Invader(self.canvas, x, y)
                self.invaders.append(inv)

    def on_left(self, event):
        self.player.move(-SPACESHIP_SPEED)

    def on_right(self, event):
        self.player.move(SPACESHIP_SPEED)

    def on_shoot(self, event):
        bullet = self.player.shoot()
        if bullet:
            self.bullets.append(bullet)

    def move_enemies(self):
        hit_border = False
        for inv in list(self.invaders):
            bbox = inv.bbox()
            if not bbox:
                continue
            x1, y1, x2, y2 = bbox
            if x2 + self.enemy_dx > WIDTH or x1 + self.enemy_dx < 0:
                hit_border = True
                break

        if hit_border:
            self.enemy_dx = -self.enemy_dx
            for inv in list(self.invaders):
                inv.move(0, ENEMY_DROP_Y)
        else:
            for inv in list(self.invaders):
                inv.move(self.enemy_dx, 0)

    def check_collisions(self):
        for bullet in list(self.bullets):
            bb = bullet.bbox()
            if not bb:
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
                continue
            for inv in list(self.invaders):
                ib = inv.bbox()
                if boxes_overlap(bb, ib):
                    bullet.remove()
                    inv.remove()
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if inv in self.invaders:
                        self.invaders.remove(inv)
                    break

        for inv in list(self.invaders):
            ib = inv.bbox()
            if ib and ib[3] >= HEIGHT - 40:
                self.game_over(False)
                return

    def check_win(self):
        if not self.invaders:
            self.game_over(True)

    def game_loop(self):
        if not self.running:
            return

        self.move_enemies()

        for bullet in list(self.bullets):
            bullet.move()
            bbb = bullet.bbox()
            if not bbb:
                if bullet in self.bullets:
                    self.bullets.remove(bullet)
            else:
                if bbb[3] < 0:
                    bullet.remove()
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)

        self.check_collisions()
        self.check_win()
        self.root.after(GAME_TICK, self.game_loop)

    def game_over(self, won):
        self.running = False
        # remove existing restart button if any (to avoid duplicates)
        if self.restart_button:
            try:
                self.restart_button.destroy()
            except Exception:
                pass
            self.restart_button = None

        if won:
            print("YOU WIN!")
            self.canvas.create_text(
                WIDTH/2, HEIGHT/2, text="YOU WIN!", fill="white", font=("Arial", 24))
        else:
            print("GAME OVER")
            self.canvas.create_text(
                WIDTH/2, HEIGHT/2, text="GAME OVER", fill="red", font=("Arial", 24))

        # create restart button below the canvas (slide-style Button + pack)
        # store reference so we can destroy it later
        self.restart_button = tk.Button(
            self.root, text="Restart", command=self.restart)
        # pack the restart button so it appears below the canvas
        self.restart_button.pack(pady=8)

    def restart(self):
        # destroy the restart button
        if self.restart_button:
            try:
                self.restart_button.destroy()
            except Exception:
                pass
            self.restart_button = None

        # reset and start the game again
        self.setup_game()
        self.game_loop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Space Invaders")
    app = GameApp(root)
    root.mainloop()
