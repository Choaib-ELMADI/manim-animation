from manim import *


class Main(Scene):
    def plot_step_function(self, data_bits, axe):
        is_transmitting = False
        sent_bits_counter = 0

        start_x = 0
        start_y = data_bits[0]

        for i, bit in enumerate(data_bits):
            if not is_transmitting and bit == 0:
                is_transmitting = True

            if is_transmitting and sent_bits_counter <= 10:
                sent_bits_counter += 1

            if sent_bits_counter > 10:
                is_transmitting = False

            #! TRANSMIT DATA
            end_x = i + 1

            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color="BLUE" if is_transmitting else "YELLOW",
            )

            curr_bit_text = (
                Text(
                    f"{ bit }",
                    font="Cascadia Code",
                    color="BLUE" if is_transmitting else "YELLOW",
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
                vert_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, data_bits[i + 1]),
                    color="GREEN",
                )

                self.play(Create(vert_line), run_time=0.25)
                # self.add(vert_line)

            start_x = end_x
            start_y = data_bits[i + 1] if i < len(data_bits) - 1 else start_y

    def construct(self):
        #             .  .  s  d_____a_________t_____a  e  .  .
        data_bits = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1]

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        axe = (
            Axes(
                x_range=[0, 14, 1],
                y_range=[0, 2, 1],
                x_length=21,
                y_length=4,
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
            )
            .add_coordinates()
            .scale(0.5)
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
                "UART Communication Protocol",
                font="Cascadia Code",
                font_size=54,
                color="RED",
            )
            .scale(0.5)
            .next_to(borders, UP)
            .shift(UP * 0)
        )

        inactive_line_label = (
            Text("→ Inactive", font="Cascadia Code", color="YELLOW")
            .scale(0.5)
            .next_to(borders, DOWN)
            .align_to(borders, LEFT)
        )
        data_line_label = (
            Text("→ Data", font="Cascadia Code", color="BLUE")
            .scale(0.5)
            .next_to(borders, DOWN)
        )
        transition_line_label = (
            Text("→ Transition", font="Cascadia Code", color="GREEN")
            .scale(0.5)
            .next_to(borders, DOWN)
            .align_to(borders, RIGHT)
        )

        #! ---- --- -- - ---- --- -- - ---- --- -- - ---- --- -- - !#

        self.wait(0.25)
        self.add(axe)
        self.wait(0.5)

        self.plot_step_function(data_bits, axe)

        self.wait(0.25)
        ## self.play(DrawBorderThenFill(borders))
        ## self.add(borders)
        ## self.wait(1)

        self.play(Write(inactive_line_label))
        # self.add(inactive_line_label)
        self.wait(0.25)
        self.play(Write(data_line_label))
        # self.add(data_line_label)
        self.wait(0.25)
        self.play(Write(transition_line_label))
        # self.add(transition_line_label)

        self.wait(0.5)
        self.play(Write(title))
        # self.add(title)

        self.wait(2)
