from manim import *


class Main(Scene):
    def start_transmission_condition(self, data_bits, axe, d_initial_y, c_initial_y):
        start_x = 1
        d_start_y = d_initial_y + 1
        c_start_y = c_initial_y

        initial_no_data_line_1 = Line(
            axe.c2p(0, d_start_y),
            axe.c2p(0.5, d_start_y),
            color="YELLOW",
        )
        no_data_transition_line_1 = Line(
            axe.c2p(0.5, d_start_y),
            axe.c2p(0.5, d_start_y - 1),
            color="YELLOW",
        )
        initial_no_data_line_2 = Line(
            axe.c2p(0.5, d_start_y - 1),
            axe.c2p(1, d_start_y - 1),
            color="YELLOW",
        )
        no_data_transition_line_2 = Line(
            axe.c2p(1, d_start_y - 1),
            axe.c2p(1, d_start_y),
            color="YELLOW",
        )

        initial_no_clock_line_1 = Line(
            axe.c2p(0, c_start_y),
            axe.c2p(0.75, c_start_y),
            color="YELLOW",
        )
        initial_clock_transition_line = Line(
            axe.c2p(0.75, c_start_y),
            axe.c2p(0.75, c_start_y - 1),
            color="YELLOW",
        )
        initial_no_clock_line_2 = Line(
            axe.c2p(0.75, c_start_y - 1),
            axe.c2p(start_x, c_start_y - 1),
            color="YELLOW",
        )

        self.play(Create(initial_no_data_line_1), run_time=0.25)
        # self.add(initial_no_data_line_1)
        self.play(Create(no_data_transition_line_1), run_time=0.1)
        # self.add(no_data_transition_line_1)
        self.play(Create(initial_no_data_line_2), run_time=0.25)
        # self.add(initial_no_data_line_2)

        if data_bits[0]:
            self.play(Create(no_data_transition_line_2), run_time=0.1)
            # self.add(no_data_transition_line_2)

        self.play(Create(initial_no_clock_line_1), run_time=0.25)
        # self.add(initial_no_clock_line_1)
        self.play(Create(initial_clock_transition_line), run_time=0.1)
        # self.add(initial_clock_transition_line)
        self.play(Create(initial_no_clock_line_2), run_time=0.25)
        # self.add(initial_no_clock_line_2)

    def generate_clock_signal(self, length, axe, color, initial_y):
        start_x = 1
        start_y = initial_y

        for i in range(start_x, length + 1):
            end_x = i + 0.25

            low_state_start = Line(
                axe.c2p(start_x, start_y - 1),
                axe.c2p(end_x, start_y - 1),
                color=color,
            )

            rising_edge = Line(
                axe.c2p(end_x, start_y - 1),
                axe.c2p(end_x, start_y),
                color=color,
            )

            high_state = Line(
                axe.c2p(end_x, start_y),
                axe.c2p(end_x + 0.5, start_y),
                color=color,
            )

            falling_edge = Line(
                axe.c2p(end_x + 0.5, start_y),
                axe.c2p(end_x + 0.5, start_y - 1),
                color=color,
            )

            low_state_end = Line(
                axe.c2p(end_x + 0.5, start_y - 1),
                axe.c2p(end_x + 0.75, start_y - 1),
                color=color,
            )

            self.play(Create(low_state_start), run_time=0.1)
            # self.add(low_state_start)
            self.play(Create(rising_edge), run_time=0.1)
            # self.add(rising_edge)
            self.play(Create(high_state), run_time=0.1)
            # self.add(high_state)
            self.play(Create(falling_edge), run_time=0.1)
            # self.add(falling_edge)
            self.play(Create(low_state_end), run_time=0.1)
            # self.add(low_state_end)

            start_x = start_x + 1

    def stop_transmission_condition(self, data_bits, axe, d_initial_y, c_initial_y):
        d_start_y = d_initial_y + 1
        c_start_y = c_initial_y

        end_no_clock_line_1 = Line(
            axe.c2p(19, c_start_y - 1),
            axe.c2p(19.25, c_start_y - 1),
            color="YELLOW",
        )
        end_clock_transition_line = Line(
            axe.c2p(19.25, c_start_y - 1),
            axe.c2p(19.25, c_start_y),
            color="YELLOW",
        )
        end_no_clock_line_2 = Line(
            axe.c2p(19.25, c_start_y),
            axe.c2p(20, c_start_y),
            color="YELLOW",
        )

        end_no_data_transition_line_1 = Line(
            axe.c2p(19, d_start_y),
            axe.c2p(19, d_start_y - 1),
            color="YELLOW",
        )
        end_no_data_line_1 = Line(
            axe.c2p(19, d_start_y - 1),
            axe.c2p(19.5, d_start_y - 1),
            color="YELLOW",
        )
        end_no_data_transition_line_2 = Line(
            axe.c2p(19.5, d_start_y - 1),
            axe.c2p(19.5, d_start_y),
            color="YELLOW",
        )
        end_no_data_line_2 = Line(
            axe.c2p(19.5, d_start_y),
            axe.c2p(20, d_start_y),
            color="YELLOW",
        )

        self.play(Create(end_no_clock_line_1), run_time=0.25)
        # self.add(end_no_clock_line_1)
        self.play(Create(end_clock_transition_line), run_time=0.1)
        # self.add(end_clock_transition_line)
        self.play(Create(end_no_clock_line_2), run_time=0.25)
        # self.add(end_no_clock_line_2)

        if data_bits[len(data_bits) - 1]:
            self.play(Create(end_no_data_transition_line_1), run_time=0.1)
            # self.add(end_no_data_transition_line_1)

        self.play(Create(end_no_data_line_1), run_time=0.25)
        # self.add(end_no_data_line_1)
        self.play(Create(end_no_data_transition_line_2), run_time=0.1)
        # self.add(end_no_data_transition_line_2)
        self.play(Create(end_no_data_line_2), run_time=0.25)
        # self.add(end_no_data_line_2)

    def plot_step_function(self, data_bits, axe, initial_y):
        start_x = 1
        start_y = initial_y + 1

        for i, bit in enumerate(data_bits):
            custom_color = (
                "GREEN"
                if i in [0, 1, 2, 3, 4, 5, 6]
                else ("RED" if i == 7 else ("BLUE" if i == 8 or i == 17 else "ORANGE"))
            )

            #! TRANSMIT DATA
            end_x = i + 2

            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=custom_color,
            )

            curr_bit_text = (
                Text(
                    f"{ bit }",
                    font="Cascadia Code",
                    color=custom_color,
                )
                .scale(0.5)
                .next_to(line, UP, buff=0.1)
            )

            self.play(Create(line), run_time=0.5)
            # self.add(line)
            self.play(Write(curr_bit_text), run_time=0.1)
            # self.add(curr_bit_text)

            #! TRANSITION BETWEEN 1 AND 0
            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                transition_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, initial_y + data_bits[i + 1]),
                    color=custom_color,
                )

                self.play(Create(transition_line), run_time=0.25)
                # self.add(transition_line)

            start_x = end_x
            start_y = (
                initial_y + data_bits[i + 1] if i < len(data_bits) - 1 else start_y
            )

            if i in [6, 7, 8, 16, 17]:
                self.wait(0.5)

    def create_dotted_lines(self, axe, length):
        for i in range(1, length + 1):
            dotted_line = DashedLine(
                axe.c2p(i, 0),
                axe.c2p(i, 4),
                dash_length=0.05,
                dashed_ratio=0.3,
                color="GREY",
            )
            self.play(Create(dotted_line), run_time=0.1)
            # self.add(dotted_line)

    def construct(self):
        #             add______re_______ss RW  AK d____a___________t____a  AK
        data_bits = [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        axe = (
            Axes(
                x_range=[0, 20, 1],
                y_range=[0, 4, 1],
                x_length=35,
                y_length=8,
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
                x_axis_config={
                    "include_numbers": True,
                },
            )
            .scale(0.35)
            .shift(RIGHT * 0.25)
        )

        borders = SurroundingRectangle(
            axe,
            color="BLACK",
            fill_color="PURPLE",
            fill_opacity=0,
            buff=0.25,
        )

        title = (
            Text(
                "I2C Communication Protocol",
                font="Cascadia Code",
                font_size=54,
                color="RED",
            )
            .scale(0.5)
            .next_to(borders, UP)
            .shift(UP * 0)
        )

        sda_line_label = (
            Text("SDA", font="Cascadia Code", color="PURPLE")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 1.6)
        )

        scl_line_label = (
            Text("CSL", font="Cascadia Code", color="RED")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 0.2)
        )

        inactive_line_label = (
            Text("→ Inactive", font="Cascadia Code", color="YELLOW")
            .scale(0.5)
            .next_to(borders, DOWN)
            .align_to(borders, LEFT)
        )
        address_line_label = (
            Text("→ Address", font="Cascadia Code", color="GREEN")
            .scale(0.5)
            .next_to(inactive_line_label, RIGHT, buff=0.5)
        )
        RW_line_label = (
            Text("→ Read/Write", font="Cascadia Code", color="RED")
            .scale(0.5)
            .next_to(borders, DOWN)
        )
        data_line_label = (
            Text("→ Data", font="Cascadia Code", color="ORANGE")
            .scale(0.5)
            .next_to(borders, DOWN)
            .align_to(borders, RIGHT)
        )
        ACK_line_label = (
            Text("→ ACK/NACK", font="Cascadia Code", color="BLUE")
            .scale(0.5)
            .next_to(data_line_label, LEFT, buff=0.5)
        )

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        self.wait(0.25)
        self.add(axe)
        self.wait(0.25)
        self.create_dotted_lines(axe, 19)
        self.wait(0.5)

        self.play(Write(sda_line_label), run_time=0.2)
        # self.add(sda_line_label)
        self.wait(0.25)
        self.play(Write(scl_line_label), run_time=0.2)
        # self.add(scl_line_label)
        self.wait(0.25)

        self.start_transmission_condition(data_bits, axe, d_initial_y=2, c_initial_y=1)
        self.wait(0.25)

        self.generate_clock_signal(18, axe, "RED", initial_y=1)
        self.wait(0.25)

        self.plot_step_function(data_bits, axe, initial_y=2)
        self.wait(0.25)

        self.stop_transmission_condition(data_bits, axe, d_initial_y=2, c_initial_y=1)
        self.wait(0.25)

        self.play(Write(inactive_line_label))
        # self.add(inactive_line_label)
        self.wait(0.25)
        self.play(Write(address_line_label))
        # self.add(address_line_label)
        self.wait(0.25)
        self.play(Write(RW_line_label))
        # self.add(RW_line_label)
        self.wait(0.25)
        self.play(Write(ACK_line_label))
        # self.add(ACK_line_label)
        self.wait(0.25)
        self.play(Write(data_line_label))
        # self.add(data_line_label)

        self.wait(0.5)
        self.play(Write(title))
        # self.add(title)

        self.wait(2)
