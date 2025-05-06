import pygame
from puzzle import (
    #mandatory_correct,
    #forbidden_correct,
    create_puzzle
)

def main() -> None:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    half_width = SCREEN_WIDTH / 2
    half_height = SCREEN_HEIGHT / 2
    solution_surface = screen.subsurface(pygame.Rect(0, 0, SCREEN_WIDTH, half_height))
    solution_x, solution_y = solution_surface.get_offset()
    mandatory_surface = screen.subsurface(pygame.Rect(0, half_height, half_width, half_height))
    forbidden_surface = screen.subsurface(pygame.Rect(half_width, half_height, half_width, half_height))
    font = pygame.font.Font(None, 25)
    #clock = pygame.time.Clock()
    #dt = 0

    length = 4
    solution, mandatory, forbidden = create_puzzle(length)
    guess = [str(i) for i in range(length)]
    selected_idx = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                click_x, click_y = pygame.mouse.get_pos()
                if (
                    solution_x <= click_x < solution_x + 30 * length and
                    solution_y + 30 <= click_y < solution_y + 60
                ):
                    clicked_idx = (click_x - solution_x) // 30
                    if selected_idx == None:
                        selected_idx = clicked_idx
                    else:
                        if selected_idx != clicked_idx:
                            tmp = guess[selected_idx]
                            guess[selected_idx] = guess[clicked_idx]
                            guess[clicked_idx] = tmp
                        selected_idx = None
                elif (
                    solution_x <= click_x < solution_x + 120 and
                    solution_y + 60 <= click_y < solution_y + 90
                ):
                    if solution == "".join(guess):
                        solution, mandatory, forbidden = create_puzzle(length)
                        guess = [str(i) for i in range(length)]
        screen.fill("black")
        solution_surface.blit(font.render("Solution", True, "white"), (0, 0))
        for i in range(len(guess)):
            char_box_x = 30 * i
            char_box_y = 30
            if selected_idx == i:
                pygame.draw.rect(solution_surface, "white", (char_box_x, char_box_y, 30, 30))
                text_color = "black"
            else:
                text_color = "white"
            font_rect = font.render(guess[i], True, text_color)
            font_x = char_box_x + 15 - (font_rect.get_width() / 2)
            font_y = char_box_y + 15 - (font_rect.get_height() / 2)
            solution_surface.blit(font_rect, (font_x, font_y))

        btn_x = 0
        btn_y = 60
        pygame.draw.rect(solution_surface, "white", (btn_x, btn_y, 120, 30))
        btn_font_rect = font.render("GUESS", True, "black")
        btn_font_x = btn_x + 60 - (btn_font_rect.get_width() / 2)
        btn_font_y = btn_y + 15 - (btn_font_rect.get_height() / 2)
        solution_surface.blit(btn_font_rect, (btn_font_x, btn_font_y))

        mandatory_surface.blit(font.render("Mandatory", True, "white"), (0, 0))
        mandatory_surface.blit(font.render(" ".join(mandatory), True, "white"), (0, 30))

        forbidden_surface.blit(font.render("Forbidden", True, "white"), (0, 0))
        forbidden_surface.blit(font.render(" ".join(forbidden), True, "white"), (0, 30))

        pygame.display.flip()
        #dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
