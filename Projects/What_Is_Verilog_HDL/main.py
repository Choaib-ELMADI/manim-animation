from manim import *

# IS_DEBUGGING = False
IS_DEBUGGING = True


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

    def topics(self, title):
        # + Topics Element
        topics = Paragraph(
            "Definition",
            "•",
            "Digital Circuit Example",
            "•",
            "Verilog HDL",
            font="Cascadia Code",
            font_size=16,
        )
        topics_length = len(topics)

        topics[int(topics_length / 2)].next_to(title, DOWN, buff=0.2)
        for i in range(int(topics_length / 2) - 1, -1, -1):
            topics[i].next_to(topics[i + 1], LEFT, buff=0.15)
        for i in range(int(topics_length / 2), topics_length - 1):
            topics[i + 1].next_to(topics[i], RIGHT, buff=0.15)

        # - Animate Topics Element
        if not IS_DEBUGGING:
            self.play(Write(topics))
        else:
            self.add(topics)

        return topics

    def topic_definition(self):
        # + Definition Element
        hdl_definition = MarkupText(
            f"&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span fgcolor='{ORANGE}'>HDL</span> stands for\n"
            + f"&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;<span fgcolor='{ORANGE}'>H</span>ardware <span fgcolor='{ORANGE}'>D</span>escription <span fgcolor='{ORANGE}'>L</span>anguage.\n"
            + f"&#160;&#160;&#160;It describes <span fgcolor='{YELLOW}'>digital circuits</span> in a textual format,\n"
            + f"allowing us to <span fgcolor='{PURPLE}'>model</span>, <span fgcolor='{GREEN}'>simulate</span>, and <span fgcolor='{BLUE}'>synthesize</span> hardware!\n",
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

        # Returns: gate, gate_in_1_start, gate_in_2_start, gate_out_end, gate_in_1, gate_in_2, gate_out
        return (
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
            and_input_1,
            and_input_2,
            and_output,
        )

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

        # Returns: gate, gate_in_1_start, gate_in_2_start, gate_out_end, gate_in_1, gate_in_2, gate_out
        return (
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
            or_input_1,
            or_input_2,
            or_output,
        )

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

        # Returns: gate, gate_in_start, gate_out_end, gate_in, gate_out
        return (
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
            not_input,
            not_output,
        )

    def digital_circuit_example(self, length, topics):
        # + Digital Circuit Example Elements
        (
            and_gate,
            and_in_1,
            and_in_2,
            and_out,
            and_pin_1_in,
            and_pin_2_in,
            and_pin_out,
        ) = self.create_and_gate(length=length)
        (
            or_gate,
            or_in_1,
            or_in_2,
            or_out,
            or_pin_1_in,
            or_pin_2_in,
            or_pin_out,
        ) = self.create_or_gate(length=length)
        (
            not_gate,
            not_in,
            not_out,
            not_pin_in,
            not_pin_out,
        ) = self.create_not_gate(length=length)

        wire_1_part_1 = Line(or_out, or_out + RIGHT * (1.15 / 2), color=WHITE)
        wire_1_part_2 = Line(
            or_out + RIGHT * (1.15 / 2), and_in_1 + LEFT * (1.15 / 2), color=WHITE
        )
        wire_1_part_3 = Line(and_in_1 + LEFT * (1.15 / 2), and_in_1, color=WHITE)

        wire_2_part_1 = Line(not_out, not_out + RIGHT * (1.03 - 1.15 / 2), color=WHITE)
        wire_2_part_2 = Line(
            not_out + RIGHT * (1.03 - 1.15 / 2),
            and_in_2 + LEFT * (1.15 / 2),
            color=WHITE,
        )
        wire_2_part_3 = Line(and_in_2 + LEFT * (1.15 / 2), and_in_2, color=WHITE)

        or_in_1_extend = Line(end=or_in_1 + LEFT * 0.5, start=or_in_1, color=WHITE)
        or_not_vert_extend = Line(start=or_in_2, end=not_in, color=WHITE)
        or_not_hori_extend = Line(
            end=or_not_vert_extend.get_center() + LEFT * 0.5,
            start=or_not_vert_extend.get_center(),
            color=WHITE,
        )
        or_not_vert_extend_top = Line(
            end=or_not_vert_extend.get_center(), start=or_in_2, color=WHITE
        )
        or_not_vert_extend_bot = Line(
            end=or_not_vert_extend.get_center(), start=not_in, color=WHITE
        )
        and_out_extend = Line(start=and_out, end=and_out + RIGHT * 0.5, color=WHITE)

        or_in_1_label = Text(
            "a", font="Cascadia Code", font_size=21, color=WHITE
        ).next_to(or_in_1_extend, LEFT, buff=0.1)
        or_not_hori_label = Text(
            "b", font="Cascadia Code", font_size=21, color=WHITE
        ).next_to(or_not_hori_extend, LEFT, buff=0.1)
        and_out_label = Text(
            "out", font="Cascadia Code", font_size=21, color=WHITE
        ).next_to(and_out_extend, RIGHT, buff=0.1)

        or_gate_module_box = DashedVMobject(
            SurroundingRectangle(
                or_gate,
                buff=0.15,
            ),
            num_dashes=30,
            dashed_ratio=0.6,
        )
        not_gate_module_box = DashedVMobject(
            SurroundingRectangle(
                not_gate,
                buff=0.15,
            ),
            num_dashes=30,
            dashed_ratio=0.6,
        )
        and_gate_module_box = DashedVMobject(
            SurroundingRectangle(
                and_gate,
                buff=0.15,
            ),
            num_dashes=30,
            dashed_ratio=0.6,
        )
        module_box = DashedVMobject(
            SurroundingRectangle(
                VGroup(or_gate_module_box, not_gate_module_box, and_gate_module_box),
                buff=0.15,
                color=GREEN,
            ),
            num_dashes=40,
            dashed_ratio=0.6,
        )

        digital_circuit_example = VGroup(
            and_gate,
            or_gate,
            not_gate,
            wire_1_part_1,
            wire_1_part_2,
            wire_1_part_3,
            wire_2_part_1,
            wire_2_part_2,
            wire_2_part_3,
            or_in_1_extend,
            or_not_vert_extend_top,
            or_not_vert_extend_bot,
            or_not_hori_extend,
            and_out_extend,
            or_in_1_label,
            or_not_hori_label,
            and_out_label,
        )

        verilog_hdl_code = MarkupText(
            f"<span fgcolor='{ORANGE}'>module</span> <span fgcolor='{YELLOW}'>circuit (</span>out, a, b<span fgcolor='{YELLOW}'>)</span>;\n"
            + f"    <span fgcolor='{PURPLE}'>output reg  </span>out;\n"
            + f"    <span fgcolor='{PURPLE}'>input  wire </span>a;\n"
            + f"    <span fgcolor='{PURPLE}'>input  wire </span>b;\n"
            + f"\n"
            + f"    <span fgcolor='{PURPLE}'>wire </span>wire_1;\n"
            + f"    <span fgcolor='{PURPLE}'>wire </span>wire_2;\n"
            + f"\n"
            + f"    <span fgcolor='{RED}'>or  or_1  </span><span fgcolor='{YELLOW}'>(</span>wire_1, a, b<span fgcolor='{YELLOW}'>)</span>;\n"
            + f"    <span fgcolor='{RED}'>not not_1 </span><span fgcolor='{YELLOW}'>(</span>wire_2, b<span fgcolor='{YELLOW}'>)</span>;\n"
            + f"    <span fgcolor='{RED}'>and and_1 </span><span fgcolor='{YELLOW}'>(</span>out, wire_1, wire_2<span fgcolor='{YELLOW}'>)</span>;\n"
            + f"\n"
            + f"<span fgcolor='{ORANGE}'>endmodule </span><span fgcolor='{GREEN}'>// circuit</span>\n"
            + f"\n",
            font="Cascadia Code",
            font_size=20,
        ).shift(RIGHT * 3)
        verilog_hdl_code_box = always_redraw(
            lambda: SurroundingRectangle(
                verilog_hdl_code, color=WHITE, fill_opacity=0.05, buff=0.25
            )
        )
        verilog_hdl_code_title = always_redraw(
            lambda: Text(
                "Verilog HDL", color=WHITE, font="Cascadia Code", font_size=18
            ).next_to(verilog_hdl_code_box, DOWN)
        )

        design_modules = Text(
            "These are the design modules!",
            font="Cascadia Code",
            font_size=21,
            color=ORANGE,
        ).next_to(module_box, DOWN, buff=0.5)
        underline = Underline(design_modules, buff=0.05, color=ORANGE, stroke_width=3)

        lower_level_modules = Text(
            "Lower Level Modules",
            font="Cascadia Code",
            font_size=20,
            color=YELLOW,
        ).next_to(or_not_hori_label, LEFT, buff=0.5)
        lower_level_modules_box = SurroundingRectangle(
            lower_level_modules,
            buff=0.1,
        )
        or_gate_module_arrow = CurvedArrow(
            start_point=or_gate_module_box.get_edge_center(LEFT),
            end_point=lower_level_modules_box.get_corner(UR) + LEFT * 0.2,
            angle=PI / 4,
            color=YELLOW,
            stroke_width=3,
            tip_length=0.1,
        )
        or_gate_module_arrow_circle = Circle(
            radius=0.02, color=YELLOW, fill_color=YELLOW, fill_opacity=1
        ).move_to(or_gate_module_arrow.get_start())
        not_gate_module_arrow = CurvedArrow(
            start_point=not_gate_module_box.get_edge_center(LEFT),
            end_point=lower_level_modules_box.get_corner(DR) + LEFT * 0.2,
            angle=-PI / 4,
            color=YELLOW,
            stroke_width=3,
            tip_length=0.1,
        )
        not_gate_module_arrow_circle = Circle(
            radius=0.02, color=YELLOW, fill_color=YELLOW, fill_opacity=1
        ).move_to(not_gate_module_arrow.get_start())
        and_gate_module_arrow = CurvedArrow(
            start_point=and_gate_module_box.get_edge_center(LEFT),
            end_point=lower_level_modules_box.get_edge_center(RIGHT),
            angle=-PI / 3,
            color=YELLOW,
            stroke_width=3,
            tip_length=0.1,
        )
        and_gate_module_arrow_circle = Circle(
            radius=0.02, color=YELLOW, fill_color=YELLOW, fill_opacity=1
        ).move_to(and_gate_module_arrow.get_start())

        higher_level_module = Text(
            "Higher Level Module",
            font="Cascadia Code",
            font_size=20,
            color=GREEN,
        ).next_to(and_out_label, RIGHT, buff=0.5)
        higher_level_module_box = SurroundingRectangle(
            higher_level_module,
            buff=0.1,
        )
        digital_circuit_arrow = CurvedArrow(
            start_point=module_box.get_edge_center(RIGHT)
            + (module_box.get_height() / 4) * DOWN,
            end_point=higher_level_module_box.get_edge_center(DOWN),
            angle=PI / 2,
            color=GREEN,
            stroke_width=3,
            tip_length=0.1,
        )
        digital_circuit_arrow_circle = Circle(
            radius=0.02, color=GREEN, fill_color=GREEN, fill_opacity=1
        ).move_to(digital_circuit_arrow.get_start())

        code_highlight_box_1 = (
            Rectangle(
                color=YELLOW,
                height=0.34,
                width=2.55,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + RIGHT * 0.5)
        )
        code_highlight_box_2 = (
            Rectangle(
                color=YELLOW,
                height=0.34,
                width=2.55,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + DOWN * 0.32 + RIGHT * 0.5)
        )
        code_highlight_box_3 = (
            Rectangle(
                color=YELLOW,
                height=0.34,
                width=2.55,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + 2 * DOWN * 0.32 + RIGHT * 0.5)
        )

        code_highlight_box_4 = (
            Rectangle(
                color=RED,
                height=0.34,
                width=1.95,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + 4 * DOWN * 0.32 + RIGHT * 0.5)
        )
        code_highlight_box_5 = (
            Rectangle(
                color=RED,
                height=0.34,
                width=1.95,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + 5 * DOWN * 0.32 + RIGHT * 0.5)
        )

        code_highlight_box_6 = (
            Rectangle(
                color=PURPLE,
                height=0.34,
                width=4.95,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + 7 * DOWN * 0.32 + RIGHT * 0.5)
        )
        code_highlight_box_7 = (
            Rectangle(
                color=GOLD,
                height=0.34,
                width=4.95,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.58 + 8 * DOWN * 0.32 + RIGHT * 0.5)
        )
        code_highlight_box_8 = (
            Rectangle(
                color=GRAY,
                height=0.34,
                width=4.95,
                stroke_width=1.5,
                fill_opacity=0.05,
            )
            .align_to(verilog_hdl_code, LEFT)
            .shift(UP * 1.57 + 9 * DOWN * 0.32 + RIGHT * 0.5)
        )

        # - Animate Digital Circuit Example Elements
        if not IS_DEBUGGING:
            self.play(Create(wire_1_part_1), run_time=0.35)
            self.play(Create(wire_1_part_2), run_time=0.35)
            self.play(Create(wire_1_part_3), run_time=0.35)
            self.play(Create(wire_2_part_1), run_time=0.35)
            self.play(Create(wire_2_part_2), run_time=0.35)
            self.play(Create(wire_2_part_3), run_time=0.35)
            self.play(
                Create(or_not_vert_extend_top),
                Create(or_not_vert_extend_bot),
                run_time=0.35,
            )
            self.play(
                Create(or_in_1_extend),
                Create(or_not_hori_extend),
                Create(and_out_extend),
                run_time=0.35,
            )
            self.play(
                Write(or_in_1_label),
                Write(or_not_hori_label),
                Write(and_out_label),
            )
        else:
            self.add(wire_1_part_1, wire_1_part_2, wire_1_part_3)
            self.add(wire_2_part_1, wire_2_part_2, wire_2_part_3)
            self.add(
                or_in_1_extend,
                or_not_vert_extend_top,
                or_not_vert_extend_bot,
                or_not_hori_extend,
                and_out_extend,
            )
            self.add(or_in_1_label, or_not_hori_label, and_out_label)

        if not IS_DEBUGGING:
            self.play(
                Create(or_gate_module_box),
                Create(not_gate_module_box),
                Create(and_gate_module_box),
            )
            self.play(
                Create(module_box),
            )
        else:
            self.add(or_gate_module_box, not_gate_module_box, and_gate_module_box)
            self.add(module_box)

        if not IS_DEBUGGING:
            self.play(Write(design_modules))
            self.play(Create(underline))
            self.play(Write(lower_level_modules))
            self.add(
                or_gate_module_arrow_circle,
                not_gate_module_arrow_circle,
                and_gate_module_arrow_circle,
            )
            self.play(
                Create(or_gate_module_arrow),
                Create(not_gate_module_arrow),
                Create(and_gate_module_arrow),
                run_time=0.75,
            )
            self.play(Write(higher_level_module))
            self.add(
                digital_circuit_arrow_circle,
            )
            self.play(
                Create(digital_circuit_arrow),
                run_time=0.75,
            )
        else:
            self.add(design_modules, underline)
            self.add(lower_level_modules, higher_level_module)
            self.add(
                or_gate_module_arrow_circle,
                not_gate_module_arrow_circle,
                and_gate_module_arrow_circle,
                digital_circuit_arrow_circle,
            )
            self.add(
                or_gate_module_arrow,
                not_gate_module_arrow,
                and_gate_module_arrow,
                digital_circuit_arrow,
            )

        self.waiting_to_read(
            wait_counter=4, wait_delay=0.8, note_color=BLUE
        )  # ! ---- ---- ----

        self.play(
            FadeOut(
                or_gate_module_box,
                not_gate_module_box,
                and_gate_module_box,
                module_box,
                design_modules,
                underline,
                lower_level_modules,
                higher_level_module,
                or_gate_module_arrow,
                not_gate_module_arrow,
                and_gate_module_arrow,
                digital_circuit_arrow,
                or_gate_module_arrow_circle,
                not_gate_module_arrow_circle,
                and_gate_module_arrow_circle,
                digital_circuit_arrow_circle,
            )
        )

        self.wait(0.25)  # ! ---- ---- ----

        topics[2].set_color(WHITE)
        topics[4].set_color(YELLOW)

        self.wait(0.25)  # ! ---- ---- ----

        self.play(digital_circuit_example.animate.shift(LEFT * 3.5))  # type: ignore

        if not IS_DEBUGGING:
            self.play(Write(verilog_hdl_code))
            self.play(Create(verilog_hdl_code_box))  # type: ignore
            self.play(Write(verilog_hdl_code_title))  # type: ignore
        else:
            self.add(verilog_hdl_code, verilog_hdl_code_box, verilog_hdl_code_title)

        self.waiting_to_read(
            wait_counter=4, wait_delay=0.8, note_color=BLUE
        )  # ! ---- ---- ----

        # ! 1
        self.play(Create(code_highlight_box_1), run_time=0.5)
        self.wait(0.1)  # ! ---- ---- ----
        self.play(
            ApplyMethod(and_pin_out.set_color, YELLOW),
            ApplyMethod(and_out_extend.set_color, YELLOW),
            ApplyMethod(and_out_label.set_color, YELLOW),
            run_time=0.1,
        )
        self.play(
            VGroup(
                and_pin_out,
                and_out_extend,
                and_out_label,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                and_pin_out,
                and_out_extend,
                and_out_label,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.wait(0.1)  # ! ---- ---- ----
        self.play(FadeOut(code_highlight_box_1), run_time=0.5)

        # ! 2
        self.play(Create(code_highlight_box_2), run_time=0.5)
        self.wait(0.1)  # ! ---- ---- ----
        self.play(
            ApplyMethod(or_in_1_label.set_color, YELLOW),
            ApplyMethod(or_in_1_extend.set_color, YELLOW),
            ApplyMethod(or_pin_1_in.set_color, YELLOW),
            run_time=0.1,
        )
        self.play(
            VGroup(
                or_in_1_label,
                or_in_1_extend,
                or_pin_1_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                or_in_1_label,
                or_in_1_extend,
                or_pin_1_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.wait(0.1)  # ! ---- ---- ----
        self.play(FadeOut(code_highlight_box_2), run_time=0.5)

        # ! 3
        self.play(Create(code_highlight_box_3), run_time=0.5)
        self.wait(0.1)  # ! ---- ---- ----
        self.play(
            ApplyMethod(or_not_hori_label.set_color, YELLOW),
            ApplyMethod(or_not_hori_extend.set_color, YELLOW),
            ApplyMethod(or_not_vert_extend_top.set_color, YELLOW),
            ApplyMethod(or_not_vert_extend_bot.set_color, YELLOW),
            ApplyMethod(or_pin_2_in.set_color, YELLOW),
            ApplyMethod(not_pin_in.set_color, YELLOW),
            run_time=0.1,
        )
        self.play(
            VGroup(
                or_not_hori_label,
                or_not_hori_extend,
                or_not_vert_extend_top,
                or_not_vert_extend_bot,
                or_pin_2_in,
                not_pin_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                or_not_hori_label,
                or_not_hori_extend,
                or_not_vert_extend_top,
                or_not_vert_extend_bot,
                or_pin_2_in,
                not_pin_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.wait(0.1)  # ! ---- ---- ----
        self.play(FadeOut(code_highlight_box_3), run_time=0.5)

        # ! 4
        self.play(Create(code_highlight_box_4), run_time=0.5)
        self.wait(0.1)  # ! ---- ---- ----
        self.play(
            ApplyMethod(or_pin_out.set_color, RED),
            ApplyMethod(wire_1_part_1.set_color, RED),
            ApplyMethod(wire_1_part_2.set_color, RED),
            ApplyMethod(wire_1_part_3.set_color, RED),
            ApplyMethod(and_pin_1_in.set_color, RED),
            run_time=0.1,
        )
        self.play(
            VGroup(
                or_pin_out,
                wire_1_part_1,
                wire_1_part_2,
                wire_1_part_3,
                and_pin_1_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                or_pin_out,
                wire_1_part_1,
                wire_1_part_2,
                wire_1_part_3,
                and_pin_1_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        wire_1_name = Text(
            "wire_1", font="Cascadia Code", font_size=18, color=RED
        ).next_to(wire_1_part_2, UR, buff=0.1)
        self.play(Write(wire_1_name))
        self.wait(0.1)  # ! ---- ---- ----
        self.play(FadeOut(code_highlight_box_4), run_time=0.5)

        # ! 5
        self.play(Create(code_highlight_box_5), run_time=0.5)
        self.wait(0.1)  # ! ---- ---- ----
        self.play(
            ApplyMethod(not_pin_out.set_color, RED),
            ApplyMethod(wire_2_part_1.set_color, RED),
            ApplyMethod(wire_2_part_2.set_color, RED),
            ApplyMethod(wire_2_part_3.set_color, RED),
            ApplyMethod(and_pin_2_in.set_color, RED),
            run_time=0.1,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        wire_2_name = Text(
            "wire_2", font="Cascadia Code", font_size=18, color=RED
        ).next_to(wire_2_part_2, DR, buff=0.1)
        self.play(Write(wire_2_name))
        self.wait(0.1)  # ! ---- ---- ----
        self.play(FadeOut(code_highlight_box_5), run_time=0.5)

        """
        # ! 6
        self.play(Create(code_highlight_box_5), run_time=0.5)
        self.play(
            ApplyMethod(not_pin_out.set_color, RED),
            ApplyMethod(wire_2_part_1.set_color, RED),
            ApplyMethod(wire_2_part_2.set_color, RED),
            ApplyMethod(wire_2_part_3.set_color, RED),
            ApplyMethod(and_pin_2_in.set_color, RED),
            run_time=0.1,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(FadeOut(code_highlight_box_5), run_time=0.5)

        # ! 7
        self.play(Create(code_highlight_box_5), run_time=0.5)
        self.play(
            ApplyMethod(not_pin_out.set_color, RED),
            ApplyMethod(wire_2_part_1.set_color, RED),
            ApplyMethod(wire_2_part_2.set_color, RED),
            ApplyMethod(wire_2_part_3.set_color, RED),
            ApplyMethod(and_pin_2_in.set_color, RED),
            run_time=0.1,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(FadeOut(code_highlight_box_5), run_time=0.5)

        # ! 8
        self.play(Create(code_highlight_box_5), run_time=0.5)
        self.play(
            ApplyMethod(not_pin_out.set_color, RED),
            ApplyMethod(wire_2_part_1.set_color, RED),
            ApplyMethod(wire_2_part_2.set_color, RED),
            ApplyMethod(wire_2_part_3.set_color, RED),
            ApplyMethod(and_pin_2_in.set_color, RED),
            run_time=0.1,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(
            VGroup(
                not_pin_out,
                wire_2_part_1,
                wire_2_part_2,
                wire_2_part_3,
                and_pin_2_in,
            ).animate.scale(
                1 / 1.1
            ),  # type: ignore
            run_time=0.5,
        )
        self.play(FadeOut(code_highlight_box_5), run_time=0.5)
        """

    def construct(self):
        self.wait(0.25)  # ! ---- ---- ----

        # & Introduction                                                        :
        title = self.topic_introduction("What is HDL?")

        self.wait(0.25)  # ! ---- ---- ----

        # & Topics                                                              :
        topics = self.topics(title)

        self.wait(0.5)  # ! ---- ---- ----

        # & Definition                                                          :
        topics[0].set_color(YELLOW)

        self.wait(0.25)  # ! ---- ---- ----

        hdl_definition = self.topic_definition()
        self.waiting_to_read(
            wait_counter=4, wait_delay=0.8, note_color=BLUE
        )  # ! ---- ---- ----
        self.play(FadeOut(hdl_definition))

        self.wait(0.5)  # ! ---- ---- ----

        # & Digital Circuit Example                                             :
        topics[0].set_color(WHITE)
        topics[2].set_color(YELLOW)

        self.wait(0.25)  # ! ---- ---- ----

        self.digital_circuit_example(length=0.3, topics=topics)

        self.wait(2)  # ! ---- ---- ----
