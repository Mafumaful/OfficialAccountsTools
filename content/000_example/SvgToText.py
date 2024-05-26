# svg to text

from manim import *

class SVGToText(Scene):
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

        # Create a Text object
        text = Text("文章标题", color=BLACK, font="msjh")
        
        # Position the text where you want it to be
        text.next_to(svg_mobject, DOWN)

        # Add the text to the scene
        self.play(Write(text))
        self.wait(2)

        # Optionally, you can add further animations or manipulations


# import config
from manim import config
config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 7.0
config.frame_width = 14.0
config.frame_rate = 30
# white background
config.background_color = WHITE
scene = SVGToText()
scene.render()