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
        #RELXY = altura (esquerdo > direito)
        #RELWIDTH = largura da tela
        #RELHEIGHT = altura da tela

        self.frame_2 = Frame(self.janela, bd=4, bg='light blue',
                             highlightbackground='white', highlightthickness=4)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def botoes_frame1(self):
        #botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar",
                                bd=3, bg='#20B2AA', fg='white')
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar",
                                bd=3, bg='#20B2AA', fg='white')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão novo
        self.bt_novo = Button(self.frame_1, text="Novo",
                              bd=3, bg='#20B2AA', fg='white')
        self.bt_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar",
                                 bd=3, bg='#20B2AA', fg='white')
        self.bt_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        #botão apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar",
                                bd=3, bg='#20B2AA', fg='white')
        self.bt_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
#label concurso
        self.lb_codigo = Label(self.frame_1, text="Mês",
                               bg = 'light blue', fg='white', font= 'bold')
        self.lb_codigo.place(relx= 0.25, rely= 0.65)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.25, rely= 0.75, relwidth= 0.1)
#label ano
        self.lb_ano = Label(self.frame_1, text="Concurso",
                            bg = 'light blue', fg='white', font= 'bold')
        self.lb_ano.place(relx=0.04, rely=0.35)
        self.ano_entry = Entry(self.frame_1)
        self.ano_entry.place(relx=0.05, rely=0.45, relwidth=0.1)

        self.lb_mes = Label(self.frame_1, text="Ano",
                            bg = 'light blue', fg='white', font= 'bold')
        self.lb_mes.place(relx=0.05, rely=0.65)
        self.mes_entry = Entry(self.frame_1)
        self.mes_entry.place(relx=0.05, rely=0.75, relwidth=0.1)
    def lista_frame2(self):
        #Treeview = tabelinha com rolagem
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Concurso")
        self.listaCli.heading("#2", text="Ano")
        self.listaCli.heading("#3", text="Mês")
        self.listaCli.heading("#4", text="1º")
        self.listaCli.heading("#5", text="2º")
        self.listaCli.heading("#6", text="3º")
        self.listaCli.heading("#7", text="4º")
        self.listaCli.heading("#8", text="5º")
        self.listaCli.heading("#9", text="6º")

    #tamanho
        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=20)
        self.listaCli.column("#2", width=10)
        self.listaCli.column("#3", width=10)
        self.listaCli.column("#4", width=10)
        self.listaCli.column("#5", width=10)
        self.listaCli.column("#6", width=10)
        self.listaCli.column("#7", width=10)
        self.listaCli.column("#8", width=10)
        self.listaCli.column("#9", width=10)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight= 0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


Aplication()