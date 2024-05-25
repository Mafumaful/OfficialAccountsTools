from manim import *

class TextTransform(Scene):
    def construct(self):
        # Create the initial and target text
        initial_text = Text("文章标题", color=BLACK, font="msjh")
        initial_text._set_color_by_t2c({"文章": GREEN, "标题": PURE_BLUE})

        target_text = Text("这个是小节标题", color=BLACK, font="msjh")
        target_text._set_color_by_t2c({"这个是": PURE_RED, "小节": DARKER_GREY, "标题": PURPLE})

        # Display the initial text
        self.play(Write(initial_text))
        self.wait(1)

        # Transform the initial text into the target text
        self.play(Transform(initial_text, target_text))
        self.wait(1)

# if __name__ == "__main__":
from manim import config
config.background_color = WHITE
config.pixel_height = 150
config.pixel_width = 854
config.frame_rate = 30
scene = TextTransform()
scene.render()
