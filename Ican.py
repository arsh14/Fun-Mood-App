from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import random
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.graphics import Color


class OptWindow(Screen):
    pass

class CustomLayout(GridLayout):

    background_image = ObjectProperty(
        Image(
            source='backapp.jpg', anim_delay=.1))

class CustomLayout2(FloatLayout):

    background_image = ObjectProperty(
        Image(
            source='backapp.jpg', anim_delay=.1))

class SecondWindow(Screen):

    def plays(self):
        item = [1, 2, 3]
        i = item[random.randrange(len(item))]

        if i == 1:
            x = "Hai Apna Dil To Awara (128Kbps)-(BigMusic.In).mp3"

        elif i == 2:
            x = "Musafir-Hoon-Yaaron-(RaagSong.Com).mp3"
        else:
            x = "Zindagi-Ek-Safar-Hai-(RaagSong.Com).mp3"
        self.sound = SoundLoader.load(x)
        if self.sound:
            self.sound.play()
            print(x, " is being played ")


    def stop(self):
        self.sound.stop()



class WindowManager(ScreenManager):
    pass


kv=Builder.load_file("mine.kv")


class MineApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MineApp().run()