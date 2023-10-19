
"""
Shapes App
Drawing shapes with Matplotlib

[*]                                                                                            [*]
[*] Capstone Project                                                                           [*]
[*]                                                                                            [*]
[@]Code:
"""

import streamlit as st
from env_colors import Color
from shapes import Circle, Square, EquilateralTriangle, Rectangle, Canvas


LOADED = False

# [>]                                                                                            #
# [>] Canvas Helper                                                                              #
# [>]                                                                                            #


class CanvasHelper:
    @staticmethod
    def create_example():
        shapes = []

        c1 = Circle(xy=(50, 50), radius=10,
                    color=Color.GREEN, alpha=0.5, fill=True)
        shapes.append(c1)
        print(c1.__str__())

        shapes.append(
            Circle(xy=(55, 55), radius=20, color=Color.GREEN, alpha=0.5, fill=False))
        print(shapes[-1].__str__())

        shapes.append(
            Square(xy=(-40, 45), side=20, color=Color.BLUE, alpha=0.5, fill=True))
        print(shapes[-1].__str__())

        shapes.append(
            Square(xy=(-45, 40), side=40, color=Color.BLUE, alpha=0.5, fill=False))
        print(shapes[-1].__str__())

        shapes.append(
            EquilateralTriangle(xy=(0, 0), side=20, color=Color.PINK, alpha=0.5, fill=True))
        print(shapes[-1].__str__())

        shapes.append(
            EquilateralTriangle(xy=(-10, -10), side=40, color=Color.PINK, alpha=0.5, fill=False))
        print(shapes[-1].__str__())

        shapes.append(
            Rectangle(xy=(-40, -55), width=100, height=20, color=Color.RED, alpha=0.5, fill=False))
        print(shapes[-1].__str__())

        shapes.append(
            Rectangle(xy=(-35, -50), width=90, height=10,
                      color=Color.RED, alpha=0.5, fill=True)
        )
        print(shapes[-1].__str__())

        return shapes


# [>]                                                                                            #
# [>] Header                                                                                     #
# [>]                                                                                            #

def c_canvas_config():
    # st.header("Shapes App    🟢 🔺 🟨")
    with st.expander("Canvas Configuration"):

        st.session_state["width_range"] = st.slider(
            "Width range (min x and max x)", -1000, 1000, (-250, 250))
        st.session_state["height_range"] = st.slider(
            "Height range (min y and max y)", -1000, 1000, (-250, 250))
        st.session_state["axes_text_size"] = st.slider(
            "Text size", 1, 10, 5)

        col1, col2 = st.columns(2)

        with col1:
            st.session_state["axes_text_color"] = st.color_picker(
                'Axes text color:',
                value=Color.GRAY
            )

        with col2:
            st.session_state["box_color"] = st.color_picker(
                'Box color:', value=Color.GRAY)



# [>]                                                                                            #
# [>] Side bar                                                                                   #
# [>]                                                                                            #

def c_side_bar():
    with st.sidebar:
        st.header("Shapes App    🟢 🔺 🟨")
        c_canvas_config()

        c_shape_bar()


# region Shape Bar

# [>]                                                                                            #
# [>] draw shape bar - position x, y                                                             #
# [>]                                                                                            #


def c_shape_bar_position_section(show: bool = True):
    """
     It shows the widgets of shape's position configuration and returns the users' choices.

    Returns:
        - x_pos : a number (between x_min and x_max)
        - y_pos : a number (between y_min and y_max)

    """
    # position
    if show:

        # x_pos = st.number_input(
        #     "X position", step=1,
        #     min_value=st.session_state["width_range"][0],
        #     max_value=st.session_state["width_range"][1],
        #     value=50
        # )

        x_pos = st.slider(
            "X position", step=1,
            min_value=st.session_state["width_range"][0],
            max_value=st.session_state["width_range"][1],
            value=50
        )

        # st.caption(
        #     "Remember, the X position should be a number inside the X range (min x and max x)." +
        #     str(st.session_state["width_range"])
        # )

        # y_pos = st.number_input(
        #     "Y position", step=1,
        #     min_value=st.session_state["height_range"][0],
        #     max_value=st.session_state["height_range"][1],
        #     value=50
        # )

        y_pos = st.slider("Y position", step=1,
            min_value=st.session_state["height_range"][0],
            max_value=st.session_state["height_range"][1],
            value=50)

        # st.caption(
        #     "Remember, the X position should be a number inside the Y range (min y and max y)." +
        #     str(st.session_state["height_range"])
        # )

        return x_pos, y_pos
    return None, None


# [>]                                                                                            #
# [>] draw shape bar - color                                                                     #
# [>]                                                                                            #

def c_shape_bar_color_section(show: bool = True):
    """
    It shows the widgets of shape's color configuration and returns the users' choices.

    Returns:
        - color : hexadecimal of a color
        - alpha : a number between 0 an 1
        - fill : boolean
    """
    # color

    if show:
        color = st.color_picker('Color:', value=Color.BLUE)

        alpha = st.number_input(
            "Color alpha (level of transparency)", step=0.1,
            min_value=0.0,
            max_value=1.0,
            value=0.5
        )

        fill = st.toggle("Fill Color?")

        return color, alpha, fill

    return None, None, None


