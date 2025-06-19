import numpy as np
import cv2
import base64
from nicegui import ui
from nicegui.elements.image import Image

# def _convert_np_to_base64(img: np.ndarray) -> str:
#     _, buffer = cv2.imencode('.jpg', img)
#     jpg_as_text = base64.b64encode(buffer).decode('utf-8')
#     return f'data:image/jpeg;base64,{jpg_as_text}'



def static_view(image_label: str, image_url: str) -> None:
    with ui.card().classes('w-full'):
        ui.label(image_label).classes('text-xl font-semibold')
        img = ui.image(image_url).classes('w-full')
    # return img

def stream_view(image_label: str, image_url: str) -> None:
    with ui.card().classes('w-full'):
        ui.label(image_label).classes('text-xl font-semibold')
        # img = ui.image(image_url).classes('w-full')
        ui.html(f'''
            <video autoplay loop muted playsinline style="width: 100%; height: auto;">
                <source src="{image_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        ''')
    # return img

def update_stream_view(image: Image) -> None:
    None