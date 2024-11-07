from manim import *


class Main(Scene):
    def construct(self):
        text = Tex("1 2 3")
        self.play(Write(text))
        self.wait(1)
