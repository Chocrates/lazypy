import sys
import ctypes
from sdl2 import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

window = None
screen_surface = None
event = SDL_Event()
quit = False

key_surfaces = {
    key_press_surfaces.KEY_PRESS_SURFACE_DEFAULT: None,
    key_press_surfaces.KEY_PRESS_SURFACE_UP: None,
    key_press_surfaces.KEY_PRESS_SURFACE_DOWN: None,
    key_press_surfaces.KEY_PRESS_SURFACE_LEFT: None,
    key_press_surfaces.KEY_PRESS_SURFACE_TOTAL: None
}

class key_press_surfaces(enum):
    KEY_PRESS_SURFACE_DEFAULT = 0
    KEY_PRESS_SURFACE_UP = 1
    KEY_PRESS_SURFACE_DOWN = 2
    KEY_PRESS_SURFACE_LEFT = 3
    KEY_PRESS_SURFACE_TOTAL =4

def init():
    success = True
    global window
    global screen_surface
    if SDL_Init(SDL_INIT_VIDEO) < 0:
        print('SDL could not initialize.  SDL_Error: %s' % SDL_GetError())
        success = False
    else:
        window = SDL_CreateWindow(b'SDL Tutorial', SDL_WINDOWPOS_UNDEFINED,\
            SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN)
        if window is None:
            print('Window could not be created. SDL_Error: %s' % SDL_GetError())
            success = False
        else:
            screen_surface = SDL_GetWindowSurface(window)

    return success

def load_media():
    success = True
    global key_surfaces

    key_surfaces[KEY_PRESS_SURFACE_DEFAULT] = load_surface(b'press.bmp')
    if key_surfaces[KEY_PRESS_SURFACE_DEFAULT] is None:
        print('Unable to load default image %s.  SDL_Error: %s' % ('press.bmp',SDL_GetError()))
        success = False

    key_surfaces[KEY_PRESS_SURFACE_UP] = load_surface(b'up.bmp')
    if key_surfaces[KEY_PRESS_SURFACE_UP] is None:
        print('Unable to load default image %s.  SDL_Error: %s' % ('up.bmp',SDL_GetError()))
        success = False
    
    key_surfaces[KEY_PRESS_SURFACE_DOWN] = load_surface(b'down.bmp')
    if key_surfaces[KEY_PRESS_SURFACE_DOWN] is None:
        print('Unable to load default image %s.  SDL_Error: %s' % ('down.bmp',SDL_GetError()))
        success = False

    key_surfaces[KEY_PRESS_SURFACE_LEFT] = load_surface(b'left.bmp')
    if key_surfaces[KEY_PRESS_SURFACE_LEFT] is None:
        print('Unable to load default image %s.  SDL_Error: %s' % ('left.bmp',SDL_GetError()))
        success = False

    key_surfaces[KEY_PRESS_SURFACE_RIGHT] = load_surface(b'right.bmp')
    if key_surfaces[KEY_PRESS_SURFACE_RIGHT] is None:
        print('Unable to load default image %s.  SDL_Error: %s' % ('right.bmp',SDL_GetError()))
        success = False

    return success

def load_surface(path):
    loaded_surface = SDL_LoadBMP(path)
    if loaded_surface is None:
        print('Unable to load image %s. SDL Error: %s' %(path, SDL_GetError()))
    return loaded_surface

def close():
    global key_surfaces
    global window
    for key in key_surfaces:
        SDL_FreeSurface(key_surfaces[key])

    SDL_DestroyWindow(window)
    window = None
    
    SDL_Quit()
    

def main():
    global event
    global quit
    global key_surfaces
    if not init():
        print('Failed to initialize')
    else:
        if not load_media():
            print('Failed to load media')
        else:
            while not quit:
                while SDL_PollEvent(ctypes.byref(event)) != 0:
                    if event.type == SDL_QUIT:
                        quit = True
                    elif event.type == SDL_KEYDOWN:
                        if event.key.keysym.sym == SDKLK_UP:
                            current_surface = key_surface[KEY_PRESS_SURFACE_UP]
                        elif event.key.keysym.sym == SDKLK_DOWN:
                            current_surface = key_surface[KEY_PRESS_SURFACE_DOWN]
                        elif event.key.keysym.sym == SDKLK_LEFT:
                            current_surface = key_surface[KEY_PRESS_SURFACE_LEFT]
                        elif event.key.keysym.sym == SDKLK_RIGHT:
                            current_surface = key_surface[KEY_PRESS_SURFACE_RIGHT]
                        else:
                            current_surface = key_surface[KEY_PRESS_SURFACE_DEFAULT]
                        
                SDL_BlitSurface(current_surface, None, screen_surface, None)
                SDL_UpdateWindowSurface(window)
    close()



if __name__ == '__main__':
    main()
    
