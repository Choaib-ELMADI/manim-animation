from manim import *


class Main(Scene):
    def construct(self):
        circle_1 = Circle(radius=3)
        circle_2 = Circle(radius=2.5, color=BLUE)
        circle_3 = Circle(radius=1.5, color=PURPLE, fill_opacity=1)

        circles_group = Group(circle_1, circle_2, circle_3)

        self.add(circles_group)
        self.play(Create(circle_1))
