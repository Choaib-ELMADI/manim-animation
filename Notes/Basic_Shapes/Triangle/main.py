from manim import *


class Main(Scene):
    def construct(self):
        triangle_1 = Triangle(color="PURPLE").scale(4)
        triangle_2 = Triangle(color="YELLOW").scale(4).rotate(30)
        triangle_3 = Triangle(color="GREEN").scale(2.5)
        triangle_4 = Triangle(color="RED").scale(0.5).rotate(-50)

        triangles_group = Group(triangle_1, triangle_2, triangle_3, triangle_4)
        triangles = [triangle_1, triangle_2, triangle_3, triangle_4]

        # self.add(triangles_group)
        # self.play(Create(triangle_1), run_time=2)
        # self.wait()

        for i in range(0, 4):
            self.play(Create(triangles[i]), run_time=1)
            self.wait()
