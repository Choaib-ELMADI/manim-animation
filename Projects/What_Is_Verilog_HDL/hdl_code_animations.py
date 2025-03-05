from manim import *

# IS_DEBUGGING = False
IS_DEBUGGING = True


class Main(Scene):
    def digital_circuit_example(self):
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
                color=ORANGE,
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
                color=GREEN,
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
                color=BLUE,
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

        highlight_boxes = [
            code_highlight_box_1,
            code_highlight_box_2,
            code_highlight_box_3,
            code_highlight_box_4,
            code_highlight_box_5,
            code_highlight_box_6,
            code_highlight_box_7,
            code_highlight_box_8,
        ]

        self.add(verilog_hdl_code, verilog_hdl_code_box, verilog_hdl_code_title)

        for i in range(len(highlight_boxes)):
            self.play(Create(highlight_boxes[i]), run_time=0.5)
            self.wait(0.25)
            self.play(FadeOut(highlight_boxes[i]), run_time=1)

    def construct(self):
        self.digital_circuit_example()
        self.wait(1)
