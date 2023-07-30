from tkinter import *
from tkinter import simpledialog
from baloes import baloes
import requisicoes as call
import math
import time
import threading
from tkinter import messagebox

root = Tk()

root.geometry("700x700")
root.title("Gerenciamento")

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)


scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Cria um Frame para conter todos os widgets
main_frame = Frame(canvas)
canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Vincula a barra de rolagem ao Frame



frame = {}


def entregar_balao(frame, balao_frame, father_frame1, father_frame2, quantidade, cores, sem_baloes_adquiridos):
    if len(cores) > 0:
        call.baloes_pendentes[frame.valor1][cores[0]] = False
        call.Baloes_adquiridos[frame.valor1][cores.pop(0)] = True
        
    update_info(frame, balao_frame, father_frame1, father_frame2, quantidade, sem_baloes_adquiridos)

   
def update_info(frame, balao_frame, father_frame1, father_frame2, quantidade, sem_baloes_adquiridos):
    for i in range (0, len(balao_frame)):
        balao_frame[i].destroy()

    if sem_baloes_adquiridos != 0:
        sem_baloes_adquiridos.destroy()
    
    tem_balao = False
    for i in range(0,call.Quantidade_de_exercicios):
        if call.baloes_pendentes[frame.valor1][call.baloes[i]]:
            tem_balao = True
            quantidade += 1
            x = Frame(master=father_frame1,relief=RAISED, borderwidth=2,width=25, height=25, bg = baloes[call.baloes[i]])
            balao_frame.append(x)
            x.grid(row=0, column=i, padx=5, pady=5, sticky="w")
    if not(tem_balao):
       frame['highlightbackground'] = 'black'
       sem_baloes_pendentes = Label(master=father_frame1, text="Sem balões pendentes", bg="white", font = ("Arial", 12))
       sem_baloes_pendentes.grid(row = 0, column=0,pady=10,sticky="s")
      

    for i in range(0,call.Quantidade_de_exercicios):
        if call.Baloes_adquiridos[frame.valor1][call.baloes[i]]:
            balao_frame = Frame(master=father_frame2,relief=RAISED, borderwidth=2,width=25, height=25, bg = baloes[call.baloes[i]])
            balao_frame.grid(row=0, column=i, padx=5, pady=5, sticky="w")
    


def info(frame):
   student_screen = Tk()
   student_screen.title(frame.valor1)
   student_screen.geometry("450x450")
   student_screen.config(bg = "lightblue")

   info_frame = Frame(master=student_screen, relief=RAISED, borderwidth=2,width=450, height=50, bg = "white")
   info_frame.grid(row = 0, column=0, padx=10, pady=10, sticky="ew")
   info_frame.pack_propagate(0)

   Nome_text = Label(master=info_frame, text="Nome", bg = "white", font=("Arial", 18))
   Nome_text.grid(row = 0, column= 0, padx= 5, sticky="w")

   equal_sign = Label(master=info_frame, text="=", bg = "white", font=("Arial", 18))
   equal_sign.grid(row = 0, column=1, padx=5, sticky="w")

   Nome = Label(master=info_frame, text=frame.valor1, bg = "white",  font=("Arial", 18))
   Nome.grid(row=0, column=2, padx=5, sticky="w")

   Numero_text = Label(master=info_frame, text="Número", bg = "white", font=("Arial", 18))
   Numero_text.grid(row = 1, column= 0, padx=5, pady=10, sticky="w")

   equal_sign2 = Label(master=info_frame, text="=", bg = "white", font=("Arial", 18))
   equal_sign2.grid(row = 1, column=1, padx=5, sticky="w")


   Numero = Label(master=info_frame, text=frame.valor2, bg = "white", font=("Arial", 18))
   Numero.grid(row=1, column=2, padx=5, sticky="w")


   info_baloons_text = Frame(master=student_screen, relief=RAISED, borderwidth=2,width=450, height=300, bg = "white")
   info_baloons_text.grid(row = 1, column=0, padx=10, pady=10, sticky="ew")
   info_baloons_text.pack_propagate(0)

   baloes_pendentes_text = Label(master=info_baloons_text,text="Balões Pendentes", bg = "white", font=("Arial", 18))
   baloes_pendentes_text.grid(row = 0, column=0, padx=5,pady=5, sticky="ew")

   info_baloons_pendentes = Frame(master=student_screen, relief=RAISED, borderwidth=2,width=450, height=300, bg = "white")
   info_baloons_pendentes.grid(row=2, column=0, padx=10, sticky="ew")
   
   balao_dependente_frame = []
   tem_balao = False
   Quantidade_de_balao_pendente = 0
   Cores_pendentes = []
   
   i = -1
   for balao in call.baloes:
        if call.baloes_pendentes[frame.valor1][balao] == True:
            i += 1
            tem_balao = True
            Quantidade_de_balao_pendente += 1
            x = Frame(master=info_baloons_pendentes,relief=RAISED, borderwidth=2,width=25, height=25, bg = baloes[balao])
            Cores_pendentes.append(balao)
            balao_dependente_frame.append(x)
            x.grid(row=0, column=i, padx=5, pady=5, sticky="w")
   if not(tem_balao):
       sem_baloes_pendentes = Label(master=info_baloons_pendentes, text="Sem balões pendentes", bg="white", font = ("Arial", 12))
       sem_baloes_pendentes.grid(row = 0, column=0,pady=10,sticky="s")

   print(len(balao_dependente_frame))

   info_baloons_adquiridos_text = Frame(master=student_screen, relief=RAISED, borderwidth=2,width=450, height=300, bg = "white")
   info_baloons_adquiridos_text.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
   info_baloons_adquiridos_text.pack_propagate(0)

   baloes_adquiridos_text = Label(master=info_baloons_adquiridos_text,text="Balões Adquiridos", bg = "white", font=("Arial", 18))
   baloes_adquiridos_text.grid(row=0, column=0, padx=10, sticky="ew", pady=10)
                
   info_baloes_adquiridos = Frame(master=student_screen, relief=RAISED, borderwidth=2,width=450, height=300, bg = "white")
   info_baloes_adquiridos.grid(row=4, column=0, padx=10, sticky="ew")

   tem_balao = False
   i = -1
   for balao in call.baloes:
        if call.Baloes_adquiridos[frame.valor1][balao]:
            i += 1
            tem_balao = True
            balao_frame = Frame(master=info_baloes_adquiridos,relief=RAISED, borderwidth=2,width=25, height=25, bg = baloes[balao])
            balao_frame.grid(row=0, column=i, padx=5, pady=5, sticky="w")

   sem_baloes_adquiridos = 0
   if not(tem_balao):
       sem_baloes_adquiridos = Label(master=info_baloes_adquiridos, text="Sem balões adquiridos", bg="white", font = ("Arial", 12))
       sem_baloes_adquiridos.grid(row=0, column=0, pady=10, sticky="s")
   
   btn = Button(master=student_screen, text="Entregar Balão", width=10, height=2, command=lambda f=frame, b=balao_dependente_frame, j = info_baloons_pendentes, k = info_baloes_adquiridos, q = Quantidade_de_balao_pendente, p = Cores_pendentes, s = sem_baloes_adquiridos: entregar_balao(f,b,j, k, q, p,s))
   btn.grid(row = 5, column=0, padx=50, pady=10, sticky="s")

        
   student_screen.mainloop()    


