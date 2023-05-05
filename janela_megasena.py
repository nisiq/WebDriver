from tkinter import *
from tkinter import ttk

janela = Tk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.botoes_frame1()
        self.lista_frame2()
        janela.mainloop() #manter janela
    def tela(self):
        self.janela.title("MEGA-SENA")
        self.janela.configure(background= 'light blue') #cor de fundo da minha tela
        self.janela.geometry("600x550") #tamanho da minha tela
        #responsivo
        self.janela.resizable(True, True ) #permitir que mexa no tamanho da tela
        self.janela.maxsize(width=900, height=700)  #maximo que quero da minha tela (largura/altura)
        self.janela.minsize(width=300, height=200) #minimo que irei permitir
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd= 4, bg= 'light blue',
                             highlightbackground='white', highlightthickness= 4)
        #bd =          bg = background highlightback = cor da borda do frame / highlighttth = largura da borda
        #place = posição especifica/fica estático
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        #RELX = largura (esquerdo > direito)
        #RELXY = altura
        #RELWIDTH = largura da tela
        #RELHEIGHT = altura da tela

        self.frame_2 = Frame(self.janela, bd=4, bg='light blue',
                             highlightbackground='white', highlightthickness=4)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def botoes_frame1(self):
        #botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar",
                                bd=3, bg='#20B2AA', fg='white')
        self.bt_buscar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão novo
        self.bt_novo = Button(self.frame_1, text="Novo",
                              bd=3, bg='#20B2AA', fg='white')
        self.bt_novo.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #botão apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar",
                                bd=3, bg='#20B2AA', fg='white')
        self.bt_apagar.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.15)
#label N1
        self.lb_codigo = Label(self.frame_1, text="N1",
                               bg = 'light blue', fg='white', font= 'bold')
        self.lb_codigo.place(relx= 0.10, rely= 0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.07, rely= 0.55, relwidth= 0.1, relheight=0.10)
# label N2
        self.lb_codigo = Label(self.frame_1, text="N2",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.25, rely=0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.22, rely=0.55, relwidth=0.1, relheight=0.10)
# label N3
        self.lb_codigo = Label(self.frame_1, text="N3",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.40, rely=0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.37, rely=0.55, relwidth=0.1, relheight=0.10)
# label N4
        self.lb_codigo = Label(self.frame_1, text="N4",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.55, rely=0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.52, rely=0.55, relwidth=0.1, relheight=0.10)
# label N5
        self.lb_codigo = Label(self.frame_1, text="N5",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.70, rely=0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.67, rely=0.55, relwidth=0.1, relheight=0.10)
# label N6
        self.lb_codigo = Label(self.frame_1, text="N6",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.85, rely=0.45)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.82, rely=0.55, relwidth=0.1, relheight=0.10)


    def lista_frame2(self):
        self.lb_codigo = Label(self.frame_2, text="O seu jogo deu:",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.38, rely=0.25)
        self.codigo_entry = Entry(self.frame_2)
        self.codigo_entry.place(relx=0.38, rely=0.35, relwidth=0.2, relheight=0.20)

        self.lb_codigo = Label(self.frame_2, text="DUQUES | TERNOS | QUADRAS | QUINAS | MEGAS",
                               bg='light blue', fg='white', font='bold')
        self.lb_codigo.place(relx=0.18, rely=0.65)





Aplication()