from Livre import *
from Adherent import *
from Auteur import *
from Emprunt import *
from Personne import *
from Bib import *
from datetime import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import ttkbootstrap as m
# from ttkbootstrap.constants import *


b=Bib()
def Ajouter_Livre():
    def aj():
        try: 
            code=codelvar.get()
            titre=titvar.get()
            nom=nomvar.get()
            prenom=prevar.get()
            codeA=codeavar.get()
            nombre_exemp=int(numvar.get())
            b.ajouterLivre(code,titre,nom,prenom,codeA,nombre_exemp)
            messagebox.showinfo("Successful"," le Livre Bien Ajouté")
            f1.destroy()
        except Exception as e:
            messagebox.showerror("ERROR",str(e))

    f1=Toplevel(f)
    f1.configure(bg="#2c3e50")
    
    f1.title("Ajouter Livre")
    codel=Label(f1,text="Code Livre (L1234): ",font=("arial",12,"bold"))
    codelvar=StringVar()
    ecodel=Entry(f1,textvariable=codelvar,font=("arial",12,"bold"))
    titl=Label(f1,text="Titre: ",font=("arial",12,"bold"))
    titvar=StringVar()
    etit=Entry(f1,textvariable=titvar,font=("arial",12,"bold"))
    nom=Label(f1,text="Nom de L'auteur: ",font=("arial",12,"bold"))
    nomvar=StringVar()
    enom=Entry(f1,textvariable=nomvar,font=("arial",12,"bold"))
    pre=Label(f1,text="Prenom de L'auteur: ",font=("arial",12,"bold"))
    prevar=StringVar()
    epre=Entry(f1,textvariable=prevar,font=("arial",12,"bold"))
    codea=Label(f1,text="Code de L'auteur (A1234) ",font=("arial",12,"bold"))
    codeavar=StringVar()
    ecodea=Entry(f1,textvariable=codeavar,font=("arial",12,"bold"))
    
    num=Label(f1,text="Nombres Exemplaires: ",font=("arial",12,"bold"))
    numvar=StringVar()
    enum=Entry(f1,textvariable=numvar,font=("arial",12,"bold"))
    btn01=Button(f1,text="Ajouter",font=("arial",12,"bold"),width=6,command=aj)
    # ----------------------position--------------
    codel.grid(row=0,column=0,padx=15,pady=10)
    ecodel.grid(row=0,column=1,padx=15,pady=10)
    titl.grid(row=1,column=0,padx=15,pady=10)
    etit.grid(row=1,column=1,padx=15,pady=10)
    nom.grid(row=2,column=0,padx=15,pady=10)
    enom.grid(row=2,column=1,padx=15,pady=10)
    pre.grid(row=3,column=0,padx=15,pady=10)
    epre.grid(row=3,column=1,padx=15,pady=10)
    codea.grid(row=4,column=0,padx=15,pady=10)
    ecodea.grid(row=4,column=1,padx=15,pady=10)
    num.grid(row=5,column=0,padx=15,pady=10)
    enum.grid(row=5,column=1,padx=15,pady=10)
    btn01.grid(row=6,column=1,padx=15,pady=10)

