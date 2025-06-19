from typing import NamedTuple
import numpy as np
import cv2
from nicegui import ui
from nicegui.elements.interactive_image import InteractiveImage


class Point(NamedTuple):
    x: int
    y: int


def map_view(image_label: str, image_url: str) -> InteractiveImage:
    with ui.card().classes('w-full'):
        ui.label(image_label).classes('text-xl font-semibold')
        map_image = ui.interactive_image(image_url).classes('w-full')
    return map_image


def update_map_view(map_image: InteractiveImage, target: Point, current: Point) -> None:
    # map_image._interactions.clear()
    map_image.content += f'<circle cx="{current.x}" cy="{current.y}" r="50" fill="none" stroke="green" stroke-width="5" />'
    map_image.content += f'<circle cx="{target.x}" cy="{target.y}" r="50" fill="none" stroke="red" stroke-width="5" />'

