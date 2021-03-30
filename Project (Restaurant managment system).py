
from tkinter import* 
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Managment System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(root,width=800,height=1000,relief=RAISED)
f2.place(x=950,y=250)

#=============================================================================================
#                      TIME
#=====================================================================================================
localtime=time.asctime(time.localtime(time.time()))

lb1Info=Label(Tops,font=('helvetica',50,'bold'),text="MAK RESTAURANT",fg="black")
lb1Info.grid(row=0,column=0)

lb1Info=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="steel blue")
lb1Info.grid(row=1,column=0)


def exitpressed():
    root.destroy()

def reset():
    rand.set("")
    fries.set("")
    burg.set("")
    pizza.set("")
    cola.set("")
    briya.set("")
    gst.set("")
    stotal.set("")
    total.set("")
    stax.set("")
    ice.set("")
    cost.set("")
    sand.set("")
    tea.set("")

def Total():
    x=random.randint(10000,500000)
    randomTotal=str(x)
    rand.set(randomTotal)

    if (fries.get()==""):
        cof=0
    else:
        cof=float(fries.get())

        
    if (burg.get()==""):
        cobr=0
    else:
        cobr=float(burg.get())


    if (pizza.get()==""):
        cop=0
    else:
        cop=float(pizza.get())

    if (cola.get()==""):
        coc=0
    else:
        coc=float(cola.get())


    if (briya.get()==""):
        cob=0
    else:
        cob=float(briya.get())

    if (ice.get()==""):
        coi=0
    else:
        coi=float(ice.get())


    if (sand.get()==""):
        cos=0
    else:
        cos=float(sand.get())

    if (tea.get()==""):
        cot=0
    else:
        cot=float(tea.get())




















    costofries=cof*50
    costofburger=cobr*69
    costofpizza=cop*99
    costofcola=coc*35
    costofbriyani=cob*140
    costoficecream=coi*30
    costofsandwich=cos*69
    costoftea=cot*25

    
    GST = ((costofries+costofburger+costofpizza+costofcola+costofbriyani+costoficecream+costofsandwich+costoftea)*0.18)
    Totalcost=(costofries+costofburger+costofpizza+costofcola+costofbriyani+costoficecream+costofsandwich+costoftea)

    Stax=((costofries+costofburger+costofpizza+costofcola+costofbriyani+costoficecream+costofsandwich+costoftea)/99)
    costofmeal="Rs", str('%.2f' % (costofries+costofburger+costofpizza+costofcola+costofbriyani+costoficecream+costofsandwich+costoftea))
    Servicetax="Rs",str('%.2f' % Stax)
    Gst="Rs",str('%.2f' % GST)
    totalcost="Rs",str('%.2f' % (GST+Totalcost+Stax))

    stax.set(Servicetax)
    cost.set(costofmeal)
    
    stotal.set(costofmeal)
    gst.set(Gst)
    total.set(totalcost)
    
 

    









#===============================food left side====================
lb1Reference=Label(f1,font=('arial',16,'bold'),text="Reference")
lb1Reference.grid(row=0,column=0)
rand=StringVar()
txtReference=Entry(f1,font=('arial',16,"bold"),textvariable=rand,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtReference.grid(row=0,column=1)


lb1fries=Label(f1,font=('arial',16,'bold'),text="Fries")
lb1fries.grid(row=1,column=0)
fries=StringVar()
txtfries=Entry(f1,font=('arial',16,"bold"),textvariable=fries,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtfries.grid(row=1,column=1)

lb1burger=Label(f1,font=('arial',16,'bold'),text="Burger")
lb1burger.grid(row=2,column=0)
burg=StringVar()
txtburger=Entry(f1,font=('arial',16,"bold"),textvariable=burg,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtburger.grid(row=2,column=1)

lb1pizza=Label(f1,font=('arial',16,'bold'),text="Pizza")
lb1pizza.grid(row=3,column=0)
pizza=StringVar()
txtpizza=Entry(f1,font=('arial',16,"bold"),textvariable=pizza,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtpizza.grid(row=3,column=1)


lb1cola=Label(f1,font=('arial',16,'bold'),text="Cola")
lb1cola.grid(row=4,column=0)
cola=StringVar()
txtcola=Entry(f1,font=('arial',16,"bold"),textvariable=cola,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtcola.grid(row=4,column=1)


lb1Briyani=Label(f1,font=('arial',16,'bold'),text="Briyani")
lb1Briyani.grid(row=5,column=0)
briya=StringVar()
txtpizza=Entry(f1,font=('arial',16,"bold"),textvariable=briya,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtpizza.grid(row=5,column=1)


lb1Sandwich=Label(f1,font=('arial',16,'bold'),text="Sandwich")
lb1Sandwich.grid(row=6,column=0)
sand=StringVar()
txtsand=Entry(f1,font=('arial',16,"bold"),textvariable=sand,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtsand.grid(row=6,column=1)
#==============================================food right side==========================================


lb1ice=Label(f1,font=('arial',16,'bold'),text="Ice Cream")
lb1ice.grid(row=0,column=2)
ice=StringVar()
txtice=Entry(f1,font=('arial',16,"bold"),textvariable=ice,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtice.grid(row=0,column=3)

lb1tea=Label(f1,font=('arial',16,'bold'),text="Tea")
lb1tea.grid(row=1,column=2)
tea=StringVar()
txttea=Entry(f1,font=('arial',16,"bold"),textvariable=tea,bg="powder blue",bd=10,insertwidth=4,justify="right")
txttea.grid(row=1,column=3)



lb1cost=Label(f1,font=('arial',16,'bold'),text="Cost Of Meal")
lb1cost.grid(row=2,column=2)
cost=StringVar()
txtcost=Entry(f1,font=('arial',16,"bold"),textvariable=cost,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtcost.grid(row=2,column=3)

lb1stax=Label(f1,font=('arial',16,'bold'),text="Service Tax")
lb1stax.grid(row=3,column=2)
stax=StringVar()
txtstax=Entry(f1,font=('arial',16,"bold"),textvariable=stax,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtstax.grid(row=3,column=3)

lb1gst=Label(f1,font=('arial',16,'bold'),text="GST")
lb1gst.grid(row=4,column=2)
gst=StringVar()
txtgst=Entry(f1,font=('arial',16,"bold"),textvariable=gst,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtgst.grid(row=4,column=3)

lb1stotal=Label(f1,font=('arial',16,'bold'),text="Sub Total")
lb1stotal.grid(row=5,column=2)
stotal=StringVar()
txtstotal=Entry(f1,font=('arial',16,"bold"),textvariable=stotal,bg="powder blue",bd=10,insertwidth=4,justify="right")
txtstotal.grid(row=5,column=3)

lb1total=Label(f1,font=('arial',16,'bold'),text="Total Cost")
lb1total.grid(row=6,column=2)
total=StringVar()
txttotal=Entry(f1,font=('arial',16,"bold"),textvariable=total,bg="powder blue",bd=10,insertwidth=4,justify="right")
txttotal.grid(row=6,column=3)
#============================================button===============================================================

btntotal=Button(f1,font=('arial',16,'bold'),text="Total",padx=8,pady=8,fg="black",bg="green",width=10,bd=16,command=Total)
btntotal.grid(row=8,column=1)

btnreset=Button(f1,font=('arial',16,'bold'),text="Reset",padx=8,pady=8,fg="black",bg="red",width=10,bd=16,command=reset).grid(row=8,column=2)
btnexit=Button(f1,font=('arial',16,'bold'),text="Exit",padx=8,pady=8,fg="black",bg="yellow",width=10,bd=16,command=exitpressed).grid(row=8,column=3)
