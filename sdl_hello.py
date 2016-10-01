import sys
import ctypes
from sdl2 import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

window = None
screen_surface = None
hello_surface = None
event = SDL_Event()
quit = False

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
    global hello_surface
    hello_surface = SDL_LoadBMP(b'hello.bmp')
    if hello_surface is None:
        print('Unable to load image %s.  SDL_Error: %s' % ('hello.bmp',SDL_GetError()))
        success = False
    
    return success

def close():
    global hello_surface
    global window
    SDL_FreeSurface(hello_surface)
    hello_surface = None
    SDL_DestroyWindow(window)
    window = None
    
    SDL_Quit()
    

def main():
    global event
    global quit
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
                SDL_BlitSurface(hello_surface, None, screen_surface, None)
                SDL_UpdateWindowSurface(window)
    close()



if __name__ == '__main__':
    main()
    
