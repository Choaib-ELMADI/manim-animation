from manim import *

IS_DEBUGGING = False


class Main(Scene):
    def construct(self):
        title = Text(
            "Cortex-M3/4 Processors Bit Banding Feature",
            font="Cascadia Code",
            font_size=54,
            color="RED",
        ).scale(0.5)

        if IS_DEBUGGING:
            title.to_edge(UP)

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

        self.wait(0.25)

        # ! ---- ---- ---- ---- ----

        if not IS_DEBUGGING:
            self.play(Write(title), run_time=1.5)
        else:
            self.add(title)

        if not IS_DEBUGGING:
            self.play(title.animate.to_edge(UP), run_time=1)  # type: ignore

        self.wait(0.5)

        topics[int(topics_length / 2)].next_to(title, DOWN, buff=0.2)
        for i in range(int(topics_length / 2) - 1, -1, -1):
            topics[i].next_to(topics[i + 1], LEFT, buff=0.15)
        for i in range(int(topics_length / 2), topics_length - 1):
            topics[i + 1].next_to(topics[i], RIGHT, buff=0.15)

        if not IS_DEBUGGING:
            self.play(Write(topics), run_time=1.5)
        else:
            self.add(topics)

        self.wait(1)

        # * Definition:

        topics[0].set_color(YELLOW)
        self.wait(0.5)

        for line in bit_banding_def:
            if not IS_DEBUGGING:
                self.play(Write(line), run_time=1)
            else:
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
            {
                "name": "Code Area",
                "size": "0.5GB",
                "start_address": "0x00000000",
                "end_address": "0x1FFFFFFF",
                "height": 0.75,
                "color": YELLOW_C,
            },
            {
                "name": "SRAM",
                "size": "0.5GB",
                "start_address": "0x20000000",
                "end_address": "0x3FFFFFFF",
                "height": 0.75,
                "color": GREEN_A,
            },
            {
                "name": "Peripheral",
                "size": "0.5GB",
                "start_address": "0x40000000",
                "end_address": "0x5FFFFFFF",
                "height": 0.75,
                "color": BLUE,
            },
            {
                "name": "Vendor Specific",
                "size": "511MB",
                "start_address": "0xE0100000",
                "end_address": "0xFFFFFFFF",
                "height": 0.75,
                "color": PURPLE_B,
            },
            {
                "name": "Private Peripheral Bus",
                "size": "1.0MB",
                "start_address": "0xE0000000",
                "end_address": "0xE00FFFFF",
                "height": 0.75,
                "color": GREEN_B,
            },
            {
                "name": "External Device",
                "size": "1.0GB",
                "start_address": "0xA0000000",
                "end_address": "0xDFFFFFFF",
                "height": 0.75,
                "color": WHITE,
            },
            {
                "name": "External RAM",
                "size": "1.0GB",
                "start_address": "0x60000000",
                "end_address": "0x9FFFFFFF",
                "height": 0.75,
                "color": YELLOW_B,
            },
        ]
        memory_areas_rectangles = []
        memory_areas_names = []
        memory_areas_sizes = []
        memory_areas_starts = []
        memory_areas_ends = []

        for i, memory_area in enumerate(memory_areas):
            for j, rect in enumerate(memory_areas_rectangles):
                if j <= 2 and len(memory_areas_rectangles) <= 3:
                    if not IS_DEBUGGING:
                        self.play(
                            VGroup(*memory_areas_rectangles[0 : min(2, len(memory_areas_rectangles)) + 1], *memory_areas_names[0 : min(2, len(memory_areas_rectangles)) + 1], *memory_areas_sizes[0 : min(2, len(memory_areas_rectangles)) + 1], *memory_areas_starts[0 : min(2, len(memory_areas_rectangles)) + 1], *memory_areas_ends[0 : min(2, len(memory_areas_rectangles)) + 1]).animate.shift(  # type: ignore
                                DOWN * rect.get_height()
                            )
                        )
                        break
                    else:
                        rect.shift(DOWN * rect.get_height())
                        memory_areas_names[j].shift(DOWN * rect.get_height())
                        memory_areas_sizes[j].shift(DOWN * rect.get_height())
                        memory_areas_starts[j].shift(DOWN * rect.get_height())
                        memory_areas_ends[j].shift(DOWN * rect.get_height())
                if j >= 3:
                    if not IS_DEBUGGING:
                        self.play(
                            VGroup(*memory_areas_rectangles[3 : min(5, len(memory_areas_rectangles)) + 1], *memory_areas_names[3 : min(5, len(memory_areas_rectangles)) + 1], *memory_areas_sizes[3 : min(5, len(memory_areas_rectangles)) + 1], *memory_areas_starts[3 : min(5, len(memory_areas_rectangles)) + 1], *memory_areas_ends[3 : min(5, len(memory_areas_rectangles)) + 1]).animate.shift(  # type: ignore
                                UP * rect.get_height()
                            )
                        )
                        break
                    else:
                        rect.shift(UP * rect.get_height())
                        memory_areas_names[j].shift(UP * rect.get_height())
                        memory_areas_sizes[j].shift(UP * rect.get_height())
                        memory_areas_starts[j].shift(UP * rect.get_height())
                        memory_areas_ends[j].shift(UP * rect.get_height())

            memory_area_rectangle = Rectangle(
                color=memory_area["color"],
                height=memory_area["height"],
                width=4,
                fill_opacity=0.1,
            )
            memory_area_rectangle.move_to(
                DOWN * memory_area_rectangle.get_height() * 0.75
            )

            if not IS_DEBUGGING:
                self.play(DrawBorderThenFill(memory_area_rectangle), run_time=1)
            else:
                self.add(memory_area_rectangle)

            memory_areas_rectangles.append(memory_area_rectangle)

            memory_area_name = Text(
                memory_area["name"],
                font="Cascadia Code",
                font_size=16,
                color=memory_area["color"],
            ).move_to(memory_area_rectangle.get_center())

            if not IS_DEBUGGING:
                self.play(Write(memory_area_name))
            else:
                self.add(memory_area_name)

            memory_areas_names.append(memory_area_name)

            memory_area_size = Text(
                memory_area["size"],
                font="Cascadia Code",
                font_size=16,
                color=memory_area["color"],
            ).next_to(memory_area_rectangle, RIGHT, buff=0.25)

            if not IS_DEBUGGING:
                self.play(Write(memory_area_size))
            else:
                self.add(memory_area_size)

            memory_areas_sizes.append(memory_area_size)

            memory_area_start = (
                Text(
                    memory_area["start_address"],
                    font="Cascadia Code",
                    font_size=14,
                    color=memory_area["color"],
                )
                .next_to(memory_area_rectangle, LEFT, buff=0.25)
                .shift(DOWN * (memory_area_rectangle.get_height() / 2) * 0.7)
            )

            memory_area_end = (
                Text(
                    memory_area["end_address"],
                    font="Cascadia Code",
                    font_size=14,
                    color=memory_area["color"],
                )
                .next_to(memory_area_rectangle, LEFT, buff=0.25)
                .shift(UP * (memory_area_rectangle.get_height() / 2) * 0.7)
            )

            if not IS_DEBUGGING:
                self.play(Write(memory_area_start), Write(memory_area_end))
            else:
                self.add(memory_area_start, memory_area_end)

            memory_areas_starts.append(memory_area_start)
            memory_areas_ends.append(memory_area_end)

            self.wait(0.25)

        self.wait(1)
        self.play(FadeOut(*memory_areas_sizes, shift=DOWN * 0.5))  # type: ignore

        if not IS_DEBUGGING:
            self.play(
                VGroup(*memory_areas_starts, *memory_areas_ends).animate.next_to(  # type: ignore
                    memory_areas_rectangles[6], RIGHT, buff=0.25
                )
            )
        else:
            VGroup(*memory_areas_starts, *memory_areas_ends).next_to(
                memory_areas_rectangles[6], RIGHT, buff=0.25
            )

        if not IS_DEBUGGING:
            self.play(
                VGroup(
                    *memory_areas_rectangles,
                    *memory_areas_names,
                    *memory_areas_starts,
                    *memory_areas_ends
                ).animate.shift(  # type: ignore
                    RIGHT * 3.25
                )
            )
        else:
            VGroup(
                *memory_areas_rectangles,
                *memory_areas_names,
                *memory_areas_starts,
                *memory_areas_ends
            ).shift(RIGHT * 3.25)

        # & ---- ---- ---- ---- ----

        bitband_sram_region = Rectangle(
            GREEN_A,
            height=0.75 * 3,
            width=4,
            fill_opacity=0.1,
        )
        bitband_sram_region.move_to(DOWN * 0.75 * (0.75 + 2) + LEFT * 3.25)

        bitband_sram_region_line_1 = Line(
            start=memory_areas_rectangles[1].get_corner(DL),
            end=bitband_sram_region.get_corner(DR),
            color=GREEN_A,
        )
        bitband_sram_region_line_2 = Line(
            start=memory_areas_rectangles[1].get_corner(UL) + DOWN * 0.4,
            end=bitband_sram_region.get_corner(UR),
            color=GREEN_A,
        )

        bitband_sram_region_divider_1 = Line(
            start=bitband_sram_region.get_corner(DL) + UP * 0.75 * 0.5,
            end=bitband_sram_region.get_corner(DR) + UP * 0.75 * 0.5,
            color=GREEN_A,
        )
        bitband_sram_region_divider_2 = Line(
            start=bitband_sram_region.get_corner(DL) + UP * 0.75 * (2 - 0.25),
            end=bitband_sram_region.get_corner(DR) + UP * 0.75 * (2 - 0.25),
            color=GREEN_A,
        )

        # * 1
        midpoint = 0.5 * (  # type: ignore
            bitband_sram_region.get_edge_center(DOWN)
            + bitband_sram_region_divider_1.get_center()
        )
        bitband_sram_region_1_size = (
            Text(
                "1MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        bitband_sram_region_1_name = Text(
            "Bit-band region",
            font="Cascadia Code",
            font_size=16,
            color=GREEN_A,
        ).move_to(midpoint)
        # * 2
        midpoint = 0.5 * (  # type: ignore
            bitband_sram_region_divider_1.get_center()
            + bitband_sram_region_divider_2.get_center()
        )
        bitband_sram_region_2_size = (
            Text(
                "31MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        # * 3
        midpoint = 0.5 * (  # type: ignore
            bitband_sram_region.get_edge_center(UP)
            + bitband_sram_region_divider_2.get_center()
        )
        bitband_sram_region_3_size = (
            Text(
                "32MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        bitband_sram_region_3_name = Text(
            "Bit-band alias",
            font="Cascadia Code",
            font_size=16,
            color=GREEN_A,
        ).move_to(midpoint)

        if not IS_DEBUGGING:
            self.play(
                Create(bitband_sram_region_line_1), Create(bitband_sram_region_line_2)
            )
        else:
            self.add(bitband_sram_region_line_1, bitband_sram_region_line_2)

        if not IS_DEBUGGING:
            self.play(DrawBorderThenFill(bitband_sram_region), run_time=1.5)
        else:
            self.add(bitband_sram_region)

        bitband_sram_region_start = (
            Text(
                "0x20000000",
                font="Cascadia Code",
                font_size=14,
                color=GREEN_A,
            )
            .next_to(bitband_sram_region, LEFT, buff=0.25)
            .shift(DOWN * (bitband_sram_region.get_height() / 2) * 0.9)
        )

        bitband_sram_region_end = (
            Text(
                "0x23FFFFFF",
                font="Cascadia Code",
                font_size=14,
                color=GREEN_A,
            )
            .next_to(bitband_sram_region, LEFT, buff=0.25)
            .shift(UP * (bitband_sram_region.get_height() / 2) * 0.9)
        )

        if not IS_DEBUGGING:
            self.play(Write(bitband_sram_region_start), Write(bitband_sram_region_end))
        else:
            self.add(bitband_sram_region_start, bitband_sram_region_end)

        if not IS_DEBUGGING:
            self.play(
                Create(bitband_sram_region_divider_1),
                Create(bitband_sram_region_divider_2),
            )
        else:
            self.add(bitband_sram_region_divider_1, bitband_sram_region_divider_2)

        if not IS_DEBUGGING:
            self.play(
                Write(bitband_sram_region_1_size),
                Write(bitband_sram_region_1_name),
                Write(bitband_sram_region_2_size),
                Write(bitband_sram_region_3_size),
                Write(bitband_sram_region_3_name),
            )
        else:
            self.add(
                bitband_sram_region_1_size,
                bitband_sram_region_1_name,
                bitband_sram_region_2_size,
                bitband_sram_region_3_size,
                bitband_sram_region_3_name,
            )

        # & ---- ---- ---- ---- ----
        self.wait(1)

        bitband_peri_region = Rectangle(
            BLUE,
            height=0.75 * 3,
            width=4,
            fill_opacity=0.1,
        )
        bitband_peri_region.move_to(UP * 0.75 * (0.75 + 0.5) + LEFT * 3.25)

        bitband_peri_region_line_1 = Line(
            start=memory_areas_rectangles[2].get_corner(DL),
            end=bitband_peri_region.get_corner(DR),
            color=BLUE,
        )
        bitband_peri_region_line_2 = Line(
            start=memory_areas_rectangles[2].get_corner(UL) + DOWN * 0.4,
            end=bitband_peri_region.get_corner(UR),
            color=BLUE,
        )

        bitband_peri_region_divider_1 = Line(
            start=bitband_peri_region.get_corner(DL) + UP * 0.75 * 0.5,
            end=bitband_peri_region.get_corner(DR) + UP * 0.75 * 0.5,
            color=BLUE,
        )
        bitband_peri_region_divider_2 = Line(
            start=bitband_peri_region.get_corner(DL) + UP * 0.75 * (2 - 0.25),
            end=bitband_peri_region.get_corner(DR) + UP * 0.75 * (2 - 0.25),
            color=BLUE,
        )

        # * 1
        midpoint = 0.5 * (  # type: ignore
            bitband_peri_region.get_edge_center(DOWN)
            + bitband_peri_region_divider_1.get_center()
        )
        bitband_peri_region_1_size = (
            Text(
                "1MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        bitband_peri_region_1_name = Text(
            "Bit-band region",
            font="Cascadia Code",
            font_size=16,
            color=BLUE,
        ).move_to(midpoint)
        # * 2
        midpoint = 0.5 * (  # type: ignore
            bitband_peri_region_divider_1.get_center()
            + bitband_peri_region_divider_2.get_center()
        )
        bitband_peri_region_2_size = (
            Text(
                "31MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        # * 3
        midpoint = 0.5 * (  # type: ignore
            bitband_peri_region.get_edge_center(UP)
            + bitband_peri_region_divider_2.get_center()
        )
        bitband_peri_region_3_size = (
            Text(
                "32MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(midpoint)
            .shift(LEFT * (2 - 0.35))
        )
        bitband_peri_region_3_name = Text(
            "Bit-band alias",
            font="Cascadia Code",
            font_size=16,
            color=BLUE,
        ).move_to(midpoint)

        if not IS_DEBUGGING:
            self.play(
                Create(bitband_peri_region_line_1), Create(bitband_peri_region_line_2)
            )
        else:
            self.add(bitband_peri_region_line_1, bitband_peri_region_line_2)

        if not IS_DEBUGGING:
            self.play(DrawBorderThenFill(bitband_peri_region), run_time=1.5)
        else:
            self.add(bitband_peri_region)

        bitband_peri_region_start = (
            Text(
                "0x40000000",
                font="Cascadia Code",
                font_size=14,
                color=BLUE,
            )
            .next_to(bitband_peri_region, LEFT, buff=0.25)
            .shift(DOWN * (bitband_peri_region.get_height() / 2) * 0.9)
        )

        bitband_peri_region_end = (
            Text(
                "0x43FFFFFF",
                font="Cascadia Code",
                font_size=14,
                color=BLUE,
            )
            .next_to(bitband_peri_region, LEFT, buff=0.25)
            .shift(UP * (bitband_peri_region.get_height() / 2) * 0.9)
        )

        if not IS_DEBUGGING:
            self.play(Write(bitband_peri_region_start), Write(bitband_peri_region_end))
        else:
            self.add(bitband_peri_region_start, bitband_peri_region_end)

        if not IS_DEBUGGING:
            self.play(
                Create(bitband_peri_region_divider_1),
                Create(bitband_peri_region_divider_2),
            )
        else:
            self.add(bitband_peri_region_divider_1, bitband_peri_region_divider_2)

        if not IS_DEBUGGING:
            self.play(
                Write(bitband_peri_region_1_size),
                Write(bitband_peri_region_1_name),
                Write(bitband_peri_region_2_size),
                Write(bitband_peri_region_3_size),
                Write(bitband_peri_region_3_name),
            )
        else:
            self.add(
                bitband_peri_region_1_size,
                bitband_peri_region_1_name,
                bitband_peri_region_2_size,
                bitband_peri_region_3_size,
                bitband_peri_region_3_name,
            )

        self.wait(2)

        # * Formula:

        # ! ---- ---- ---- ---- ----

        self.wait(2)
