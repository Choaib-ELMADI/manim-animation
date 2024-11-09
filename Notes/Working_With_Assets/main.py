from manim import *

HOME_DIR = "C:\\Manim\\Assets"
icon_name = "seecs_1"


class Main(Scene):
    def construct(self):
        icon = SVGMobject(f"{HOME_DIR}\\{icon_name}.svg")
        text = Text("SEECS Club").next_to(icon, DOWN, buff=0.5)

        self.play(DrawBorderThenFill(icon), run_time=4, rate_func=linear)
        self.wait(0.5)
        self.play(Write(text), run_time=3)
