import pygame

# screen width, height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# setting width, height
SETTING_WIDTH = 400
SETTING_HEIGHT = 600

# color  ->  http://www.n2n.pe.kr/lev-1/color.htm
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED1 = (255, 0, 0)
RED2 = (255, 51, 51)
PINK1 = (255, 204, 204)
PINK2 = (255, 153, 153)
PINK3 = (255, 102, 102)


pygame.init()
pygame.display.set_caption("2048")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 버튼 object
objects = []
img_obj = []

class MainView:
    def __init__(self):    
        # 타이틀
        font_title = pygame.font.SysFont("lucidaconsole", 100, True, False) # algerian inkfree
        self.title = font_title.render("2048", True, PINK3, PINK1)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, 100))    

    def draw(self):
        # 환경 설정
        ImgButton(540, 10, 48, 48, './png/set1.png','./png/set2.png','./png/set3.png', PINK1, self.setting)
        
        # 타이틀
        screen.blit(self.title, self.title_rect)
        
        # 전적
        pygame.draw.rect(screen, PINK2, [100, 180, 400, 300], 4) # 화면, 색상, 좌상우하 좌표, 두께
        pygame.draw.line(screen, WHITE, [100, 477], [499, 477], 4)  # 화면, 색상, 좌표1, 좌표2, 두께
        pygame.draw.line(screen, WHITE, [497, 184], [497, 477], 4)  # 화면, 색상, 좌표1, 좌표2, 두께
        
        # 게임시작
        Button(100, 500, 400, 80, 50, "lucidaconsole", 'START', self.startGame)
        
        # 게임방법
        Button(100, 590, 400, 80, 50, "lucidaconsole", 'RULE', self.ruleGame)
        
        # 게임종료
        Button(100, 680, 400, 80, 50, "lucidaconsole", 'EXIT', self.exitGame)

    # 환경설정
    def setting(self):
        objects.clear()
        set = SettingView()
        set.run()

    # 게임시작 -> 게임화면으로 넘어감
    def startGame(self):
        objects.clear() # 기존 창 죽이기 -> 버튼 없애기
        game = GameView()
        game.run()
    
    # 게임규칙 -> 게임규칙 설명화면
    def ruleGame(self):
        objects.clear()
        rule = RuleView()
        rule.run()

    # 게임종료
    def exitGame(self):
        pygame.quit()

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

            for object in img_obj:
                object.checkButton()
            
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

class GameView:
    def __init__(self):
        pygame.display.set_caption("game")
        font_score = pygame.font.SysFont("lucidaconsole", 40, True, False) # algerian inkfree

        # SCORE 
        self.now_score = font_score.render("score", True, PINK3, PINK1)
        self.now_score_rect = self.now_score.get_rect(center=(SCREEN_WIDTH/4, 60))
        
        # BSET SCORE
        self.best_score = font_score.render("best", True, PINK3, PINK1)
        self.best_score_rect = self.best_score.get_rect(center=(SCREEN_WIDTH/4+SCREEN_WIDTH/2, 60))
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

class RuleView:
    def __init__(self):
        # 초기설정
        pygame.display.set_caption("rule")

        # 타이틀
        font_title = pygame.font.SysFont("lucidaconsole", 60, True, False) # algerian inkfree
        self.title = font_title.render("RULE", True, PINK3, PINK1)
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH/2, 100))

        # 게임방법
        self.rule = pygame.image.load("./png/rule3.png")

    def draw(self):
        # 메인화면
        ImgButton(540, 10, 48, 48, './png/back1.png','./png/back2.png','./png/back3.png', PINK1, self.back)

        # 타이틀
        screen.blit(self.title, self.title_rect)

        # 규칙
        screen.blit(self.rule, (70, 200))
        
    def back(self):
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

            for object in img_obj:
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

        img_obj.append(self)

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

def main():
    view = MainView()
    done = False

    while not done:
        screen.fill(PINK1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        view.draw()
        
        for object in objects:
            object.checkButton()
        
        for object in img_obj:
            object.checkButton()
        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()