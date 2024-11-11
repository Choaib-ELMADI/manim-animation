from manim import *


class Main(Scene):
    def plot_step_function(self, data_bits, axe, color, initial_y):
        start_x = 0
        start_y = initial_y

        for i, bit in enumerate(data_bits):
            end_x = i + 1
            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
            )

            # self.play(Create(line), run_time=0.25)
            self.add(line)

            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                transition_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, initial_y - 1 + data_bits[i + 1]),
                    color=color,
                )
                # self.play(Create(transition_line), run_time=0.1)
                self.add(transition_line)

            start_x = end_x
            start_y = (
                initial_y - 1 + data_bits[i + 1]
                if i < len(data_bits) - 1
                else initial_y - 1
            )

    def generate_clock_signal(self, length, axe, color, initial_y):
        start_x = 1
        start_y = initial_y

        no_clock_line_1 = Line(
            axe.c2p(0, start_y),
            axe.c2p(start_x, start_y),
            color=color,
        )

        axe.add(no_clock_line_1)

        for i in range(start_x, length + 1):
            end_x = i + 0.25

            low_state_start = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
            )

            rising_edge = Line(
                axe.c2p(end_x, start_y),
                axe.c2p(end_x, start_y + 1),
                color=color,
            )

            high_state = Line(
                axe.c2p(end_x, start_y + 1),
                axe.c2p(end_x + 0.5, start_y + 1),
                color=color,
            )

            falling_edge = Line(
                axe.c2p(end_x + 0.5, start_y + 1),
                axe.c2p(end_x + 0.5, start_y),
                color=color,
            )

            low_state_end = Line(
                axe.c2p(end_x + 0.5, start_y),
                axe.c2p(end_x + 0.75, start_y),
                color=color,
            )

            axe.add(low_state_start)
            axe.add(rising_edge)
            axe.add(high_state)
            axe.add(falling_edge)
            axe.add(low_state_end)

            start_x = start_x + 1

        no_clock_line_2 = Line(
            axe.c2p(13, start_y),
            axe.c2p(14, start_y),
            color=color,
        )

        axe.add(no_clock_line_2)

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

        #! CS/SS
        # self.play(Write(cs_line_label))
        self.add(cs_line_label)
        self.wait(0.25)
        self.plot_step_function(cs_line_data, axe, "BLUE", initial_y=7)

        #! SCLK
        # self.play(Write(sclk_line_label))
        self.add(sclk_line_label)
        self.wait(0.25)
        self.generate_clock_signal(12, axe, "RED", initial_y=4)

        #! MOSI
        # self.play(Write(mosi_line_label))
        self.add(mosi_line_label)
        self.wait(0.25)

        #! MISO
        # self.play(Write(miso_line_label))
        self.add(miso_line_label)
        self.wait(0.25)

        #! END CS/SS
        self.play(Create(cs_transition_line), run_time=0.1)
        # self.add(cs_transition_line)
        self.play(Create(cs_disable_line), run_time=0.25)
        # self.add(cs_disable_line)

        self.wait(2)
