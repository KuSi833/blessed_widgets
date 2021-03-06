from enum import Enum, auto, unique

# Maximum angle between diraction of movement and center of widget
MAX_ANGLE = 70


@unique
class HAlignment(Enum):
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()


@unique
class VAlignment(Enum):
    TOP = auto()
    MIDDLE = auto()
    BOTTOM = auto()


@unique
class State(Enum):
    IDLE = auto()
    DISABLED = auto()
    SELECTED = auto()
    CLICKED = auto()
    FOCUSED = auto()


@unique
class Side(Enum):
    TOP = auto()
    RIGHT = auto()
    BOTTOM = auto()
    LEFT = auto()


@unique
class WindowState(Enum):
    VIEW = auto()
    SELECTION = auto()
    FOCUSED = auto()


@unique
class Direction(Enum):
    DOWN = 270
    LEFT = 0
    UP = 90
    RIGHT = 180


@unique
class BorderStyle(Enum):
    SINGLE = auto()
    DOUBLE = auto()
    NONE = auto()


@unique
class Response(Enum):
    CONTINUE = auto()
    COMPLETE = auto()
    QUIT = auto()
    FOCUSED = auto()
    UNFOCUSED = auto()


@unique
class Layout(Enum):
    ABSOLUTE = auto()
    FLEX = auto()
    GRID = auto()
