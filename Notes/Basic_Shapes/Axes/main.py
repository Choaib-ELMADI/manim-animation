from manim import *


class Main(Scene):
    def construct(self):
        axe = Axes(
            x_range=(1, 11, 1),
            y_range=(0, 2, 1),
            axis_config={"include_numbers": True, "tip_shape": StealthTip},
            y_axis_config={"scaling": LogBase(custom_labels=True)},
        ).to_edge(DL)

        graph = axe.plot(lambda x: x**2, x_range=[1, 11], use_smoothing=False)

        self.play(Create(axe), run_time=5)
        self.wait()
        self.play(Create(graph), run_time=5)
