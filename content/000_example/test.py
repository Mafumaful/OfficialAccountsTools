from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

if __name__ == "__main__":
    config.background_color = WHITE
    config.pixel_height = 480
    config.pixel_width = 854
    config.frame_rate = 30
    scene = SquareToCircle()
    scene.render()