#!/usr/bin/env python3

import gettext

'''
    Switching Locale

    You can switch locales in your program using Class based gettex API
    The method gettext.translation accepts some parameters that can be used 
    to load the associated .mo files of a particular language. 
    If no .mo file is found, it raises an error

    base => is the domain and the method will look for a .po
    localedir => is the directory location of the locale folder you created
    languages => is a hint for the searching mechanism to load particular language code more resiliently
'''
el = gettext.translation('base', localedir='locale', languages=['es'])
el.install()
_ = el.gettext

def say_hello():
    '''
        This is a short function when you write your name
        yo can show a funny greeting :D
    '''
    name =  input(_('What is your name?'))
    print(_('Hello, {}. :D').format(name))

if __name__=='__main__':
    say_hello()