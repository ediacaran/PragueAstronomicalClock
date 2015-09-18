#!/usr/bin/python
# vim: set fileencoding=utf-8 :

__version__ = '0.0.1'

import kivy
from kivy.app import App
from kivy.uix.label import Label

class CrashCourseApp(App):
    def build(self):
        return Label(text="Astronomical dial")

if __name__ == '__main__':
    CrashCourseApp().run()

