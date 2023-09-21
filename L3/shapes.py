"""
Shapes and Drawing with Matplotlib

Classes:
- Canvas (class that uses Shape subclasses
- Shape (superclass)
- Circle (subclass)
- EquilateralTriangle (subclass)
- Square (subclass)
- Rectangle (subclass)
- Polygon (subclass)

This Python script defines a set of classes for representing and drawing various geometric shapes, including circles, squares, rectangles, and equilateral triangles. The shapes are represented as objects that can be drawn using the Matplotlib library.

Usage:
- Import this module to create and visualize geometric shapes.
- Each shape class provides a `draw` method that returns a Matplotlib patch representing the shape.
- You can customize the shape's appearance, including color, fill, and transparency.

[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@]Code:
"""


import matplotlib.pyplot as plt
import matplotlib.patches as patches

from env_colors import Color, TerminalTextColor

print("✅ Packages imported")

# [>]                                                                                            #
# [>] Shape                                                                                      #
# [>]                                                                                            #

class Shape:
    """
    Base class for geometric shapes.

    Attributes:
    - color (Color): The color of the shape.
    - xy (tuple): The position of the shape.
    - fill (bool): Whether the shape is filled.
    - alpha (float): The transparency of the shape.

    Methods:
    - draw(): Abstract method that must be implemented by subclasses to return a Matplotlib patch.
    - __str__(): Returns a string representation of the shape's attributes.
    - print__str__fancy(): Prints a formatted description of the shape's attributes.
    """
    color: Color = Color.BLACK
    # x1: int = 0
    # y1: int = 0
    fill: bool = False
    alpha: float = 1

    def __init__(self,
                 # x1: int = 0, y1: int = 0,
                 xy: tuple = (0, 0),
                 color: Color = Color.BLACK,
                 fill: bool = False, alpha: float = 1
                 ):
        """
        Shape class constructor
        """
        self.color = color
        self.xy = xy
        # self.x1 = x1
        # self.y1 = y1
        self.fill = fill
        self.alpha = alpha

    def draw(self):
        """
        Abstract method, must be implemented by subclasses.

        """
        return "⚠️ I am an abstract method, I do not represent any shape"

    def __str__(self):
        shift = "   "
        # return 'from new __str__: ' + object.__str__(self)
        class_name = str(type(self)).split('.')[-1].replace("'>", "")

        return f"\n💬 Class: {class_name}. \n{shift}Attributes: {self.__dict__}"
        # + str(self.__dict__)

    def print__str__fancy(self):
        """
        print the class description in a "fancy" way 😎
        """
        shift = "   "
        attributes = ""
        n_repeat = 80

        class_name = str(type(self)).split('.')[-1].replace("'>", "")

        print(
            f"👋 Class: {TerminalTextColor.GREEN}{class_name}{TerminalTextColor.RESET}\n{'-' * n_repeat}")

        for k in self.__dict__:
            attributes += f"\n{shift}{shift}- {k}: {TerminalTextColor.BLUE}{self.__dict__[k]}{TerminalTextColor.RESET}"

        print(f"\n{shift}🏷️ Attributes: ")
        print(attributes)

        print(f"\n{shift}⚡️ Draw method return ")
        print(f'\n{shift}{shift}-{str(self.draw())}')

        title = '- the end -'
        print(f'\n{title}{"-" * (n_repeat-len(title))}')


# [>]                                                                                            #
# [>] Circle                                                                                     #
# [>]                                                                                            #

class Circle(Shape):
    """
    Class for representing circles.

    Attributes:
    - radius (int): The radius of the circle.

    Methods:
    - draw(): Returns a Matplotlib Circle patch.
    """
    radius: int

    def __init__(self,
                 radius: int,
                 xy: tuple,
                 # x1: int = 0, y1: int = 0,
                 color: Color = Color.BLACK,
                 fill: bool = False, alpha: float = 1
                 ):
        super().__init__(color=color, xy=xy, fill=fill, alpha=alpha)
        self.radius = radius

    def draw(self):
        """
        Method that returns a representation of the shape by using `matplotlib.patches`.
        This object creates a shape representation that can be plotted by a canvas (`matplotlib.pyplot`).

        * Remark: You need a canvas (`matplotlib.pyplot`) that plots the shape representation.
        """
        return patches.Circle(
            xy=self.xy,
            radius=self.radius,
            fill=self.fill,
            alpha=self.alpha,
            color=self.color
        )


# [>]                                                                                            #
# [>] Square                                                                                     #
# [>]                                                                                            #

