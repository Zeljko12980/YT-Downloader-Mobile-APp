from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from pytube import YouTube

class YouTubeDownloader(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.url_label = Label(text="Paste the URL:")
        self.layout.add_widget(self.url_label)
        
        self.url_input = TextInput(hint_text='YouTube URL', multiline=False)
        self.layout.add_widget(self.url_input)
        
        self.download_button = Button(text="Download", on_press=self.download_video)
        self.layout.add_widget(self.download_button)
        
        self.status_label = Label(text="")
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def download_video(self, instance):
        url = self.url_input.text
        if not url:
            self.status_label.text = "Please enter a valid URL."
            return
        
        try:
            video = YouTube(url)
            high_res_stream = video.streams.get_highest_resolution()
            file_path = high_res_stream.download()
            self.status_label.text = f"Downloaded successfully: {file_path}"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    YouTubeDownloader().run()
