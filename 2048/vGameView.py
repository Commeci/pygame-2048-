import pygame
from vMainView import main

# game width, height
GAME_WIDTH = 600
GAME_HEIGHT = 800

# color  ->  http://www.n2n.pe.kr/lev-1/color.htm
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED1 = (255, 0, 0)
RED2 = (255, 51, 51)
PINK1 = (255, 204, 204)
PINK2 = (255, 153, 153)
PINK3 = (255, 102, 102)

objects = []
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

class GameView:
    def __init__(self):
        pygame.display.set_caption("game")
        font_score = pygame.font.SysFont("lucidaconsole", 40, True, False) # algerian inkfree

        # SCORE 
        self.now_score = font_score.render("score", True, PINK3, PINK1)
        self.now_score_rect = self.now_score.get_rect(center=(GAME_WIDTH/4, 60))
        
        # BSET SCORE
        self.best_score = font_score.render("best", True, PINK3, PINK1)
        self.best_score_rect = self.best_score.get_rect(center=(GAME_WIDTH/4+GAME_WIDTH/2, 60))
        # gameboard
        # main button
        # regame button
        pass

    def draw(self):
        # SCORE 
        screen.blit(self.now_score, self.now_score_rect)
        
        # BSET SCORE
        screen.blit(self.best_score, self.best_score_rect)
        
        # gameboard
        pygame.draw.rect(screen, PINK2, [60, 130, 460, 460], 5) # 화면, 색상, 좌상우하 좌표, 두께
        # pygame.draw.line(screen, WHITE, [70, 597], [529, 597], 5)  # 화면, 색상, 좌표1, 좌표2, 두께
        # pygame.draw.line(screen, WHITE, [527, 144], [527, 597], 5)  # 화면, 색상, 좌표1, 좌표2, 두께

        pygame.draw.rect(screen, WHITE, [70, 140, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [184, 140, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [298, 140, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [412, 140, 119, 119], 5)
        
        pygame.draw.rect(screen, WHITE, [70, 254, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [184, 254, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [298, 254, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [412, 254, 119, 119], 5)
        
        pygame.draw.rect(screen, WHITE, [70, 368, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [184, 368, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [298, 368, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [412, 368, 119, 119], 5)
        
        pygame.draw.rect(screen, WHITE, [70, 482, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [184, 482, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [298, 482, 119, 119], 5)
        pygame.draw.rect(screen, WHITE, [412, 482, 119, 119], 5)

        # main button
        Button(70, 650, 200, 80, 30, "lucidaconsole", 'MAIN', self.move_main)

        # regame button
        Button(330, 650, 200, 80, 30, "lucidaconsole", 'REGAME', self.regame)

    def move_main(self):
        objects.clear()
        main()

    def regame(self):
        rule = GameView()
        rule.run()

    def run(self):
        view = GameView()
        done = False

        while not done:
            screen.fill(PINK1)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            view.draw()

            for object in objects:
                object.checkButton()

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

class Button:
    def __init__(self, x, y, width, height, font_size, font_name, name='Button', clickFunc=None, pressEvent=False):
        self.x = x # x좌표
        self.y = y # y좌표
        self.width = width # 너비
        self.height = height # 높이
        self.font_size = font_size # 폰트 크기
        self.font_name = font_name
        self.clickFunc = clickFunc 
        self.pressEvent = pressEvent  
        self.pressed = False

        # 색상변화
        self.changeColors = {
            'normal' : '#ffffff', # 평소
            'hover' : '#E6E6E6', # 마우스가 버튼 위로 올라간 경우
            'press' : '#A8A8A8' , # 버튼이 눌렸을 경우
            'color1' : '#FF9999', # 버튼 색1
            'color2' : '#FF6666' # 버튼 색2
        }
        
        # 버튼 기본 폰트
        font = pygame.font.SysFont(self.font_name, self.font_size, True)
        
        self.buttonSurface = pygame.Surface((self.width, self.height)) # 색이나 이미지를 가지는 빈 시트
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height) # 크기와 좌표 -> xy는 좌상   
        self.buttonStyle = font.render(name, True, PINK1) # 버튼 기본 스타일

        objects.append(self)
    
    def checkButton(self):
        mouse_pos = pygame.mouse.get_pos() # 마우스 좌표 얻기
        self.buttonSurface.fill(self.changeColors['normal']) # 버튼 기본 색깔
        if self.buttonRect.collidepoint(mouse_pos): # 점이 직사각형 안에 있는지 테스트하는 함수
            self.buttonSurface.fill(self.changeColors['color1']) # 버튼 위 확인 -> 색상변경해줌
            if pygame.mouse.get_pressed(num_buttons=3)[0]: # 버튼이 눌리면
                self.buttonSurface.fill(self.changeColors['color2']) # 색 변경
                if self.pressEvent: # 눌리면
                    self.clickFunc() # 클릭 함수
                elif not self.pressed: # 이미 눌린 상태라면
                    self.clickFunc() # 클릭 함수
                    self.pressed = True # 눌렸다
            else:
                self.pressed = False # 아니면 False

        self.buttonSurface.blit(self.buttonStyle, [
            self.buttonRect.width/2 - self.buttonStyle.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonStyle.get_rect().height/2
        ])

        screen.blit(self.buttonSurface, self.buttonRect)

if __name__ == '__main__':
    rule = GameView()
    rule.run()