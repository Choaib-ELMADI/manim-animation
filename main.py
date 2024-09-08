from manim import Scene, Square, Create


class SimpleSquare(Scene):
    def construct(self):
        square = Square()  # Create a square
        self.play(Create(square))  # Animate the drawing of the square
        self.wait(2)
