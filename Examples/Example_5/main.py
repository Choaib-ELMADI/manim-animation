from manim import *


class Main(Scene):
    def construct(self):
        x_vt = ValueTracker(-4)

        axe = (
            Axes(x_range=[-4, 4, 1], y_range=[0, 16, 2], x_length=8, y_length=6)
            .set_color("WHITE")
            .add_coordinates()
        )

        parab = axe.plot(lambda x: x**2, x_range=[-4, 4]).set_color("RED")

        slope = always_redraw(
            lambda: axe.get_secant_slope_group(
                x=x_vt.get_value(),
                graph=parab,
                dx=0.01,
                dx_label="dx",
                secant_line_length=3,
                secant_line_color="GREEN",
            )
        )

        point = always_redraw(
            lambda: Dot(radius=0.1, fill_opacity=1, color="BLUE").move_to(
                axe.c2p(x_vt.get_value(), parab.underlying_function(x_vt.get_value()))
            )
        )

        self.add(axe, parab, slope, point)
        self.wait(2)
        self.play(x_vt.animate.set_value(4), run_time=4)  # type: ignore