def Ajouter_Adherent():
    def aj_A(): 
        try:
            nom = nomAvar.get()
            prenom = preAvar.get()
                # date_adhesion = entree_date.get()
            d=int(day_ent.get())
            m=int(month_ent.get())
            y=int(year_ent.get())
            date_adhesion=date(y,m,d)
            b.ajouterAdherent(nom, prenom, date_adhesion)
            messagebox.showinfo("Succès", "Adhérent ajouté avec succès.")
            f2.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    f2=Toplevel(f)
    f2.configure(bg="#2c3e50")
    f2.title("🧑‍💼 Ajouter Adherent")
    nomA=Label(f2,text="Nom Adherent: ",font=("arial",12,"bold"))
    nomAvar=StringVar()
    enomA=Entry(f2,textvariable=nomAvar,font=("arial",12,"bold"))
    preA=Label(f2,text="Prenom Adherent: ",font=("arial",12,"bold"))
    preAvar=StringVar()
    epreA=Entry(f2,textvariable=preAvar,font=("arial",12,"bold"))
    day=Label(f2,text="Day: ",font=("arial",12,"bold"))
    day_ent=Entry(f2,font=("arial",12,"bold"))

    month=Label(f2,text="Month: ",font=("arial",12,"bold"))
    month_ent=Entry(f2,font=("arial",12,"bold"))
    
    year=Label(f2,text="Year: ",font=("arial",12,"bold"))
    year_ent=Entry(f2,font=("arial",12,"bold"))
    btn001=Button(f2,text="Ajouter",font=("arial",12,"bold"),width=6,command=aj_A)
    # ----------------------position--------------
    nomA.grid(row=0,column=0,padx=15,pady=10)
    enomA.grid(row=0,column=1,padx=15,pady=10)
    preA.grid(row=1,column=0,padx=15,pady=10)
    epreA.grid(row=1,column=1,padx=15,pady=10)
    day.grid(row=2,column=0,padx=15,pady=10)
    day_ent.grid(row=2,column=1,padx=15,pady=10)
    month.grid(row=3,column=0,padx=15,pady=10)
    month_ent.grid(row=3,column=1,padx=15,pady=10)
    year.grid(row=4,column=0,padx=15,pady=10)
    year_ent.grid(row=4,column=1,padx=15,pady=10)
    btn001.grid(row=5,column=0,padx=15,pady=10)
def Rechercher_livre():
    def re_livre():
            ccode=codelivar.get()
            m=b.rechercherLivre(ccode)
            if m:
                messagebox.showinfo("Bien Trouvé",str(m))
            else:
                messagebox.showerror("HH","Non Trouvé")
    f3=Toplevel(f)
    f3.configure(bg="#2c3e50")
    f3.title("🔍Rechercher Livre")
    codeli=Label(f3,text="Code Livre : ",font=("arial",12,"bold"))
    codelivar=StringVar()
    ecodeliv=Entry(f3,textvariable=codelivar,font=("arial",12,"bold"))
    codeli.grid(row=0,column=0,padx=15,pady=10)
    ecodeliv.grid(row=0,column=1,padx=15,pady=10)
    btn0001=Button(f3,text="Rechercher",font=("arial",12,"bold"),width=12,command=re_livre)
    btn0001.grid(row=1,column=1,padx=15,pady=10)

def Rechercher_ADHERENT():
    def re_ad():
            codeA=codeavar.get()
            message=b.rechercherAdherent(codeA)
            if message:
                messagebox.showinfo("Bien Trouvé",str(message))
            else:
                messagebox.showerror("HH","Non Trouvé")
    f4=Toplevel(f)
    f4.configure(bg="#2c3e50")
    f4.title("🆔  Rechercher Adherent")
    codea=Label(f4,text="Code Adherent : ",font=("arial",12,"bold"))
    codeavar=StringVar()
    ecodea=Entry(f4,textvariable=codeavar,font=("arial",12,"bold"))
    codea.grid(row=0,column=0,padx=15,pady=10)
    ecodea.grid(row=0,column=1,padx=15,pady=10)
    btn0001=Button(f4,text="Rechercher",font=("arial",12,"bold"),width=12,command=re_ad)
    btn0001.grid(row=1,column=1,padx=15,pady=10)

