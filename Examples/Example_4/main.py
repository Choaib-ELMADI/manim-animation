from manim import *


class Main(Scene):
    def construct(self):
        vt = ValueTracker(3)
        num = always_redraw(lambda: DecimalNumber().set_value(vt.get_value()))

        self.play(FadeIn(num), run_time=2)
        self.wait()
        self.play(vt.animate.set_value(0), run_time=3, rate_func=linear)  # type: ignore
