from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

# Set window size (optional)
Window.size = (400, 600)

# Welcome Screen
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)

        # Title
        title = Label(
            text="🤲 Assalamualaikum!",
            font_size=30,
            color=(1, 0.84, 0, 1),  # Gold color
        )

        # Subtitle
        subtitle = Label(
            text="Welcome to the Taraweeh Rakat Counter.",
            font_size=20,
            color=(1, 1, 1, 1),  # White color
        )

        # Start Button
        start_button = Button(
            text="Start",
            font_size=22,
            background_color=(0, 0.5, 1, 1),  # Blue color
            size_hint=(0.6, 0.2),
            pos_hint={"center_x": 0.5},
        )
        start_button.bind(on_press=self.go_to_counter)

        # Add widgets to layout
        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def go_to_counter(self, instance):
        self.manager.current = "counter"


# Taraweeh Counter Screen
class TaraweehCounter(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rakat_count = 0
        layout = BoxLayout(orientation="vertical", padding=50, spacing=20)

        # Title
        title = Label(
            text="🌙 Taraweeh Rakat Counter",
            font_size=30,
            color=(1, 0.84, 0, 1),  # Gold color
        )

        # Rakat Count Label
        self.rakat_label = Label(
            text=f"Rakat: {self.rakat_count}/20",
            font_size=24,
            color=(1, 1, 1, 1),  # White color
        )

        # Pray 2 Rakats Button
        pray_button = Button(
            text="✅ Pray 2 Rakats",
            font_size=20,
            background_color=(0, 1, 0, 1),  # Green color
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5},
        )
        pray_button.bind(on_press=self.pray_rakat)

        # Reset Button
        reset_button = Button(
            text="🔄 Reset",
            font_size=20,
            background_color=(1, 0, 0, 1),  # Red color
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5},
        )
        reset_button.bind(on_press=self.reset_rakat)

        # Home Button
        home_button = Button(
            text="🏠 Home",
            font_size=20,
            background_color=(0.5, 0.5, 1, 1),  # Light blue color
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5},
        )
        home_button.bind(on_press=self.go_home)

        # Add widgets to layout
        layout.add_widget(title)
        layout.add_widget(self.rakat_label)
        layout.add_widget(pray_button)
        layout.add_widget(reset_button)
        layout.add_widget(home_button)

        self.add_widget(layout)

    def pray_rakat(self, instance):
        if self.rakat_count < 20:
            self.rakat_count += 2
            self.rakat_label.text = f"Rakat: {self.rakat_count}/20"

    def reset_rakat(self, instance):
        self.rakat_count = 0
        self.rakat_label.text = f"Rakat: {self.rakat_count}/20"

    def go_home(self, instance):
        self.manager.current = "welcome"


# Screen Manager
class ScreenManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(TaraweehCounter(name="counter"))
        return sm


# Run the app
if __name__ == "__main__":
    ScreenManagerApp().run()
    