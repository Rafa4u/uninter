import pygame

print('Setup iniciado')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('loop iniciado')

while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() #end pygame