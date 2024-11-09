from turtle import title
from manim import *


class Main(Scene):
    def construct(self):
        #            .  .  s  d_____a________t_____a  e  .
        data_bits = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]

        axe = (
            Axes(
                x_range=[0, 13, 1],
                y_range=[0, 2, 1],
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
            )
            .add_coordinates()
            .to_edge(DL)
        )

        title = Text("UART Communication Protocol", color="RED").shift(UP * 2)

        self.add(axe)
        self.wait(1)

        start_x = 0
        start_y = data_bits[0]

        for i, bit in enumerate(data_bits):
            #! TRANSMIT DATA
            end_x = i + 1
            line = Line(
                axe.c2p(start_x, start_y), axe.c2p(end_x, start_y), color="BLUE"
            )
            self.play(Create(line), run_time=1)

            #! TRANSITION BETWEEN 1 AND 0
            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                vert_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, data_bits[i + 1]),
                    color=BLUE,
                )
                self.play(Create(vert_line), run_time=0.5)

            start_x = end_x
            start_y = data_bits[i + 1] if i < len(data_bits) - 1 else start_y

        self.wait(1)
        self.play(Write(title))
