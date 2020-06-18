import tkinter as tk
import locale
from locale import atof

class TelaCalculadora:
    def __init__(self, master):
        self.telaCalculadora = master
        self.telaCalculadora.title('Tela da Calculadora - Versão 1.0')
        self.telaCalculadora.geometry('400x300')

        self.frm1 = tk.Frame(self.telaCalculadora, bg = 'blue')
        self.frm2 = tk.Frame(self.telaCalculadora, bg = 'blue')
        self.frm3 = tk.Frame(self.telaCalculadora, bg = 'blue')
        self.frm4 = tk.Frame(self.telaCalculadora, bg = 'blue')
        self.frm5 = tk.Frame(self.telaCalculadora, bg = 'blue')
        self.frm6 = tk.Frame(self.telaCalculadora, bg = 'blue')

        self.frm1.pack()
        self.frm2.pack()
        self.frm3.pack()
        self.frm4.pack()
        self.frm5.pack()
        self.frm6.pack()

        self.lbl_num1 = tk.Label(self.frm1, text = '1.º Valor', bg = 'blue', font = ('verdana', '9', 'bold'), foreground = 'white')
        self.lbl_num1.pack(side = tk.LEFT, padx = 10, pady = 10)
        self.txt_num1 = tk.Entry(self.frm1, width = 20)
        self.txt_num1.pack(side = tk.LEFT)

        self.lbl_num2 = tk.Label(self.frm2, text = '2.º Valor', bg = 'blue', font = ('verdana', '9', 'bold'), foreground = 'white')
        self.lbl_num2.pack(side = tk.LEFT, padx = 10, pady = 10)
        self.txt_num2 = tk.Entry(self.frm2, width = 20)
        self.txt_num2.pack(side = tk.LEFT)

        self.lbl_res = tk.Label(self.frm3, text = 'Resultado', bg = 'blue', font = ('verdana', '9', 'bold'), foreground = 'white')
        self.lbl_res.pack(side = tk.LEFT, padx = 10, pady = 10)
        self.txt_res = tk.Entry(self.frm3, width = 20, textvariable = var)
        self.txt_res.pack(side = tk.LEFT)

        self.btn_soma = tk.Button(self.frm4, text = 'SOMAR', width = 15, bg = 'white', font = ('verdana', '10', 'bold'), foreground = 'black', command = self.calculaSoma)
        self.btn_soma.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.btn_sub = tk.Button(self.frm4, text = 'SUBTRAÇÃO', width = 15, bg = 'white', font = ('verdana', '10', 'bold'), foreground = 'black', command = self.calculaSubtracao)
        self.btn_sub.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.btn_mult = tk.Button(self.frm5, text = 'MULTIPLICAÇÃO', width = 15, bg = 'white', font = ('verdana', '10', 'bold'), foreground = 'black', command = self.calculaMultiplicacao)
        self.btn_mult.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.btn_div = tk.Button(self.frm5, text = 'DIVISÃO', width = 15, bg = 'white', font = ('verdana', '10', 'bold'), foreground = 'black', command = self.calculaDivisâo)
        self.btn_div.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.btn_sair = tk.Button(self.frm6, text = 'SAIR', width = 15, bg = 'white', font = ('verdana', '10', 'bold'), foreground = 'black', command = self.sair)
        self.btn_sair.pack(side = tk.LEFT, padx = 10, pady = 10)


    def calculaSoma(self):
        n1 = float(self.txt_num1.get())
        var.set(n1+atof(self.txt_num2.get()))

    def calculaSubtracao(self):
        n1 = float(self.txt_num1.get())
        var.set(n1-atof(self.txt_num2.get()))

    def calculaMultiplicacao(self):
        n1 = float(self.txt_num1.get())
        var.set(n1*atof(self.txt_num2.get()))

    def calculaDivisâo(self):
        n1 = float(self.txt_num1.get())
        var.set(n1/atof(self.txt_num2.get()))

    def sair(self):
        self.telaCalculadora.destroy()


janela = tk.Tk()
var = tk.StringVar()
TelaCalculadora(janela)
janela.configure(bg = 'blue')
janela.mainloop()