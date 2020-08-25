from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#methods

class MyTranslator:
    """ This function is used to translate source language into destination language"""

    def __init__(self):
        self.langs=list(LANGUAGES.values())

    def run(self, txt='Type text here', src='english', dest='hindi'):
        self.translator=Translator()
        self.txt = txt
        self.src = src
        self.dest = dest
        try:
            self.translated=self.translator.translate(self.txt,src=self.src,dest=self.dest)
        except:
            self.translated = self.translator.translate(self.txt)


        self.ttext = self.translated.text
        return self.ttext




#GUI part
root=Tk()
root.geometry('450x620')
root.title('Translator App')
root.resizable(0,0)
root.configure(bg='orange')

root.wm_iconbitmap("Translation-80_icon-icons.com_57255.ico")

def get():
    """ This function is used to get the source language and destination language to insert
     in destination text"""

    s=sourceLangs.get()
    d=destLangs.get()
    message=sourceText.get(1.0,END)
    translator=MyTranslator()
    text=translator.run(txt=message,src=s,dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)

app_name=Label(root,text='GOOGLE Translator',font=('arial',20,'bold'),
               bg='violet',fg='midnight blue',height='2')
app_name.pack(side=TOP,fill=BOTH)

frame=Frame(root).pack(side=BOTTOM)
sourceText=Text(frame,font=('arial',10),height=12,wrap=WORD)
sourceText.pack(side=TOP,padx=15,pady=15)

# creating a translator button
transbtn=Button(frame,text='Translate',font=('arial',10,'bold'),
                   bg='green',fg='black',activebackground='red',
                   relief=GROOVE,command=get)
transbtn.pack(side=TOP,pady=15)

langs=MyTranslator().langs

# creating a combobox
sourceLangs=ttk.Combobox(frame,values=langs,width=20)
sourceLangs.place(x=30,y=310)
sourceLangs.set('english')

destLangs=ttk.Combobox(frame,values=langs,width=20)
destLangs.place(x=280,y=310)
destLangs.set('hindi')

destText=Text(frame,font=('arial',10),height=12,wrap=WORD)
destText.pack(side=TOP,padx=15,pady=15)

status_bar=Label(frame,text='Created by: Bhagyawanth_Avantagi',font=('arial',10,'bold'),bg='blue')
status_bar.pack(side=BOTTOM,fill=BOTH)

root.mainloop()


