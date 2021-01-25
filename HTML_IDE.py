from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser 
root=Tk()
root.minsize(680,670)
root.maxsize(680,670)
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
run_img=ImageTk.PhotoImage(Image.open("download.jpg"))

label_file_name=Label(root,text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80,bg="slate gray",fg="white")
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)
name=""
run=""
def openfile():
    try:
        global name
        global run
        my_text.delete(1.0,END)
        input_file_name.delete(0,END)
        HTML_file=filedialog.askopenfilename(title="Open HTML File",filetypes=(("HTML Files","*.html"),))
        run=HTML_file
        name=os.path.basename(HTML_file)
        formated_name=name.split('.')[0]
        input_file_name.insert(END,formated_name)
        root.title(formated_name)
        HTML_file=open(HTML_file,'r')
        paragraph=HTML_file.read()
        my_text.insert(END,paragraph)
        HTML_file.close()
    except:
        messagebox.showerror("Error","Unable to open file")
def save():
    input_name=input_file_name.get()
    file=open(input_name+".html","w")
    data=my_text.get("1.0",END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("Update","Success")
def run():
    webbrowser.open(run)
open_button=Button(root,text="Open file",command=openfile,image=open_img)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root,text="SAVE",image=save_img,command=save)
save_button.place(relx=0.12,rely=0.03,anchor=CENTER)
run_button=Button(root,text="RUN",image=run_img,command=run)
run_button.place(relx=0.19,rely=0.03,anchor=CENTER)
root.mainloop()