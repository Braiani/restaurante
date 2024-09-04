from customtkinter import CTk, CTkToplevel
from Main import Main
from Login import Login
from Categoria import Categoria
from Splash import Splash
from Cart import Cart
from Products_view import ProductsView
from Cart_view import CartView


class Restaurante:
    def __init__(self) -> None:
        self.logado = None
        self.app_master = None
        self.root = None
        self.shouldLogin = True
        self.cart = None
        self.itens_cart = 0
        self.init()

    def create_show_products(self, categoria_id):
        def function():
            self.show_products(category_id=categoria_id)

        return function

    def init(self):
        temp_ctk = CTk()
        splash = Splash(temp_ctk)
        splash.start()

        if self.shouldLogin and self.logado is None:
            root = CTk()
            login = Login(root)
            login.start()
            self.logado = login.get_logado()
            if not self.logado:
                print('Saindo do programa!')
                exit()

        root = CTk()
        self.root = root
        self.app_master = Main(self.root)

        self.app_master.janela.configure(fg_color=self.app_master.get_colors('black'))

        self.app_master.set_geometry(width=800, height=600, fullscreen=False)
        self.app_master.set_grid_column_weight(columns=3, weight=2)

        self.app_master.apply_background_image()

        frame_title = self.app_master.adicionar_frame(options={
            'config': {
                'border_width': 2,
                'corner_radius': 32,
                'border_color': self.app_master.get_colors('medium_green'),
                'fg_color': self.app_master.get_colors('dark_gray'),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 0,
                'column': 0,
                'columnspan': 3,
                'pady': (50, 100)
            }
        })

        self.app_master.adicionar_label(master=frame_title, text=self.app_master.title, options={
            'config': {
                'font': ('Arial', 32),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 0,
                'column': 1,
                'padx': (20,20),
                'pady': (20,0)
            }
        })
        self.app_master.adicionar_label(master=frame_title, text=f'Seja bem vindo {self.logado["name"]}', options={
            'config': {
                'font': ('Arial', 28),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 1,
                'column': 1,
                'padx': (20,20),
                'pady': (0,20)
            }
        })

        categorias = Categoria().getAll()
        column = 0
        row = 2

        for categoria in categorias:
            if column == 3:
                column = 0
                row += 1

            categoria_id = int(categoria["id"])
            self.app_master.adicionar_button(text=categoria["descricao"], command=self.create_show_products(categoria_id=categoria_id), options={
                'config': {
                    'height': 50,
                    'corner_radius': 32,
                    'fg_color': self.app_master.get_colors('dark_gray'),
                    'bg_color': '#000001',
                    'border_width': 2,
                    'border_color': self.app_master.get_colors('dark_green')
                },
                'opacity': '#000001',
                'grid': {
                    'row': row,
                    'column': column,
                    'pady': (0, 30),
                    'sticky': 'nwes'
                }
            })
            column += 1

        row += 1
        self.app_master.adicionar_button(text='Carrinho', command=self.open_cart_view, options={
            'config': {
                'height': 50,
                'corner_radius': 32,
                'fg_color': self.app_master.get_colors('dark_gray'),
                'bg_color': '#000001',
                'border_width': 3,
                'border_color': self.app_master.get_colors('dark_green')
            },
            'opacity': '#000001',
            'grid': {
                'row': row,
                'column': 0,
                'pady': (40, 0),
                'sticky': 'nwes'
            }
        })

        self.app_master.adicionar_button(text='Sair', command=lambda: self.app_master.close(), options={
            'config': {
                'height': 50,
                    'corner_radius': 32,
                    'fg_color': self.app_master.get_colors('dark_gray'),
                    'bg_color': '#000001',
                    'border_width': 2,
                    'border_color': self.app_master.get_colors('dark_green')
            },
            'opacity': '#000001',
            'grid': {
                'row': row,
                'column': 2,
                'pady': (40, 0),
                'sticky': 'nwes'
            }
        })

        self.app_master.start()

    def open_cart_view(self):
        self.app_master.minimize()
        CartView(parent=self)

    def show_products(self, category_id: int):
        self.app_master.minimize()
        ProductsView(category_id=category_id, parent=self)
    
    def deiconify(self):
        self.app_master.deiconify()

if __name__ == '__main__':
    Restaurante()
