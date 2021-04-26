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

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)



def print2screen(charList):
    vartop = 0
    for line in charList:
        text = font.render(line, True, blue, white)
        textRect = text.get_rect()
        textRect.top = vartop
        vartop += 40
        textRect.left = 20
        display_surface.blit(text, textRect)
        
    



# infinite loop
while True:
    display_surface.fill(white)
    print2screen(charList)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()



#if __name__ == "__main__":
    bob = character.Hero()
    characterSheet = bob.__str__()
