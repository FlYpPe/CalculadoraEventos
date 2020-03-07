import tkinter as tk

def ingresar0():
    cajaMantisa.insert(0,"0")


def ingresar1():
    cajaMantisa.insert(0, "1")


def ingresar2():
    cajaMantisa.insert(0, "2")


def ingresar3():
    cajaMantisa.insert(0, "3")


def ingresar4():
    cajaMantisa.insert(0, "4")


def ingresar5():
    cajaMantisa.insert(0, "5")


def ingresar6():
    cajaMantisa.insert(0, "6")


def ingresar7():
    cajaMantisa.insert(0, "7")


def ingresar8():
    cajaMantisa.insert(0, "8")


def ingresar9():
    cajaMantisa.insert(0, "9")




ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Calculadora")
ventanaPrincipal.geometry('200x400')
cajaMantisa = tk.Entry(ventanaPrincipal, text="0")
cajaMantisa.place(x=50,y=30,width=480,height=40)
btnmen = tk.Button(ventanaPrincipal, text= "===")
btnmen.place(x=5,y=5,width=20,height=20)
btnIgual = tk.Button(ventanaPrincipal, text= "=", width =10)
btnIgual.place(x=150,y=350,width=50,height=50)
btnPunto = tk.Button(ventanaPrincipal, text= ".", width =10)
btnPunto.place(x=100,y=350,width=50,height=50)
btn0 = tk.Button(ventanaPrincipal, text= "0", width =10, command=ingresar0())
btn0.place(x=50,y=350,width=50,height=50)
btnMM = tk.Button(ventanaPrincipal, text= "+/-", width =10)
btnMM.place(x=0,y=350,width=50,height=50)

##===================
btn1 = tk.Button(ventanaPrincipal, text= "1", width =10, command=ingresar1())
btn1.place(x=0,y=300,width=50,height=50)
btn2 = tk.Button(ventanaPrincipal, text= "2", width =10, command=ingresar2())
btn2.place(x=50,y=300,width=50,height=50)
btn3 = tk.Button(ventanaPrincipal, text= "3", width =10, command=ingresar3())
btn3.place(x=100,y=300,width=50,height=50)
btnMas = tk.Button(ventanaPrincipal, text= "+", width =10)
btnMas.place(x=150,y=300,width=50,height=50)

##============================
btn4 = tk.Button(ventanaPrincipal, text= "4", width =10, command=ingresar4())
btn4.place(x=0,y=250,width=50,height=50)
btn5 = tk.Button(ventanaPrincipal, text= "5", width =10, command=ingresar5())
btn5.place(x=50,y=250,width=50,height=50)
btn6 = tk.Button(ventanaPrincipal, text= "6", width =10, command=ingresar6())
btn6.place(x=100,y=250,width=50,height=50)
btnMenos = tk.Button(ventanaPrincipal, text= "-", width =10)
btnMenos.place(x=150,y=250,width=50,height=50)

##================================

btnMult = tk.Button(ventanaPrincipal, text= "X", width =10)
btnMult.place(x=150,y=200,width=50,height=50)
btn9 = tk.Button(ventanaPrincipal, text= "9", width =10, command=ingresar9())
btn9.place(x=100,y=200,width=50,height=50)
btn8 = tk.Button(ventanaPrincipal, text= "8", width =10, command=ingresar8())
btn8.place(x=50,y=200,width=50,height=50)
btn7 = tk.Button(ventanaPrincipal, text= "7", width =10, command=ingresar7())
btn7.place(x=0,y=200,width=50,height=50)

##====================================
btnCE = tk.Button(ventanaPrincipal, text= "1/x", width =10)
btnCE.place(x=0,y=150,width=50,height=50)
btnC = tk.Button(ventanaPrincipal, text= "x^2", width =10)
btnC.place(x=50,y=150,width=50,height=50)
btnDelet = tk.Button(ventanaPrincipal, text= " SQRT ", width =10)
btnDelet.place(x=100,y=150,width=50,height=50)
btnPorciento = tk.Button(ventanaPrincipal, text= "/", width =10)
btnPorciento.place(x=150,y=150,width=50,height=50)

##================



btnCE = tk.Button(ventanaPrincipal, text= "%", width =10)
btnCE.place(x=0,y=100,width=50,height=50)
btnC = tk.Button(ventanaPrincipal, text= "CE", width =10)
btnC.place(x=50,y=100,width=50,height=50)
btnDelet = tk.Button(ventanaPrincipal, text= "C", width =10)
btnDelet.place(x=100,y=100,width=50,height=50)
btnDivision = tk.Button(ventanaPrincipal, text= "<x|", width =10)
btnDivision.place(x=150,y=100,width=50,height=50)

btnMC = tk.Button(ventanaPrincipal, text= "MC", width =10)
btnMC.place(x=0,y=80,width=40,height=20)
btnMR = tk.Button(ventanaPrincipal, text= "MR", width =10)
btnMR.place(x=40,y=80,width=40,height=20)
btnMM = tk.Button(ventanaPrincipal, text= "M+", width =10)
btnMM.place(x=80,y=80,width=40,height=20)
btnMN = tk.Button(ventanaPrincipal, text= "M-", width =10)
btnMN.place(x=120,y=80,width=40,height=20)
btnMS = tk.Button(ventanaPrincipal, text= "MS", width =10)
btnMS.place(x=160,y=80,width=40,height=20)




ventanaPrincipal.mainloop()