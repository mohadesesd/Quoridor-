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
import settings
import time

class  Gameq2App(BoxLayout, App):
    
    def callback(self, instance):

        if (self.turn=='True'):
                i = (instance.pos[0]-75)//100
                j = (instance.pos[1]-75)//100
                u = (self.b2.pos[0]-75)//100
                k = (self.b2.pos[1]-75)//100
                data = {'i':i,'j':j,'u':u,'k':k}
                time.sleep(1)
                req = self.session.post(settings.url['gameq2isvalidplayer'],data=data)#valid
                res = str(req.content)[2:-1]
                if (res=='True'):
                        print('Hello')
                        instance.background_color = (1, 1/255, 76/255, 1)
                        self.b2.background_color = (74/255, 1/255, 76/255, 1)
                        self.b2 = instance
                        time.sleep(0.100)
                        req = self.session.post(settings.url['gameq2is_end'])#is_end
                        res = str(req.content)[2:-1]
                        if (res=='True'):
                                exit()
                else:
                        print('hello')
    def callbackwv(self, instance):
                i = (instance.pos[0]-50)//100
                j = (instance.pos[1]-75)//100
                u = j-1
                data = {'i':i,'j':j}
                time.sleep(1)
                req1 = self.session.post(settings.url['gameq2isvalidvwall'],data=data)
                res1 = str(req1.content)[2:-1]
                time.sleep(1)
                req2 = self.session.post(settings.url['gameq2havewall'])
                res2 = str(req2.content)[2:-1]
                if(res1=='True' and res2=='True'):                
                        instance.background_color = (8/255, 224/255, 163/255, 1)
                        for t in range(len(self.wallv)):
                                if( (self.wallv[t].pos[0]-50)//100 == i and (self.wallv[t].pos[1]-75)//100==u):
                                        self.wallv[t].background_color = (8/255, 224/255, 163/255, 1)
                                        break
                        req=self.session.get(settings.url['gameq2pluswall'])
    def callbackwh(self,instance):
                i=(instance.pos[0]-75)//100
                j=(instance.pos[1]-50)//100
                u=i+1
                data={'i':i,'j':j}
                req1=self.session.post(settings.url['gameq2isvalidhwall'],data=data)
                res1=str(req1.content)[2:-1]
                req2=self.session.poxt(settings.url['gameq2havewall'])
                res2=str(req2.content)[2:-1]
                if(res1=='True' and res2=='True'):                
                        instance.background_color=(7/255, 173/255, 224/255,1)
                        for t in range(len(self.wallh)):
                                if( (self.wallh[t].pos[0]-50)//100 == u and (self.wallh[t].pos[1]-75)//100==j):
                                        self.wallh[t].background_color=(8/255, 224/255, 163/255,1)
                                        break
                        req=self.session.get(settings.url['gameq2pluswall'])
    def build(self):
        req=requests.get(settings.url['gameq2turn'])#turn
        self.turn=str(req.content)[2:-1]
        time.sleep(0.100)
        layout = FloatLayout()
        Window.size = (1000, 1000)
        player = []
        for i in range(9):
            for j in range(9):
                if(i == 4 and j == 0):
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

                else:
                    self.b1 = Button(pos=(75+i*100, 75+j*100),
                                     size_hint=(None, None),
                                     size=(75, 75), background_color=(74/255, 1/255, 76/255, 1))
                    layout.add_widget(self.b1)
                    player.append(self.b1)
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

