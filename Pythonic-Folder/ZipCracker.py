from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import zipfile
import pyzipper
import time
import _tkinter
import os
from threading import Thread
from images_ import img1, img2, img3, img4

root = Tk()


def getfile():

    while True:

        password_cracked = False

        file = filedialog.askopenfilename(title='Zip file to crack')
        if len(file) > 1:
            if zipfile.is_zipfile(file):
                lb4.configure(text=file)
                messagebox.showinfo(title='File Selected', message=f'Success {file}')
                zf = pyzipper.AESZipFile(file, 'r',  compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES)
                fname = file.split('/')[-1]
                load_list = messagebox.showinfo(title='Word List', message='Press Ok To Select A Password List')
                wdlist = filedialog.askopenfilename(title='Password List')
                pwdlen = len(list(open(wdlist, 'rb')))
                lb6 = Label(lb5, text=f'Passwords : {pwdlen}' ,width=90, height=2, background='black', fg='cyan', font=('Arial', 9))
                lb6.place(x=-253, y=10)
                lb8 = Label(lb5, text=f'Brute Force : Running' , width=40, height=2, background='black', fg='cyan', font=('Arial', 9))
                lb8.place(x=-82, y=40)
                lb9 = Label(lb5, width=40, height=2, background='black', fg='cyan', font=('Arial', 9))
                lb9.place(x=-60, y=70)
                time.sleep(1)
                with open(wdlist, 'rb') as wordlist:
                    passwordsList = wordlist.readlines()
                
                if len(passwordsList) < 1:

                    break

                for word in passwordsList:
                    password = word.strip()

                    try: 
                        zf.extractall(pwd=password)
                        lb9.configure(text=f'Password Cracked : {password.decode()}')
                        messagebox.showinfo(title='Password Cracked', message=f'Password : {password.decode()}\n\nFollow on instagram : Apkaless')
                        password_cracked = True
                        break

                    except _tkinter.TclError:
                        pass

                    except KeyboardInterrupt:
                        root.destroy()
                        exit(0)

                    except:
                        lb9.configure(text=f'Current Password : {password.decode()}')

                lb6 = Label(lb5, text=f'Number Of Passwords in List : {pwdlen}' ,width=90, height=2, background='black', fg='cyan', font=('Arial', 8))
                lb6.place(x=-190, y=10)

                lb8.configure(text='Brute Force : Finished')

                if password_cracked == False:

                    lb9.configure(text='Password Not Found', width=25, height=2)
                    lb9.place(x=-30, y=70)

                break
                       
            else:
                messagebox.showerror(title='File Type Error', message='The Selected File Not Correct!')
                break
        else:
            messagebox.showerror(title='No File Selected', message='You Havn\'t Selected Any File')
            break
    os.remove('pngegg3.png')
    os.remove('pngegg4.png')
    os.remove('pngegg5.png')
    os.remove('applogo.png')
    exit(0)
# root configuration
root.geometry('700x500')
root.resizable(False,False)

icodata = img4[0]

with open('applogo.png', 'wb') as f:
    f.write(icodata)


img = PhotoImage(file='applogo.png')
root.wm_iconphoto(False, img)

root.title('ZIP FILES CRACKER SCRIPTED BY APKALESS IRAQ')
root.configure(background='black')

#==================================================================

# widgets

# set the image

p1 = img1[0]
p2 = img2[0]
p3 = img3[0]

with open('pngegg3.png', 'wb') as f:
    f.write(p1)
with open('pngegg4.png', 'wb') as f:
    f.write(p2)

with open('pngegg5.png', 'wb') as f:
    f.write(p3)
    
bgimg = PhotoImage(file='pngegg3.png')
bgimg2 = PhotoImage(file='pngegg4.png')
bgimg3 = PhotoImage(file='pngegg5.png')

# set canvas
canvas = Canvas(root, width=700, height=700, bg='black', borderwidth='0', highlightbackground='black', highlightthickness=1)
canvas.pack(fill = 'both', expand = True)
canvas.place(x=0, y=0)
canvas.create_image(50,250, image=bgimg)

canvas2 = Canvas(canvas, width=300, height=700, highlightthickness=0, highlightbackground='black', highlightcolor='black', background='black')
canvas2.place(x=500,y=0)
canvas2.create_image(50,250, image=bgimg3)

#set frame that contains the rights
frame = Frame(root, width=400, height=100, background='black', highlightbackground='red')
frame.place(x=25, y=40)

#set label
lb = Label(root, text='Script By: Apkaless IRAQ', fg='green', bg='black', font=('Arial', 13))
lb.place(x=30, y=45)

lb2 = Label(root, text='Password Breacher', fg='red', bg='black', font=('Arial', 14))
lb2.place(x=30, y=77)

lb3 = Label(frame, image=bgimg2, background='black', width=400, height=400)
lb3.place(x=180, y=0)


#set ask for file
lb4 = Label(root, width=62, height=2, background='black', fg='cyan', font=('Arial', 10))
lb4.place(x=0, y=200)

lb5 = Label(root, width=60, height=100, background='black', fg='cyan', font=('Arial', 9))
lb5.place(x=0, y=330)

#set btn

button = Button(root, text='Click Here To Select A File', width=40, height=1, background='black', font=('Arial', 11), fg='cyan', command=Thread(target=getfile).start)
button.place(x=55, y=250)
button.configure(highlightthickness=1, highlightcolor='cyan', borderwidth=1, highlightbackground='cyan')
os.remove('pngegg3.png')
os.remove('pngegg4.png')
os.remove('pngegg5.png')
os.remove('applogo.png')
root.mainloop()