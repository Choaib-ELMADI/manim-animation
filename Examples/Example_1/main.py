from manim import *


class Main(Scene):
    def construct(self):
        name = Text("Choaib", color="RED").to_edge(UL, buff=0.5)
        square = Square(side_length=1, color="GREEN", fill_opacity=1).shift(LEFT * 3)
        triangle = Triangle().to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(square), run_time=2)
        self.play(Create(triangle))

        self.play(name.animate.to_edge(UR), run_time=2)  # type: ignore
        self.play(square.animate.scale(2), triangle.animate.to_edge(DL), run_time=3)  # type: ignore
