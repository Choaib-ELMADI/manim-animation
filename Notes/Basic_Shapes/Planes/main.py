from manim import *


class Main(Scene):
    def construct(self):
        plane = (
            NumberPlane(x_range=[-4, 4, 1], x_length=8, y_range=[0, 16, 2], y_length=6)
            .to_edge(DL)
            .add_coordinates()
        )

        parab = plane.plot(lambda x: x**2, x_range=[-4, 4], color="RED")

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")
        func_label = (
            MathTex("f(x)={x}^{2}")
            .scale(0.75)
            .next_to(parab, RIGHT, buff=0.5)
            .set_color("PURPLE")
        )

        area = plane.get_riemann_rectangles(
            graph=parab,
            x_range=[-2, 3],
            dx=0.2,
            stroke_width=0.1,
            stroke_color="YELLOW",
        )

        self.play(Create(plane), run_time=3)
        self.play(Create(VGroup(parab, labels, func_label)), run_time=3)
        self.wait()
        self.play(Create(area), run_time=4)
