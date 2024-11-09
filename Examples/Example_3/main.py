from manim import *


class Main(Scene):
    def construct(self):
        number = MathTex("ln(2) + ln(2) = 2ln(2)")
        box = always_redraw(
            lambda: SurroundingRectangle(
                number, color="PURPLE", fill_opacity=0.25, fill_color="RED", buff=0.25
            )
        )
        name = always_redraw(lambda: Text("Logarithm").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(number, box, name)), run_time=3)
        self.play(number.animate.shift(RIGHT * 3), run_time=2)  # type: ignore
