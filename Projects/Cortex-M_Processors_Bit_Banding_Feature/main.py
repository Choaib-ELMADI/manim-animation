from manim import *


class Main(Scene):
    def construct(self):
        title = (
            Text(
                "Cortex-M3/4 Processors Bit Banding Feature",
                font="Cascadia Code",
                font_size=54,
                color="RED",
            )
            .scale(0.5)
            .to_edge(UP)
        )

        main_axes = Paragraph(
            "- Definition " "- Memory Layout " "- Something Else " "- And Last",
            font="Cascadia Code",
            font_size=16,
        ).next_to(title, DOWN, buff=0.2)

        bit_banding_def = Paragraph(
            "Bit-banding",
            "is a feature that enables every single bit",
            "in the bit-band region to be directly accessible!",
            "(in a single instruction)",
            font="Cascadia Code",
            font_size=21,
            line_spacing=0.75,
            alignment="center",
        )
        bit_banding_def[0].set_color(YELLOW)
        bit_banding_def[-1].set_color(ORANGE)

        # self.play(Write(title), run_time=1.5)
        self.add(title)
        # self.play(title.animate.to_edge(UP), run_time=1)  # type: ignore
        self.wait(0.5)

        # self.play(Write(main_axes), run_time=1)
        self.add(main_axes)
        self.wait(0.5)

        main_axes[0].set_color(YELLOW)
        self.wait(0.25)

        for line in bit_banding_def:
            self.add(line)
            # self.play(Write(line), run_time=1)
            self.wait(0.25)

        self.play(FadeOut(bit_banding_def, shift=DOWN * 0.5))  # type: ignore

        main_axes[0].set_color(WHITE)
        main_axes[1].set_color(YELLOW)

        self.wait(2)
