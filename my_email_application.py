from tkinter import *
import smtplib          # It is stand for simple mail transfer protocol
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root= Tk()
root.geometry('800x600+200+25')
root.title("Uday Mail Application")
root.config(bg='#282828')

Label_0=Label(root, text="Mail", bg="#282828",width=20, fg="white", font=("Times New Roman",30))
Label_0.place(x=190,y=20)

Label_1=Label(root, text="Your Email ID:",fg="white",bg="#282828", width=20, font=("Times New Roman",13))
Label_1.place(x=90,y=90)

#for getting entry input
Rmail=StringVar()
Rpswrd=StringVar()
Rsender=StringVar()
Rsubject=StringVar()

emailE=Entry(root, width=40, textvariable=Rmail,font=("Times New Roman",13))
emailE.place(x=250, y=90)

Label_2=Label(root, text="Your Password:", fg="white",bg="#282828",width=20, font=("Times New Roman",13))
Label_2.place(x=90,y=140)

passwordE=Entry(root, width=40, show="*", textvariable=Rpswrd,font=("Times New Roman",13))
passwordE.place(x=250, y=140)

Label_3=Label(root, text="Sent To Email:",fg="white",bg="#282828", width=20, font=("Times New Roman",13))
Label_3.place(x=90,y=190)

senderE=Entry(root, width=40, textvariable=Rsender,font=("Times New Roman",13))
senderE.place(x=250, y=190)

Label_4=Label(root, text="Subject:",fg="white",bg="#282828", width=20, font=("Times New Roman",13))
Label_4.place(x=100,y=240)

subjectE=Entry(root, width=40, textvariable=Rsubject,font=("Times New Roman",13))
subjectE.place(x=250, y=240)

Label_5=Label(root, text="Message:",fg="white",bg="#282828", width=20, font=("Times New Roman",13))
Label_5.place(x=100,y=290)

msgbodyE=Text(root, width=60, height=9 ,font=("Times New Roman",13))
msgbodyE.place(x=250, y=290)


Label_7=Label(root, text="</Developed By :- Uday Vaishnav/> ",fg="white",bg="#282828",width=80, font=("Times New Roman",12))
Label_7.place(x=310,y=570)

def sendemail():

    try:
        mymsg=MIMEMultipart()
        mymsg['From']=str(Rmail.get())
        mymsg['To']= str(Rsender.get())
        mymsg['Subject']= str(Rsubject.get())

        mymsg.attach(MIMEText(msgbodyE.get(1.0,'end'), 'plain'))

        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(Rmail.get()), str(Rpswrd.get()))
        text=mymsg.as_string()
        server.sendmail(str(Rmail.get()), str(Rsender.get()), text)

        Label_6=Label(root, text="Done!", width=20,fg='green',bg="#282828", font=("Times New Roman",15))
        Label_6.place(x=320,y=530)

        server.quit()
    except:
        Label_6=Label(root, text="Something went wrong!", width=20,fg='red',bg="#282828", font=("Times New Roman",15))
        Label_6.place(x=310,y=530)

send=PhotoImage(file="C:\\Users\\RAVI\\Desktop\\Language\\Email\\Send_but.png")
Button(root,image=send,bg="#282828",bd=0,command=sendemail).place(x=390, y=470)

root.mainloop()
