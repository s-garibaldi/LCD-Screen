import pygame
import sys
import time

# Configuration
SCREEN_WIDTH = 800  # You can set to 1920 for full HD
SCREEN_HEIGHT = 480  # Or 1080 for full HD
BG_COLOR = (10, 40, 120)  # Deep blue
TEXT_COLOR = (255, 255, 255)  # White
LOGO_TEXT = "Vulcan Industries"
FADE_IN_DURATION = 2.0  # seconds
WELCOME_MSG = "Welcome! Tap to continue."

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Vulcan Industries Opening Screen")
clock = pygame.time.Clock()

# Load font
font_logo = pygame.font.SysFont("Arial", 72, bold=True)
font_welcome = pygame.font.SysFonst("Arial", 48)

def fade_in_logo():
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        alpha = min(255, int((elapsed / FADE_IN_DURATION) * 255))
        screen.fill(BG_COLOR)
        # Render logo text
        text_surface = font_logo.render(LOGO_TEXT, True, TEXT_COLOR)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        if alpha >= 255:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)

def welcome_page():
    button_rect = pygame.Rect(0, 0, 400, 100)
    button_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    button_color = (255, 255, 255)
    button_text_color = BG_COLOR
    running = True
    while running:
        screen.fill(BG_COLOR)
        # Logo
        text_surface = font_logo.render(LOGO_TEXT, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        screen.blit(text_surface, text_rect)
        # Button
        pygame.draw.rect(screen, button_color, button_rect, border_radius=20)
        btn_text = font_welcome.render(WELCOME_MSG, True, button_text_color)
        btn_text_rect = btn_text.get_rect(center=button_rect.center)
        screen.blit(btn_text, btn_text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.FINGERDOWN:
                pos = event.pos if hasattr(event, 'pos') else (event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT)
                if button_rect.collidepoint(pos):
                    running = False
        clock.tick(60)

def main():
    fade_in_logo()
    time.sleep(0.5)
    welcome_page()
    # After welcome, you can proceed to your main app or exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main() 