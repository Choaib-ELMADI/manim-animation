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

    def create_and_gate(self, x=0.5):
        and_top_horiz_line = Line(start=[-x, x, 0], end=[x, x, 0])  # type: ignore
        and_bot_horiz_line = Line(start=[-x, -x, 0], end=[x, -x, 0])  # type: ignore
        and_lft_verti_line = Line(
            and_top_horiz_line.get_start(), and_bot_horiz_line.get_start()
        )
        and_rgt_curve_line = ArcBetweenPoints(
            and_top_horiz_line.get_end(), and_bot_horiz_line.get_end(), radius=-x
        )

        and_input_1 = Line(
            start=and_lft_verti_line.get_start() + (2 * x / 4) * DOWN,
            end=and_lft_verti_line.get_start() + (2 * x / 4) * DOWN + LEFT * x,
        )
        and_input_2 = Line(
            start=and_lft_verti_line.get_start() + 3 * (2 * x / 4) * DOWN,
            end=and_lft_verti_line.get_start() + 3 * (2 * x / 4) * DOWN + LEFT * x,
        )
        and_output = Line(
            start=and_rgt_curve_line.get_arc_center() + RIGHT * x,
            end=and_rgt_curve_line.get_arc_center() + RIGHT * x * 2,
        )

        gate_name = Text(
            "AND",
            font="Cascadia Code",
            font_size=60 * x,
        ).move_to(
            (and_lft_verti_line.get_center() + and_output.get_start()) / 2  # type: ignore
        )

        if not IS_DEBUGGING:
            self.play(Create(and_top_horiz_line), Create(and_bot_horiz_line))
            self.play(Create(and_lft_verti_line), Create(and_rgt_curve_line))
            self.play(Create(and_input_1), Create(and_input_2), Create(and_output))
            self.play(Write(gate_name))
        else:
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
            (and_lft_verti_line.get_start() + (2 * x / 4) * DOWN + LEFT * x),
            (and_lft_verti_line.get_start() + 3 * (2 * x / 4) * DOWN + LEFT * x),
            (and_rgt_curve_line.get_arc_center() + RIGHT * x * 2),
        ]

    def digital_circuit_example(self, length):
        # + Digital Circuit Example Elements
        and_gate, and_in_1, and_in_2, and_out = self.create_and_gate(x=length)
        self.play(and_gate.animate.shift(UP))

        # - Animate Digital Circuit Example Elements

    def construct(self):
        self.wait(0.25)  # ! ---- ---- ----

        self.topic_introduction("What is HDL?")

        self.wait(0.25)  # ! ---- ---- ----

        hdl_definition = self.topic_definition()

        self.waiting_to_read(
            wait_counter=4, wait_delay=0.8, note_color=BLUE
        )  # ! ---- ---- ----

        self.play(FadeOut(hdl_definition))

        self.wait(0.25)  # ! ---- ---- ----

        self.digital_circuit_example(length=0.35)

        self.wait(0.25)  # ! ---- ---- ----
