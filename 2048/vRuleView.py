import pygame

# rule width, height
RULE_WIDTH = 600
RULE_HEIGHT = 800

# color  ->  http://www.n2n.pe.kr/lev-1/color.htm
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED1 = (255, 0, 0)
RED2 = (255, 51, 51)
PINK1 = (255, 204, 204)
PINK2 = (255, 153, 153)
PINK3 = (255, 102, 102)

objects = []
screen = pygame.display.set_mode((RULE_WIDTH, RULE_HEIGHT))
pygame.init()

class RuleView:
    def __init__(self):
        # 초기설정
        pygame.display.set_caption("rule")
        #self.screen = pygame.display.set_mode((RULE_WIDTH, RULE_HEIGHT)) # pygame.NOFRAME -> 메인바 없애는거
        self.clock = pygame.time.Clock()

        # 메인화면으로
        #self.back = pygame.image.load("./png/back1.png")
        # 타이틀
        font_title = pygame.font.SysFont("lucidaconsole", 60, True, False) # algerian inkfree
        self.title = font_title.render("RULE", True, PINK3, PINK1)
        self.title_rect = self.title.get_rect(center=(RULE_WIDTH/2, 100))

        # 게임방법
        self.rule = pygame.image.load("./png/rule3.png")

    def draw(self):
        # 메인화면
        # self.screen.blit(self.back, (545, 10))
        ImgButton(540, 10, 48, 48, './png/back1.png','./png/back2.png','./png/back3.png', PINK1, self.back)

        # 타이틀
        screen.blit(self.title, self.title_rect)

        # 규칙
        screen.blit(self.rule, (70, 200))
        
    def back(self):
        objects.clear()
        from vMainView import main
        main()

    def run(self):
        view = RuleView()
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
            self.clock.tick(30)

        pygame.quit()

class ImgButton:
    def __init__(self, x, y, width, height, img, hover_img, press_img, back_color, clickFunc=None, pressEvent=False):
        self.x = x # x좌표
        self.y = y # y좌표
        self.width = width # 너비
        self.height = height # 높이
        self.clickFunc = clickFunc # 버튼 클릭 연결 함수
        self.pressEvent = pressEvent 
        self.back_color = back_color
        self.pressed = False

        # 이미지
        self.img = img
        self.hover_img = hover_img
        self.press_img = press_img
        
        self.buttonSurface = pygame.Surface((self.width, self.height)) # 색이나 이미지를 가지는 빈 시트
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height) # 크기와 좌표 -> xy는 좌상   
        self.buttonStyle = pygame.image.load(self.img) # 버튼 기본 스타일

        objects.append(self)

        # self.back = pygame.image.load("./png/back1.png")
    
    def checkButton(self):
        mouse_pos = pygame.mouse.get_pos() # 마우스 좌표 얻기
        self.buttonSurface.fill(self.back_color) # 버튼 기본 색깔
        if self.buttonRect.collidepoint(mouse_pos): # 점이 직사각형 안에 있는지 테스트하는 함수
            self.buttonStyle = pygame.image.load(self.hover_img) # 버튼 위 확인 -> 색상변경해줌
            if pygame.mouse.get_pressed(num_buttons=3)[0]: # 버튼이 눌리면
                self.buttonStyle = pygame.image.load(self.press_img) # 색 변경
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
    rule = RuleView()
    rule.run()