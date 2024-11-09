from manim import *


class Main(Scene):
    def construct(self):
        rectangle = Rectangle(color="PURPLE", height=4, width=8)
        circle = Circle().to_edge(DOWN)
        arrow = Line(start=circle.get_center(), end=rectangle.get_bottom()).add_tip(
            tip_shape=StealthTip, tip_length=0.1
        )

        self.play(Create(rectangle), run_time=2)
        self.wait()
        self.play(Create(circle), run_time=2)
        self.wait()
        self.play(Create(arrow), run_time=2)
        self.wait()

        self.play(
            rectangle.animate.shift(RIGHT * 3),  # type: ignore
            circle.animate.shift(RIGHT * 3),  # type: ignore
            arrow.animate.shift(RIGHT * 3),  # type: ignore
            run_time=3,
        )
