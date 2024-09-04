from customtkinter import CTk
from customtkinter import CTkToplevel
from customtkinter import CTkImage
from customtkinter import CTkLabel
import PIL
from PIL import Image
from PIL import ImageFilter
from Application import Application
import os

class Main(Application):
    def __init__(self, janela: CTk|CTkToplevel, centered: bool = True):
        super().__init__(janela=janela)
        self.set_geometry(800, 600, centered)
        self.set_title(self.title)
        self.images = []

    def start(self):
        self.janela.mainloop()

    @staticmethod
    def set_blur(img: Image, blur: int):
        if img.mode not in ('RGB', 'L'):
            img = img.convert('RGB')
        return img.filter(ImageFilter.GaussianBlur(blur))

    # Refatorar esse código
    def adicionar_label_image(self, filename: str, text, options=None):
        if options is None:
            options = {}

        if not os.path.isfile(filename):
            raise Exception(f"Arquivo {filename} não encontrado")

        image = Image.open(filename)
        if options.get('blur', False):
            image = self.set_blur(image, options['blur'])

        img = CTkImage(image)
        self.set_options_elements(element=img, options=options)

        if options['config'].get('size', False):
            del options['config']['size']

        label = CTkLabel(self.janela, image=img, text=text)
        self.set_options_elements(options, label)
        self.positional_element(element=label, options=options)

    def apply_background_image(self):
        image_background = f"{self.get_base_path()}/images/background.png"
        self.adicionar_label_image(filename=image_background, text='', options={
            'config': {
                'size': (self.janela.winfo_screenwidth(), self.janela.winfo_screenheight())
            },
            'blur': 1,
            'place': {
                'x': 0,
                'y': 0
            }
        })


if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()