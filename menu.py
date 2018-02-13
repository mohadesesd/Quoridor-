from kivy.graphics import *
from kivy.app import  App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.clock import *
import requests
from kivy.graphics.vertex_instructions import *
from kivy.graphics.context_instructions import Color


import network
import gameq2
import gameq4



class registerationApp(BoxLayout, App):
        """ This class is used to make a registeration form """
        def callback1(self, instance):        
                """ This function is called when you press button b1"""
                data={'name':self.name1.text, 'familyname':self.familyname.text,
                        'username':self.username.text, 'password':self.password.text,
                        'confirmpassword':self.confirmpassword.text,
                        'email':self.email.text, 'gender':self.gender.text}
                if(network.register(data,self.session)[0]):
                        self.stop()
                        loginmenuApp().run()
                else:
                        self.stop()
                        self.run()

        def callback2(self, instance):
  
                """ This function is called when you press button b2"""
                self.stop()
                enterymenuApp().run() 

        def build(self):                
                """ This function is used to make application """
                layout = FloatLayout()
                Window.size = (800, 1000)
                with layout.canvas:
                        Rectangle(size=(800, 1000), pos=(0, 0), source='/home/msd/Desktop/l.jpg')

                self.l1 = Label(text='[b][color=#600968][size=40]Registeration![/size][/color][/b]',
                                pos=(200, 900),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)		
                self.l2 = Label(text='[b][color=#600968][size=40]Name:[/size][/color][/b]',
                                pos=(80, 800),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)	
                self.name1 = TextInput(multiline=False,
                                      pos=(400, 800),
                                      size_hint=(None,None),
			              size=(300, 50),
                                      hint_text='Enter your name',
                                      hint_text_color=(213/250, 175/250, 214/250, 1))
                self.l3 = Label(text='[b][color=#600968][size=40]Family Name:[/size][/color][/b]',
                                pos=(80, 700),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.familyname = TextInput(multiline=False,
                                            pos=(400, 700),
                                            size_hint=(None, None),
                                            size=(300, 50),
                                            hint_text='Enter your family name',
                                            hint_text_color=(213/250, 175/250, 214/250, 1))
                self.l4 = Label(text='[b][color=#600968][size=40]User Name:[/size][/color][/b]',
                                pos=(80, 600),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.username = TextInput(multiline=False,
                                          pos=(400, 600),
                                          size_hint=(None, None),
                                          size=(300, 50),
                                          hint_text='Enter a username',
                                          hint_text_color=(213/250, 175/250, 214/250, 1))
                self.l5 = Label(text='[b][color=#600968][size=40]PassWord:[/size][/color][/b]',
                                pos=(80, 500),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.password = TextInput(multiline=False,
                                          pos=(400, 500),
                                          size_hint=(None, None),
			                  size=(300, 50),
                                          password=True)
                self.l6 = Label(text='[b][color=#600968][size=40]Confirm PassWord:[/size][/color][/b]',
                                pos=(80, 400),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.confirmpassword = TextInput(multiline=False,
                                                pos=(400, 400),
                                                size_hint=(None, None),
			                        size=(300, 50),
                                                password=True)
                self.l7 = Label(text='[b][color=#600968][size=40]E-mail:[/size][/color][/b]',
                                pos=(80, 300),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.email = TextInput(multiline=False,
                                       pos=(400, 300),
                                       size_hint=(None, None),
		                       size=(300, 50),
                                       hint_text='Enter your E-mail adress',
                                       hint_text_color=(213/250, 175/250, 214/250, 1))
                self.l8 = Label(text='[b][color=#600968][size=40]Gender:[/size][/color][/b]',
                                pos=(80, 200),
                                size_hint=(None, None),
                                size=(300, 70),
                                markup=True)
                self.gender = TextInput(multiline=False,
                                        pos=(400, 200),
                                        size_hint=(None, None),
			                size=(300, 50),
                                        hint_text='Male or Female',
                                        hint_text_color=(213/250, 175/250, 214/250, 1))
                layout.add_widget(self.l1)
                layout.add_widget(self.l2)
                layout.add_widget(self.name1)
                layout.add_widget(self.l3)
                layout.add_widget(self.familyname)
                layout.add_widget(self.l4)
                layout.add_widget(self.username)
                layout.add_widget(self.l5)
                layout.add_widget(self.password)
                layout.add_widget(self.l6)
                layout.add_widget(self.confirmpassword)
                layout.add_widget(self.l7)
                layout.add_widget(self.email)
                layout.add_widget(self.l8)
                layout.add_widget(self.gender)
                self.b1 = Button(text='[color=#0c0c0c][size=40]Submit[/size][/color]',
			        pos=(300, 100),
		       	        size_hint=(None, None),
		                size=(200, 50),
		                background_color=(100/250, 50/250, 125/250, 1),
                                markup=True)
                self.b2 = Button(text='[color=#0c0c0c][size=40]Back[/size][/color]',
			        pos=(300, 50),
		       	        size_hint=(None, None),
		                size=(200, 50),
		                background_color=(100/250, 50/250, 125/250, 1),
                                markup=True)
                layout.add_widget(self.b1)
                layout.add_widget(self.b2)
                self.b1.bind(on_press=self.callback1)
                self.b2.bind(on_press=self.callback2)
                return layout


class loginApp(BoxLayout, App):
        def callback1(self,instance):
                data = {'username':self.username.text, 'password':self.password.text}
                p = network.login(data, self.session)
                if(p[0]):
                        self.stop()
                        loginmenuApp().run()
                else:
                        self.stop()
                        self.run()
	
        def callback2(self, instance):
                self.stop()
                enterymenuApp().run() 

        def build(self):
                layout = FloatLayout()
                Window.size = (700, 700)
                with layout.canvas:
                        Rectangle(size=(700, 700), pos=(0, 0), source='/home/msd/Desktop/l.jpg')

                self.l1 = Label(text='[b][color=#600968][size=50]Login![/size][/color][/b]',
                                pos=(150, 600),
                                size_hint=(None, None),
                                size=(300, 50),
                                markup=True)		
                self.l2 = Label(text='[b][color=#600968][size=40]User Name:[/size][/color][/b]',
                                pos=(20, 500),
                                size_hint=(None, None),
                                size=(300, 50),
                                markup=True)	
                self.username = TextInput(multiline=False,
                                    pos=(300, 500),
                                    size_hint=(None, None),
			            size=(300, 50))
                self.l3 = Label(text='[b][color=#600968][size=40]PassWord:[/size][/color][/b]',
                                pos=(20, 400),
                                size_hint=(None, None),
                                size=(300, 50),
                                markup=True)
                self.password = TextInput(multiline=False,
                                    pos=(300, 400),
                                    size_hint=(None,None),
                                    size=(300, 50),
                                    password=True)
                self.b1 = Button(text='[color=#0c0c0c][size=40]Login[/size][/color]',
			        pos=(300, 300),
		       	        size_hint=(None, None),
		                size=(200, 50),
		                background_color=(100/250, 50/250, 125/250, 1),
                                markup=True)
                self.b2 = Button(text='[color=#0c0c0c][size=40]Back[/size][/color]',
			        pos=(300, 250),
		       	        size_hint=(None, None),
		                size=(200, 50),
		                background_color=(100/250, 50/250, 125/250, 1),
                                markup=True)
                layout.add_widget(self.l1)
                layout.add_widget(self.l2)
                layout.add_widget(self.username)
                layout.add_widget(self.l3)
                layout.add_widget(self.password)
                layout.add_widget(self.b1)
                layout.add_widget(self.b2)
                self.b1.bind(on_press=self.callback1)
                self.b2.bind(on_press=self.callback2)
                return layout


class enterymenuApp(BoxLayout, App):
        session=requests.Session()
        """  This class is used to make an application to make enterance menu  """

        def callback1(self, instance):
                """  This function is called when you press button btn1
                        it runs registeration application that is maked in netwok.py  """
                self.stop()
                registerationApp.session = self.session
                registerationApp().run()

        def callback2(self, instance):
                """  This function is called when you press button btn2
                it runs login application that is maked in network.py """
                self.stop()
                loginApp.session=self.session
                loginApp().run()

        def callback3(self, instance):
                """  This funtion is called when you press button btn3 
			it exit the program """
                exit()

        def build(self):
                """  This function is used to make your application  """
                layout = FloatLayout()
                Window.size = (1000, 500)
                with layout.canvas:
                        RoundedRectangle(size=(500, 500), pos=(500, 0), source='/home/msd/Desktop/qu.jpg')

                self.l1 = Label(text='[b][color=#600968][size=40]Hello,Wellcome![/size][/color][/b]',
                           pos=(100, 400),
                           size_hint=(None, None),
                           size=(300, 70),
                           markup=True)
                self.btn1 = Button(text='[b][color=#600968][size=40]Register[/size][/color][/b]',
                              pos=(100, 300),
                              size_hint=(None, None),
                              size=(300, 70),
                              markup=True,
                              background_color=(100/255, 50/255, 125/255, 1))
                self.btn2 = Button(text='[b][color=#600968][size=40]Login[/size][/color][/b]',
                              pos=(100, 200),
                              size_hint=(None, None),
                              size=(300, 70),
                              markup=True,
                              background_color=(100/255, 50/255, 125/255, 1))
                self.btn3 = Button(text='[b][color=#600968][size=40]Exit[/size][/color][/b]',
                              pos=(100, 100),
                              size_hint=(None, None),
                              size=(300, 70),
                              markup=True,
                              background_color=(100/255, 50/255, 125/255, 1))
                layout.add_widget(self.l1)
                layout.add_widget(self.btn1)
                layout.add_widget(self.btn2)
                layout.add_widget(self.btn3)
                self.btn1.bind(on_press=self.callback1)
                self.btn2.bind(on_press=self.callback2)
                self.btn3.bind(on_press=self.callback3)
                return layout


class loginmenuApp(BoxLayout, App):
         """this application is used to show your login menu"""
         session = enterymenuApp.session
         def callback1(self, instance):
                """this function call when you press quoridor 2player game"""
                self.stop()
                gameq2.Gameq2App().run()

         def callback2(self, instance):
                """this function call when you press quridor 4player game"""
                self.stop()
                gameq4.Gameq4App().run()
                        
         def callback3(self, instance):
                """this function is used to test server"""
                network.gq2(self.session)
                        
         def callback4(self, instance):
                """this function is used to log out your session"""
                p = network.logout(self.session)
                if(p[0]):
                        self.stop()
                        enterymenuApp().run()
         
         def callback5(self, instance):
                """this function is used to exit app"""
                exit()
         
         def build(self):
                """  This function is used to make your application  """
                layout = FloatLayout()
                Window.size = (1000, 1000)
                with layout.canvas:
                        Rectangle(size=(1000,1000), pos=(0,0), source='/home/msd/Desktop/g.jpg')
                self.btn1 = Button(text='[b][color=#600968][size=20]Quoridor(2players)[/size][/color][/b]',
                                    pos=(600, 800),
                                    size_hint=(None, None),
                                    size=(300, 80),
                                    markup=True,
                                    background_color=(100/250, 50/250, 125/250, 1))
                self.btn2 = Button(text='[b][color=#600968][size=20]Quoridor(4players)[/size][/color][/b]',
                                    pos=(600, 650),
                                    size_hint=(None, None),
                                    size=(300, 80),
                                    markup=True,
                                    background_color=(100/250, 50/250, 125/250, 1))
                self.btn3 = Button(text='[b][color=#600968][size=20]Test server[/size][/color][/b]',
                              pos=(600, 500),
                              size_hint=(None, None),
                              size=(300, 80),
                              markup=True,
                              background_color=(100/250, 50/250, 125/250, 1))
                self.btn4 = Button(text='[b][color=#600968][size=20]Logout[/size][/color][/b]',
                              pos=(600, 350),
                              size_hint=(None, None),
                              size=(300, 80),
                              markup=True,
                              background_color=(100/250, 50/250, 125/250, 1))
                self.btn5 = Button(text='[b][color=#600968][size=20]Exit[/size][/color][/b]',
                              pos=(600, 200),
                              size_hint=(None, None),
                              size=(300, 80),
                              markup=True,
                              background_color=(100/250, 50/250, 125/250, 1))
                layout.add_widget(self.btn1)
                layout.add_widget(self.btn2)
                layout.add_widget(self.btn3)
                layout.add_widget(self.btn4)
                layout.add_widget(self.btn5)
                self.btn1.bind(on_press=self.callback1)
                self.btn2.bind(on_press=self.callback2)
                self.btn3.bind(on_press=self.callback3)
                self.btn4.bind(on_press=self.callback4)
                self.btn5.bind(on_press=self.callback5)
                return layout

