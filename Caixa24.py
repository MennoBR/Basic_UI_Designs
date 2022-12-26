from tkinter import *
import time

root = Tk()
root.geometry("500x500")
root.title('BANCO 24 HORAS')
root.configure(bg ="grey")

Tops = Frame(root, bg="red", width=500, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, bg="black", width=300, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg="white", width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lb11 = Label(Tops, font=('aria',30,'bold'), text="BANCO 24 HORAS", fg="red", bg="white", bd=10, anchor='w')
lb11.grid(row=0, column=0)
lb12 = Label(Tops, font=('aria',20,'bold'), text=localtime, fg="black", bg="white", bd=10, anchor='w')
lb12.grid(row=1, column=0)

number = StringVar()
amount = StringVar()
withd = StringVar()
acca = " "

def bank():
    global acca
    accno = ["0009879", "0001234", "0009829", "2030456"]
    account = number.get()
    if account in accno:
        Label.config(text="Usuário Registrado")
        bank = {"0009879":10000, "0001234":20000, "0009829":30000}
        balance = bank[account]
        acca = balance
    else:
        Label.config(text="Usuário Não Registrado")


def deposit():
    global acca
    amo = float(amount.get())
    bal = acca+amo
    label3.config(text=("Saldo Total:",str(bal)))


def withdrawn():
    global acca
    wd = float(withd.get())
    if acca>=wd:
        ace = acca-wd
        label4.config(text=("Saldo Total :",str(ace)))
    else:
        label4.config(text="Saldo Insuficiente")

def bal():
    global acca
    label5.config(text=("Saldo Total",str(acca)))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")


lbl = Label(f1, font=('aria' ,16, 'bold'),text="Número da Conta:              ", bg = "black",fg="white",bd=10,anchor='w')
lbl.grid(row=0, column=3)
txt = Entry(f1,font=('aria',16, 'bold'), textvariable=number, bd=6, insertwidth=4, bg="white" ,justify='right')
txt.grid(row=0, column=4)
btnsubmit = Button(f2, padx=16, pady=4, bd=10 , fg="black", font=('aria', 16, 'bold'), width=7, text="ENTRAR", bg="white", command=bank)
btnsubmit.grid(row=0, column=4)

lblTotal = Label(f1, text="             ", fg="white", bg="black")
lblTotal.grid(row=3, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Digite o valor a ser depositado: ", fg="white", bg = "black", bd=10, anchor='w')
lbl.grid(row=4, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=amount , bd=6,insertwidth=4, bg="white", justify='right')
txt.grid(row=4, column=4)
label3 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label3.grid(row=5, column=4)
btndeposit = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="DEPÓSITO", bg="white", command=deposit)
btndeposit.grid(row=4, column=4)

lblTotal = Label(f1, text="            ", fg="white", bg="black")
lblTotal.grid(row=7, columnspan=10)

lbl = Label(f1, font=('aria', 16, 'bold'), text="Digite o valor a ser sacado: ", fg="white", bg = "black", bd=10, anchor='w')
lbl.grid(row=8, column=3)
txt = Entry(f1, font=('ariel', 16, 'bold'), textvariable=amount , bd=6,insertwidth=4, bg="white", justify='right')
txt.grid(row=8, column=4)
label4 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label4.grid(row=5, column=4)
label5 = Label(f1, fg="white", bg="black", font=('aria', 16, 'bold'))
label5.grid(row=10, column=4)

btnwithdraw = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SAQUE", bg="White", command=withdrawn)
btnwithdraw.grid(row=8, column=4)
btnbal = Button(f2, padx=16, pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="SALDO", bg="white", command=bal)
btnbal.grid(row=10, column=4)
btnreset = Button(f2,padx=16,pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'), width=7, text="INÍCIO", bg="white",command=reset)
btnreset.grid(row=11, column=4)
btnexit = Button(f2,padx=16,pady=4, bd=10, fg="black", font=('ariel', 16, 'bold'),width=7, text="SAIR", bg="white", command=root.destroy)
btnexit.grid(row=12, column=4)


root.mainloop()

