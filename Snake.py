# Snake Game

# Importing packages
import pygame as pg
import random

# Initializing Pygame
pg.init()

# Creating a game window
width = 400
height = 400
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# Setting up the Title
pg.display.set_caption("Snake Game")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

# Drawing a Snake
snake_block = 10


def snake(snake_block, snake_list):
    for x in snake_list:
        pg.draw.rect(screen, (255, 0, 0), [x[0], x[1], snake_block, snake_block])


def main_func():
    # Game Loop
    game_over = False
    game_end = False

    # Co-ordinates of the snake
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    Length_of_snake = 1

    # Drawing Foods
    foodx = round(random.randrange(0, width - snake_block) / 10) * 10
    foody = round(random.randrange(0, height - snake_block) / 10) * 10

    while not game_over:
        while game_end == True:
            screen.fill((0, 120, 0))
            font_style = pg.font.Font('freesansbold.ttf', 24)
            value = font_style.render("GAME OVER!  Play Again? 'P'", True, (200, 0, 0))
            screen.blit(value, (20, 200))

            # For displaying the score
            score = Length_of_snake - 1
            score_font = pg.font.Font('freesansbold.ttf', 32)
            value = score_font.render("Your Score : " + str(score), True, (0, 0, 255))
            screen.blit(value, (20, 20))
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        main_func()
                elif event.type == pg.QUIT:
                    game_over = True
                    game_end = False

        # For quiting the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

            # Checking if keystroke is pressed or not
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = - snake_block
                elif event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pg.K_LEFT:
                    x1_change = - snake_block
                    y1_change = 0
                elif event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        # If the snake touches boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_end = True

        # Moving the snake
        x1 += x1_change
        y1 += y1_change

        # For the background
        screen.fill((0, 120, 120))

        # Drawing Food
        pg.draw.rect(screen, (0, 255, 0), [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Increasing the snake
        # if x1 == foodx and y1 == foody:
        # Length_of_snake += 1

        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_end = True

        snake(snake_block, snake_list)

        # Updating everything
        pg.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10) * 10
            foody = round(random.randrange(0, height - snake_block) / 10) * 10
            Length_of_snake += 1

        clock.tick(10)
    pg.quit()
    quit()


main_func()
