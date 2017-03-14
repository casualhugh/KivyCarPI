#Imports (there are lots due to Kivy UI)
from kivy.app import App

from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from mysettings_JSON import settings_json
from kivy.animation import Animation
from functools import partial
import time

#Variables
Window.size= (1024, 600)
Window.clearcolor = (0.2, 0.2, 0.2, 1)

class ColourWheel():
    pass

#Seperated Widgets
class StatusBar(BoxLayout):
    def Shutdown():
        pass

    def Reboot():
        pass

    def Bluetooth():
        pass

    def EngineState():
        pass

    def OBD2State():
        pass

class BottomBar(BoxLayout):
    def SongMetaData():
        pass

    def JumpBack():
        pass

    def PlayPause():
        pass

    def Skip():
        pass

    def Mute():
        pass

    def VolumeDown():
        pass

    def VolumeUp():
        pass

class Tile(Button):
    pass



class LiveTiles(GridLayout):
    pass


#The Different Screens
class HomeScreen(Screen):
    pass
class MusicScreen(Screen):
    #Replaces bottom bar with nothing and background is the cover art
    #Small Tiles = [mute, voldown, volup, skipback, playpause, skip]
    #LiveTiles.tiles_names = ["Mute", "Volume Down", "Volume Up", "Go Back", "Play/Pause", "Skip"]
    pass
class ControlScreen(Screen):
    #LiveTiles.tiles_names = ["Cancel", "Up Arrow", "Set", "Left Arrow", "Down Arrow", "Right Arrow"]
    #Tiles = [Cancel(), UpArrow(), Set(), LeftArrow(), DownArrow(),RightArrow()]
    #momentarily presses each button on the Control interface
    def Cancel(self):
        pass

    def Set(self):
        pass

    def UpArrow(self):
        pass

    def DownArrow(self):
        pass

    def LeftArrow(self):
        pass

    def RightArrow(self):
        pass

class AuxScreen(Screen):
    #retrieve last chosen settings for this screen
    #Convert to tiles list
    #All possible functions in this class ie change heat, work mode radio etc
    pass

class ReverseScreen(Screen):
    def LoadCamera(self):
        cam = Camera(play=True)

    def LoadSensors(self):
        pass

    def Display(self):
        self.LoadCamera()
        self.LoadSensors()


class GaugeScreen(Screen):
    #retrieve Last chosen Gauges from file
    #Once recieved convert into table for tiles (six tiles)
    #include setting for different types of gauges ie label, gauge, both
    pass


class SettingScreen(Screen):
    #Tiles = [ConfigureGauges(), ConfigureAux(), ResetSettings(), BluetoothSetup(), ConfigureHome(), ConfigureSettings()]

    def ConfigureGauges(self):
        pass

    def ConfigureAux(self):
        pass

    def ResetSettings(self):
        pass

    def BluetoothSetup(self):
        pass

    def ConfigureHome(self):
        pass

    def ConfigureSettings(self):
        pass

class BluetoothScreen(Screen):
    pass
class MainScreenManager(ScreenManager):
    lastscreen = ObjectProperty('home_screen')

class HomeInterface(BoxLayout):
    pass

class MainApp(App):
    time = StringProperty()
    def update(self, *args):
        self.time = str(time.strftime("%I:%M:%S %p"))+"\n"+str(time.strftime("%d-%m-%y"))

    def build(self):
        Clock.schedule_interval(self.update, 1)
        return HomeInterface()
    def build_config(selfself, config):
        config.setdefaults('example', {
            })
    def build_settings(self, settings):
        settings.add_json_panel('NAME',
                                self.config,
                                data=settings_json)


#Simply runs the application when the Window opens
if __name__ == "__main__":
    MainApp().run()