import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 30)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)


score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

#highest_score_rect = pygame.Rect(320, 300, 170, 60)




screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

# highest_score_surface = title_font.render(f'Highest Score: {game.score}', True, Colors.white)
# scores = []
# scores.append(game.score)
# highest_score = max(scores)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    # highest_score_surface = title_font.render(f'Highest Score: {highest_score}', True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    # screen.blit(highest_score_surface, (320, 500, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                  centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)


