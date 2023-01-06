import pygame
import os


width, height = 1980, 1080
win = (width, height)
screen = pygame.display.set_mode(win)

MAX_ITERATIONS = 20 # max number of iterations 
RE_MIN = -2
RE_MAX = 1
IM_MIN = -1 
IM_MAX = 1


# calculate how many iterations is needed to get to certain point on complex plane
def mandelbrot(c):
    z = 0
    n = 0 
    while abs(z) <= 2 and n < MAX_ITERATIONS:
        z = z*z + c
        n += 1
    return n


def main():
    print(mandelbrot(0+0j))


    for i in range(width):
        for j in range(height):
            # map screen ersuolution to complex plane within Re: [-2, 1], Im: [-1, 1]
            c = complex(RE_MIN + (i/width) * (RE_MAX - RE_MIN),
                IM_MIN + (j/height) * (IM_MAX - IM_MIN))
            n = mandelbrot(c)
            color = 255 - int(n*255/MAX_ITERATIONS)
            screen.set_at((i, j), (color, color, 126))
    print("FINISHED CALCULATING")
    pygame.display.update()

    while True:  
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

if __name__ == "__main__":
    main()