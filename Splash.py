import customtkinter as ctk
import PIL
from PIL import Image
from Main import Main
import os, sys
from Produtos import Produtos
import threading
import requests


class Splash(Main):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(350, 280, True)
        self.set_title('Splash')
        self.set_grid_column_weight(columns=1, weight=3)
        self.loading_text = 'Carregando...'

        self.adicionar_imagem(image=self.get_icon(), image_options={
            'config': {
                'size': (200, 200)
            }
        }, label_options={
            'grid': {
                'pady': (10, 0)
            }
        })

        self.label = self.adicionar_label(text=self.loading_text, options={
            'config': {
                'font': ('Arial', 16)
            },
            'grid': {
                'row': 1,
                'pady': (5, 0)
            }
        })

        self.progressbar = self.adicionar_progressbar(options={
            'grid': {
                'row': 2,
                'pady': (5, 0)
            }
        })

        thread = threading.Thread(target=self.check_and_download_images)
        thread.start()

        self.janela.protocol("WM_DELETE_WINDOW", self.on_closing)

    def check_and_download_images(self):
        try:
            path = os.path.dirname(os.path.abspath(sys.argv[0]))
            if not os.path.isdir(f"{path}/images"):
                os.mkdir(f"{path}/images")

            produtos = Produtos(self.connector)
            produtos = produtos.get_all()
            total_produtos = len(produtos)

            list_imagens_download_avulsas = {
                'Login': 'https://blogmaladeviagem.com.br/wp-content/uploads/2019/10/Fogo-caipira-2.png',
                'background': 'https://i.pinimg.com/736x/ce/1a/18/ce1a18dcf0c6cfc9b5538dfae8e4aa09.jpg',
                'cart': 'https://www.clker.com//cliparts/j/s/U/7/a/W/shopping-cart-hi.png',
                'back': 'https://cdn-icons-png.flaticon.com/512/5548/5548528.png',
                'trash': 'https://cdn3.iconfinder.com/data/icons/linecons-free-vector-icons-pack/32/trash-512.png',
            }

            total_downloads = total_produtos + len(list_imagens_download_avulsas)
            increment_value = (100/total_downloads) / 2
            self.increment_progressbar(increment_value)

            count = 0
            self.loading_text += f" {count} de {total_downloads} imagens"

            for key, value in list_imagens_download_avulsas.items():
                count += 1
                self.loading_text = f"Carregando... {count} de {total_downloads} imagens"
                self.label.configure(text=self.loading_text)

                filename = f"{path}/images/{key}.png"
                if not os.path.isfile(filename):
                    self.download_save(value, filename)
                    self.step_progressbar()

            for produto in produtos:
                count += 1
                self.loading_text = f"Carregando... {count} de {total_downloads} imagens"
                self.label.configure(text=self.loading_text)
                
                self.step_progressbar()
                filename = f"{path}/images/{produto['description']}.png"
                if not os.path.isfile(filename):
                    self.download_save(produto['image'], filename)

            self.janela.after(0, self.close_window)
        except Exception as e:
            print(f"Erro ao carregar as imagens: {e}")
            self.janela.after(0, self.close_window)

    @staticmethod
    def download_save(url, filename):
        try:
            get_image = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1'})
            get_image.raise_for_status()
            with open(filename, 'wb') as file:
                file.write(get_image.content)
            return True
        except Exception as e:
            print(f"Erro ao fazer download da image: {e}")
            raise Exception(e)


    def step_progressbar(self):
        self.progressbar.step()

    def stop_progressbar(self):
        self.progressbar.stop()

    def increment_progressbar(self, value):
        self.progressbar.configure(determinate_speed=value)

    @staticmethod
    def get_icon():
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        filename = f"{path}/icon.png"
        img = Image.open(filename)
        return img

    def close_window(self):
        self.progressbar.stop()
        self.janela.destroy()

    def on_closing(self):
        self.janela.destroy()

    def start(self):
        self.janela.mainloop()

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()