# [>]                                                                                            #
# [>] Circle                                                                                     #
# [>]                                                                                            #

def c_circle(
    x_pos: int, y_pos: int, color: str, alpha: float, fill: bool, shape_option: str
) -> None:
    """
    Circle's specific features
    """
    radius = st.slider("Circle radius", 1, 100, 50)

    s = Circle(xy=(x_pos, y_pos), radius=radius, color=color, alpha=alpha, fill=fill)

    btn_add_shape = st.button(f"Add {shape_option}")

    if btn_add_shape:
        st.session_state["shapes"].append(s)


# [>]                                                                                            #
# [>] Square                                                                                     #
# [>]                                                                                            #

def c_square(
    x_pos: int, y_pos: int, color: str, alpha: float, fill: bool, shape_option: str
) -> None:
    """
    Square's specific features
    """
    side = st.slider("Square side", 1, 100, 50)

    s = Square(xy=(x_pos, y_pos), side=side, color=color, alpha=alpha, fill=fill)

    btn_add_shape = st.button(f"Add {shape_option}")

    if btn_add_shape:
        st.session_state["shapes"].append(s)

# [>]                                                                                            #
# [>] Rectangle                                                                                  #
# [>]                                                                                            #

def c_rectangle(
    x_pos: int, y_pos: int, color: str, alpha: float, fill: bool, shape_option: str
) -> None:
    """
    Rectangle's specific features
    """
    width = st.slider("Rectangle width", 1, 100, 50)
    height = st.slider("Rectangle height", 1, 100, 25)

    s = Rectangle(
        xy=(x_pos, y_pos), width=width, height=height,
        color=color, alpha=alpha, fill=fill
    )

    btn_add_shape = st.button(f"Add {shape_option}")

    if btn_add_shape:
        st.session_state["shapes"].append(s)


# [>]                                                                                            #
# [>] Equilateral Triangle                                                                       #
# [>]                                                                                            #

def c_equilateral_triangle(
    x_pos: int, y_pos: int, color: str, alpha: float, fill: bool, shape_option: str
) -> None:
    """
    Rectangle's specific features
    """
    side = st.slider("Triangle side", 1, 100, 50)

    s = EquilateralTriangle(xy=(x_pos, y_pos), side=side, color=color, alpha=alpha, fill=fill)

    btn_add_shape = st.button(f"Add {shape_option}")

    if btn_add_shape:
        st.session_state["shapes"].append(s)


# [>]                                                                                            #
# [>] draw shape bar                                                                             #
# [>]                                                                                            #

def c_shape_bar():

    # [i] Shapes type (available).
    options = ["Please, select a shape type", "Circle",
               "Square", "EquilateralTriangle", "Rectangle"]

    shape_option = st.selectbox(
        label="Select the shape to add:",
        options=options
    )

    # [i] Common features of all shapes.

    x_pos, y_pos = c_shape_bar_position_section(shape_option != options[0])

    color, alpha, fill = c_shape_bar_color_section(shape_option != options[0])

    # [i] Shape's specific features.

    if shape_option == "Circle":
        c_circle(x_pos, y_pos, color, alpha, fill, shape_option)

    elif shape_option == "Square":
        c_square(x_pos, y_pos, color, alpha, fill, shape_option)

    elif shape_option == "EquilateralTriangle":
        c_equilateral_triangle(x_pos, y_pos, color, alpha, fill, shape_option)

    elif shape_option == "Rectangle":
        c_rectangle(x_pos, y_pos, color, alpha, fill, shape_option)

# endregion


# [>]                                                                                            #
# [>] Canvas bar                                                                                 #
# [>]                                                                                            #

def c_canvas_bar():
    col1, col2 = st.columns(2)
    with col1:
        btn_load_example = st.button("Load examples", use_container_width=True)

    with col2:
        btn_clear_shapes = st.button("Clear canvas", use_container_width=True)

    if btn_load_example:
        st.session_state["shapes"] = CanvasHelper.create_example()

    if btn_clear_shapes:
        st.session_state["shapes"] = []


# [*]                                                                                            #
# [*] MAIN                                                                                       #
# [*]                                                                                            #

if __name__ == "__main__":

    # Initializes shapes state (list of shapes that will be drawn on the canvas)
    if "shapes" not in st.session_state:
        st.session_state["shapes"] = []


    tab1, tab2 = st.tabs(["Canvas", "Memory"])

    with tab1:
        st.header("Canvas")



        # sidebar
        c_side_bar()

        # canvas
        c_canvas_bar()

        canvas = Canvas(
            width_range=st.session_state["width_range"],
            height_range=st.session_state["height_range"],
            axes_text_size=st.session_state["axes_text_size"],
            axes_text_color=st.session_state["axes_text_color"],
            box_color=st.session_state["box_color"],
        )

        canvas.render(shapes=st.session_state["shapes"], is_streamlit=True)

    with tab2:
        st.subheader("🧩 Shapes state:")
        st.write(st.session_state["shapes"])

        st.subheader("🧠 All memory:")
        st.write(st.session_state)
