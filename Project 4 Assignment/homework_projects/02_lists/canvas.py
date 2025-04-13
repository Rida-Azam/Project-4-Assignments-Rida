import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Grid")

        # Create a canvas
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Draw the grid
        self.cells = []
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
                self.cells.append(cell)

        # Create eraser (pink square)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

        # Bind mouse motion to erasing
        self.canvas.bind("<Motion>", self.erase)

    def erase(self, event):
        """ Erase blue squares when the eraser overlaps them """
        self.canvas.moveto(self.eraser, event.x, event.y)

        overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        for item in overlapping_items:
            if item in self.cells:
                self.canvas.itemconfig(item, fill="white")  # Change color to white

if __name__ == "__main__":
    root = tk.Tk()
    app = EraseCanvasApp(root)
    root.mainloop()
