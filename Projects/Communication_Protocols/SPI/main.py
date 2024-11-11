from manim import *


class Main(Scene):

    def plot_step_function(self, data_bits, axe, color, initial_y, initial_x=0):
        start_x = initial_x
        start_y = initial_y

        for i, bit in enumerate(data_bits):
            end_x = initial_x + i + 1
            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
            )

            self.play(Create(line), run_time=0.25)
            # self.add(line)

            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                transition_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, initial_y - 1 + data_bits[i + 1]),
                    color=color,
                )
                self.play(Create(transition_line), run_time=0.1)
                # self.add(transition_line)

            start_x = end_x
            start_y = (
                initial_y - 1 + data_bits[i + 1]
                if i < len(data_bits) - 1
                else initial_y - 1
            )

    def construct(self):
        cs_line_data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        axe = (
            Axes(
                x_range=[0, 14, 1],
                y_range=[0, 7, 1],
                x_length=28,
                y_length=14,
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
                x_axis_config={
                    "include_numbers": True,
                },
            )
            .scale(0.45)
            .shift(RIGHT * 0.5)
        )

        cs_line_label = (
            Text("CS", font="Cascadia Code", color="BLUE")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 6, DOWN * 0.3)
        )
        cs_transition_line = Line(
            axe.c2p(13, 6),
            axe.c2p(13, 7),
            color="BLUE",
        )
        cs_disable_line = Line(
            axe.c2p(13, 7),
            axe.c2p(14, 7),
            color="BLUE",
        )

        sclk_line_label = (
            Text("SCLK", font="Cascadia Code", color="RED")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 4, DOWN * 0.2)
        )

        mosi_line_label = (
            Text("MOSI", font="Cascadia Code", color="PURPLE")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 2)
        )

        miso_line_label = (
            Text("MISO", font="Cascadia Code", color="GREEN")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 0.25)
        )

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        self.wait(0.25)
        # self.play(Create(axe))
        self.add(axe)
        self.wait(1)

        # self.play(Write(cs_line_label))
        self.add(cs_line_label)
        self.wait(0.25)
        self.plot_step_function(cs_line_data, axe, "BLUE", initial_y=7)

        # self.play(Write(sclk_line_label))
        self.add(sclk_line_label)
        self.wait(0.25)

        # self.play(Write(mosi_line_label))
        self.add(mosi_line_label)
        self.wait(0.25)

        # self.play(Write(miso_line_label))
        self.add(miso_line_label)
        self.wait(0.25)

        self.play(Create(cs_transition_line), run_time=0.1)
        # self.add(cs_transition_line)
        self.play(Create(cs_disable_line), run_time=0.25)
        # self.add(cs_disable_line)

        self.wait(2)
