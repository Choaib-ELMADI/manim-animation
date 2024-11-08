from manim import *


class Main(Scene):
    def construct(self):
        rectangle_1 = Rectangle(color="PURPLE", height=5, width=8)
        rectangle_2 = Rectangle(
            color="GREEN", height=4, width=7, grid_xstep=3.5, grid_ystep=2
        )
        rectangle_3 = Rectangle(
            color="YELLOW",
            height=3,
            width=6,
            grid_xstep=2,
            grid_ystep=1.5,
            mark_paths_closed=False,
        )
        rectangle_4 = Rectangle(
            color="RED",
            height=2,
            width=5,
            grid_xstep=1,
            grid_ystep=1,
            mark_paths_closed=False,
            close_new_points=False,
        )

        rectangles_group = Group(rectangle_1, rectangle_2, rectangle_3, rectangle_4)
        rectangles = [rectangle_1, rectangle_2, rectangle_3, rectangle_4]

        # self.add(rectangles_group)
        # self.play(Create(rectangle_1), run_time=2)
        # self.wait()

        for i in range(0, 4):
            self.play(Create(rectangles[i]), run_time=1)
            self.wait()
