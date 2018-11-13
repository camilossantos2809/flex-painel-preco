import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


CONFIG = {}


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title('painel_precos (CONFIG)')
        self.pack(fill=tk.BOTH, expand=0)

        self['borderwidth'] = 10

        self.frame_flex = ttk.Labelframe(self, text="Banco de dados - Flex")
        self.frame_flex['padding'] = (5, 5)
        self.frame_flex['borderwidth'] = 2
        self.frame_flex['relief'] = 'sunken'
        self.frame_flex.grid(column=0, row=0, padx=10)

        self.lbl_flex_ip = tk.Label(self.frame_flex, text="IP")
        self.lbl_flex_ip.grid(column=0, row=0)
        self.txt_flex_ip = tk.Entry(self.frame_flex, width=20)
        self.txt_flex_ip.grid(column=1, row=0, sticky='W', pady=5)

        self.lbl_flex_porta = tk.Label(self.frame_flex, text="Porta")
        self.lbl_flex_porta.grid(column=0, row=1)
        self.txt_flex_porta = tk.Entry(self.frame_flex, width=20)
        self.txt_flex_porta.grid(column=1, row=1, sticky='W', pady=5)

        self.lbl_flex_database = tk.Label(
            self.frame_flex, text="Nome Database")
        self.lbl_flex_database.grid(column=0, row=2)
        self.txt_flex_database = tk.Entry(self.frame_flex, width=20)
        self.txt_flex_database.grid(column=1, row=2, sticky='W', pady=5)

        self.lbl_flex_user = tk.Label(self.frame_flex, text="Usuário")
        self.lbl_flex_user.grid(column=0, row=3)
        self.txt_flex_user = tk.Entry(self.frame_flex, width=20)
        self.txt_flex_user.grid(column=1, row=3, sticky='W', pady=5)

        self.lbl_flex_password = tk.Label(self.frame_flex, text="Senha")
        self.lbl_flex_password.grid(column=0, row=4)
        self.txt_flex_password = tk.Entry(self.frame_flex, width=20, show='*')
        self.txt_flex_password.grid(column=1, row=4, sticky='W', pady=5)

        self.frame_actions = tk.Frame(self)
        self.frame_actions.grid(column=0, row=1, sticky='N,W', pady=5)
        self.button_gravar = tk.Button(
            self.frame_actions, text="Gravar", command=self.set_data_into_json)
        self.button_gravar.grid(column=0, row=1, sticky='N,W', pady=5)

        self.get_data_from_json()

    def get_data_from_json(self):
        if os.path.exists('config.json'):
            with open('config.json') as file:
                CONFIG = json.load(file)
            self.txt_flex_ip.insert(0, CONFIG['flex']['ip'])
            self.txt_flex_porta.insert(0, CONFIG['flex']['port'])
            self.txt_flex_database.insert(0, CONFIG['flex']['databasename'])
            self.txt_flex_user.insert(0, CONFIG['flex']['username'])
            self.txt_flex_password.insert(0, CONFIG['flex']['password'])

    def set_data_into_json(self):
        CONFIG['flex'] = {}
        CONFIG['flex']['ip'] = self.txt_flex_ip.get()
        CONFIG['flex']['port'] = self.txt_flex_porta.get()
        CONFIG['flex']['databasename'] = self.txt_flex_database.get()
        CONFIG['flex']['username'] = self.txt_flex_user.get()
        CONFIG['flex']['password'] = self.txt_flex_password.get()

        with open('config.json', 'w') as file:
            json.dump(CONFIG, file)

        messagebox.showinfo(
            "Gravação concluída!",
            "Gravação das configurações concluída!\n\nReinicie o serviço da API para aplicação das novas configurações"
        )


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('350x300')

    style = ttk.Style()
    style.theme_use('clam')

    app = MainWindow(root)
    root.mainloop()
