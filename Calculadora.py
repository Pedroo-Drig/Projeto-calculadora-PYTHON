from tkinter import *
from tkinter import ttk

#cores
preto = '#3b3b3b'
branco = '#feffff'
azul = '#38576b'
cinzenta = '#ECEFF1'
laranja = '#FFAB40'


janela = Tk()
janela.title("Calculadora")
janela.geometry("320x410")
janela.iconphoto(False, PhotoImage(file='python.png'))

#frames
frame_tela = Frame(janela, width=320, height=60, bg=azul)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=320 , height=368)
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todos_valores = ''

valor_texto = StringVar()

#função
def entrar_valores(event):

    global todos_valores

    if event in ['%','/','*','-','+','.']:
        if todos_valores == '':
            return
        elif todos_valores[-1] in ['%','/','*','-','+','.']:
            todos_valores = todos_valores.rsplit(todos_valores[-1], 1)[0] + event
            valor_texto.set(todos_valores)

        else:
            todos_valores = todos_valores + str(event)
            valor_texto.set(todos_valores)

    else:
        todos_valores = todos_valores + str(event)
        valor_texto.set(todos_valores)


    

def calcular():
    global resultado
    global todos_valores

    if todos_valores[-1] in ['%','/','*','-','+','.']:
        todos_valores = todos_valores.rsplit(todos_valores[-1],1)[0]

    resultado = eval(todos_valores)
    todos_valores = str(resultado)
    valor_texto.set(resultado)

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#label
app_label = Label(frame_tela, textvariable= valor_texto, width=21, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=azul, fg=branco)
app_label.place(x=8, y=0)

#botões
b_1 = Button(frame_corpo, command = lambda: limpar_tela(),text="C", width=15, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'),text="%", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=160, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'),text="/", width=7, height=3, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=240, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'),text="7", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=70)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'),text="8", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=80, y=70)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'),text="9", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=160, y=70)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'),text="*", width=7, height=3, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=240, y=70)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'),text="4", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=140)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'),text="5", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=80, y=140)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'),text="6", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=160, y=140)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'),text="-", width=7, height=3, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=240, y=140)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'),text="1", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=210)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'),text="2", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=80, y=210)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'),text="3", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=160, y=210)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'),text="+", width=7, height=3, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=240, y=210)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'),text="0", width=15, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=280)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'),text=".", width=7, height=3, bg=cinzenta, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=160, y=280)
b_18 = Button(frame_corpo, command = lambda: calcular(),text="=", width=7, height=3, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=240, y=280)

janela.mainloop()