def ajoute_Emprunte():
    def aj_em():
        try: 
            codeaa=codeavar.get()
            codell=codelvar.get()
            b.ajouterEmprunt(codeaa,codell)
            messagebox.showinfo("Bien Ajouté","Successful Emprurnt")
            f5.destroy()
        except Exception as e:
               messagebox.showerror("Erreur",str(e))
    f5=Toplevel(f)
    f5.configure(bg="#2c3e50")
    f5.title("📖 Ajouter Emprunt")
    codea=Label(f5,text="Code Adherent : ",font=("arial",12,"bold"))
    codeavar=StringVar()
    ecodea=Entry(f5,textvariable=codeavar,font=("arial",12,"bold"))
    codel=Label(f5,text="Code Livre : ",font=("arial",12,"bold"))
    codelvar=StringVar()
    ecodel=Entry(f5,textvariable=codelvar,font=("arial",12,"bold"))
    codea.grid(row=0,column=0,padx=15,pady=10)
    ecodea.grid(row=0,column=1,padx=15,pady=10)
    codel.grid(row=1,column=0,padx=15,pady=10)
    ecodel.grid(row=1,column=1,padx=15,pady=10)

    btn0001=Button(f5,text="Emprunter",font=("arial",12,"bold"),width=12,command=aj_em)
    btn0001.grid(row=2,column=1,padx=15,pady=10)
  
def Retourne_Emp():
    def retour_emp():
        try:    
            codeeem=codeemvar.get()
            b.retourEmprunt(codeeem)
            messagebox.showinfo("Bien Retoune","Sucessful Return")
            f6.destroy()
        except Exception as e:
            messagebox.showerror("Errror",str(e))
    f6=Toplevel(f)
    f6.configure(bg="#2c3e50")
    f6.title("📤 retour Emprunt")
    codeem=Label(f6,text="Code Emprunt : ",font=("arial",12,"bold"))
    codeemvar=StringVar()
    ecodeem=Entry(f6,textvariable=codeemvar,font=("arial",12,"bold"))
    codeem.grid(row=0,column=0,padx=15,pady=10)
    ecodeem.grid(row=0,column=1,padx=15,pady=10)

    btn0001=Button(f6,text="RetourEmpr",font=("arial",12,"bold"),width=12,command=retour_emp)
    btn0001.grid(row=1,column=1,padx=15,pady=10)


#    - -  -   -  - - - -changing------------
def top_emp():
    try:
        top_books = b.topEmprunts()
        if top_books:
            result = "\n".join([f"{livre.get_code()} - {livre.get_titre()} ({livre.getNbrEmprunt()} emprunts)" for livre in top_books])
            messagebox.showinfo("Top Emprunts", result)
        else:
            messagebox.showinfo("Info", "Aucun livre emprunté pour l'instant.")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))       

def afficher_Emp_act():
        try:
            emprenteurs = b.emprunteurs()
            result = "\n".join([str(ad) for ad in emprenteurs])
            messagebox.showinfo(" Emprunteurs Actifs :", result)
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

def Date_Possibilite_Emprunt():
    def chercher():
        try:
            code = codelvar.get()
            date_disponible = b.datePossibiliteEmprunt(code)
            messagebox.showinfo("Disponibilité", date_disponible)
            f7.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
    f7=Toplevel(f)
    f7.configure(bg="#2c3e50")
    f7.title("⏳ Date Disponibilité d'un Livre")
    codel=Label(f7,text="Code Livre : ",font=("arial",12,"bold"))
    codelvar=StringVar()
    ecodel=Entry(f7,textvariable=codelvar,font=("arial",12,"bold"))
    codel.grid(row=0,column=0,padx=15,pady=10)
    ecodel.grid(row=0,column=1,padx=15,pady=10)

    btn0001=Button(f7,text="Verifier",font=("arial",12,"bold"),width=12,command=chercher)
    btn0001.grid(row=1,column=1,padx=15,pady=10)
def Rapp():
        try:
            r=b.getRapport()
            mes=''
            for k, v in r.items():
                mes += f"{k}: {v}"
            messagebox.showinfo("Library",str(mes))
        except Exception as m:
            messagebox.showerror("Erreur",(m))


def quitter_app():
    qui = messagebox.askyesno("Quitter", "Are You Sure to Out?")
    if qui:
        f.quit()



f=Tk()
# f=m.Window(themename="superhero")
f.geometry("888x555")
f.title("Bibliothéque")
# --------------------image background---------------------
imagebib="WhatsApp Image 2025-01-30 at 23.16.38_5f487c33.jpg"
image=Image.open(imagebib)
img=image.resize((1400,700))
picture=ImageTk.PhotoImage(img)
pic=Label(f,image=picture)
pic.place(x=0,y=0)


