import requests
from bs4 import BeautifulSoup
import json
    
    
def get_iran_wikipedia():
    import requests
    import json

    # Set the URL of the Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"

    # Set the parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": "shahid irani",
        "srprop": "size",
        "utf8": 1,
    }

    # Send a GET request to the API and get the JSON response
    response = requests.get(url, params=params)
    data = response.json()

    # Get the search results from the JSON response
    search_results = data["query"]["search"]

    # Loop through the search results and print the titles
    for result in search_results:
        print(result["title"])


import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 1200, 850
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Football Game")

# Set up game variables
player_width = 20
player_height = 40
player_speed = 2

ball_x = screen_width // 2
ball_y = screen_height // 2
ball_radius = 10
ball_dx = 4
ball_dy = 4

goal_width = 100
goal_height = 200
goal1_x = 0
goal1_y = screen_height // 2 - goal_height // 2
goal2_x = screen_width - goal_width
goal2_y = screen_height // 2 - goal_height // 2

score1 = 0
score2 = 0

players1 = []
players2 = []

def change_possion_player1():
    players = []

    for i in range(7):
        
        player_x = random.randint(0, screen_width // 2 - player_width)
        player_y = random.randint(0, screen_height - player_height)
        players.append([player_x, player_y])
    return players

def change_possion_player2():
    players = []
    for i in range(7):
        player2_x = random.randint(screen_width // 2, screen_width - player_width)
        player2_y = random.randint(0, screen_height - player_height)
        players.append([player2_x, player2_y])
    return players
        
players2 = change_possion_player2()
players1 = change_possion_player1()

running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move players
    keys = pygame.key.get_pressed()
    if keys [pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_w] and players1[0][1] > 0:
        for player in players1:
            player[1] -= player_speed
    if keys[pygame.K_s] and players1[-1][1] < screen_height - player_height:
        for player in players1:
            player[1] += player_speed
    if keys[pygame.K_UP] and players2[0][1] > 0:
        for player in players2:
            player[1] -= player_speed
    if keys[pygame.K_DOWN] and players2[-1][1] < screen_height - player_height:
        for player in players2:
            player[1] += player_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        players2 = change_possion_player2()
    if keys[pygame.K_a] or keys[pygame.K_d]:
        players1 = change_possion_player1()

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with players
    for player in players1:
        if ball_x - ball_radius <= player[0] + player_width and player[1] <= ball_y <= player[1] + player_height:
            ball_dx = abs(ball_dx)
    for player in players2:
        if ball_x + ball_radius >= player[0] and player[1] <= ball_y <= player[1] + player_height:
            ball_dx = -abs(ball_dx)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_radius:
        ball_dy = -ball_dy

    # Ball collision with goals
    if ball_x - ball_radius <= goal1_x + goal_width and goal1_y <= ball_y <= goal1_y + goal_height:
        score2 += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = -3
        ball_dy = 3
    if ball_x + ball_radius >= goal2_x and goal2_y <= ball_y <= goal2_y + goal_height:
        score1 += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = 3
        ball_dy = -3

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw players
    for player in players1:
        pygame.draw.rect(screen, (0, 0, 255), (player[0], player[1], player_width, player_height))
    for player in players2:
        pygame.draw.rect(screen, (255, 0, 0), (player[0], player[1], player_width, player_height))

    # Draw ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)

    # Draw goals
    pygame.draw.rect(screen, (0, 0, 255), (goal1_x, goal1_y, goal_width, goal_height))
    pygame.draw.rect(screen, (255, 0, 0), (goal2_x, goal2_y, goal_width, goal_height))

    # Draw score
    score_text = "Score: {} - {}".format(score1, score2)
    font = pygame.font.Font(None, 36)
    text = font.render(score_text, True, (255, 255, 255))
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
