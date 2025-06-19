from pathlib import Path
from nicegui import ui, app
from datetime import datetime
from widgets.map_view import map_view, update_map_view, Point
from widgets.stream_view import static_view, stream_view, update_stream_view
import random

# --- Styling ---
AMAZON_BLUE = '#146eb4'  # Amazon logo blue
ui.colors(primary=AMAZON_BLUE)
# ui.dark_mode().enable()

resources_path = Path(__file__).parent.parent / 'resources'
app.add_static_files('/resources', resources_path)

# --- Title Banner ---
with ui.header().classes('items-center justify-center'):
    ui.label('🐾 Vulcan Pick Amnesty Patrol 🐾').classes('text-3xl text-white font-bold')

time_label = ui.label().classes('ml-auto text-right')

# --- Main Content Grid (2x2) ---
with ui.grid(columns=2).classes('w-full gap-2'):
    # Top Left: Robot Wrist View, Top Right: Robot Front View
    front_image = stream_view('Robot Front View', '/resources/episode_front.mp4')
    wrist_image = stream_view('Robot Wrist View', '/resources/rotated.mov')
    # Bottom Left: Workcell Map
    map_image = map_view('Workcell Map', '/resources/workcell.png')
    # Bottom Right: Item Image
    item_image = static_view('Item Image', '/resources/chicken.jpg')

# --- Bottom Panel: Joint Info and Buttons ---
# with ui.row().classes('w-full items-center justify-between'):
with ui.grid(columns=2).classes('w-full gap-2'):
    # Left: Robot Telemetry
    with ui.card().classes('w-full'):
        ui.label('Robot Telemetry').classes('text-xl font-semibold')
        telemetry_label = ui.label().classes('w-full font-mono whitespace-pre overflow-auto')

    # Right: Item Data
    with ui.card().classes('w-full'):
        def log_success():
            print(f"[{datetime.now()}] SUCCESS clicked")
        def log_failure():
            print(f"[{datetime.now()}] FAILURE clicked")
        ui.label('Item Data').classes('text-xl font-semibold')
        item_label = ui.label().classes('w-full font-mono whitespace-pre overflow-auto')
        with ui.row():
            ui.button('SUCCESS', color='green', on_click=log_success).classes('text-white')
            ui.button('FAILURE', color='red', on_click=log_failure).classes('text-white')


def update():
    update_stream_view(front_image)
    update_stream_view(wrist_image)
    # Draw item and robot location on map
    # + random.randint(-10, 10)
    update_map_view(map_image, Point(1000, 700), Point(340, 550))
    update_stream_view(item_image)

    time_label.set_text(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    telemetry_label.set_text(
        "J1: 0.0, J2: 0.0, J3: 0.0\n"
        "J4: 0.0, J5: 0.0, J6: 0.0\n"
        "X: 0.0, Y: 0.0, Thea: 0.0\n"
    )
    item_label.set_text("ASIN: B0CKPMKM6V\n" "Yellow Rubber Chicken Squeak Mini Rubber Chicks Squeezable Squeaky Toy Chicken Noisemaker for Shower Bath Birthday Novelty Favors Decorations Gift, 1.38 x 2.17 x 2.76 Inch")


# --- Run the app ---
ui.timer(0.1, update)
ui.run(title='Vulcan Pick Amnesty Patrol')
