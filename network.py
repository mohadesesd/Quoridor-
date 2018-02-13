from kivy.graphics import *
from kivy.app import  App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import *
import requests

import gameq2
import gameq4
import qu2
import qu4
import settings

def is_valid(data):
        """check if data is valid or not"""
        if(data!='' and ('      ' not in data)and (' ' not in data) and (len(data)<=100)):
                        return True
        else:
                        return False

def is_validemail(email):
        """check if email is valid or not"""
        if(email!='' and ('      ' not in email) and 
           (' ' not in email)and ('@' in email)and
                ('.' in email) and (len(email)<=150)):
                return True
        else:
                return False

def is_validgender(gender):
        """check if gender is valid or not"""
        if(gender== 'Female' or gender == 'Male' or gender=='male' or gender=='female'):
                return True
        else:
                return False

def register(data,session):
        """check if data is valid or not (if it is valid send a request to server to 
        check if it is possible to register or not"""
        if(is_valid(data['name'])):
                if(is_valid(data['familyname'])):
                        if(is_valid(data['username'])):
                                if(is_valid(data['password'])):
                                        if(data['password']==data['confirmpassword']):
                                                if(is_validemail(data['email'])):
                                                                if(is_validgender(data['gender'])):
                                                                        req = session.post(settings.url['register'],data=data)
                                                                        res = str(req.content)[2:-1]
                                                                        if(res=='you haved register!'):
                                                                                return (True, res)
        return (False,'you cant register!')

def login(data, session):
        """send a request to server to check out if it is possible to login or not"""
        req = session.post(settings.url['login'],data=data)
        res = str(req.content)[2:-1]
        if(res=='you haved logged in'):
                return (True, res)
        return (False, 'you cant logged in')

def logout(session):
        """send a request to server to check out if it is possible to logout or not"""
        req = session.get(settings.url['logout'])
        res = str(req.content)[2:-1]
        if(res=='you have been logged out'):
                return (True, res)
        return (False, 'you are not logged in')

def gq2(session):
        #req=session.post(settings.url['gameq2clone'])
        #res=str(req.content)[2:-1]
        #if(res=='play game'):
        #       return True
        #else:
        #       return False"""
        qu2.Gameq2App.session=session
        App.get_running_app().stop()
        qu2.Gameq2App().run()


def gq4(session):
        #req=session.post(settings.usl['gameq4clone'])
        #res=str(req.content)[2:-1]
        #if(res=='play game'):
         #       App.get_running_app().stop()
         #       gameq4.Gameq4App().run()
          #      return True	
        #else:
        #	return False
        pass                	
