from kivy.graphics import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import *
from kivy.graphics.context_instructions import Color
from kivy.core.window import Window
import requests

class  Gameq4App(BoxLayout, App):
    def callback(self, instance):
        if (q4.turn==0):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-75)//100
                u = (self.b2.pos[0]-75)//100
                k = (self.b2.pos[1]-75)//100
                if (q4.isvalidplayer(q4, i, j, u, k)):
                        instance.background_color = (1, 1/255, 76/255, 1)
                        self.b2.background_color = (74/255, 1/255, 76/255, 1)
                        self.b2 = instance
                        q4.turn = (q4.turn+1)%4
                        if(q4.is_end(q4)):
                                exit()
                        print(i, j, u, k)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_player[i][j], end=' ')
                                print()
        elif(q4.turn==1):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-75)//100
                u = (self.b3.pos[0]-75)//100
                k = (self.b3.pos[1]-75)//100
                if (q4.isvalidplayer(q4, i, j, u, k)):
                        instance.background_color = (6/255, 6/255, 173/255, 1)
                        self.b3.background_color = (74/255, 1/255, 76/255, 1)
                        self.b3 = instance
                        q4.turn = (q4.turn+1)%4
                        if(q4.is_end(q4)):
                                exit()
                        print(i, j, u, k)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_player[i][j], end=' ')
                                print()
        elif(q4.turn==2):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-75)//100
                u = (self.b4.pos[0]-75)//100
                k = (self.b4.pos[1]-75)//100
                if (q4.isvalidplayer(q4, i, j, u, k)):
                        instance.background_color = (249/255, 241/255, 2/255,1)
                        self.b4.background_color = (74/255, 1/255, 76/255, 1)
                        self.b4 = instance
                        q4.turn = (q4.turn+1)%4
                        if(q4.is_end(q4)):
                                exit()
                        print(i, j, u, k)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_player[i][j], end=' ')
                                print()
        elif(q4.turn==3):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-75)//100
                u = (self.b5.pos[0]-75)//100
                k = (self.b5.pos[1]-75)//100
                if (q4.isvalidplayer(q4, i, j, u, k)):
                        instance.background_color = (14/255, 249/255, 1/255,1)
                        self.b5.background_color = (74/255, 1/255, 76/255, 1)
                        self.b5 = instance
                        q4.turn = (q4.turn+1)%4
                        if(q4.is_end(q4)):
                                exit()
                        print(i, j, u, k)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_player[i][j], end=' ')
                                print()
    def callbackwv(self, instance):
                i = (instance.pos[0]-50)//100
                j = (instance.pos[1]-75)//100
                u = j-1
                if(q4.isvalidvwall(q4, i, j) and q4.have_wall(q4)):                
                        instance.background_color=(8/255, 224/255, 163/255, 1)
                        for t in range(len(self.wallv)):
                                if( (self.wallv[t].pos[0]-50)//100 == i and (self.wallv[t].pos[1]-75)//100==u):
                                        self.wallv[t].background_color = (8/255, 224/255, 163/255, 1)
                                        break

                        if(q4.turn == 0):
                                q4.turn= (q4.turn+1)%4
                                q4.player1w += 1
                        elif(q4.turn==1):
                                q4.turn= (q4.turn+1)%4
                                q4.player2w += 1
                        elif(q4.turn==2):
                                q4.turn= (q4.turn+1)%4
                                q4.player3w += 1
                        else:
                                q4.turn= (q4.turn+1)%4
                                q4.player4w += 1
                        print(i, j)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_vwall[i][j], end=' ')
                                print()
    def callbackwh(self,instance):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-50)//100
                u = i+1
                if(q4.isvalidhwall(q4, i, j)and q4.have_wall(q4)):
                        instance.background_color = (7/255, 173/255, 224/255, 1)
                        for t in range(len(self.wallh)):
                                if((self.wallh[t].pos[0]-75)//100==u and (self.wallh[t].pos[1]-50)//100==j):
                                        self.wallh[t].background_color = (7/255, 173/255, 224/255, 1)
                                        break
                        if(q4.turn == 0):
                                q4.turn= (q4.turn+1)%4
                                q4.player1w += 1
                        elif(q4.turn==1):
                                q4.turn= (q4.turn+1)%4
                                q4.player2w += 1
                        elif(q4.turn==2):
                                q4.turn= (q4.turn+1)%4
                                q4.player3w += 1
                        else:
                                q4.turn= (q4.turn+1)%4
                                q4.player4w += 1
                        print(i, j)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_hwall[i][j],end=' ')
                                print()
    def build(self):
        layout = FloatLayout()
        Window.size = (1000, 1000)
        player = []
        for i in range(9):
            for j in range(9):
                if ((not (i == 4 and j == 0))and (not(i == 4 and j == 8))and (not(i==0 and j==4))and (not(i==8 and j==4))):
                    self.b1 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(74/255, 1/255, 76/255, 1))
                    layout.add_widget(self.b1)
                    player.append(self.b1)

                elif(i == 4 and j == 0):
                    self.b2 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(1, 1/255, 76/255, 1))
                    layout.add_widget(self.b2)
                    player.append(self.b2)
                elif(i==4 and j==8):
                    self.b3 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(6/255, 6/255, 173/255, 1))
                    layout.add_widget(self.b3)
                    player.append(self.b3)
                elif(i==0 and j==4):
                    self.b4 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(249/255, 241/255, 2/255, 1))
                    layout.add_widget(self.b4)
                    player.append(self.b4)

                elif(i==8 and j ==4):
                    self.b5 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(14/255, 249/255, 1/255, 1))
                    layout.add_widget(self.b5)
                    player.append(self.b5)
                
        self.wallv=[]#amodi
        for i in range(1, 9):
            for j in range(9):
                self.w1=Button(pos=(75-25+i*100, 75+j*100),
                                         size_hint=(None, None),
                                         size=(25, 75), background_color=(238/255, 177/255, 239/255, 1))
                layout.add_widget(self.w1)
                self.wallv.append(self.w1)
        self.wallh = []#ofoghi
        for i in range(9):
            for j in range(1, 9):
                self.w2=Button(pos=(75+i*100, 75-25+j*100),
                                         size_hint=(None, None),
                                         size=(75, 25), background_color=(238/255, 177/255, 239/255, 1))
                layout.add_widget(self.w2)
                self.wallh.append(self.w2)
        for x in range(len(player)):
                    player[x].bind(on_press=self.callback)
        for i in range(len(self.wallv)):
                self.wallv[i].bind(on_press=self.callbackwv)
        for i in range(len(self.wallh)):
                self.wallh[i].bind(on_press=self.callbackwh)
        return layout

