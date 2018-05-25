from tkinter import*
import random
from tkinter.messagebox import showerror,showinfo
soluce=""
numero=1
def premier(event):
    d.grid_remove()
    can.grid(column=0,row=0,pady=10,padx=10)
    creer()
def creer():
    global can,x,soluce
    can.delete("all")
    fene.title("Mastermind")
    couleur1=random.randint(0,3)
    couleur2=random.randint(0,3)
    couleur3=random.randint(0,3)
    couleur4=random.randint(0,3)
    soluce=str(couleur1)+" "+str(couleur2)+" "+str(couleur3)+" "+str(couleur4)
    can.create_rectangle(50,50,100,100,fill=liste[couleur1])
    can.create_rectangle(150,50,200,100,fill=liste[couleur2])
    can.create_rectangle(250,50,300,100,fill=liste[couleur3])
    can.create_rectangle(350,50,400,100,fill=liste[couleur4])
    x=can.create_rectangle(40,40,410,110,fill="black")
    prochain()
def montre():
    global x
    can.delete(x)
def compte(x,y):
    nb=0
    x.strip()
    y.strip()
    for loop in range(len(x)):
        if x[loop] == y[loop]:
            nb+=1
    bonnePlaces=nb-3
    bonnesCouleurs=0
    liste=y.split(" ")
    for loop in x:
        if loop in liste:
            del liste[liste.index(loop)]
    for loop in liste:
        if loop:
            bonnesCouleurs+=1
    return 4-bonnesCouleurs,bonnePlaces
            
def prochain():
    global soluce,numero
    colors=["red","green","blue","yellow"]
    nb=[0]*4
    buttons=[]
    if numero>10:
       montre()
       showerror("Perdu","Vous n'avez pas reussi dans le nombre de tour imparti")
       fene.unbind("<Return>")
    else:
        def changer(x):
           nb[x]+=1
           nb[x]=nb[x]%len(colors)
           buttons[x].config(bg=colors[nb[x]])
        def valider(event):
            solution=""
            for loop in nb:
                solution+=str(loop)+" "
            for loop in buttons:
                loop.grid_remove()
            for loop in range(4):
                Label(fen,bg=colors[nb[loop]],height=2,width=5).grid(column=loop,row=0,pady=15,padx=25)
            if soluce.strip()==solution.strip():
                montre()
                showinfo("Bravo!","Vous avez termine le niveau.")
                Label(fene,text="4 : 4").grid(column=1,row=numero-1,padx=25)
            else:
                nb10,nb11=compte(soluce,solution)
                showinfo("Resultat",str(nb10)+" bonne(s) couleur(s) .\n"+str(nb11)+" bonne(s) place(s) avec couleur")
                Label(fene,text=str(nb10)+" : "+str(nb11)).grid(column=1,row=numero-1,padx=25)
                prochain()
        
        
    
    fen=Frame()
    fen.grid(column=0,row=numero)
    numero+=1
    for loop in range(4):
        buttons.append(Button(fen,height=2,width=5,bg=colors[0],command= lambda x=loop :changer(x)))
        buttons[-1].grid(column=loop,row=0,pady=15,padx=25)
    fene.bind("<Return>",valider)


x=0
liste=["red","green","blue","yellow"]
fene=Tk()
texte="Bienvenue au mastermind! \nLes regles de jeu sont simples: \nEn moins de 10 tours, le but est de trouver la combinaison de couleurs correcte choisie par l'ordinateur.\
En cliquant sur un bouton on passe a la prochaine couleur. Apres chaque ligne, on vous informe du nombre de bonnes couleurs a la bonne place.\
Cela est le cas si un carre est de bonne couleur et se situe a la bonne place. Sinon on indique aussi le nombre de couleur(s) correcte(s) au total.\nBonne chance!"
d=Message(fene,text=texte, width=300)
d.grid()
can=Canvas(fene,bg="white",height=150,width=450)
fene.bind("<Return>",premier)
fene.mainloop()
