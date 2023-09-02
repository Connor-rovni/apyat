from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
            



lost=0
max_lost=10
goal=75
class Enemy(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y >win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0
            lost=lost+1





class Enemy2(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y >win_height:
            self.rect.x=randint(80,win_width-80)
            self.rect.y=0


score=0


win_width=700
win_height=500
window=display.set_mode((win_width,win_height))
display.set_caption('catch the banana')
background=transform.scale(image.load('jungle.jpg'),(win_width,win_height))
clock=time.Clock()

monkey=Player('monke.png',5,win_height-100,80,100,10)


bananas=sprite.Group()
for i in range(1,5):
    banana=Enemy('bananas.png',randint(80,win_width-80),40,80,50,randint(1,5))
    bananas.add(banana)

bombs=sprite.Group()
for i in range(1,5):
    bomb=Enemy2('bomb.png',randint(80,win_width-80),40,80,50,randint(1,5))
    bombs.add(bomb)

mixer.init()
mixer.music.load('junglesound.ogg')
mixer.music.play()

nyam=mixer.Sound('nyam.ogg')



font.init()
font2=font.SysFont('Georgia',36)

font.init()
font=font.Font(None,70)
win=font.render('YOU WIN!',True,(255,215,0))
lose=font.render('YOU LOSE!',True,(180,0,0))




finish=False
game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False


    if not finish:
        window.blit(background,(0,0))



        monkey.update()
        bananas.update()
        bombs.update()


        monkey.reset()
        bananas.draw(window)
        bombs.draw(window)

      
        if sprite.spritecollide(monkey,bananas,False):
            score=score+1
            nyam.play()
            banana=Enemy('bananas.png',randint(80,win_width-80),40,80,50,randint(1,2))
            bananas.add(banana)



        if sprite.spritecollide(monkey,bombs,False) or lost >= max_lost:
            finish=True
            window.blit(lose,(200,200))
        
        if sprite.spritecollide(monkey,bananas,True):
            scoere=score+1
            nyam.play()            
            banana=Enemy('bananas.png',randint(80,win_width-80),-40,80,50,randint(1,5))
            bananas.add(banana)

        if score >= goal:
            finish=True
            window.blit(win,(200,200))


        text=font2.render('Счёт:'+str(score),1,(255,255,255))
        window.blit(text,(10,20))

        text_lose=font2.render('Пропущено:'+str(lost),1,(255,255,255))
        window.blit(text_lose,(10,50))



        display.update()
    time.delay(50)

