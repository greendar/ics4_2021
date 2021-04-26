import pygame
import character

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 400
Y = 400

# characterSheet = __str__ method from class Hero ***************************************
bob = character.Hero()
characterSheet = bob.__str__()
charList = characterSheet.split('\n')


print(charList)

"""
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)


text1 = font.render('apple apple', True, blue, white)
textRect1 = text1.get_rect()
textRect1.left = 20
text2 = font.render('banana', True, blue, white)
textRect2 = text2.get_rect()
textRect2.top = 40
textRect2.left = 20

# infinite loop
while True:
    display_surface.fill(white)
    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()



#if __name__ == "__main__":
    bob = character.Hero()
    characterSheet = bob.__str__()
"""
