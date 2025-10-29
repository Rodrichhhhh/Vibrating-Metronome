from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from plyer import vibrator



class TempoApp(App):

    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        
        self.bpm_input = TextInput(hint_text="Enter BPM", font_size=50, input_filter='int', multiline=False)
        self.layout.add_widget(self.bpm_input)

        
        self.label = Label(text="Ready", font_size=50)
        self.layout.add_widget(self.label)

       
        self.button = Button(text="Start Tempo", size_hint=(1, 0.3))
        self.button.bind(on_press=self.start_tempo)
        self.layout.add_widget(self.button)

        self.button2 = Button(text="Stop", size_hint=(1, 0.3))
        self.button2.bind(on_press=self.stop_tempo)
        self.layout.add_widget(self.button2)

        
        self.sound = SoundLoader.load("TempoBeep.wav")
        if not self.sound:
            print("Failed to load sound!")

        return self.layout

    
    def start_tempo(self, instance):
        try:
            self.BPM = int(self.bpm_input.text)
        except ValueError:
            self.label.text = "Invalid BPM"
            return

        
        self.counter = 3
        Clock.schedule_interval(self.countdown_tick, 1)

    
    def countdown_tick(self, dt):
        if self.counter > 0:
            self.label.text = str(self.counter)
            print(self.counter)
            self.counter = self.counter - 1
        else:
            self.label.text = "Go!"
            print("Go!")
            Clock.unschedule(self.countdown_tick)
            self.start_metronome()  
            

    
    def start_metronome(self):
        interval = 60 / self.BPM  
        Clock.schedule_interval(self.play_beat, interval)
        self.label.text = f"Tempo: {self.BPM} BPM"

   
    def play_beat(self, dt):
        if self.sound:
            self.sound.play()
            print("Tick")


    def vibrate_beat(self, dt):
       vibrator.vibrate(0.1)



    def stop_tempo(self, dt): 
        Clock.unschedule(self.play_beat)
        Clock.unschedule(self.vibrate_beat)




if __name__ == "__main__":
    TempoApp().run()
