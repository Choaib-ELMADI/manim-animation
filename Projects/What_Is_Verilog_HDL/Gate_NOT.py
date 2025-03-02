from manim import *

IS_DEBUGGING = False
# IS_DEBUGGING = True


class Gate_NOT(Scene):
    length = 2

    def construct(self):
        not_top_line = Line(
            start=[-self.length, self.length, 0], end=[self.length, 0, 0]  # type: ignore
        )
        not_bot_line = Line(
            start=[-self.length, -self.length, 0], end=[self.length, 0, 0]  # type: ignore
        )
        not_lft_line = Line(
            start=[-self.length, self.length, 0], end=[-self.length, -self.length, 0]  # type: ignore
        )
        not_circle = Circle(radius=self.length / 5, color=WHITE).next_to(
            not_top_line.get_end(), buff=0
        )

        not_input = Line(
            start=not_lft_line.get_center(),
            end=not_lft_line.get_center() + LEFT * self.length,
        )
        not_output = Line(
            start=not_top_line.get_end() + RIGHT * 2 * (self.length / 5),
            end=not_top_line.get_end()
            + RIGHT * 2 * (self.length / 5)
            + RIGHT * self.length,
        )

        gate_name = Text(
            "NOT",
            font="Cascadia Code",
            font_size=50 * self.length,
        ).next_to(not_lft_line, buff=0.15 * self.length)

        if not IS_DEBUGGING:
            self.play(Create(not_top_line), Create(not_bot_line))
            self.play(Create(not_lft_line))
            self.play(Create(not_circle))
            self.play(Create(not_input), Create(not_output))
            self.play(Write(gate_name))
        else:
            self.add(not_top_line, not_bot_line, not_lft_line, not_circle)
            self.add(not_input, not_output)
            self.add(gate_name)

        self.wait(2)
