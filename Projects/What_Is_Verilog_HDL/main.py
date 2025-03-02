from manim import *

IS_DEBUGGING = False
# IS_DEBUGGING = True


class Main(Scene):
    def waiting_to_read(
        self, wait_counter=8, wait_delay=0.6, note_position=0.4, note_color=ORANGE
    ):
        waiting_note = Text(
            "- Pause to read -", font="Cascadia Code", font_size=16, color=note_color
        ).move_to(
            DOWN * (self.camera.frame_height / 2) + UP * note_position  # type: ignore
        )

        for _ in range(int(wait_counter / 2)):
            self.add(waiting_note)
            self.wait(wait_delay)
            self.remove(waiting_note)
            self.wait(wait_delay)

    def topic_introduction(self, text_title):
        # + Title Element
        title = Text(
            text_title,
            font="Cascadia Code",
            font_size=54,
            color="RED",
        ).scale(0.5)

        # - Animate Title Element
        if not IS_DEBUGGING:
            self.play(Write(title))
            self.play(title.animate.to_edge(UP), run_time=1)  # type: ignore
        else:
            self.add(title)
            title.to_edge(UP)

        return title

    def topic_definition(self):
        # + Definition Element
        hdl_definition = MarkupText(
            f"&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span fgcolor='{ORANGE}'>HDL</span> stands for\n"
            + f"&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span fgcolor='{ORANGE}'>H</span>ardware <span fgcolor='{ORANGE}'>D</span>escription <span fgcolor='{ORANGE}'>L</span>anguage.\n"
            + f"It describes <span fgcolor='{YELLOW}'>digital circuits</span> in textual format!",
            font="Cascadia Code",
            font_size=21,
        )

        # - Animate Definition Element
        if not IS_DEBUGGING:
            self.play(Write(hdl_definition))
        else:
            self.add(hdl_definition)

        return hdl_definition

    def create_and_gate(self, length=0.5):
        # + AND Gate Elements
        and_top_horiz_line = Line(start=[-length - (length / 2), length, 0], end=[length - (length / 2), length, 0]).shift(RIGHT * 1.25)  # type: ignore
        and_bot_horiz_line = Line(start=[-length - (length / 2), -length, 0], end=[length - (length / 2), -length, 0]).shift(RIGHT * 1.25)  # type: ignore
        and_lft_verti_line = Line(
            and_top_horiz_line.get_start(), and_bot_horiz_line.get_start()
        )
        and_rgt_curve_line = ArcBetweenPoints(
            and_top_horiz_line.get_end(), and_bot_horiz_line.get_end(), radius=-length
        )

        and_input_1 = Line(
            start=and_lft_verti_line.get_start() + (2 * length / 4) * DOWN,
            end=and_lft_verti_line.get_start()
            + (2 * length / 4) * DOWN
            + LEFT * length,
        )
        and_input_2 = Line(
            start=and_lft_verti_line.get_start() + 3 * (2 * length / 4) * DOWN,
            end=and_lft_verti_line.get_start()
            + 3 * (2 * length / 4) * DOWN
            + LEFT * length,
        )
        and_output = Line(
            start=and_rgt_curve_line.get_arc_center() + RIGHT * length,
            end=and_rgt_curve_line.get_arc_center() + RIGHT * length * 2,
        )

        gate_name = Text(
            "AND",
            font="Cascadia Code",
            font_size=60 * length,
        ).move_to(
            (and_lft_verti_line.get_center() + and_output.get_start()) / 2  # type: ignore
        )

        # - Animate AND Gate Elements
        # if not IS_DEBUGGING:
        #     self.play(Create(and_top_horiz_line), Create(and_bot_horiz_line))
        #     self.play(Create(and_lft_verti_line), Create(and_rgt_curve_line))
        #     self.play(Create(and_input_1), Create(and_input_2), Create(and_output))
        #     self.play(Write(gate_name))
        # else:
        self.add(
            and_top_horiz_line,
            and_bot_horiz_line,
            and_lft_verti_line,
            and_rgt_curve_line,
        )
        self.add(and_input_1, and_input_2, and_output)
        self.add(gate_name)

        return [
            VGroup(
                and_top_horiz_line,
                and_bot_horiz_line,
                and_lft_verti_line,
                and_rgt_curve_line,
                and_input_1,
                and_input_2,
                and_output,
                gate_name,
            ),
            (and_lft_verti_line.get_start() + (2 * length / 4) * DOWN + LEFT * length),
            (
                and_lft_verti_line.get_start()
                + 3 * (2 * length / 4) * DOWN
                + LEFT * length
            ),
            (and_rgt_curve_line.get_arc_center() + RIGHT * length * 2),
        ]

    def create_or_gate(self, length=0.5):
        # + OR Gate Elements
        or_top_arc = ArcBetweenPoints(
            start=[-length, -length, 0], end=[length, 0, 0], angle=PI / 4  # type: ignore
        ).shift(UP * 1.25 + LEFT * 1.25)
        or_bot_arc = ArcBetweenPoints(
            start=[-length, length, 0],  # type: ignore
            end=[length, 0, 0],  # type: ignore
            angle=-PI / 4,
        ).shift(UP * 1.25 + LEFT * 1.25)
        or_lft_arc = ArcBetweenPoints(
            start=[-length, length, 0],  # type: ignore
            end=[-length, -length, 0],  # type: ignore
            angle=-PI / 3,
        ).shift(UP * 1.25 + LEFT * 1.25)

        or_input_1 = Line(
            start=or_lft_arc.get_start()
            + (2 * length / 4) * DOWN
            + RIGHT * PI / 15 * length,
            end=or_lft_arc.get_start() + (2 * length / 4) * DOWN + LEFT * length,
        )
        or_input_2 = Line(
            start=or_lft_arc.get_start()
            + 3 * (2 * length / 4) * DOWN
            + RIGHT * PI / 15 * length,
            end=or_lft_arc.get_start() + 3 * (2 * length / 4) * DOWN + LEFT * length,
        )
        or_output = Line(
            start=or_top_arc.get_end(),
            end=or_top_arc.get_end() + RIGHT * length,
        )

        gate_name = Text(
            "OR",
            font="Cascadia Code",
            font_size=60 * length,
        ).shift(UP * 1.25 + LEFT * 1.25)

        # - Animate OR Gate Elements
        # if not IS_DEBUGGING:
        #     self.play(Create(or_top_arc), Create(or_bot_arc))
        #     self.play(Create(or_lft_arc))
        #     self.play(Create(or_input_1), Create(or_input_2), Create(or_output))
        #     self.play(Write(gate_name))
        # else:
        self.add(
            or_top_arc,
            or_bot_arc,
            or_lft_arc,
        )
        self.add(or_input_1, or_input_2, or_output)
        self.add(gate_name)

        return [
            VGroup(
                or_top_arc,
                or_bot_arc,
                or_lft_arc,
                or_input_1,
                or_input_2,
                or_output,
                gate_name,
            ),
            (or_lft_arc.get_start() + (2 * length / 4) * DOWN + LEFT * length),
            (or_lft_arc.get_start() + 3 * (2 * length / 4) * DOWN + LEFT * length),
            (or_top_arc.get_end() + RIGHT * length),
        ]

    def create_not_gate(self, length=0.5):
        # + NOT Gate Elements
        not_top_line = Line(
            start=[-length, length, 0], end=[length, 0, 0]  # type: ignore
        ).shift(DOWN * 1.25 + LEFT * 1.25)
        not_bot_line = Line(
            start=[-length, -length, 0], end=[length, 0, 0]  # type: ignore
        ).shift(DOWN * 1.25 + LEFT * 1.25)
        not_lft_line = Line(
            start=[-length, length, 0], end=[-length, -length, 0]  # type: ignore
        ).shift(DOWN * 1.25 + LEFT * 1.25)
        not_circle = Circle(radius=length / 5, color=WHITE).next_to(
            not_top_line.get_end(), buff=0
        )

        not_input = Line(
            start=not_lft_line.get_center(),
            end=not_lft_line.get_center() + LEFT * length,
        )
        not_output = Line(
            start=not_top_line.get_end() + RIGHT * 2 * (length / 5),
            end=not_top_line.get_end() + RIGHT * 2 * (length / 5) + RIGHT * length,
        )

        gate_name = Text(
            "NOT",
            font="Cascadia Code",
            font_size=50 * length,
        ).next_to(not_lft_line, buff=0.15 * length)

        # - Animate NOT Gate Elements
        # if not IS_DEBUGGING:
        #     self.play(Create(not_top_line), Create(not_bot_line))
        #     self.play(Create(not_lft_line))
        #     self.play(Create(not_circle))
        #     self.play(Create(not_input), Create(not_output))
        #     self.play(Write(gate_name))
        # else:
        self.add(not_top_line, not_bot_line, not_lft_line, not_circle)
        self.add(not_input, not_output)
        self.add(gate_name)

        return [
            VGroup(
                not_top_line,
                not_bot_line,
                not_lft_line,
                not_circle,
                not_input,
                not_output,
                gate_name,
            ),
            (not_lft_line.get_center() + LEFT * length),
            (not_top_line.get_end() + RIGHT * 2 * (length / 5) + RIGHT * length),
        ]

    def digital_circuit_example(self, length, title_element):
        # + Title Element
        digital_circuit_title = Text(
            "Digital Circuit Example",
            font="Cascadia Code",
            font_size=54,
            color="RED",
        ).scale(0.5)

        # - Animate Title Element
        if not IS_DEBUGGING:
            self.play(Write(digital_circuit_title))
            self.play(
                title_element.animate.shift(LEFT * 10),
                digital_circuit_title.animate.to_edge(UP),  # type: ignore
                run_time=1,
            )
        else:
            self.add(digital_circuit_title)
            self.remove(title_element)
            digital_circuit_title.to_edge(UP)

        and_gate, and_in_1, and_in_2, and_out = self.create_and_gate(length=length)
        or_gate, or_in_1, or_in_2, or_out = self.create_or_gate(length=length)
        not_gate, not_in, not_out = self.create_not_gate(length=length)

        wire_1_part_1 = Line(or_out, or_out + RIGHT * (1.15 / 2), color=ORANGE)
        wire_1_part_2 = Line(
            or_out + RIGHT * (1.15 / 2), and_in_1 + LEFT * (1.15 / 2), color=ORANGE
        )
        wire_1_part_3 = Line(and_in_1 + LEFT * (1.15 / 2), and_in_1, color=ORANGE)

        wire_2_part_1 = Line(not_out, not_out + RIGHT * (1.03 - 1.15 / 2), color=GREEN)
        wire_2_part_2 = Line(
            not_out + RIGHT * (1.03 - 1.15 / 2),
            and_in_2 + LEFT * (1.15 / 2),
            color=GREEN,
        )
        wire_2_part_3 = Line(and_in_2 + LEFT * (1.15 / 2), and_in_2, color=GREEN)

        or_in_1_extend = Line(start=or_in_1, end=or_in_1 + LEFT * 0.5, color=YELLOW)
        or_in_2_extend = Line(start=or_in_2, end=or_in_2 + LEFT * 0.5, color=YELLOW)
        not_in_extend = Line(start=not_in, end=not_in + LEFT * 0.5, color=YELLOW)
        and_out_extend = Line(start=and_out, end=and_out + RIGHT * 0.5, color=BLUE)

        if not IS_DEBUGGING:
            self.play(Create(wire_1_part_1))
            self.play(Create(wire_1_part_2))
            self.play(Create(wire_1_part_3))
            self.play(Create(wire_2_part_1))
            self.play(Create(wire_2_part_2))
            self.play(Create(wire_2_part_3))
            self.play(
                Create(or_in_1_extend), Create(or_in_2_extend), Create(not_in_extend)
            )
            self.play(Create(and_out_extend))
        else:
            self.add(wire_1_part_1, wire_1_part_2, wire_1_part_3)
            self.add(wire_2_part_1, wire_2_part_2, wire_2_part_3)
            self.add(or_in_1_extend, or_in_2_extend, not_in_extend, and_out_extend)

        # dist = Text(f"{not_out[0] - and_in_2[0]}")
        # self.add(dist)

    def construct(self):
        self.wait(0.25)  # ! ---- ---- ----

        # & Introduction                                                        :
        title = self.topic_introduction("What is HDL?")

        self.wait(0.25)  # ! ---- ---- ----

        # & Definition                                                          :
        hdl_definition = self.topic_definition()
        self.waiting_to_read(
            wait_counter=4, wait_delay=0.8, note_color=BLUE
        )  # ! ---- ---- ----
        self.play(FadeOut(hdl_definition))

        self.wait(0.25)  # ! ---- ---- ----

        # & Digital Circuit Example                                             :
        self.digital_circuit_example(length=0.3, title_element=title)

        self.wait(2)  # ! ---- ---- ----
