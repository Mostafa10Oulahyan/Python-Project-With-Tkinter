from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time

def loging():
    if usernam.get() == "" or Pasword.get() == "":
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires !")
    elif usernam.get() == 'PERSONNE' and Pasword.get() == "2025":
        messagebox.showinfo("Succès", "Connexion réussie !")
        root.destroy()
        import App
    else:
        messagebox.showerror("Erreur", "Informations incorrectes !")
def toggle_password():
    if Pasword.cget("show") == "*":
        Pasword.configure(show="")
        show_pass_btn.configure(text="👁") 
    else:
        Pasword.configure(show="*")
        show_pass_btn.configure(text="👁‍🗨")
#--------------------------Animation-------------------
def fade_in(window, duration=0.01):
    alpha = 0.0
    while alpha < 1.0:
        window.attributes("-alpha", alpha)
        alpha += 0.05
        time.sleep(duration)
        window.update()

 
def animate_widget(widget, start_x, start_y, end_x, end_y, duration=0.01):
    delta_x = (end_x - start_x) / 50
    delta_y = (end_y - start_y) / 50
    for _ in range(50):
        start_x += delta_x
        start_y += delta_y
        widget.place(x=int(start_x), y=int(start_y)) 
        time.sleep(duration)
        root.update()


root = CTk()
root.geometry("940x500")
root.resizable(0, 0)
root.title("Login Page")
set_appearance_mode("dark")  

image = CTkImage(Image.open("image.jpg"), size=(940, 500))
image_label = CTkLabel(root, image=image, text="")
image_label.place(x=0, y=0)

title_label = CTkLabel(root, text="🔷 Employee Management System",
                       font=("Arial", 24, "bold"), 
                       bg_color="transparent", 
                       text_color="#00ccff")
title_label.place(x=270, y=50)
def on_entry_focus(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")

def on_entry_leave(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)


usernam = CTkEntry(root, placeholder_text="USERNAME:PERSONNE", width=200,height=30, fg_color="#f2f2f2", text_color="black")
usernam.insert(0, "USERNAME:PERSONNE")
usernam.bind("<FocusIn>", lambda event: on_entry_focus(usernam, "USERNAME:PERSONNE"))
usernam.bind("<FocusOut>", lambda event: on_entry_leave(usernam, "USERNAME:PERSONNE"))
usernam.place(x=380, y=150)

Pasword = CTkEntry(root, placeholder_text="Entrez le mot de passe : 2025", width=200,height=30,fg_color="#f2f2f2", text_color="black", show="*")
Pasword.insert(0, "Entrez le mot de passe : 2025")
Pasword.bind("<FocusIn>", lambda event: on_entry_focus(Pasword, "Entrez le mot de passe : 2025"))
Pasword.bind("<FocusOut>", lambda event: on_entry_leave(Pasword, "Entrez le mot de passe : 2025"))
Pasword.place(x=380, y=200)
show_pass_btn = CTkButton(root, text="👁‍🗨", width=10, height=10, fg_color="gray", hover_color="#555",
                          font=("Arial", 12), command=toggle_password)
show_pass_btn.place(x=590, y=200)
Submit = CTkButton(root, text="🔑 Connexion", cursor="hand2", font=("Arial", 14, "bold"),
                   fg_color="#00ccff", hover_color="#0099cc", command=loging)
Submit.place(x=380, y=250)




fade_in(root)


animate_widget(usernam, -220, 150, 380, 150)
animate_widget(Pasword, 940, 210, 380, 200)
animate_widget(Submit, -240, 280, 410, 250)

root.mainloop()