def update_screen():
    global frame
    time.sleep(1)
    print("estou sendo chamado")
    for nome in call.Nome_dos_alunos:
        for balao in call.baloes:
            if call.baloes_pendentes[nome][balao] == True:
                frame[nome]['highlightbackground'] = 'red'
                


def call_update_screen():
    while not(parar):
        update_screen()
        time.sleep(2)
               
def ao_fechar_janela():
    global parar
    senha_inserida = simpledialog.askstring("Senha", "Digite a senha:", show='*')
    senha_correta = "inatel2023"  # Substitua pela senha correta
    if senha_inserida == senha_correta:
        call.parar = True
        parar = True
        thread.join()
        root.destroy()  # Fechar a janela se a senha estiver correta
    else:
        messagebox.showerror("Erro", "Senha incorreta. Fechamento cancelado.")


def main_screen():

   
    root.protocol("WM_DELETE_WINDOW", ao_fechar_janela)

    
    Tamanho_matriz = math.sqrt(call.Total_de_competidores)
    index = 0
    if int(Tamanho_matriz) < Tamanho_matriz:
        Tamanho_matriz = Tamanho_matriz + 1

    Tamanho_matriz = int(Tamanho_matriz)
    for i in range(Tamanho_matriz):
     for j in range(Tamanho_matriz):
        if index == call.Total_de_competidores:
            break

        nome = call.Nome_dos_alunos[index]
        frame[nome] = Frame(master = main_frame, relief = RAISED, borderwidth=2, width=200, height=200, bg="white")
        frame[nome]['highlightbackground'] = 'black'  # Substitua 'red' pela cor desejada
        frame[nome]['highlightthickness'] = 5
        frame[nome].grid(row = i, column=j, padx = 5, pady = 5)
        frame[nome].pack_propagate(0)
        frame[nome].valor1 = nome
        frame[nome].valor2 = "Número de identificação"
        label1 = Label(master=frame[nome], text=call.Nome_dos_alunos[index])
        label1.pack(pady=10)  
        label2 = Label(master=frame[nome], text = "Número de identificação")
        label2.pack(pady=10)
        index = index + 1
        btn = Button(master = frame[nome], text = "Check", width=10, height=2, command=lambda f=frame[nome]: info(f))
        btn.pack(pady=60)
        btn.place(x = 55, y = 140)

    main_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
    root.mainloop()

thread = threading.Thread(target=call_update_screen)
parar = False
thread.start()
main_screen()

