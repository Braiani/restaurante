from Main import Main
from Cart import Cart
from customtkinter import CTkToplevel
from PIL import Image
from tkinter import messagebox

class CartView(Main):
    def __init__(self, parent):
        surface = CTkToplevel()
        self.parent = parent
        super().__init__(janela=surface)
        self.cart = Cart(self.connector)
        self.janela.configure(fg_color=self.get_colors('black'))
        self.set_geometry(width=1920, height=1080, center=True, fullscreen=False)
        self.minsize_cols = (1920 - 350) // 5
        self.set_grid_column_weight(columns=4, options={'minsize': self.minsize_cols})
        self.set_icon()
        self.set_itens_screen()

    def set_itens_screen(self):
        joins = [{
            'table': 'products',
            'foreing_key': 'product_id',
            'primary_key': 'id'
        }]

        select = 'cart.id, cart.product_id, cart.quantity as quantidade, products.description as produto, products.price as preco'

        itens = self.cart.get_open_cart(join=joins, select_join=select)
        self.apply_background_image()

        frame_title = self.adicionar_frame(options={
            'config': {
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
        self.adicionar_label(text='Carrinho', master=frame_title, options={
            'config': {
                'font': ('Arial', 28),
            },
            'grid': {
                'padx': (50,50),
                'pady': (5,15)
            }
        })

        scrollable_frame = self.adicionar_frame(scrollable=True, options={
            'config': {
                'border_width': 2,
                'corner_radius': 32,
                'border_color': self.get_colors('medium_green'),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 1,
                'column': 0,
                'columnspan': 4,
                'padx': (50, 50),
                'pady': (5, 10),
                'sticky': 'nsew'
            }
        })

        scrollable_frame.grid_rowconfigure(0, weight=1)  # Permite que a primeira linha se expanda
        header_frame = self.adicionar_frame(master=scrollable_frame, options={
            'config': {
                'border_width': 2,
                'corner_radius': 0,
                'border_color': self.get_colors('medium_green'),
                'fg_color': self.get_colors('dark_gray'),
                'bg_color': self.get_colors('dark_gray'),
            },
            'grid': {
                'row': 0,
                'column': 0,
                'columnspan': 4,
                'sticky': 'ew'
            }
        })

        headers = ['Produto', 'Descrição', 'Preço', 'Quantidade', 'Ação']
        for index, header in enumerate(headers):
            padx = (0, self.minsize_cols)
            if index == 0:
                padx = (50, self.minsize_cols)
            elif index == 3:
                padx = (0, 150)
            elif index == 4:
                padx = (0, 0)
            self.adicionar_label(text=header, master=header_frame, options={
                'config': {
                    'font': ('Arial', 16, 'bold'),
                    'fg_color': 'transparent',
                    'bg_color': self.get_colors('dark_gray')
                },
                'grid': {
                    'row': 0,
                    'column': index,
                    'padx': padx,
                    'pady': (10, 10),
                    'sticky': 'nsew'
                }
            })
        row = 1

        if itens:
            for item in itens:
                img_file = f"{self.get_base_path()}/images/{item['produto']}.png"

                frame = self.adicionar_frame(master=scrollable_frame, options={
                    'config':{
                        'fg_color': 'transparent',
                        'bg_color': '#000001',
                    },
                    'grid': {
                        'row': row,
                        'column': 0,
                        'padx': (50, 50),
                        'pady': (10, 10),
                    }
                })

                self.adicionar_imagem(master=frame,image=Image.open(img_file), image_options={
                    'config': {
                        'size': (200, 200),
                    }
                }, label_options={
                    'config': {
                        'text': ''
                    },
                    'grid': {
                        'row': row,
                        'column': 0,
                        'pady': (5, 5),
                        'padx': (0, self.minsize_cols - 150),
                        'sticky': 'nwse'
                    }
                })

                self.adicionar_label(master=frame,text=f"{item['produto']}", options={
                    'config': {
                        'font': ('Arial', 16),
                        'fg_color': 'transparent'
                    },
                    'grid': {
                        'row': row,
                        'column': 1,
                        'pady': (5, 5),
                        'padx': (0, self.minsize_cols),
                        'sticky': 'nwse'
                    }
                })

                self.adicionar_label(master=frame, text=f"R$ {item['preco']:.2f}", options={
                    'config': {
                        'font': ('Arial', 16),
                        'fg_color': 'transparent'
                    },
                    'grid': {
                        'row': row,
                        'column': 2,
                        'pady': (5, 5),
                        'padx': (0, self.minsize_cols),
                        'sticky': 'nwse'
                    }
                })

                self.adicionar_label(master=frame, text=f"{item['quantidade']}", options={
                    'config': {
                        'font': ('Arial', 16),
                        'fg_color': 'transparent'
                    },
                    'grid': {
                        'row': row,
                        'column': 3,
                        'pady': (5, 5),
                        'padx': (0, 150),
                        'sticky': 'nwse'
                    }
                })

                trash_image = Image.open(f"{self.get_base_path()}/images/trash.png")
                self.adicionar_button(master=frame,text='Remover', command=self.create_remove_item_from_cart(item['id']), options={
                    'config': {
                        'corner_radius': 32,
                        'border_color': self.get_colors('medium_green'),
                        'border_width': 2,
                        'image': trash_image,
                    },
                    'grid': {
                        'row' :row,
                        'column': 4,
                        'pady': (5, 5),
                        'padx': (0, 0),
                        'sticky': 'w'
                    }
                })
                row += 1

            for row in range(len(itens)):
                scrollable_frame.grid_rowconfigure(row, weight=1)


        self.janela.grid_rowconfigure(1, weight=1)
        for column in range(len(headers)):
            self.janela.grid_columnconfigure(column, weight=1)

        back_image = Image.open(f"{self.get_base_path()}/images/back.png")
        self.adicionar_button(text='Voltar', command=lambda: self.close_windows(), options={
            'config': {
                'height': 50,
                'corner_radius': 32,
                'fg_color': 'transparent',
                'border_color': self.get_colors('medium_green'),
                'border_width': 2,
                'image': back_image,
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 2,
                'column': 0,
                'pady': (20, 20),
                'sticky': 'w'
            }
        })
        self.adicionar_button(text='Fechar Conta', command=lambda: self.fechar_conta(), options={
            'config': {
                'height': 50,
                'corner_radius': 32,
                'fg_color': 'transparent',
                'border_color': self.get_colors('medium_green'),
                'border_width': 2,
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 2,
                'column': 3,
                'pady': (20, 20),
                'sticky': 'e'
            }
        })

    def create_remove_item_from_cart(self, cart_id):
        def function():
            self.remove_item_from_cart(cart_id=cart_id)

        return function

    def remove_item_from_cart(self, cart_id):
        response = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja excluir esse item?")
        if not response:
            messagebox.showinfo('Informação', 'Operação cancelada')
            return
        try:
            self.cart.remove_item(cart_id)
            messagebox.showinfo('Sucesso', 'Item removido com sucesso')
            self.refresh_screen()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao remover item: {e}')

    def refresh_screen(self):
        self.janela.destroy()
        self.__init__(parent=self.parent)

    def fechar_conta(self):
        total = self.cart.get_total()

        if total == 0 or total is None or total == '' or total == False:
            messagebox.showerror('Erro', 'Não é possível fechar uma conta sem itens')
            return

        response = messagebox.askyesno("Confirmação", f"Você tem certeza de que deseja fechar a conta no valor de R$ {total:.2f}?")
        if not response:
            messagebox.showinfo('Informação', 'Operação cancelada')
            return
        try:
            self.cart.finish_cart()
            messagebox.showinfo('Sucesso', f"Conta fechada com sucesso \n O valor total é de R$ {total:.2f}")
            self.close_windows()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao fechar conta: {e}')

    def close_windows(self):
        self.janela.destroy()
        self.parent.deiconify()

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()