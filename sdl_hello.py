import sys
from enum import Enum
import ctypes
from sdl2 import *
from sdl2.sdlimage import *


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

window = None
event = SDL_Event()
quit = False
texture = None
renderer = None

def init():
    success = True
    global window
    global renderer
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
            renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)
            if not renderer:
                print('Renderer could not be created. SDL Error: %s' % SDL_GetError())
                success = False
            else:
                SDL_SetRenderDrawColor(renderer,0xFF, 0xFF, 0xFF,0xFF)

                img_flags = IMG_INIT_PNG
                if not (IMG_Init(img_flags) & img_flags):
                    print('SDL image could not initialize. SDL_image error: %s' % IMG_GetError())
                    success = False

    return success

def load_texture(path):
    global renderer
    new_texture = None
    loaded_surface = IMG_Load(path)
    if not loaded_surface:
        print('Unable to load image %s. SDL_Image error: %s' % (path, IMG_GetError()))
    else:
        new_texture = SDL_CreateTextureFromSurface(renderer,loaded_surface)
        if not new_texture:
            print('Unable to create texture from %s. SDL Error: %s' % (path, SDL_GetError()))
        SDL_FreeSurface(loaded_surface)
    return new_texture

def load_media():
    success = True
    return success

def close():
    global window
    global texture
    global renderer
    
    SDL_DestroyTexture(texture)
    SDL_DestroyRenderer(renderer) 
    SDL_DestroyWindow(window)
    window = None
    
    IMG_Quit()
    SDL_Quit()
    

def main():
    global event
    global quit
    global renderer
    global texture
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
        
                    SDL_SetRenderDrawColor(renderer, 0xFF,0xFF,0xFF,0xFF)
                    SDL_RenderClear(renderer)
                    fill_rect = SDL_Rect( int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/4), int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
                    print(fill_rect)
                    SDL_SetRenderDrawColor(renderer, 0xFF,0x00,0x00,0xFF)
                    SDL_RenderFillRect(renderer, ctypes.byref(fill_rect))

                    outline_rect = SDL_Rect( int(SCREEN_WIDTH/6), int(SCREEN_HEIGHT/6), int(SCREEN_WIDTH * 2/3), int(SCREEN_HEIGHT * 2/3))
                    SDL_SetRenderDrawColor(renderer, 0x00, 0xFF, 0x00, 0xFF)
                    SDL_RenderDrawRect(renderer, ctypes.byref(outline_rect))
                    

    close()



if __name__ == '__main__':
    main()
    
