from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image

class BoxLayoutMain(BoxLayout):
    pass

class OverlayLayout(RelativeLayout):
    pass

class MyImageButton(Button):
    pass  # Define if needed

class MyApp(App):
    def exit_confirmation(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Do you want to exit the application?'))
        btn_layout = BoxLayout()
        btn_yes = Button(text='Yes')
        btn_yes.bind(on_press=self.exit_app)  # Bind the "Yes" button to exit_app method
        btn_no = Button(text='No')
        btn_no.bind(on_press=self.dismiss_popup)
        btn_layout.add_widget(btn_yes)
        btn_layout.add_widget(btn_no)
        content.add_widget(btn_layout)
        self.popup = Popup(title='Exit Confirmation', content=content, size_hint=(0.8, 0.6))
        self.popup.open()

    def exit_app(self, instance):
        self.stop()  # Stop the application

    def dismiss_popup(self, instance):
        self.popup.dismiss()

    def build(self):
        return BoxLayoutMain()

if __name__ == "__main__":
    MyApp().run()
