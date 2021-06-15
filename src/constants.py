from enum import Enum, auto, unique

# Maximum angle between diraction of movement and center of widget
MAX_ANGLE = 50


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
class ButtonState(Enum):
    IDLE = auto()
    DISABLED = auto()
    SELECTED = auto()
    CLICKED = auto()


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


@unique
class Direction(Enum):
    UP = 90
    LEFT = 180
    DOWN = 270
    RIGHT = 0
