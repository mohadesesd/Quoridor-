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

class winApp(BoxLayout, App):
        """this application run when the game is end"""
        def build(self):
                Window.size = (700, 700)
                layout = FloatLayout()
                with layout.canvas:
                        RoundedRectangle(size=(700, 700), source = '/home/msd/Desktop/d.jpg', pos = (0, 0))
                return layout


class  Gameq4App(BoxLayout, App):
    """this application include your moves and place wall and so on in your graphics envionment"""

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
                                self.stop()
                                winApp().run()
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
                                self.stop()
                                winApp().run()
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
                                self.stop()
                                winApp().run()
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
                        instance.background_color = (14/255, 249/255, 1/255, 1)
                        self.b5.background_color = (74/255, 1/255, 76/255, 1)
                        self.b5 = instance
                        q4.turn = (q4.turn+1)%4
                        if(q4.is_end(q4)):
                                self.stop()
                                winApp().run()
                        print(i, j, u, k)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_player[i][j], end=' ')
                                print()

    def callbackwv(self, instance):
                """when you click on a wall place a  vertical wall for you"""
                i = (instance.pos[0]-50)//100
                j = (instance.pos[1]-75)//100
                u = j-1
                if(q4.isvalidvwall(q4, i, j) and q4.have_wall(q4)):                
                        instance.background_color = (8/255, 224/255, 163/255, 1)
                        for t in range(len(self.wallv)):
                                if( (self.wallv[t].pos[0]-50)//100 == i and (self.wallv[t].pos[1]-75)//100==u):
                                        self.wallv[t].background_color = (8/255, 224/255, 163/255, 1)
                                        break

                        if(q4.turn == 0):
                                q4.turn = (q4.turn+1)%4
                                q4.player1w += 1
                        elif(q4.turn==1):
                                q4.turn = (q4.turn+1)%4
                                q4.player2w += 1
                        elif(q4.turn==2):
                                q4.turn = (q4.turn+1)%4
                                q4.player3w += 1
                        else:
                                q4.turn = (q4.turn+1)%4
                                q4.player4w += 1
                        print(i, j)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_vwall[i][j], end=' ')
                                print()

    def callbackwh(self, instance):
                """this function place a horizontal wall for you """
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
                                q4.turn = (q4.turn+1)%4
                                q4.player1w += 1
                        elif(q4.turn==1):
                                q4.turn = (q4.turn+1)%4
                                q4.player2w += 1
                        elif(q4.turn==2):
                                q4.turn = (q4.turn+1)%4
                                q4.player3w += 1
                        else:
                                q4.turn = (q4.turn+1)%4
                                q4.player4w += 1
                        print(i,j)
                        for i in range(9):
                                for j in range(9):
                                        print(q4.board_hwall[i][j],end=' ')
                                print()

    def build(self):
        """this function call when your application run"""
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
                                         size=(25, 75), background_color=(238/250, 177/250, 239/250, 1))
                layout.add_widget(self.w1)
                self.wallv.append(self.w1)
              
        self.wallh = []#ofoghi
        for i in range(9):
            for j in range(1, 9):
                self.w2=Button(pos=(75+i*100, 75-25+j*100),
                                         size_hint=(None, None),
                                         size=(75, 25), background_color=(238/250, 177/250, 239/250, 1))
                layout.add_widget(self.w2)
                self.wallh.append(self.w2)
        for x in range(len(player)):
                    player[x].bind(on_press=self.callback)
        for i in range(len(self.wallv)):
                self.wallv[i].bind(on_press=self.callbackwv)

        for i in range(len(self.wallh)):
                self.wallh[i].bind(on_press=self.callbackwh)

        return layout