class Square(Shape):
    side: int

    def __init__(self, side: int, xy: tuple, color: Color = Color.BLUE, fill: bool = False, alpha: float = 1):
        super().__init__(color=color, xy=xy, fill=fill, alpha=alpha)
        self.side = side

    def draw(self):
        """
        Method that returns a representation of the shape by using `matplotlib.patches`.
        This object creates shapes representation that can be drawn by a canvas (`matplotlib.pyplot`).

        * Remark: You need a canvas (`matplotlib.pyplot`) that plots the shape representation.
        """
        return patches.Rectangle(
            xy=self.xy,
            width=self.side,
            height=self.side,
            fill=self.fill,
            alpha=self.alpha,
            color=self.color
        )


# [>]                                                                                            #
# [>] Rectangle                                                                                  #
# [>]                                                                                            #

class Rectangle(Shape):
    width: int
    height: int

    def __init__(self,
                 width: int, height: int, xy: tuple,
                 color: Color = Color.BLACK, fill: bool = False, alpha: float = 1
                 ):
        super().__init__(color=color, xy=xy, fill=fill, alpha=alpha)
        self.width = width
        self.height = height

    def draw(self):
        """
        Method that returns a representation of the shape by using `matplotlib.patches`.
        This object creates a shape representation that can be plotted by a canvas (`matplotlib.pyplot`).

        * Remark: You need a canvas (`matplotlib.pyplot`) that plots the shape representation.
        """
        return patches.Rectangle(
            xy=self.xy,
            width=self.width,
            height=self.height,
            fill=self.fill,
            alpha=self.alpha,
            color=self.color
        )


# [>]                                                                                            #
# [>] EquilateralTriangle                                                                        #
# [>]                                                                                            #

class EquilateralTriangle(Shape):
    """
    Class for representing equilateral triangles.

    Attributes:
    - side (int): The length of each side of the equilateral triangle.

    Methods:
    - draw(): Returns a Matplotlib Polygon patch representing the equilateral triangle.
    """
    side: int

    def __init__(self,
                 side: int,
                 xy: tuple,
                 color: Color = Color.BLACK, fill: bool = False, alpha: float = 1
                 ):
        super().__init__(color=color, xy=xy, fill=fill, alpha=alpha)
        self.side = side

    def draw(self):
        """
        Method that returns a representation of the shape by using `matplotlib.patches`.
        This object creates a shape representation that can be plotted by a canvas (`matplotlib.pyplot`).

        * Remark: You need a canvas (`matplotlib.pyplot`) that plots the shape representation.
        """
        xs = [self.xy[0], self.side + self.xy[0],
              self.side / 2 + self.xy[0], self.xy[0]]
        ys = [self.xy[1], self.xy[1],
              (3**0.5) * self.side / 2 + self.xy[1], self.xy[1]]

        return patches.Polygon(
            list(zip(xs, ys)),
            fill=self.fill,
            alpha=self.alpha,
            color=self.color
        )

# [>]                                                                                            #
# [>] Canvas                                                                                     #
# [>]                                                                                            #

class Canvas:
  # constructor
  def __init__(self,
    width_range: tuple = (-300, 300), height_range: tuple = (-200,200),
    box_color : Color = Color.GRAY, axes_text_color: Color = Color.GRAY,
    axes_text_size = 5,
  ):
    self.background_color = Color.WHITE

    self.width_range = width_range
    self.height_range = height_range

    self.box_color = box_color
    self.axes_text_size = axes_text_size
    self.axes_text_color = axes_text_color

    # self.__ax_refresh()

  def __ax_refresh(self):
    self.fig, self.ax = plt.subplots()

    # Set axis limits
    self.ax.set_xlim(self.width_range[0], self.width_range[1])
    self.ax.set_ylim(self.height_range[0], self.height_range[1])

    # Set the aspect ratio to be equal
    self.ax.set_aspect('equal')

    self.change_box_color(self.box_color)
    self.change_axes_text_color(self.axes_text_color)


  # method
  def change_box_color(self, color: Color):
    self.ax.spines['bottom'].set_color(color)
    self.ax.spines['top'].set_color(color)
    self.ax.spines['right'].set_color(color)
    self.ax.spines['left'].set_color(color)

  # method
  def change_axes_text_color(self, color: Color):
    self.ax.tick_params(axis='x', colors=color)
    self.ax.tick_params(axis='y', colors=color)

  # method
  def render(self, shapes:list[Shape], show_box=True, show_coordinates=True,
        is_streamlit = False):

    # ax
    self.__ax_refresh()

    # Change the behavior of the canvas box and its coordinates
    if not show_box:
      self.change_box_color(self.background_color)
    if not show_coordinates:
      self.change_axes_text_color(self.background_color)

    # Print Shapes
    for shape in shapes:
      self.ax.add_patch(shape.draw())

    # PLT
    plt.yticks(fontsize=self.axes_text_size)
    plt.xticks(fontsize=self.axes_text_size)

    # Show the plot
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(50, 50)

    if not is_streamlit:
        plt.show()
    else:
        import streamlit as st
        st.pyplot(self.fig)

