from manim import *

IS_DEBUGGING = False
# IS_DEBUGGING = True


class Gate_AND(Scene):
    length = 0.5

    def construct(self):
        and_top_horiz_line = Line(start=[-self.length, self.length, 0], end=[self.length, self.length, 0])  # type: ignore
        and_bot_horiz_line = Line(start=[-self.length, -self.length, 0], end=[self.length, -self.length, 0])  # type: ignore
        and_lft_verti_line = Line(
            and_top_horiz_line.get_start(), and_bot_horiz_line.get_start()
        )
        and_rgt_curve_line = ArcBetweenPoints(
            and_top_horiz_line.get_end(),
            and_bot_horiz_line.get_end(),
            radius=-self.length,
        )

        and_input_1 = Line(
            start=and_lft_verti_line.get_start() + (2 * self.length / 4) * DOWN,
            end=and_lft_verti_line.get_start()
            + (2 * self.length / 4) * DOWN
            + LEFT * self.length,
        )
        and_input_2 = Line(
            start=and_lft_verti_line.get_start() + 3 * (2 * self.length / 4) * DOWN,
            end=and_lft_verti_line.get_start()
            + 3 * (2 * self.length / 4) * DOWN
            + LEFT * self.length,
        )
        and_output = Line(
            start=and_rgt_curve_line.get_arc_center() + RIGHT * self.length,
            end=and_rgt_curve_line.get_arc_center() + RIGHT * self.length * 2,
        )

        gate_name = Text(
            "AND",
            font="Cascadia Code",
            font_size=60 * self.length,
        ).move_to(
            (and_lft_verti_line.get_center() + and_output.get_start()) / 2  # type: ignore
        )

        if not IS_DEBUGGING:
            self.play(Create(and_top_horiz_line), Create(and_bot_horiz_line))
            self.play(Create(and_lft_verti_line), Create(and_rgt_curve_line))
            self.play(Create(and_input_1), Create(and_input_2), Create(and_output))
            self.play(Write(gate_name))
        else:
            self.add(
                and_top_horiz_line,
                and_bot_horiz_line,
                and_lft_verti_line,
                and_rgt_curve_line,
            )
            self.add(and_input_1, and_input_2, and_output)
            self.add(gate_name)

        self.wait(2)
