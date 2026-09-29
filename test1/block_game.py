import random
import tkinter as tk

BOARD_COLS = 10
BOARD_ROWS = 18
CELL_SIZE = 28
WIDTH = BOARD_COLS * CELL_SIZE
HEIGHT = BOARD_ROWS * CELL_SIZE

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
]

COLORS = [
    "#ff6b6b",
    "#feca57",
    "#48dbfb",
    "#1dd1a1",
    "#5f27cd",
    "#ff9ff3",
    "#c8d6e5",
]


class BlockGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Block Line Game")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT + 40, bg="#f2f2f2")
        self.canvas.pack()

        self.board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.score = 0
        self.game_over = False
        self.current = None
        self.current_piece = None
        self.next_piece = None

        self.root.bind("<KeyPress-Left>", self.move_left)
        self.root.bind("<KeyPress-Right>", self.move_right)
        self.root.bind("<KeyPress-Up>", self.place_block)
        self.root.bind("<KeyPress-Down>", self.place_block)
        self.root.bind("<KeyPress-r>", self.restart_game)

        self.new_piece()
        self.draw()
        self.root.after(500, self.tick)

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)

        self.current = {
            "shape": shape,
            "color": color,
            "x": BOARD_COLS // 2 - len(shape[0]) // 2,
            "y": 0,
        }
        self.current_piece = self.current

        if self.collides(self.current, 0, 0):
            self.game_over = True

    def collides(self, piece, dx, dy):
        for row_index, row in enumerate(piece["shape"]):
            for col_index, value in enumerate(row):
                if not value:
                    continue

                x = piece["x"] + col_index + dx
                y = piece["y"] + row_index + dy

                if x < 0 or x >= BOARD_COLS or y >= BOARD_ROWS:
                    return True

                if y >= 0 and self.board[y][x] != 0:
                    return True

        return False

    def move_left(self, event=None):
        if self.game_over:
            return
        if not self.collides(self.current, -1, 0):
            self.current["x"] -= 1
            self.draw()

    def move_right(self, event=None):
        if self.game_over:
            return
        if not self.collides(self.current, 1, 0):
            self.current["x"] += 1
            self.draw()

    def place_block(self, event=None):
        if self.game_over:
            return
        self.lock_piece()

    def tick(self):
        if self.game_over:
            return

        if not self.collides(self.current, 0, 1):
            self.current["y"] += 1
        else:
            self.lock_piece()

        self.draw()
        self.root.after(500, self.tick)

    def lock_piece(self):
        for row_index, row in enumerate(self.current["shape"]):
            for col_index, value in enumerate(row):
                if not value:
                    continue
                x = self.current["x"] + col_index
                y = self.current["y"] + row_index
                if y >= 0:
                    self.board[y][x] = self.current["color"]

        self.clear_lines()
        self.new_piece()
        self.draw()

    def clear_lines(self):
        rows_to_clear = []
        for row_index, row in enumerate(self.board):
            if all(cell != 0 for cell in row):
                rows_to_clear.append(row_index)

        for row_index in reversed(rows_to_clear):
            del self.board[row_index]
            self.board.insert(0, [0 for _ in range(BOARD_COLS)])
            self.score += 10

    def restart_game(self, event=None):
        self.board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.score = 0
        self.game_over = False
        self.new_piece()
        self.draw()
        self.root.after(500, self.tick)

    def draw(self):
        self.canvas.delete("all")

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                x0 = col * CELL_SIZE
                y0 = row * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                fill = self.board[row][col] if self.board[row][col] else "#ffffff"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline="#d9d9d9")

        if self.current is not None:
            for row_index, row in enumerate(self.current["shape"]):
                for col_index, value in enumerate(row):
                    if not value:
                        continue
                    x = (self.current["x"] + col_index) * CELL_SIZE
                    y = (self.current["y"] + row_index) * CELL_SIZE
                    self.canvas.create_rectangle(
                        x,
                        y,
                        x + CELL_SIZE,
                        y + CELL_SIZE,
                        fill=self.current["color"],
                        outline="#111111",
                    )

        self.canvas.create_text(10, HEIGHT + 8, anchor="w", text=f"Score: {self.score}", font=("Arial", 14, "bold"))

        if self.game_over:
            self.canvas.create_text(
                WIDTH / 2,
                HEIGHT / 2,
                text="Game Over\nPress R to restart",
                font=("Arial", 22, "bold"),
                fill="#222222",
            )


def main():
    root = tk.Tk()
    game = BlockGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
