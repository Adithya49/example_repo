import tkinter as tk
from PIL import Image
from tkinter import filedialog
root=tk.Tk()
canvas1=tk.Canvas(root, width=300,height=250,bg='azure3',relief='raised')
canvas1.pack()

label1 = tk.Label(root,text='Images to PDF converter',bg='azure3')
label1.config(font=('helvetica',20))
canvas1.create_window(150,60,window=label1)
def getfile():
    global lst
    files= filedialog.askopenfilenames()
    lst=list(files)
    print(lst)
def converttopdf():
    global pdf1,pd
    pdf1=[]
    pd=[]
    for i in lst:
        pd.append(Image.open(i))
    for i in pd:
        pdf1.append(i.convert('RGB'))
    file= filedialog.asksaveasfilename(defaultextension='.pdf')
    pdf2=pdf1[1:]
    pdf1[0].save(file,save_all=True,append_images=pdf2)
button1=tk.Button(text="    Insert files     ",command=getfile,bg='royalblue',fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,130,window=button1)

button2=tk.Button(text='Convert into pdf',command=converttopdf,bg='royalblue',fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,180,window=button2)

root.mainloop()