class q4 :
        board_player = [[ '-' for i in range(9)] for j in range(9)]
        board_hwall = [['-' for i in range(9)] for j in range(9)]#ofoghi j+1
        board_vwall = [['-' for i in range(9)]for j in range(9)]#amodi i-1 
        board_point = [['-' for i in range(8)]for j in range(8)]
        board_player[8][4] = '*'
        board_player[0][4] = '+'
        board_player[4][0] = '&'
        board_player[4][8] = '#'
        turn = 0
        player1w = 0
        player2w = 0
        player3w = 0
        player4w = 0
        def is_end(self):
                """this function check if game end or not"""
                for i in range(9):
                        if (self.board_player[8][i]=='+' or self.board_player[0][i]=='*' or self.board_player[i][0]=='#' or self.board_player[i][8]=='&'):
                                if(self.turn==0):
                                        print('player1 you win')
                                elif(self.turn==1):
                                        print('player2 you win')
                                elif(self.turn==2):
                                        print('player3 you win')
                                else:
                                        print('player4 you win')
                                return True
                return False

        def isvalidplayer(self, i, j, u, k):
                """this function check if move is possible or not"""
                i, j = j, i
                u, k = k, u
                if(self.turn==0):
                        character1 = '+'
                        character2 = ['*', '&', '#']
                elif(self.turn==1):
                        character1 = '*'
                        character2 = ['+', '&', '#']
                elif(self.turn==2):
                        character1 = '&'
                        character2 = ['+', '*', '#']
                else:
                        character1 = '#'
                        character2 = ['+', '&', '*']
                if(self.board_player[i][j]=='-'):
                      if((u-i==1) and (k==j) and self.board_hwall[i][j]=='-') :#paeen
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((i-u==1)and(k==j) and self.board_hwall[u][k]=='-'):#bala
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(i==u)and self.board_vwall[u][k]=='-'):#chap
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(i==u)and self.board_vwall[i][j]=='-'):#raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(i-u==1)and self.board_hwall[u][k]=='+' and 
                           self.board_hwall[u][k-1]=='+' and self.board_hwall[u][k+1]=='-' and 
                           (self.board_player[u][k+1]==character2[0] or self.board_player[u][k+1]==character2[1] 
                           or self.board_player[u][k+1]==character2[2])) :#bala-chap
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(i-u==1)and self.board_hwall[u][k]=='+' and 
                          self.board_hwall[u][k+1]=='+'and self.board_hwall[u][k-1]=='-' and 
                          (self.board_player[u][k-1]==character2[0] or self.board_player[u][k-1]==character2[1] 
                          or self.board_player[u][k-1]==character2[2])):#bala_raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(u-i==1)and self.board_hwall[u-1][k]=='+'and
                          self.board_hwall[u-1][k-1]=='+' and self.board_hwall[u-1][k+1]=='-' and 
                          (self.board_player[u][k+1]==character2[0] or self.board_player[u][k+1]==character2[1] 
                          or self.board_player[u][k+1]==character2[2])):#paeen_chap
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(u-i==1)and self.board_hwall[u-1][k]=='+'and
                          self.board_hwall[u-1][k+1]=='+' and self.board_hwall[u-1][k-1]=='-'and 
                          (self.board_player[u][k-1]==character2[0] or self.board_player[u][k-1]==character2[1] 
                          or self.board_player[u][k-1]==character2[2])):#paeen_raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(i-u==1)and self.board_vwall[u][k]=='+' and 
                           self.board_vwall[u+1][k]=='+' and self.board_vwall[u-1][k]=='-' and 
                           (self.board_player[u-1][k]==character2[0] or self.board_player[u-1][k]==character2[1] 
                           or self.board_player[u-1][k]==character2[2])) :#bala-chap
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(i-u==1)and self.board_vwall[u][k]=='+' and
                          self.board_vwall[u][k+1]=='+'and self.board_vwall[u][k-1]=='-' and 
                          (self.board_player[u+1][k]==character2[0] or self.board_player[u+1][k]==character2[1] 
                          or self.board_player[u+1][k]==character2[2])):#bala_raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==1)and(u-i==1)and self.board_vwall[u][k+1]=='+'and
                          self.board_vwall[u+1][k+1]=='+' and  self.board_vwall[u+1][k-1]=='-' and 
                          (self.board_player[u-1][k]==character2[0] or self.board_player[u-1][k]==character2[1] 
                          or self.board_player[u-1][k]==character2[2])):#paeen_chap
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==1)and(u-i==1)and self.board_vwall[u][k+1]=='+'and
                          self.board_vwall[u+1][k]=='+' and self.board_vwall[u+1][k+1]=='-'and  
                          (self.board_player[u+1][k]==character2[0] or self.board_player[u+1][k]==character2[1] 
                          or self.board_player[u+1][k]==character2[2])):#paeen_raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((u-i==2)and(j==k)and self.board_hwall[u-1][j]=='-' and 
                          self.board_hwall[u][k]=='-' and 
                          (self.board_player[u-1][j]==character2[0] or self.board_player[u-1][j]==character2[1]
                          or self.board_player[u-1][j]==character2[2])):#paeen
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((i-u==2)and (j==k) and self.board_hwall[u][k]=='-' and 
                           self.board_hwall[i-1][j]=='-'and  
                           (self.board_player[u+1][j]==character2[0] or self.board_player[u+1][j]==character2[1]
                           or self.board_player[u+1][j]==character2[2])):#bala
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((j-k==2)and(i==u) and self.board_vwall[u][k]=='-' and self.board_vwall[u][k+1]=='-' and
                           (self.board_player[u][k+1]==character2[0] or self.board_player[u][k+1]==character2[1]
                           or self.board_player[u][k+1]==character2[2] )):#chapp
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      elif((k-j==2)and(i==u) and self.board_vwall[i-1][j]=='-' and self.board_vwall[i][j]=='-' and
                           (self.board_player[u][k-1]==character2[0] or self.board_player[u][k-1]==character2[1] 
                           or self.board_player[u][k-1]==character2[2])):#raast
                                self.board_player[i][j] = character1
                                self.board_player[u][k] = '-'
                                return True
                      return False
                return False

        def isvalidvwall(self, i, j):#amodi
                """this function check if place vertical wall is valid or not"""
                i, j = j, i-1
                if(i-1 in range(9) and self.board_vwall[i][j]=='-' and self.board_vwall[i-1][j]=='-'):
                        if(self.board_point[i-1][j]=='-'):
                                self.board_vwall[i][j] = '+'
                                self.board_vwall[i-1][j] = '+'
                                self.board_point[i-1][j] = '.'
                                return True
                        return False
                return False

        def isvalidhwall(self, i, j):#ofoghi
                """this function check if place horizontal wall is valid or not"""
                i, j = j-1, i
                if(j+1 in range(9) and self.board_hwall[i][j]=='-' and self.board_hwall[i][j+1]=='-'):
                        if(self.board_point[i][j]=='-'):
                                self.board_hwall[i][j] = '+'
                                self.board_hwall[i][j+1] = '+'
                                self.board_point[i][j] = '.'
                                return True
                        return False
                return False

        def have_wall(self):
                """this function check if player have wall or not"""
                if(self.turn==0):
                        if(self.player1w<4):
                                return True
                        return False
                elif(self.turn==1):
                        if(self.player2w<4):
                                return True
                        return False 
                elif(self.turn==2):
                        if(self.player3w<4):
                                return True
                        return False   
                elif(self.turn==3):
                        if(self.player4w<4):
                                return True
                        return False

