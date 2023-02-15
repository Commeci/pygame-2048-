import pygame

# setting width, height
SETTING_WIDTH = 600
SETTING_HEIGHT = 800

# color  ->  http://www.n2n.pe.kr/lev-1/color.htm
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED1 = (255, 0, 0)
RED2 = (255, 51, 51)
PINK1 = (255, 204, 204)
PINK2 = (255, 153, 153)
PINK3 = (255, 102, 102)

screen = pygame.display.set_mode((SETTING_WIDTH, SETTING_HEIGHT))
pygame.init()
clock = pygame.time.Clock()

objects = []

class SettingView:
    def __init__(self):
        pygame.display.set_caption("setting")
        # 음량조절
        self.sound = pygame.image.load("./png/sound1.png")
        # 밤낮모드 on/off
        self.mod = pygame.image.load("./png/mod1.png")
        font_mod = pygame.font.SysFont("lucidaconsole", 20, True, False) # algerian inkfree
        self.mod_day = font_mod.render("day", True, PINK2, PINK1)
        self.mod_day_rect = self.mod_day.get_rect(center=(300, 330))
        self.mod_night = font_mod.render("night", True, PINK2, PINK1)
        self.mod_night_rect = self.mod_night.get_rect(center=(400, 330))
        # 테마 (색깔)
        self.theme = pygame.image.load("./png/theme1.png")
        # 언어
        self.lang = pygame.image.load("./png/lang1.png")

    def draw(self):
        # 메인으로
        ImgButton(540, 10, 48, 48, './png/back1.png','./png/back2.png','./png/back3.png', PINK1, self.back)
        # 틀
        pygame.draw.rect(screen, WHITE, [80, 80, 440, 640], 4) # 화면, 색상, 좌상우하 좌표, 두께
        # 음량조절
        screen.blit(self.sound, (100, 150))
        # 밤낮모드 on/off
        screen.blit(self.mod, (100, 300))
        screen.blit(self.mod_day, self.mod_day_rect)
        screen.blit(self.mod_night, self.mod_night_rect)
        # 테마 (색깔)
        screen.blit(self.theme, (100, 450))
        # 언어
        screen.blit(self.lang, (100, 600))

    def back(self):
        objects.clear()
        from vMainView import main
        main()

    def run(self):
        view = SettingView()
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
    rule = SettingView()
    rule.run()