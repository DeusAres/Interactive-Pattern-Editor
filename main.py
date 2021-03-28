import PySimpleGUI as sg

defined_size = (100, 1)
layout = [
    [sg.Text(text="PATTERN EDITOR", justification="center", size=defined_size)],
    [sg.Graph(
        graph_bottom_left = (0,500), graph_top_right = (500, 0),
        background_color = "#FFFFFF", canvas_size=(500, 500), pad=(0, 20),
        drag_submits = True, enable_events = True, key = '-GRAPH-'
        )
    ],
    [
        sg.Button("Crop"), 
        sg.Input(key='-IMPORT-', enable_events=True, visible=False),
        sg.FileBrowse("Import image", key = '-IMAGE-', target='-IMPORT-'),
        sg.Checkbox("Rotate", key = '-ROTATE-')
    ]

]

mainWindow = sg.Window("Pattern editor", layout, finalize = True)
dragging = False
start_point = end_point = prior_rect = None
while True:
    event, values = mainWindow.read()
    print(event)
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == '-IMPORT-':
        graph = mainWindow['-GRAPH-']
        image = graph.draw_image(filename = values['-IMAGE-'],  location=(0,100))
    if event == '-GRAPH-':
        x, y = values["-GRAPH-"]
        if not dragging:
                start_point = (x, y)
                dragging = True
                drag_figures = graph.get_figures_at_location((x,y))
                lastxy = x, y
        else:
            end_point = (x, y)
        if prior_rect:
            graph.delete_figure(prior_rect)
        delta_x, delta_y = x - lastxy[0], y - lastxy[1]
        lastxy = x,y
        if None not in (start_point, end_point):
            #if values['-MOVE-']:
            for fig in drag_figures:
                graph.move_figure(fig, delta_x, delta_y)
                graph.update()
    if values['-ROTATE-']:
        x, y = values["-GRAPH-"]
        rotate_figure = graph.get_figures_at_location((x,y))
        image 

    #if event == ''
mainWindow.close()