#---------------------------Titre----------------------------------------
titre=Label(f,text="📚 Gestion de Bibliothéque",font=("Arial",23,"bold"), bg='#456890',fg="#d6b117")
titre.pack(pady=20)

#---------------------------Logo----------------------------------------------
logo = ImageTk.PhotoImage(Image.open("WhatsApp Image 2025-02-01 at 18.48.42_223ecf74.jpg").resize((150, 100)))
logo1 = Label(f, image=logo, borderwidth=0)
logo1.place(x=0, y=10) 

#-------------------------------------Hover-------------------------------------------
bnt1=Button(f,text="📚 Ajouter un livre",font=("Courier New",12, "bold"),width=50,command=Ajouter_Livre,fg="#CD853F",bg="black",height=2,bd=0)
bnt2=Button(f,text="🧑‍💼 Ajouter un Adherent",font=("Courier New",12, "bold"),width=50,command=Ajouter_Adherent,height=2,fg="#CD853F",bg="black",bd=0)
bnt3=Button(f,text="🔍 Rechercher Livre",font=("Courier New",12, "bold"),width=50,command=Rechercher_livre,height=2,fg="#CD853F",bg="black",bd=0)
bnt4=Button(f,text="🆔 Rechercher Adherent",font=("Courier New",12, "bold"),width=50,command=Rechercher_ADHERENT,height=2,fg="#CD853F",bg="black",bd=0)
bnt5=Button(f,text="📖 Ajouter un Emprunt",font=("Courier New",12, "bold"),width=50,command=ajoute_Emprunte,height=2,fg="#CD853F",bg="black",bd=0)
bnt6=Button(f,text="📤 Retourner un Emprunt",font=("Courier New",12, "bold"),width=50,command=Retourne_Emp,height=2,fg="#CD853F",bg="black",bd=0)
bnt7=Button(f,text="📊 Afficher Top Emprunt",font=("Courier New",12, "bold"),width=50,command=top_emp,height=2,fg="#CD853F",bg="black",bd=0)
bnt8=Button(f,text="🏆 Afficher Emprunt Actifs",font=("Courier New",12, "bold"),width=50,command=afficher_Emp_act,height=2,fg="#CD853F",bg="black",bd=0)
bnt9=Button(f,text="⏳ Date Possibilité Emprunt",font=("Courier New",12, "bold"),width=50,command=Date_Possibilite_Emprunt,height=2,fg="#CD853F",bg="black",bd=0)
bnt10=Button(f,text="📜 RAPPORT",font=("Courier New",12, "bold"),width=50,command=Rapp,height=2,fg="#CD853F",bg="black",bd=0)
bnt11 = Button(f, text="❌ Quitter", font=("Courier New", 12, "bold"), width=50, command=quitter_app, fg="red", bg="black", height=2, bd=0)


all_boutonn=[bnt1,bnt2,bnt3,bnt4,bnt5,bnt6,bnt7,bnt8,bnt9,bnt10,bnt11]
for btn in all_boutonn:
    btn.bind("<Enter>",lambda event , x=btn: on_enter(x))
for btn in all_boutonn:
    btn.bind("<Leave>",lambda event , x=btn: on_leave(x))
def on_enter(x) :
    x.configure(bg="#CD853F",fg="black",bd=7) 
def on_leave(x) :
    x.configure(fg="#CD853F", bg="black",bd=0)  

bnt1.pack(pady=2,padx=10)
bnt2.pack(pady=5,padx=10)
bnt3.pack(pady=5,padx=10)
bnt4.pack(pady=5,padx=10)
bnt5.pack(pady=5,padx=10)
bnt6.pack(pady=5,padx=10)
bnt7.pack(pady=5,padx=10)
bnt8.pack(pady=5,padx=10)
bnt9.pack(pady=5,padx=10)
bnt10.pack(pady=5,padx=10)
bnt11.pack(pady=5,padx=10)


f.mainloop()