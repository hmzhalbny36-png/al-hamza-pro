from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.graphics.texture import Texture
from PIL import Image, ImageDraw
import io

class AlHamzaProApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.label_title = Label(text='[b]Al-Hamza Pro[/b]\nمعالج الصور', markup=True, font_size='24sp')
        self.layout.add_widget(self.label_title)
        
        self.btn_process = Button(text='اضغط لإنشاء وتعديل الصورة', size_hint=(1, 0.3))
        self.btn_process.bind(on_press=self.process_and_show)
        self.layout.add_widget(self.btn_process)
        
        self.image_display = KivyImage(size_hint=(1, 0.6))
        self.layout.add_widget(self.image_display)
        
        self.status_label = Label(text='انتظر الضغط على الزر', font_size='16sp')
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def process_and_show(self, instance):
        try:
            self.status_label.text = 'جاري معالجة الصورة...'
            
            img = Image.new('RGB', (800, 600), color=(73, 109, 137))
            d = ImageDraw.Draw(img)
            d.text((250, 280), "Al-Hamza Pro", fill=(255, 255, 0))
            img.save("logo_test.jpg")
            
            with Image.open("logo_test.jpg") as img_opened:
                width, height = img_opened.size
                new_size = (width // 2, height // 2)
                resized_img = img_opened.resize(new_size)
                resized_img.save("output_logo_test.jpg")
            
            with open("output_logo_test.jpg", "rb") as f:
                data = f.read()
                texture = Texture.create(size=(400, 300))
                texture.blit_buffer(data, colorfmt='rgb', bufferfmt='ubyte')
                self.image_display.texture = texture
            
            self.status_label.text = '✓ تمت المعالجة وعرض الصورة بنجاح!'
            
        except Exception as e:
            self.status_label.text = f'خطأ: {str(e)}'

if __name__ == '__main__':
    AlHamzaProApp().run()
