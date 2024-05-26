from manim import *

class SVGToTextAnimation(Scene):
    def construct(self):
        # Load the SVG file
        svg_path = "../../svg/hotel-svgrepo-com.svg"
        svg_mobject = SVGMobject(svg_path)
        
        # Scale and position the SVG as needed
        svg_mobject.scale(2)
        svg_mobject.to_edge(UP)

        # Add the SVG to the scene
        self.play(DrawBorderThenFill(svg_mobject))
        self.wait(1)

        # Create a Text object to replace the SVG
        text = Text("文章标题", color=BLACK, font="msjh")
        text._set_color_by_t2c({"文章": GREEN, "标题": PURPLE})
        text.scale(2)
        text.move_to(svg_mobject.get_center())

        # Transition from SVG to Text
        self.play(Transform(svg_mobject, text))
        self.wait(2)

# import config
from manim import config
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 7.0
config.frame_width = 14.0
config.frame_rate = 30
# white background
config.background_color = WHITE
scene = SVGToTextAnimation()
scene.render()