from tkinter import *
root = Tk()
root.title("Diagnostico casero")
root.geometry("300x300")
root.minsize(250,250)
root.maxsize(350,350)
root.configure(background="white")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Te sientes mal?", bg = "white",fg= "black")
Question1.place(relx=0.5 ,rely=0.1 ,anchor= CENTER )
question1_r1=Radiobutton(root, text = "si", variable=question1_radioButton, value="yes",bg ="white")
question1_r1.place(relx=0.5 ,rely=0.25 ,anchor= CENTER )
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no",bg ="white")
question1_r2.place(relx=0.5 ,rely=0.4 ,anchor= CENTER )

question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="Te sientes bien?",bg ="white",fg= "black")
Question2.place(relx=0.5 ,rely=0.55 ,anchor= CENTER )
question2_r1=Radiobutton(root, text = "si", variable=question2_radioButton, value="yes",bg ="white")
question2_r1.place(relx=0.5 ,rely=0.7 ,anchor= CENTER )
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no",bg ="white")
question2_r2.place(relx=0.5 ,rely=0.85 ,anchor= CENTER )

def heart_diagnostic_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+50
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+1
        print(score)
        
    if score == 1:
        messagebox.showinfo("Reporte","Estas sano :D")
    elif  score == 50: 
        messagebox.showinfo("Reporte","Considera ir al doctor XD")
    elif  score == 51:
        messagebox.showinfo("Reporte","COMO???")
    elif  score == 0:
        messagebox.showinfo("Reporte","COMO???")
        
btn = Button(root, text= "Resultados", command= heart_diagnostic_score)
btn.place(relx=0.5 ,rely=0.95 ,anchor= CENTER )

root.mainloop()