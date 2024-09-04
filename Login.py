import customtkinter as ctk
from tkinter import messagebox
from Usuarios import Usuarios
from Main import Main
import pywinstyles

class Login(Main):
    def __init__(self, janela: ctk.CTk):
        super().__init__(janela=janela)
        self.set_geometry(800, 600, True)
        self.set_title('Login')
        self.set_grid_column_weight(columns=1, weight=3)
        self.entradas = []
        self.logado = False
        self.usuario = None
        self.set_itens_screen()

    def set_itens_screen(self):
        login_image = f"{self.get_base_path()}/images/Login.png"
        self.adicionar_label_image(filename=login_image, text='', options={
            'config': {
                'size': (800,600)
            },
            'blur': 6,
            'background': True,
            'place': {
                'x': 0,
                'y': 0
            }
        })

        self.adicionar_label(text='Usuário', options={
            'config': {
                'font': ('Arial', 16),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 0,
                'column': 0,
                'padx': (60, 0),
                'pady': (60, 0),
            }
        })
        usuario = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200,
                'bg_color': '#000001',
                'border_color': self.get_colors('medium_green'),
            },
            'opacity': '#000001',
            'grid': {
                'row': 1,
                'column': 0,
                'padx': (60, 0),
                'pady': (5, 0)
            }
        })
        self.entradas.append(usuario)

        self.adicionar_label(text='Senha', options={
            'config': {
                'font': ('Arial', 16),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 2,
                'column': 0,
                'padx': (60, 0),
                'pady': (10, 0)
            }
        })

        senha = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200,
                'show': '*',
                'bg_color': '#000001',
                'border_color': self.get_colors('medium_green'),
            },
            'opacity': '#000001',
            'grid': {
                'row': 3,
                'column': 0,
                'padx': (60, 0),
                'pady': (5, 0)
            }
        })

        self.entradas.append(senha)

        self.adicionar_label(text='Confirmar Senha', options={
            'config': {
                'font': ('Arial', 16),
                'bg_color': '#000001',
            },
            'opacity': '#000001',
            'grid': {
                'row': 4,
                'column': 0,
                'padx': (60, 0),
                'pady': (10, 0)
            }
        })

        conf_senha = self.adicionar_entry(options={
            'config': {
                'corner_radius': 25,
                'height': 30,
                'width': 200,
                'show': '*',
                'bg_color': '#000001',
                'border_color': self.get_colors('medium_green'),
            },
            'opacity': '#000001',
            'grid': {
                'row': 5,
                'column': 0,
                'padx': (60, 0),
                'pady': (5, 0)
            }
        })

        self.entradas.append(conf_senha)

        self.adicionar_button(text='Entrar', command=lambda: self.validar_login(), options={
            'config': {
                'height': 50,
                'corner_radius': 32,
                'fg_color': self.get_colors('dark_gray'),
                'bg_color': '#000001',
                'border_width': 2,
                'border_color': self.get_colors('medium_green'),
            },
            'opacity': '#000001',
            'grid': {
                'row': 6,
                'column': 0,
                'padx': (60, 0),
                'pady': (20, 0)
            }
        })

    def get_logado(self):
        if self.logado:
            return self.usuario
        
        return False

    def validar_login(self):
        usuario = self.entradas[0].get()
        senha = self.entradas[1].get()
        confirmar_senha = self.entradas[2].get()

        if not usuario or not senha:
            messagebox.showerror('Erro', 'Usuário e senha são obrigatórios')
            return
        
        if usuario == senha:
            messagebox.showerror('Erro', 'Usuário e senha não podem coincidir')
            return
        
        if senha != confirmar_senha:
            messagebox.showerror('Erro', 'Senhas não coincidem!')
            return

        usuarios = Usuarios(usuario, senha, self.connector)
        result = usuarios.validar_login()

        if result:
            messagebox.showinfo('Sucesso', "Login Realizado com sucesso!")
            self.janela.destroy()
            self.logado = True
            self.usuario = result[0]
            return

        messagebox.showerror('Erro', 'Credenciais inválidas!')

if __name__ == '__main__':
    from Restaurante import Restaurante
    Restaurante()