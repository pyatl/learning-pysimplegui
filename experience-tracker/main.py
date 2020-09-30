
import os
import PySimpleGUI as sg


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets/' )


def experience_tracker():

    NAME = 'Experience Tracker'

    BACKGROUND = '#F0F0F0'

    happy_face = os.path.join(ASSETS_DIR, 'happy.png')
    serious_face = os.path.join(ASSETS_DIR, 'serious.png')
    sad_face = os.path.join(ASSETS_DIR, 'sad.png') 

    layout= [[sg.Text(NAME,size=(17,1), font=("Helvetica", 25))],
                [  
                sg.Button('', button_color=(BACKGROUND,BACKGROUND),
                                image_filename=happy_face, image_size=(50, 50), image_subsample=2, border_width=0, key='happy'),
                                sg.Text(' ' * 2),
                sg.Button('', button_color=(BACKGROUND,BACKGROUND),
                                image_filename=serious_face, image_size=(100, 100), image_subsample=2, border_width=0, key='serious'),
                                sg.Text(' ' * 2),
                sg.Button('', button_color=(BACKGROUND,BACKGROUND),
                                image_filename=sad_face, image_size=(100, 100), image_subsample=2, border_width=0, key='sad'),
                                sg.Text(' ' * 2),
                ]
            ]

        
    window = sg.Window(NAME, layout, default_element_size=(20, 1),
            font=("Helvetica", 25))
        
    while(True):
        event, values = window.read(timeout=100) # Poll every 100 ms
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        elif event == 'happy':
            print('happy')
        elif event == 'serious':
            print('serious')
        elif event == 'sad':
            print('sad')



experience_tracker()