from manim import *


class Main(Scene):
    def plot_step_function(
        self, data_bits, axe, color, initial_y, CPHA=0, dy=0, disabled=True
    ):
        initial_x = 1.5 if CPHA else 0 if disabled else 0.5
        start_x = initial_x
        start_y = initial_y

        if not disabled:
            additional_line = Line(
                axe.c2p(0, start_y),
                axe.c2p(initial_x, start_y),
                color=color,
            )
            # self.play(Create(additional_line), run_time=0.25)
            self.add(additional_line)

        for i, bit in enumerate(data_bits):
            end_x = initial_x + i + 1
            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
            )

            if CPHA and i == len(data_bits) - 1:
                pass
            else:
                # self.play(Create(line), run_time=0.25)
                self.add(line)

            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                transition_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, initial_y - dy + data_bits[i + 1]),
                    color=color,
                )
                # self.play(Create(transition_line), run_time=0.1)
                self.add(transition_line)

            start_x = end_x
            start_y = (
                initial_y - dy + data_bits[i + 1]
                if i < len(data_bits) - 1
                else initial_y - dy
            )

        if not disabled:
            additional_line = Line(
                axe.c2p(13.5, start_y),
                axe.c2p(14, start_y),
                color=color,
            )
            # self.play(Create(additional_line), run_time=0.25)
            self.add(additional_line)

    def generate_clock_signal(self, length, axe, color, initial_y, CPOL=0):
        start_x = 1
        start_y = initial_y + 1 if CPOL else initial_y

        no_clock_line_1 = Line(
            axe.c2p(0, start_y),
            axe.c2p(start_x, start_y),
            color=color,
        )
        # self.play(Create(no_clock_line_1), run_time=0.25)
        self.add(no_clock_line_1)

        for i in range(start_x, length + 1):
            end_x = i + 0.25

            ##!## NAME IS INVERTED IF CPOL IS "1"
            low_state_start = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
            )

            ##!## NAME IS INVERTED IF CPOL IS "1"
            rising_edge = Line(
                axe.c2p(end_x, start_y),
                axe.c2p(end_x, start_y - 1 if CPOL else start_y + 1),
                color=color,
            )

            ##!## NAME IS INVERTED IF CPOL IS "1"
            high_state = Line(
                axe.c2p(end_x, start_y - 1 if CPOL else start_y + 1),
                axe.c2p(end_x + 0.5, start_y - 1 if CPOL else start_y + 1),
                color=color,
            )

            ##!## NAME IS INVERTED IF CPOL IS "1"
            falling_edge = Line(
                axe.c2p(end_x + 0.5, start_y - 1 if CPOL else start_y + 1),
                axe.c2p(end_x + 0.5, start_y),
                color=color,
            )

            ##!## NAME IS INVERTED IF CPOL IS "1"
            low_state_end = Line(
                axe.c2p(end_x + 0.5, start_y),
                axe.c2p(end_x + 0.75, start_y),
                color=color,
            )

            # self.play(Create(low_state_start), run_time=0.1)
            self.add(low_state_start)
            # self.play(Create(rising_edge), run_time=0.25)
            self.add(rising_edge)
            # self.play(Create(high_state), run_time=0.1)
            self.add(high_state)
            # self.play(Create(falling_edge), run_time=0.25)
            self.add(falling_edge)
            # self.play(Create(low_state_end), run_time=0.1)
            self.add(low_state_end)

            start_x = start_x + 1

        no_clock_line_2 = Line(
            axe.c2p(13, start_y),
            axe.c2p(14, start_y),
            color=color,
        )
        # self.play(Create(no_clock_line_2), run_time=0.25)
        self.add(no_clock_line_2)

    def create_dotted_lines(self, axe, length):
        for i in range(1, length + 1):
            dotted_line = DashedLine(
                axe.c2p(i, 0),
                axe.c2p(i, 7.25),
                dash_length=0.05,
                dashed_ratio=0.3,
                color="GREY",
            )
            # self.play(Create(dotted_line), run_time=0.1)
            self.add(dotted_line)

    def construct(self):
        cs_line_data = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mosi_line_data = [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        miso_line_data = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        axe = (
            Axes(
                x_range=[0, 14, 1],
                y_range=[0, 7.25, 1],
                x_length=28,
                y_length=14,
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
                x_axis_config={
                    "include_numbers": True,
                    "include_tip": False,
                    "numbers_to_exclude": [0, 14],
                },
            )
            .scale(0.45)
            .shift(RIGHT * 0.5)
        )
        extra_y_axis = (
            axe.get_y_axis()
            .copy()
            .next_to(axe, RIGHT, buff=0)
            .align_to(DOWN)
            .shift(LEFT * 0.08, UP * 0.1)
        )

        cs_line_label = (
            Text("CS", font="Cascadia Code", color="BLUE")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 6, DOWN * 0.5)
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
        self.add(axe, extra_y_axis)
        self.wait(0.25)
        self.create_dotted_lines(axe, 13)
        self.wait(0.5)

        #! CS/SS
        # self.play(Write(cs_line_label))
        self.add(cs_line_label)
        self.wait(0.25)
        self.plot_step_function(cs_line_data, axe, "BLUE", initial_y=7, dy=1)
        self.wait(0.25)

        #! SCLK
        # self.play(Write(sclk_line_label))
        self.add(sclk_line_label)
        self.wait(0.25)
        #
        #! CPOL est CLOCK POLARITY
        #! CPOL = 0 horloge est active en etat HIGH
        #! CPOL = 1 horloge est active en etat LOW
        #
        self.generate_clock_signal(12, axe, "RED", initial_y=4, CPOL=0)
        self.wait(0.25)

        #! MOSI
        # self.play(Write(mosi_line_label))
        self.add(mosi_line_label)
        self.wait(0.25)
        #
        #! CPHA est CLOCK PHASE
        #! CPHA = 0 lecture en leading (1er) edge
        #! CPHA = 1 lecture en trailing (2ème) edge
        #
        self.plot_step_function(
            mosi_line_data, axe, "PURPLE", CPHA=1, initial_y=2, disabled=False
        )
        self.wait(0.25)

        #! MISO
        # self.play(Write(miso_line_label))
        self.add(miso_line_label)
        self.wait(0.25)
        #
        #! CPHA est CLOCK PHASE
        #! CPHA = 0 lecture en leading (1er) edge
        #! CPHA = 1 lecture en trailing (2ème) edge
        #
        self.plot_step_function(
            miso_line_data, axe, "GREEN", CPHA=1, initial_y=0, disabled=False
        )
        self.wait(0.25)

        #! END CS/SS
        # self.play(Create(cs_transition_line), run_time=0.1)
        self.add(cs_transition_line)
        self.wait(0.25)
        # self.play(Create(cs_disable_line), run_time=0.25)
        self.add(cs_disable_line)

        self.wait(2)
