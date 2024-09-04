import customtkinter as ctk
from Main import Main
from Cart import Cart
from customtkinter import CTkToplevel
from Produtos import Produtos
from PIL import Image
from tkinter import messagebox

class ProductsView(Main):
    def __init__(self, category_id: int, parent):
        surface = CTkToplevel()
        self.category_id = category_id
        self.parent = parent
        super().__init__(janela=surface)
        self.janela.configure(fg_color=self.get_colors('black'))
        self.set_geometry(width=1200, height=800, center=True, fullscreen=True)
        self.set_grid_column_weight(columns=5, weight=1)
        self.set_row_configure(rows=10, weight=1)
        self.set_icon()
        self.set_itens_screen()
    

    def set_itens_screen(self):
        prod = Produtos(self.connector)
        joins = [{
            'table': 'categories',
            'foreing_key': 'category_id',
            'primary_key': 'id'
        }]

        select_join = 'products.id, products.description as produto, products.price as preco, products.image as image, categories.description as categoria'

        produtos = prod.get_all_by_category(category=self.category_id, join=joins, select_join=select_join)

        self.apply_background_image()


        frame_title = self.adicionar_frame(options={
            'config': {
                'width': 100,
                'height': 50,
                'border_width': 2,
                'corner_radius': 32,
                'border_color': self.get_colors('medium_green'),
                'fg_color': self.get_colors('dark_gray'),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 0,
                'column': 0,
                'columnspan': 5,
                'pady': (10, 5)
            }
        })

        self.adicionar_label(text=self.title, master=frame_title, options={
            'config': {
                'font': ('Arial', 32),
                'fg_color': 'transparent'
            },
            'grid': {
                'padx': (50, 50),
                'pady': (10, 5)
            }
        })
        self.adicionar_label(text=f'Produtos da Categoria {produtos[0]["categoria"]}', master=frame_title, options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'padx': (50,50),
                'pady': (5,10)
            }
        })
        
        row = 2
        column = 0
        for produto in produtos:
            if column == 5:
                column = 0
                row += 1

            text = f"{produto['produto']} - R$ {produto['preco']:.2f}"
            img_file = f"{self.get_base_path()}/images/{produto['produto']}.png"
            img = Image.open(img_file)

            frame = self.adicionar_frame(options={
                'config':{
                    'border_width': 2,
                    'corner_radius': 10,
                    'border_color': self.get_colors('medium_green'),
                    'fg_color': self.get_colors('dark_gray'),
                    'bg_color': '#000001'
                },
                'opacity': '#000001',
                'grid': {
                    'row': row,
                    'column': column,
                    'padx': (30, 30),
                    'pady': (30, 30)
                }
            })


            self.adicionar_imagem(master=frame, image=img, image_options={
                'config': {
                    'size': (200, 200),
                }
            }, label_options={
                'config': {
                    'text': ''
                },
                'grid': {
                    'row': 0,
                    'column': 0,
                    'pady': (30,0)
                }
            })

            self.adicionar_label(master=frame, text=text, options={
                'config': {
                    'font': ('Arial', 16),
                    'fg_color': 'transparent'
                },
                'grid': {
                    'row': 1,
                    'column': 0,
                    'pady': (15,0)
                }
            })
            
            cart_image = Image.open(f"{self.get_base_path()}/images/cart.png")
            self.adicionar_button(master=frame, text='Adicionar ao Carrinho', command=self.create_add_product_to_cart(produto['id']), options={
                'config': {
                    'corner_radius': 32,
                    'fg_color': 'transparent',
                    'border_width': 2,
                    'border_color': self.get_colors('medium_green'),
                    'image': cart_image
                },
                'grid': {
                    'row': 2,
                    'column': 0,
                    'pady': (15,15)
                }
            })

            column += 1

        back_image = Image.open(f"{self.get_base_path()}/images/back.png")
        self.adicionar_button(text='Voltar', command=lambda: self.close_windows(), options={
            'config': {
                'corner_radius': 32,
                'fg_color': 'transparent',
                'bg_color': '#000001',
                'border_color': self.get_colors('medium_green'),
                'border_width': 2,
                'image': back_image
            },
            'opacity': '#000001',
            'grid': {
                'row': row + 1,
                'column': 0,
                'pady': (20, 20)
            }
        })
    
    def create_add_product_to_cart(self, product_id):
        def function():
            self.add_item_to_cart(product_id=product_id)

        return function

    def add_item_to_cart(self, product_id):
        cart = Cart(self.connector)
        dialog = ctk.CTkInputDialog(text="Digite a quantidade:", title="Quantidade")
        quantity = dialog.get_input()
        print(quantity)
        if quantity is None:
            messagebox.showwarning(title="Atenção", message="Produto não adicionado!")
            return
        try:
            add_cart = cart.add_item(product_id=product_id, quantity=quantity)
            if add_cart:
                messagebox.showinfo('Sucesso', 'Produto adicionado ao carrinho!')
            else:
                messagebox.showerror('Erro', 'Erro ao adicionar item ao carrinho!')
        except Exception as e:
            print(f"Erro ao adicionar item ao carrinho: {e}")

    def close_windows(self):
        self.janela.destroy()
        self.parent.deiconify()

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()