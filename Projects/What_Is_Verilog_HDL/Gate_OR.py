from manim import *

IS_DEBUGGING = False
# IS_DEBUGGING = True


class Gate_OR(Scene):
    length = 2

    def construct(self):
        or_top_arc = ArcBetweenPoints(
            start=[-self.length, -self.length, 0], end=[self.length, 0, 0], angle=PI / 4  # type: ignore
        ).shift(UP * 1.5)
        or_bot_arc = ArcBetweenPoints(
            start=[-self.length, self.length, 0],  # type: ignore
            end=[self.length, 0, 0],  # type: ignore
            angle=-PI / 4,
        ).shift(UP * 1.5)
        or_lft_arc = ArcBetweenPoints(
            start=[-self.length, self.length, 0],  # type: ignore
            end=[-self.length, -self.length, 0],  # type: ignore
            angle=-PI / 3,
        ).shift(UP * 1.5)

        or_input_1 = Line(
            start=or_lft_arc.get_start()
            + (2 * self.length / 4) * DOWN
            + RIGHT * PI / 15 * self.length,
            end=or_lft_arc.get_start()
            + (2 * self.length / 4) * DOWN
            + LEFT * self.length,
        )
        or_input_2 = Line(
            start=or_lft_arc.get_start()
            + 3 * (2 * self.length / 4) * DOWN
            + RIGHT * PI / 15 * self.length,
            end=or_lft_arc.get_start()
            + 3 * (2 * self.length / 4) * DOWN
            + LEFT * self.length,
        )
        or_output = Line(
            start=or_top_arc.get_end(),
            end=or_top_arc.get_end() + RIGHT * self.length,
        )

        gate_name = Text(
            "OR",
            font="Cascadia Code",
            font_size=60 * self.length,
        ).shift(UP * 1.5)

        if not IS_DEBUGGING:
            self.play(Create(or_top_arc), Create(or_bot_arc))
            self.play(Create(or_lft_arc))
            self.play(Create(or_input_1), Create(or_input_2), Create(or_output))
            self.play(Write(gate_name))
        else:
            self.add(
                or_top_arc,
                or_bot_arc,
                or_lft_arc,
            )
            self.add(or_input_1, or_input_2, or_output)
            self.add(gate_name)

        self.wait(2)
