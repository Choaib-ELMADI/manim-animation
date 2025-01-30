from manim import *

IS_DEBUGGING = False


class Main(Scene):
    def construct(self):
        self.wait(0.25)  # ! ---- ---- ----

        # + Title Element
        title = Text(
            "Cortex-M3/4 Processors Bit Banding Feature",
            font="Cascadia Code",
            font_size=54,
            color="RED",
        ).scale(0.5)

        # - Animate Title Element
        if not IS_DEBUGGING:
            self.play(Write(title), run_time=1.5)
            self.play(title.animate.to_edge(UP), run_time=1)  # type: ignore
        else:
            self.add(title)
            title.to_edge(UP)

        self.wait(0.5)  # ! ---- ---- ----

        # + Topics Element
        topics = Paragraph(
            "Definition",
            "•",
            "Memory Layout",
            "•",
            "Formula",
            "•",
            "Example",
            "•",
            "Demonstration",
            "•",
            "Conclusion",
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
            self.play(Write(topics), run_time=1.5)
        else:
            self.add(topics)

        self.wait(0.5)  # ! ---- ---- ----
        """
        # & Definition                                                          :
        topics[0].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----

        # + Definition Element
        bit_banding_def = Paragraph(
            "Bit-banding",
            "is a feature that enables every single bit",
            "in the bit-band region to be directly accessible,",
            "in a single instruction!",
            font="Cascadia Code",
            font_size=21,
            line_spacing=0.75,
            alignment="center",
        )
        bit_banding_def[0].set_color(YELLOW)
        bit_banding_def[-1].set_color(ORANGE)

        # - Animate Definition Element
        for i, line in enumerate(bit_banding_def):
            if not IS_DEBUGGING:
                self.play(Write(line), run_time=1)
            else:
                self.add(line)

            if i != len(bit_banding_def) - 1:
                self.wait(0.25)

        underline = Underline(
            bit_banding_def[-1], buff=0.05, color=ORANGE, stroke_width=3
        )

        if not IS_DEBUGGING:
            self.play(Create(underline))
        else:
            self.add(underline)

        self.wait(2)  # ! ---- ---- ----

        self.play(FadeOut(bit_banding_def, underline))  # type: ignore

        self.wait(0.5)  # ! ---- ---- ----

        # & Memory Layout                                                       :
        topics[0].set_color(WHITE)
        topics[2].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----

        # + Memory Elements
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

            # + Memory Area Element
            memory_area_rectangle = Rectangle(
                color=memory_area["color"],
                height=memory_area["height"],
                width=4,
                fill_opacity=0.1,
            )
            memory_area_rectangle.move_to(
                DOWN * memory_area_rectangle.get_height() * 0.75
            )
            memory_areas_rectangles.append(memory_area_rectangle)

            # + Memory Name Element
            memory_area_name = Text(
                memory_area["name"],
                font="Cascadia Code",
                font_size=16,
                color=memory_area["color"],
            ).move_to(memory_area_rectangle.get_center())
            memory_areas_names.append(memory_area_name)

            # + Memory Size Element
            memory_area_size = Text(
                memory_area["size"],
                font="Cascadia Code",
                font_size=16,
                color=memory_area["color"],
            ).next_to(memory_area_rectangle, RIGHT, buff=0.25)
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
            memory_areas_starts.append(memory_area_start)
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
            memory_areas_ends.append(memory_area_end)

            # - Animate Memory Elements
            if not IS_DEBUGGING:
                self.play(DrawBorderThenFill(memory_area_rectangle), run_time=1)
            else:
                self.add(memory_area_rectangle)

            if not IS_DEBUGGING:
                self.play(
                    Write(memory_area_name),
                    Write(memory_area_size),
                    Write(memory_area_start),
                    Write(memory_area_end),
                )
            else:
                self.add(
                    memory_area_name,
                    memory_area_size,
                    memory_area_start,
                    memory_area_end,
                )

            if i != len(memory_areas) - 1:
                self.wait(0.25)  # ! ---- ---- ----

        self.wait(1)  # ! ---- ---- ----

        self.play(FadeOut(*memory_areas_sizes))  # type: ignore

        # - Animate Memory Areas Start and End Elements
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

        # - Animate Memory Elements
        if not IS_DEBUGGING:
            self.play(
                VGroup(
                    *memory_areas_rectangles,
                    *memory_areas_names,
                    *memory_areas_starts,
                    *memory_areas_ends,
                ).animate.shift(  # type: ignore
                    RIGHT * 3.25
                )
            )
        else:
            VGroup(
                *memory_areas_rectangles,
                *memory_areas_names,
                *memory_areas_starts,
                *memory_areas_ends,
            ).shift(RIGHT * 3.25)

        # + Bit Band Region 1 Elements
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
        bitband_sram_region_1_size = (
            Text(
                "1MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_sram_region.get_edge_center(DOWN)
                    + bitband_sram_region_divider_1.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_sram_region_1_name = Text(
            "Bit-band region",
            font="Cascadia Code",
            font_size=16,
            color=GREEN_A,
        ).move_to(
            0.5
            * (  # type: ignore
                bitband_sram_region.get_edge_center(DOWN)
                + bitband_sram_region_divider_1.get_center()
            )
        )
        bitband_sram_region_2_size = (
            Text(
                "31MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_sram_region_divider_1.get_center()
                    + bitband_sram_region_divider_2.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_sram_region_3_size = (
            Text(
                "32MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_sram_region.get_edge_center(UP)
                    + bitband_sram_region_divider_2.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_sram_region_3_name = Text(
            "Bit-band alias",
            font="Cascadia Code",
            font_size=16,
            color=GREEN_A,
        ).move_to(
            0.5
            * (  # type: ignore
                bitband_sram_region.get_edge_center(UP)
                + bitband_sram_region_divider_2.get_center()
            )
        )
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

        # - Animate Bit Band Region 1 Elements
        if not IS_DEBUGGING:
            self.play(
                Create(bitband_sram_region_line_1), Create(bitband_sram_region_line_2)
            )
            self.play(DrawBorderThenFill(bitband_sram_region), run_time=1.5)
            self.play(Write(bitband_sram_region_start), Write(bitband_sram_region_end))
            self.play(
                Create(bitband_sram_region_divider_1),
                Create(bitband_sram_region_divider_2),
                Write(bitband_sram_region_1_size),
                Write(bitband_sram_region_1_name),
                Write(bitband_sram_region_2_size),
                Write(bitband_sram_region_3_size),
                Write(bitband_sram_region_3_name),
            )
        else:
            self.add(bitband_sram_region_line_1, bitband_sram_region_line_2)
            self.add(bitband_sram_region)
            self.add(bitband_sram_region_start, bitband_sram_region_end)
            self.add(
                bitband_sram_region_divider_1,
                bitband_sram_region_divider_2,
                bitband_sram_region_1_size,
                bitband_sram_region_1_name,
                bitband_sram_region_2_size,
                bitband_sram_region_3_size,
                bitband_sram_region_3_name,
            )

        self.wait(0.5)  # ! ---- ---- ----

        # + Bit Band Region 2 Elements
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
        bitband_peri_region_1_size = (
            Text(
                "1MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_peri_region.get_edge_center(DOWN)
                    + bitband_peri_region_divider_1.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_peri_region_1_name = Text(
            "Bit-band region",
            font="Cascadia Code",
            font_size=16,
            color=BLUE,
        ).move_to(
            0.5
            * (  # type: ignore
                bitband_peri_region.get_edge_center(DOWN)
                + bitband_peri_region_divider_1.get_center()
            )
        )
        bitband_peri_region_2_size = (
            Text(
                "31MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_peri_region_divider_1.get_center()
                    + bitband_peri_region_divider_2.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_peri_region_3_size = (
            Text(
                "32MB",
                font="Cascadia Code",
                font_size=14,
            )
            .move_to(
                0.5
                * (  # type: ignore
                    bitband_peri_region.get_edge_center(UP)
                    + bitband_peri_region_divider_2.get_center()
                )
            )
            .shift(LEFT * (2 - 0.35))
        )
        bitband_peri_region_3_name = Text(
            "Bit-band alias",
            font="Cascadia Code",
            font_size=16,
            color=BLUE,
        ).move_to(
            0.5
            * (  # type: ignore
                bitband_peri_region.get_edge_center(UP)
                + bitband_peri_region_divider_2.get_center()
            )
        )
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

        # - Animate Bit Band Region 2 Elements
        if not IS_DEBUGGING:
            self.play(
                Create(bitband_peri_region_line_1), Create(bitband_peri_region_line_2)
            )
            self.play(DrawBorderThenFill(bitband_peri_region), run_time=1.5)
            self.play(Write(bitband_peri_region_start), Write(bitband_peri_region_end))
            self.play(
                Create(bitband_peri_region_divider_1),
                Create(bitband_peri_region_divider_2),
                Write(bitband_peri_region_1_size),
                Write(bitband_peri_region_1_name),
                Write(bitband_peri_region_2_size),
                Write(bitband_peri_region_3_size),
                Write(bitband_peri_region_3_name),
            )
        else:
            self.add(bitband_peri_region_line_1, bitband_peri_region_line_2)
            self.add(bitband_peri_region)
            self.add(bitband_peri_region_start, bitband_peri_region_end)
            self.add(
                bitband_peri_region_divider_1,
                bitband_peri_region_divider_2,
                bitband_peri_region_1_size,
                bitband_peri_region_1_name,
                bitband_peri_region_2_size,
                bitband_peri_region_3_size,
                bitband_peri_region_3_name,
            )

        self.wait(2)  # ! ---- ---- ----

        self.play(
            FadeOut(
                *memory_areas_rectangles,
                *memory_areas_names,
                *memory_areas_starts,
                *memory_areas_ends,
                bitband_sram_region,
                bitband_sram_region_line_1,
                bitband_sram_region_line_2,
                bitband_sram_region_divider_1,
                bitband_sram_region_divider_2,
                bitband_sram_region_1_size,
                bitband_sram_region_1_name,
                bitband_sram_region_2_size,
                bitband_sram_region_3_size,
                bitband_sram_region_3_name,
                bitband_sram_region_start,
                bitband_sram_region_end,
                bitband_peri_region,
                bitband_peri_region_line_1,
                bitband_peri_region_line_2,
                bitband_peri_region_divider_1,
                bitband_peri_region_divider_2,
                bitband_peri_region_1_size,
                bitband_peri_region_1_name,
                bitband_peri_region_2_size,
                bitband_peri_region_3_size,
                bitband_peri_region_3_name,
                bitband_peri_region_start,
                bitband_peri_region_end,
            )
        )

        self.wait(0.5)  # ! ---- ---- ----

        # & Formula                                                             :
        topics[2].set_color(WHITE)
        topics[4].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----

        # + Formula Elements
        formula_part_1 = MarkupText(
            f'<span fgcolor="{GREEN}">ALIAS_SRAM_ADDRESS</span>'
            + f'<span fgcolor="{BLUE}"> = </span>',
            font="Cascadia Code",
            font_size=20,
        )
        formula_part_2 = MarkupText(
            f'<span fgcolor="{GOLD}">ALIAS_SRAM_BASE</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{YELLOW}">(</span>'
            + f'<span fgcolor="{ORANGE}">(</span>'
            + f'<span fgcolor="{PURPLE}">(uint32_t)</span>'
            + f'<span fgcolor="{GREEN}">target</span>'
            + f'<span fgcolor="{BLUE}"> - </span>'
            + f'<span fgcolor="{GOLD}">BITBAND_SRAM_BASE</span>'
            + f'<span fgcolor="{ORANGE}">)</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">32</span>'
            + f'<span fgcolor="{YELLOW}">)</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{PURPLE}">(</span>'
            + f'<span fgcolor="{GREEN}">bit_n</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">4</span>'
            + f'<span fgcolor="{PURPLE}">)</span>',
            font="Cascadia Code",
            font_size=20,
        )
        formula = VGroup(formula_part_1, formula_part_2).arrange(DOWN, buff=0.15)
        formula.move_to(ORIGIN)
        box = always_redraw(
            lambda: SurroundingRectangle(
                formula, color=WHITE, fill_opacity=0.05, buff=0.25
            )
        )

        # - Animate Formula Elements
        if not IS_DEBUGGING:
            self.play(Write(formula))
            self.play(Create(box))  # type: ignore
        else:
            self.add(formula, box)

        self.wait(1)  # ! ---- ---- ----

        self.play(formula.animate.scale(0.75).arrange(RIGHT, buff=0.15).next_to(topics[5], DOWN * 2.25))  # type: ignore

        self.wait(0.5)  # ! ---- ---- ----

        # & Example                                                             :
        topics[4].set_color(WHITE)
        topics[6].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----

        # + Example Elements
        formula_copy = formula.copy()
        alias_sram_base_formula = (
            MarkupText(
                f'<span fgcolor="{GOLD}">ALIAS_SRAM_BASE</span>'
                + f'<span fgcolor="{BLUE}">   = </span>'
                + f'<span fgcolor="{GOLD}">0x22000000</span>',
                font="Cascadia Code",
                font_size=18,
            )
            .align_to(box, LEFT)
            .shift(UP * 0.4)
        )
        bitband_sram_base_formula = MarkupText(
            f'<span fgcolor="{GOLD}">BITBAND_SRAM_BASE</span>'
            + f'<span fgcolor="{BLUE}"> = </span>'
            + f'<span fgcolor="{GOLD}">0x20000000</span>',
            font="Cascadia Code",
            font_size=18,
        ).align_to(box, LEFT)
        target_address_formula = (
            MarkupText(
                f'<span fgcolor="{BLUE}">let </span>'
                + f'<span fgcolor="{GREEN}">target</span>'
                + f'<span fgcolor="{BLUE}">        = </span>'
                + f'<span fgcolor="{GREEN}">0x20020014</span>',
                font="Cascadia Code",
                font_size=18,
            )
            .align_to(box, LEFT)
            .shift(DOWN * 0.4)
        )
        bit_n_formula = (
            MarkupText(
                f'<span fgcolor="{BLUE}">let </span>'
                + f'<span fgcolor="{GREEN}">bit_n</span>'
                + f'<span fgcolor="{BLUE}">         = </span>'
                + f'<span fgcolor="{GREEN}">0x00000005</span>',
                font="Cascadia Code",
                font_size=18,
            )
            .align_to(box, LEFT)
            .shift(DOWN * 0.4 * 2)
        )
        target_formula_part_1 = MarkupText(
            f'<span fgcolor="{GREEN}">ALIAS_SRAM_ADDRESS</span>'
            + f'<span fgcolor="{BLUE}"> = </span>',
            font="Cascadia Code",
            font_size=20,
        )
        target_formula_part_2 = MarkupText(
            f'<span fgcolor="{GOLD}">0x22000000</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{YELLOW}">(</span>'
            + f'<span fgcolor="{ORANGE}">(</span>'
            + f'<span fgcolor="{PURPLE}">(uint32_t)</span>'
            + f'<span fgcolor="{GREEN}">0x20020014</span>'
            + f'<span fgcolor="{BLUE}"> - </span>'
            + f'<span fgcolor="{GOLD}">0x20000000</span>'
            + f'<span fgcolor="{ORANGE}">)</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">32</span>'
            + f'<span fgcolor="{YELLOW}">)</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{PURPLE}">(</span>'
            + f'<span fgcolor="{GREEN}">0x00000005</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">4</span>'
            + f'<span fgcolor="{PURPLE}">)</span>',
            font="Cascadia Code",
            font_size=20,
        )
        target_formula = (
            VGroup(target_formula_part_1, target_formula_part_2)
            .arrange(RIGHT, buff=0.15)
            .scale(0.75)
            .move_to(ORIGIN + DOWN * 0.4 * 6)
        )
        computed_formula_1_part_1 = MarkupText(
            f'<span fgcolor="{GREEN}">ALIAS_SRAM_ADDRESS</span>'
            + f'<span fgcolor="{BLUE}"> = </span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_1_part_2 = MarkupText(
            f'<span fgcolor="{GOLD}">0x22000000</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{YELLOW}">(</span>'
            + f'<span fgcolor="{GREEN}">0x00020014</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">32</span>'
            + f'<span fgcolor="{YELLOW}">)</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{PURPLE}">(</span>'
            + f'<span fgcolor="{GREEN}">0x00000005</span>'
            + f'<span fgcolor="{BLUE}"> x </span>'
            + f'<span fgcolor="{RED}">4</span>'
            + f'<span fgcolor="{PURPLE}">)</span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_1 = (
            VGroup(computed_formula_1_part_1, computed_formula_1_part_2)
            .arrange(RIGHT, buff=0.15)
            .scale(0.75)
            .move_to(ORIGIN + DOWN * 0.4 * 6)
        )
        computed_formula_2_part_1 = MarkupText(
            f'<span fgcolor="{GREEN}">ALIAS_SRAM_ADDRESS</span>'
            + f'<span fgcolor="{BLUE}"> = </span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_2_part_2 = MarkupText(
            f'<span fgcolor="{GOLD}">0x22000000</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{GREEN}">0x004000A0</span>'
            + f'<span fgcolor="{BLUE}"> + </span>'
            + f'<span fgcolor="{GREEN}">0x00000014</span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_2 = (
            VGroup(computed_formula_2_part_1, computed_formula_2_part_2)
            .arrange(RIGHT, buff=0.15)
            .scale(0.75)
            .move_to(ORIGIN + DOWN * 0.4 * 6)
        )
        computed_formula_3_part_1 = MarkupText(
            f'<span fgcolor="{GREEN}">ALIAS_SRAM_ADDRESS</span>'
            + f'<span fgcolor="{BLUE}"> = </span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_3_part_2 = MarkupText(
            f'<span fgcolor="{YELLOW}">0x224000B4</span>',
            font="Cascadia Code",
            font_size=20,
        )
        computed_formula_3 = (
            VGroup(computed_formula_3_part_1, computed_formula_3_part_2)
            .arrange(RIGHT, buff=0.15)
            .scale(0.75)
            .move_to(ORIGIN + DOWN * 0.4 * 6)
        )

        # - Animate Example Elements
        self.play(formula_copy.animate.move_to(ORIGIN + DOWN * 0.4 * 6))  # type: ignore

        self.wait(0.5)  # ! ---- ---- ----

        if not IS_DEBUGGING:
            self.play(Write(alias_sram_base_formula))
            self.play(Write(bitband_sram_base_formula))
            self.play(Write(target_address_formula))
            self.play(Write(bit_n_formula))
        else:
            self.add(
                alias_sram_base_formula,
                bitband_sram_base_formula,
                target_address_formula,
                bit_n_formula,
            )

        self.wait(0.5)  # ! ---- ---- ----

        self.play(Transform(formula_copy, target_formula))

        self.wait(0.5)  # ! ---- ---- ----

        self.play(Transform(formula_copy, computed_formula_1))

        self.wait(0.5)  # ! ---- ---- ----

        self.play(Transform(formula_copy, computed_formula_2))

        self.wait(0.5)  # ! ---- ---- ----

        self.play(Transform(formula_copy, computed_formula_3))

        self.wait(0.5)  # ! ---- ---- ----

        self.play(formula_copy.animate.scale(1.5))  # type: ignore

        final_box = always_redraw(
            lambda: SurroundingRectangle(
                formula_copy, color="WHITE", fill_opacity=0.05, buff=0.25
            )
        )
        alias_sram_address_explanation = Paragraph(
            "This 32-bit word controls the specific bit in the alias region,",
            "allowing direct access to modify it.",
            "It gives us the possibility of atomic-level access,",
            "ensuring precise and efficient bit manipulation.",
            font="Cascadia Code",
            font_size=18,
            line_spacing=0.75,
            alignment="center",
        ).shift(DOWN * 0.15)
        explanation_box = SurroundingRectangle(
            alias_sram_address_explanation,
            color="WHITE",
            fill_opacity=0.05,
            buff=0.25,
        )

        if not IS_DEBUGGING:
            self.play(Create(final_box))  # type: ignore
        else:
            self.add(final_box)

        self.wait(1)  # ! ---- ---- ----

        self.play(
            FadeOut(
                alias_sram_base_formula,
                bitband_sram_base_formula,
                target_address_formula,
                bit_n_formula,
            ),
            formula_copy.animate.align_to(box, LEFT).shift(RIGHT * 0.25),  # type: ignore
        )

        self.wait(0.5)  # ! ---- ---- ----

        if not IS_DEBUGGING:
            for i, line in enumerate(alias_sram_address_explanation):
                self.play(Write(line), run_time=1)

                if i != len(alias_sram_address_explanation) - 1:
                    self.wait(0.25)  # ! ---- ---- ----

            self.play(Create(explanation_box))  # type: ignore
        else:
            for i, line in enumerate(alias_sram_address_explanation):
                self.add(line)

                if i != len(alias_sram_address_explanation) - 1:
                    self.wait(0.25)  # ! ---- ---- ----

            self.add(explanation_box)

        curved_arrow = always_redraw(
            lambda: CurvedArrow(
                final_box.get_edge_center(RIGHT),
                explanation_box.get_edge_center(DOWN)
                + RIGHT * (explanation_box.get_width() / 4),
                angle=PI / 3,
                color=WHITE,
                stroke_width=3,
                tip_length=0.2,
            )
        )

        if not IS_DEBUGGING:
            self.play(Create(curved_arrow))  # type: ignore
        else:
            self.add(curved_arrow)

        self.wait(2)  # ! ---- ---- ----

        self.play(
            FadeOut(
                formula_copy,
                formula,
                final_box,
                box,
                curved_arrow,
                alias_sram_address_explanation,
                explanation_box,
            )
        )

        self.wait(0.5)  # ! ---- ---- ----

        # & Demonstration                                                        :
        topics[6].set_color(WHITE)
        topics[8].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----
        """

        # + Demonstration Elements
        c_code = MarkupText(
            f"<span fgcolor='{GREEN_A}'>#</span><span fgcolor='{PURPLE}'>include</span> <span fgcolor='{GREEN_A}'>&lt;</span><span fgcolor='{GREEN}'>stdint.h</span><span fgcolor='{GREEN_A}'>&gt;</span>\n"
            + f"\n"
            + f"<span fgcolor='{PURPLE}'>void</span> <span fgcolor='{BLUE}'>main</span><span fgcolor='{YELLOW}'>(</span><span fgcolor='{PURPLE}'>void</span><span fgcolor='{YELLOW}'>) {{</span>\n"
            + f"    <span fgcolor='{ORANGE}'>uint8_t</span> <span fgcolor='{WHITE}'>temp =</span> <span fgcolor='{RED}'>2;</span>\n"
            + f"\n"
            + f"    <span fgcolor='{WHITE}'>temp |=</span> <span fgcolor='{PURPLE}'>0x</span><span fgcolor='{RED}'>4;</span>\n"
            + f"    <span fgcolor='{WHITE}'>temp &amp;= ~</span><span fgcolor='{PURPLE}'>0x</span><span fgcolor='{RED}'>4;</span>\n"
            + f"<span fgcolor='{YELLOW}'>}}</span>\n"
            + f"\n",
            font="Cascadia Code",
            font_size=20,
        )
        c_code_box = always_redraw(
            lambda: SurroundingRectangle(
                c_code, color=WHITE, fill_opacity=0.05, buff=0.25
            )
        )
        c_code_title = always_redraw(
            lambda: Text(
                "Bit Masking", color=WHITE, font="Cascadia Code", font_size=18
            ).next_to(c_code_box, UP)
        )
        target_c_code = MarkupText(
            f"<span fgcolor='{WHITE}'>temp |=</span> <span fgcolor='{PURPLE}'>0x</span><span fgcolor='{RED}'>4;</span>",
            font="Cascadia Code",
            font_size=20,
        )

        # - Animate Demonstration Elements
        if not IS_DEBUGGING:
            self.play(Write(c_code))
            self.play(Create(c_code_box))  # type: ignore
            self.play(Write(c_code_title))  # type: ignore
        else:
            self.add(c_code, c_code_box, c_code_title)

        self.wait(1)  # ! ---- ---- ----

        self.play(Transform(c_code, target_c_code))

        self.play(c_code.animate.shift(LEFT * 4.35))  # type: ignore

        arrow = Arrow(
            start=c_code_box.get_edge_center(RIGHT) + LEFT * 0.25,
            end=c_code_box.get_edge_center(RIGHT) + RIGHT * 6,
            color=WHITE,
            stroke_width=3,
            tip_length=0.2,
        )

        if not IS_DEBUGGING:
            self.play(Create(arrow))
        else:
            self.add(arrow)

        assembly_code = MarkupText(
            f"<span fgcolor='{GREEN}'>ldrb r3,</span> <span fgcolor='{YELLOW}'>[</span><span fgcolor='{WHITE}'>r7,</span> <span fgcolor='{BLUE}'>#7</span><span fgcolor='{YELLOW}'>]</span>\n"
            + f"<span fgcolor='{GREEN}'>orr  r3, r3,</span> <span fgcolor='{BLUE}'>#4</span>\n"
            + f"<span fgcolor='{GREEN}'>strb r3,</span> <span fgcolor='{YELLOW}'>[</span><span fgcolor='{WHITE}'>r7,</span> <span fgcolor='{BLUE}'>#7</span><span fgcolor='{YELLOW}'>]</span>\n",
            font="Cascadia Code",
            font_size=20,
        ).next_to(arrow, RIGHT, buff=0.25)
        assembly_code_box = SurroundingRectangle(
            assembly_code, color=WHITE, fill_opacity=0.05, buff=0.25
        )
        assembly_code_title = Text(
            "Assembly Code", color=WHITE, font="Cascadia Code", font_size=18
        ).next_to(assembly_code_box, UP)

        if not IS_DEBUGGING:
            self.play(Write(assembly_code))
            self.play(Create(assembly_code_box))  # type: ignore
            self.play(Write(assembly_code_title))  # type: ignore
        else:
            self.add(assembly_code, assembly_code_box, assembly_code_title)

        compiler_note_up = Text(
            "Using GCC", font="Cascadia Code", font_size=18, color=PURPLE
        ).next_to(arrow, UP, buff=0.05)
        compiler_note_down = Text(
            "(arm-none-eabi-gcc)", font="Cascadia Code", font_size=18, color=ORANGE
        ).next_to(arrow, DOWN, buff=0.05)

        if not IS_DEBUGGING:
            self.play(Write(compiler_note_up), Write(compiler_note_down))
        else:
            self.add(compiler_note_up, compiler_note_down)

        self.wait(1)  # ! ---- ---- ----

        code_note_arrow = Arrow(
            c_code_box.get_edge_center(DOWN) + UP * 0.25,
            c_code_box.get_edge_center(DOWN) + DOWN * 1,
            color=WHITE,
            stroke_width=3,
            tip_length=0.2,
        )

        if not IS_DEBUGGING:
            self.play(Create(code_note_arrow))
        else:
            self.add(code_note_arrow)

        code_note = (
            MarkupText(
                f"This <span fgcolor='{BLUE}'>simple operation</span> requires "
                + f"<span fgcolor='{RED}'>3 instructions</span> to complete,\n"
                + f"wasting <span fgcolor='{YELLOW}'>clock cycles</span> and risking "
                + f"<span fgcolor='{YELLOW}'>data changes</span> before completion.",
                font="Cascadia Code",
                font_size=18,
            )
            .next_to(code_note_arrow, DR, buff=0.25)
            .align_to(c_code_box, LEFT)
            .shift(RIGHT * 0.25)
        )
        code_note_box = SurroundingRectangle(
            code_note, color=WHITE, fill_opacity=0.05, buff=0.25
        )
        code_note_box.stretch_to_fit_width(
            assembly_code_box.get_right()[0] - code_note_box.get_left()[0]
        ).shift(RIGHT * 0.475)

        if not IS_DEBUGGING:
            self.play(Write(code_note))
            self.play(Create(code_note_box))
        else:
            self.add(code_note, code_note_box)

        self.wait(2)  # ! ---- ---- ----

        self.play(
            FadeOut(
                c_code,
                c_code_box,
                c_code_title,
                assembly_code,
                assembly_code_box,
                assembly_code_title,
                arrow,
                compiler_note_up,
                compiler_note_down,
                code_note_arrow,
                code_note,
                code_note_box,
            )
        )  # type: ignore

        self.wait(0.5)  # ! ---- ---- ----

        # & Conclusion                                                           :
        topics[8].set_color(WHITE)
        topics[10].set_color(YELLOW)

        self.wait(0.5)  # ! ---- ---- ----

        #

        self.wait(2)
