import customtkinter as ctk
from PIL.Image import Image
from SqlHandler import SqlHandler
from customtkinter import CTkProgressBar as Progressbar
import os, sys
import pywinstyles


class Application:
    def __init__(self, janela: ctk.CTk):
        self.connector = SqlHandler()
        self.janela = janela
        self.images = []
        self.buttons = []
        self.background = 'gray'
        self.title = 'Restaurante do Ederson'
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.set_icon()
        ctk.deactivate_automatic_dpi_awareness()
        pywinstyles.apply_style(self.janela, 'optimised')
        pywinstyles.change_header_color(self.janela, color=self.get_colors('dark_gray'))
        pywinstyles.change_border_color(self.janela, color=self.get_colors('dark_gray'))

    def set_icon(self):
        self.janela.iconbitmap(f'{self.get_base_path()}/icon.ico')

    def set_geometry(self, width, height, center = True, fullscreen = False, x=None, y=None):
        if fullscreen:
            try:
                if os.uname().sysname:
                    self.janela.attributes('-zoomed', True)
            except AttributeError:
                self.janela.state('zoomed')
        
        if center:
            screen_width = self.janela.winfo_screenwidth()
            screen_height = self.janela.winfo_screenheight()

            x = (screen_width - width) // 2
            y = (screen_height - height) // 2

            self.janela.geometry(f"{width}x{height}+{x}+{y}")
        else:
            if x is not None and y is not None:
                self.janela.geometry(f"{width}x{height}+{x}+{y}")
            else:
                self.janela.geometry(f"{width}x{height}")

    def set_title(self, title=""):
        """
        Define o título da janela.

        Parameters:
        - title (str): O título a ser definido para a janela. O valor padrão é uma string vazia, o que resultará em nenhum título ou o título existente.

        Usage:
        - `set_title("Novo Título")` define o título da janela como "Novo Título".
        """
        self.janela.title(title)

    def set_background(self, color):
        """
       Define a cor de fundo da janela.

       Parameters:
       - color (str): A cor a ser definida como fundo da janela. Deve ser uma string representando a cor, como "red", "#FF0000", etc.

       Usage:
       - `set_background("blue")` define a cor de fundo da janela como azul.
       """
        self.background = color
        self.janela.config(background=color)

    def set_grid_column_weight(self, columns, weight = 2, options:dict=None):
        """
        Define o peso das colunas no layout de grade da janela.

        Parameters:
        - columns (int): O número de colunas que devem ter o mesmo peso.
        - weight (int): O peso a ser atribuído às colunas. O valor padrão é 2. O peso controla como a largura das colunas é ajustada quando a janela é redimensionada.

        Usage:
        - `set_grid_column_weight(3)` define o peso das primeiras 3 colunas para 2.
        - `set_grid_column_weight(3, 1)` define o peso das primeiras 3 colunas para 1.
        """
        for index in range(columns):
            if options is not None:
                self.janela.grid_columnconfigure(index, weight=weight, **options)
            else:
                self.janela.grid_columnconfigure(index, weight=weight)

    def set_row_configure(self, rows, weight=1):
        for index in range(rows):
            self.janela.grid_rowconfigure(index, weight=weight)


    @staticmethod
    def set_options_elements(options: dict, element):
        if 'opacity' in options:
            pywinstyles.set_opacity(element, color=options.get('opacity', 'white'))
        if 'config' in options:
            element.configure(**options['config'])

    @staticmethod
    def positional_element(element, options):
        """
            Configura o posicionamento de um elemento usando o método grid.

            Parameters:
            - element: O widget a ser configurado.
            - options: Um dicionário contendo opções para o método grid. Pode incluir chaves como 'row', 'column', 'padx', 'pady', e 'sticky'.

            Se 'options' contiver uma chave 'grid', seus valores substituirão os padrões.
            """
        grid_options = {
            'padx': 10,
            'pady': 10
        }

        if options is not None and 'grid' in options:
            grid_options.update(options['grid'])

        if options.get('place', False):
            element.place(**options['place'])
            return

        if options.get('pack', False):
            element.pack(**options['pack'])
            return

        element.grid(**grid_options)

    def adicionar_entry(self, options=None):
        entrada = ctk.CTkEntry(self.janela)
        self.set_options_elements(options, entrada)

        self.positional_element(element=entrada, options=options)
        return entrada

    def adicionar_imagem(self, image: Image, image_options=None, label_options=None, master=None):
        if master is None:
            master = self.janela
        img = ctk.CTkImage(image)
        self.set_options_elements(options=image_options, element=img)
        self.images.append(img)

        label = ctk.CTkLabel(master, text='', image=img)
        self.set_options_elements(label_options, label)

        self.positional_element(element=label, options=label_options)

    def adicionar_label(self, text, options=None, master=None):
        if master is None:
            master = self.janela
        label = ctk.CTkLabel(master, text=text)

        self.set_options_elements(options, label)

        self.positional_element(element=label, options=options)
        
        return label

    def adicionar_button(self, text, command, options=None, master=None):
        if master is None:
            master = self.janela
        if options['config'].get('image', False):
            options['config']['image'] = ctk.CTkImage(options['config']['image'])
        btn = ctk.CTkButton(master, text=text, command=command)

        self.set_options_elements(options, btn)

        self.positional_element(element=btn, options=options)

        self.buttons.append(btn)
        return btn

    def adicionar_progressbar(self, options=None):
        progress = Progressbar(self.janela)
        progress.set(0)
        self.set_options_elements(options, progress)
        self.positional_element(element=progress, options=options)
        return progress

    def adicionar_frame(self, master=None, options=None, scrollable=False):
        if master is None:
            master = self.janela

        if scrollable:
            frame = ctk.CTkScrollableFrame(master)
        else:
            frame = ctk.CTkFrame(master)

        self.set_options_elements(element=frame, options=options)
        self.positional_element(element=frame, options=options)
        return frame

    def minimize(self):
        self.janela.iconify()

    def maximize(self):
        self.janela.state('zoomed')

    def close(self):
        self.janela.destroy()

    def restore(self):
        self.janela.state('normal')

    def deiconify(self):
        self.janela.deiconify()

    def start(self):
        self.janela.mainloop()

    @staticmethod
    def get_base_path():
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    @staticmethod
    def get_colors(color: str):
        colors = {
            'black': '#000000',
            'dark_green': '#004d00',
            'medium_green': '#009900',
            'light_green': '#66ff66',
            'dark_gray': '#333333',
            'light_gray': '#cccccc',
            'lime_green': '#ccff66',
            'olive_green': '#808000'
        }
        if colors.get(color, False):
            return colors[color]
        return "#000000"


if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()