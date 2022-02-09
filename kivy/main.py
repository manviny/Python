import kivy

from kivy.app import App

# import and connect kivy file
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
Builder.load_file('1x2.kv')

class MyGridLayout(Widget):
 
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f'Hello {name} you {pizza} {color}')
        # self.add_widget(Label(text=f'Hello {name} you {pizza} {color}'))

class MyApp(App):

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
