from manim import *


class Main(Scene):
    def construct(self):
        square_1 = Square(side_length=4)
        square_2 = Square(side_length=3, color="RED")
        square_3 = Square(
            side_length=2, color="GREEN", fill_opacity=0.1, stroke_color="PURPLE"
        )

        squares_group = Group(square_1, square_2, square_3)

        # self.add(squares_group)
        # self.play(Create(square_1), run_time=3)
        # self.wait()

        self.play(Create(square_1), run_time=1)
        self.wait()

        self.play(Create(square_2), run_time=1)
        self.wait()

        self.play(Create(square_3), run_time=1)
        self.wait()
