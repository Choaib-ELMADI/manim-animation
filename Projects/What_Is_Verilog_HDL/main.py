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

    def digital_circuit_example(self):
        pass

        # + Digital Circuit Example Elements

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

        self.digital_circuit_example()

        self.wait(0.25)  # ! ---- ---- ----
