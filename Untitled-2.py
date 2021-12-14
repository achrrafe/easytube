import tkinter
from tkinter import*
from pytube import*
win=Tk()
win.title("easytube")
win.geometry("1000x640+110+19")
win.resizable(False,False)
text=StringVar()
logo=PhotoImage(file="logo.png")
bl1=PhotoImage(file="C:\\Users\\achraf\\Desktop\\jj\\b1.gif")
yout1=PhotoImage(file="C:\\Users\\achraf\\Desktop\\jj\\yout1.gif")
yout2=PhotoImage(file="C:\\Users\\achraf\\Desktop\\jj\\yout2.gif")
intro=Frame(width=1000,height=150).place(x=0,y=0)
contact=Button(intro,text="contact",relief="ridge",width=19,cursor="hand2",activebackground="red",activeforeground="yellow",bd=15).place(x=790,y=90)
about=Button(intro,text="about nous",relief="ridge",width=19,cursor="hand2",activebackground="red",activeforeground="yellow",bd=15).place(x=599,y=90)
l1=Label(image=logo,height=149,width=250).place(x=310,y=0)

l2=Label(image=bl1,height=149,width=290).place(x=1,y=0)
l3=Label(image=yout1,height=219,width=350).place(x=640,y=160)
l4=Label(image=yout2,height=219,width=350).place(x=640,y=400)
l6=Label(text="entrez le lien",font="arial 20").place(x=30,y=180)
url=Entry(bg="darkgray",width=34,bd=17 ,state= NORMAL,font="arial 15",textvariable=text).place(x=190,y=180)
select=Button(text="select format",relief="ridge",width=19,cursor="hand2",activebackground="red",activeforeground="yellow",bd=15,command=lambda:sel()).place(x=260,y=230)



def sel():
    global select
    global l8
    global l9
    global url
    global choix
    url=Entry(bg="darkgray",width=34,bd=17 ,state= DISABLED,font="arial 15",textvariable=text).place(x=190,y=180)
    select=Button(text="select format",relief="ridge",width=19,cursor="hand2",activebackground="red",activeforeground="yellow",bd=15,command=lambda:sel(),state=DISABLED).place(x=260,y=230)
    

    l8=Label(text="video/3gpp res= 144p",font="arial 15").place(x=14,y=292)
    b1=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel1()).place(x=260,y=292)
    l9=Label(text="video/mp4 res=360p",font="arial 15").place(x=14,y=335)
    b2=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel2()).place(x=260,y=335)
    l10=Label(text="video/mp4 res=720p",font="arial 15").place(x=14,y=378)
    b3=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel3()).place(x=260,y=378)
    l11=Label(text="video/mp4 res=1080p",font="arial 15").place(x=14,y=421)
    b4=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel4()).place(x=260,y=421)
    l12=Label(text="audio/mp3 abr=50kbps",font="arial 15").place(x=14,y=464)
    b5=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel5()).place(x=260,y=464)
    l13=Label(text="audio/mp3 abr=50kbps",font="arial 15").place(x=14,y=507)
    b6=Button(intro,text="select",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel6()).place(x=260,y=507)
    l14=Label(text="audio/mp3 abr=50kbps",font="arial 15").place(x=14,y=550)
    b7=Button(intro,text="download",relief="ridge",width=14,cursor="hand2",activebackground="red",activeforeground="yellow",bd=10,command=lambda:sel7()).place(x=260,y=550)
    def sel1():
        import datetime as dt
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        
        video=videos[0]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        c=dt.datetime.now()
        l14=Label(text="telechargement effectuer",font="arial 15",fg='cyan').place(x=400,y=292)
        l14=Label(text="title :",font="arial 15",fg='grey').place(x=392,y=335)
        l14=Label(text=yt.title,font="arial 8",fg='grey').place(x=441,y=340)
        l14=Label(text="auteur :",font="arial 15",fg='grey').place(x=392,y=378)
        l14=Label(text=yt.author,font="arial 8",fg='grey').place(x=452,y=383)
        l14=Label(text="views :",font="arial 15",fg='grey').place(x=392,y=421)
        l14=Label(text=yt.views,font="arial 8",fg='grey').place(x=452,y=426)
        l14=Label(text="format :",font="arial 15",fg='grey').place(x=392,y=464)
        l14=Label(text="mp4 res 144p",font="arial 8",fg='grey').place(x=452,y=469)
        l14=Label(text="date  :",font="arial 13",fg='grey').place(x=392,y=507)
        l14=Label(text=c,font="arial 8",fg='grey').place(x=452,y=507)
        
            
    def sel2():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[1]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15",fg='cyan').place(x=14,y=292)
    def sel3():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[2]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15",fg='cyan').place(x=14,y=292)
    def sel4():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[3]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15",fg='cyan').place(x=14,y=292)
    def sel5():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[17]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15",fg='cyan').place(x=14,y=292)
    def sel6():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[18]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15").place(x=14,y=292)
    def sel7():
        link=text.get()
        yt = YouTube(link)
        videos = yt.streams.all()
        video=videos[19]
        video.download('C:\\Users\\achraf\\Desktop\\jj')
        l14=Label(text="telechargement effectuer",font="arial 15").place(x=14,y=292)
    

    
def ss():
    
    win.mainloop()

win.mainloop()