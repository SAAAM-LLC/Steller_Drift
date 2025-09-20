import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
STAR_COLOR = (255, 255, 0)
PLANET_COLOR = (0, 255, 0)
EVENT_COLOR = (255, 0, 0)
FPS = 60

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stellar Drift - Infinite Loop")

# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.color = WHITE
        self.universe_loops = 0  # Tracks how many loops the player has been through

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def move(self, keys):
        if keys[pygame.K_w] and self.y - self.speed > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y + self.speed < HEIGHT:
            self.y += self.speed
        if keys[pygame.K_a] and self.x - self.speed > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x + self.speed < WIDTH:
            self.x += self.speed

    def reached_edge(self):
        return self.x <= 0 or self.x >= WIDTH or self.y <= 0 or self.y >= HEIGHT

# Star Class
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 5)
        self.color = STAR_COLOR

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Planet Class
class Planet:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = PLANET_COLOR

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Random Event Class
class Event:
    def __init__(self, x, y, event_type):
        self.x = x
        self.y = y
        self.size = 15
        self.event_type = event_type
        self.color = EVENT_COLOR

    def trigger_event(self):
        # Event mechanics can vary, for now, just display event type
        print(f"Event triggered: {self.event_type}")

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Generate Procedural Stars
def generate_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        star_x = random.randint(0, WIDTH)
        star_y = random.randint(0, HEIGHT)
        stars.append(Star(star_x, star_y))
    return stars

# Generate Procedural Planets
def generate_planets(num_planets):
    planets = []
    for _ in range(num_planets):
        planet_x = random.randint(100, WIDTH - 100)
        planet_y = random.randint(100, HEIGHT - 100)
        planet_size = random.randint(10, 30)
        planets.append(Planet(planet_x, planet_y, planet_size))
    return planets

# Generate Random Events
def generate_events(num_events):
    events = []
    for _ in range(num_events):
        event_x = random.randint(0, WIDTH)
        event_y = random.randint(0, HEIGHT)
        event_type = random.choice(["Alien Encounter", "Black Hole", "Resource Discovery"])
        events.append(Event(event_x, event_y, event_type))
    return events

# Main Game Loop with Infinite Universe
def game_loop():
    player = Player(WIDTH // 2, HEIGHT // 2)
    stars = generate_stars(100)
    planets = generate_planets(5)
    events = generate_events(3)

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Loop Universe: If player reaches the edge, regenerate the universe
        if player.reached_edge():
            player.x, player.y = WIDTH // 2, HEIGHT // 2  # Reset player position
            player.universe_loops += 1  # Track the loops
            stars = generate_stars(100)  # New star system
            planets = generate_planets(5)  # New planets
            events = generate_events(3)  # New random events
            print(f"Universe loop {player.universe_loops}!")

        # Draw stars, planets, and events
        for star in stars:
            star.draw()

        for planet in planets:
            planet.draw()

        for event in events:
            event.draw()

        # Check for event interaction
        for event_obj in events:
            if math.hypot(event_obj.x - player.x, event_obj.y - player.y) < 20:  # Simple proximity check
                event_obj.trigger_event()

        # Draw player spaceship
        player.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
