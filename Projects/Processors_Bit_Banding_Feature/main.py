from manim import *


class Main(Scene):
    def construct(self):
        title = (
            Text(
                "Cortex-M3/4 Processors Bit Banding Feature",
                font="Cascadia Code",
                font_size=54,
                color="RED",
            )
            .scale(0.5)
            .to_edge(UP)  #!
        )

        topics = Paragraph(
            "Definition",
            "-",
            "Memory Layout",
            "-",
            "Formula",
            "-",  #!
            "Example",
            "-",
            "Demonstration",
            "-",
            "Conclusion",
            font="Cascadia Code",
            font_size=16,
        )
        topics_length = len(topics)

        bit_banding_def = Paragraph(
            "Bit-banding",
            "is a feature that enables every single bit",
            "in the bit-band region to be directly accessible!",
            "(in a single instruction)",
            font="Cascadia Code",
            font_size=21,
            line_spacing=0.75,
            alignment="center",
        )
        bit_banding_def[0].set_color(YELLOW)
        bit_banding_def[-1].set_color(ORANGE)

        # ! ---- ---- ---- ---- ----

        # self.play(Write(title), run_time=1.5)
        self.add(title)
        self.play(title.animate.to_edge(UP), run_time=1)  # type: ignore
        self.wait(0.5)

        topics[int(topics_length / 2)].next_to(title, DOWN, buff=0.2)
        for i in range(int(topics_length / 2) - 1, -1, -1):
            topics[i].next_to(topics[i + 1], LEFT, buff=0.15)
        for i in range(int(topics_length / 2), topics_length - 1):
            topics[i + 1].next_to(topics[i], RIGHT, buff=0.15)

        # self.play(Write(topics), run_time=1.5)
        self.add(topics)
        self.wait(1)

        # * Definition:

        topics[0].set_color(YELLOW)
        self.wait(0.5)

        for line in bit_banding_def:
            # self.play(Write(line), run_time=1)
            self.add(line)
            self.wait(0.25)
        self.wait(2)

        self.play(FadeOut(bit_banding_def, shift=DOWN * 0.5))  # type: ignore
        self.wait(1)

        # * Memory Layout:

        topics[0].set_color(WHITE)
        topics[2].set_color(YELLOW)
        self.wait(0.5)

        memory_areas = [
            {"name": "Code Area", "size": "0.5 GB", "height": 0.75, "color": YELLOW_C},
            {"name": "SRAM", "size": "0.5 GB", "height": 0.75, "color": GREEN_A},
            {"name": "Peripheral", "size": "0.5 GB", "height": 0.75, "color": BLUE},
            {"name": "External RAM", "size": "1 GB", "height": 0.75, "color": YELLOW_B},
            {
                "name": "External Device",
                "size": "1 GB",
                "height": 0.75,
                "color": YELLOW_A,
            },
            {
                "name": "Private Peripheral Bus",
                "size": "- --",
                "height": 0.75,
                "color": GREEN_B,
            },
            {
                "name": "Vendor Specific",
                "size": "- --",
                "height": 0.75,
                "color": PURPLE_B,
            },
        ]
        memory_areas_rectangles = []

        for i, memory_area in enumerate(memory_areas):
            for j, rect in enumerate(memory_areas_rectangles):
                if j <= 2 and len(memory_areas_rectangles) <= 3:
                    rect.shift(DOWN * rect.get_height())
                if j >= 3:
                    rect.shift(UP * rect.get_height())

            memory_area_rectangle = Rectangle(
                color=memory_area["color"],
                height=memory_area["height"],
                width=4,
                fill_opacity=0.5,
            )
            memory_area_rectangle.move_to(
                DOWN * memory_area_rectangle.get_height() * 0.75
            )
            self.add(memory_area_rectangle)
            memory_areas_rectangles.append(memory_area_rectangle)
            self.wait(0.5)

        self.wait(1)

        #! ---- ---- ---- ---- ----

        self.wait(2)
