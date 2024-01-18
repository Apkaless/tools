import hashlib
import base64
import stat
from threading import Thread
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
import random
import os
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt




window = Tk()

window.geometry('920x920')

window.title('Password Manager')

p_ico = PhotoImage(file='icons/cyber-crime.png')

window.iconphoto(True, p_ico)

window.resizable(width=False, height=False)

window.config(bg='#2f3c42')

def os_username():
    return os.getlogin()

username = os_username()


def generate_salt():

    return random._urandom(16)


def generate_key(salt, password):

    kdf = Scrypt(salt, length=32, n=2**14, r=8, p=1)

    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def key_verify(salt, key, password):

    key = base64.urlsafe_b64decode(key)

    kdf = Scrypt(salt, length=32, n=2**14, r=8, p=1)

    return kdf.verify(password.encode(), key)

def save_salt(salt):

    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/material.txt', 'wb') as f:

        f.write(salt)

        f.close()
    
def save_key(key):

    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/key.key', 'wb') as f:

        f.write(key)

        f.close()

def load_key():
    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/key.key', 'rb') as f:

        key = f.read()

        f.close()

    return key

def load_salt():
    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/material.txt', 'rb') as f:

        salt = f.read()

        f.close()

    return salt



def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def save_password():

    global pwd

    pwd = passwordEntry.get()

    hashed_password = hash_password(pwd)
    
    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/generation.json', 'w') as f:
        data = {'master_password': f'{hashed_password}'}

        jsdata = json.dumps(data)

        f.write(jsdata)

        f.close()
        
    window.destroy()
    messagebox.showinfo(title='Password', message='Password Has Been Saved')
    
def grab_password():

    return passwordEntry.get()
 
def SetPasswordWindow():
    global window
    global passwordEntry

    window = Tk()
    window.config(bg='#2f3c42')
    window.geometry('300x400')
    window.title('Set Password')
    window.resizable(width='False', height='False')
        
    passwordEntry = Entry(window)
    
    passwordEntry.place(relx=0.3, rely=0.3)
    
    set_pass_btn = Button(window)

    set_pass_btn.config(text='Set Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                        command=save_password)
    
    set_pass_btn.place(relx=0.5, rely=0.5, anchor='center')

def LoginWindow():
    global password
    global window
    global ask_for_pass
    window = Tk()
    window.config(bg='#2f3c42')
    window.geometry('300x400')
    window.title('Login')
    window.resizable(width='False', height='False')

    txt = Label(window, text='Enter Your Password', font=('Helvetica', 12), bg='#2f3c42', fg='white')
    txt.place(relx=0.5, rely=0.2, anchor='center')

    ask_for_pass = Entry(window)
    
    ask_for_pass.place(relx=0.3, rely=0.3)
    
    set_pass_btn = Button(window)

    set_pass_btn.config(text='Log in', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                        command=check_password)
    
    set_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    
    all_buttons =[ig_btn, fb_btn, yt_btn, dc_btn, git_btn, ea_btn, ubi_btn, epic_btn, tw_btn]

    for i in all_buttons:
        i.config(state='disabled', background='#2f3c42', fg='white')
    
def check_password():

    pwd = ask_for_pass.get()
    
    data = open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/generation.json', 'r').read()

    jsdata = json.loads(data)

    master = jsdata['master_password']

    hashed_password = hash_password(pwd)

    if master == hashed_password:
        all_buttons =[ig_btn, fb_btn, yt_btn, dc_btn, git_btn, ea_btn, ubi_btn, epic_btn, tw_btn]

        for i in all_buttons:
            i.config(state='normal', background='#2f3c42', fg='white')


        else:
            window.destroy()
    else:
        messagebox.showerror(title='Password', message='Password Incorrect !')
        return  False
    
class image_resizer:

    def __init__(self, width, height) -> None:

        self.height = height
        self.width = width

    def read_image_data(self, img_path):

        image = Image.open(img_path, mode='r')

        return image
    
    def resize(self, img_path):

        img_data = self.read_image_data(img_path)

        resized_img = img_data.resize((self.width, self.height))

        image = ImageTk.PhotoImage(resized_img)

        return image


def on_hover(e):
    
     e.widget.config(bg='white', fg='black')



def on_leave(e):
    
     e.widget.config(bg='#2f3c42', fg='white')     
    
def show_password():
    
    keyword = social_key
    
    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/websites.json', 'rb') as f:

        jsdata = json.loads(f.read())

        key = load_key()

        fernet = Fernet(key)
        
        try:
            
            if keyword == 'IG':

                password = jsdata['Instagram']

                decrypted_password = fernet.decrypt(password.encode())

                ig_window.clipboard_append(decrypted_password)
                ig_window.destroy()
            elif keyword == 'YT':

                password = jsdata['YouTube']
                decrypted_password = fernet.decrypt(password.encode())

                yt_window.clipboard_append(decrypted_password)
                yt_window.destroy()
            elif keyword == 'TW':
                password = jsdata['Twitch']
                decrypted_password = fernet.decrypt(password.encode())

                tw_window.clipboard_append(decrypted_password)
                tw_window.destroy()
            elif keyword == 'GIT':

                password = jsdata['Github']
                decrypted_password = fernet.decrypt(password.encode())

                git_window.clipboard_append(decrypted_password)
                git_window.destroy()
            elif keyword == 'DIS':

                password = jsdata['Discord']
                decrypted_password = fernet.decrypt(password.encode())

                dc_window.clipboard_append(decrypted_password)
                dc_window.destroy()
            elif keyword == 'EA':

                password = jsdata['EA App']
                decrypted_password = fernet.decrypt(password.encode())

                ea_window.clipboard_append(decrypted_password)
                ea_window.destroy()
            elif keyword == 'EPIC':

                password = jsdata['Epic Games']
                decrypted_password = fernet.decrypt(password.encode())

                ep_window.clipboard_append(decrypted_password)
                ep_window.destroy()
            elif keyword == 'UBI':

                password = jsdata['Ubisoft']
                decrypted_password = fernet.decrypt(password.encode())

                ubi_window.clipboard_append(decrypted_password)
                ubi_window.destroy()
            elif keyword == 'FB':

                password = jsdata['Facebook']
                decrypted_password = fernet.decrypt(password.encode())

                fb_window.clipboard_append(decrypted_password)
                fb_window.destroy()
            else:
                messagebox.showerror(title='Error', message='Error')
        except KeyError:
            messagebox.showwarning(title='Password', message='No Password Was Inserted')
            
    messagebox.showinfo(title='Password', message=f'{password} and Saved To Your Clipboard')
    
    Thread(target=show_password).start()
    
def showinfo():

    messagebox.showinfo(title='Success', message='Password Updated')

def insert_password():

    key = load_key()

    fernet = Fernet(key)

    print('Fernet Initialized Success')

    password = insert_password_entry.get()
    print(password)
    keyword = social_key
    print(keyword)

    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/websites.json', 'rb') as f:

        data = f.read()

        jsdata = json.loads(data)

        print(jsdata, type(jsdata))

        if keyword == 'IG':

            encrypted_password = fernet.encrypt(password.encode())
            jsdata['Instagram'] = encrypted_password.decode()
            print('Encrypted_password =', encrypted_password)
            print(jsdata)
        elif keyword == 'YT':
            encrypted_password = fernet.encrypt(password.encode())
            jsdata['YouTube'] = encrypted_password

        elif keyword == 'TW':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Twitch'] = encrypted_password.decode()

        elif keyword == 'GIT':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Github'] = encrypted_password.decode()

        elif keyword == 'DIS':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Discord'] = encrypted_password.decode()

        elif keyword == 'EA':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['EA App'] = encrypted_password.decode()

        elif keyword == 'EPIC':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Epic Games'] = encrypted_password.decode()

        elif keyword == 'UBI':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Ubisoft'] = encrypted_password.decode()

        elif keyword == 'FB':
            encrypted_password = fernet.encrypt(password.encode())
            print('Encrypted_password =', encrypted_password)
            jsdata['Facebook'] = encrypted_password.decode()
        else:
            messagebox.showerror(title='Error', message='Error')

    with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/websites.json', 'w') as f:
        
        f.write(json.dumps(jsdata))
        f.close()


    update_window.destroy()

    messagebox.showinfo(title='Password', message='Password Updated')

def update_password():

    global insert_password_entry
    global update_window
    global social_key

    print('update social key', social_key)

    update_window = Tk()
    update_window.geometry('300x400')
    update_window.resizable(width=False, height=False)
    update_window.title('Insert Password')
    update_window.config(bg='#2f3c42')
    txt = Label(update_window, text='Enter Your Password', font=('Helvetica', 12), bg='#2f3c42', fg='white')
    txt.place(relx=0.5, rely=0.2, anchor='center')

    insert_password_entry = Entry(update_window, relief='flat')
    
    insert_password_entry.place(relx=0.5, rely=0.3, anchor='center')

    show_pass_btn = Button(update_window)

    show_pass_btn.config(text='Insert Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                         command=insert_password)
    
    show_pass_btn.place(relx=0.5, rely=0.5, anchor='center')

    update_window.mainloop()

def instagram_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global ig_window
    social_key = 'IG'
    print('social key', social_key)
    ig_window = Tk()
    ig_window.geometry('300x400')
    ig_window.resizable(width=False, height=False)
    ig_window.title('Instagram')
    ig_window.config(bg='#2f3c42')

    
    update_pass_btn = Button(ig_window)
    
    show_pass_btn = Button(ig_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(ig_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=ig_window).start()

    ig_window.mainloop()

def fb_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global fb_window
    social_key = 'FB'
    print('social key', social_key)
    fb_window = Tk()
    fb_window.geometry('300x400')
    fb_window.resizable(width=False, height=False)
    fb_window.title('Facebook')
    fb_window.config(bg='#2f3c42')
    
    
    update_pass_btn = Button(fb_window)
    
    show_pass_btn = Button(fb_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(fb_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=fb_window).start()

    fb_window.mainloop()

def yt_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global yt_window
    social_key = 'YT'

    yt_window = Tk()
    yt_window.geometry('300x400')
    yt_window.resizable(width=False, height=False)
    yt_window.title('YouTube')
    yt_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(yt_window)
    
    show_pass_btn = Button(yt_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(yt_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=yt_window).start()

    yt_window.mainloop()

def git_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global git_window
    social_key = 'GIT'
    git_window = Tk()
    git_window.geometry('300x400')
    git_window.resizable(width=False, height=False)
    git_window.title('Github')
    git_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(git_window)
    
    show_pass_btn = Button(git_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(git_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=git_window).start()

    git_window.mainloop()

def dc_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global dc_window
    social_key = 'DIS'
    dc_window = Tk()
    dc_window.geometry('300x400')
    dc_window.resizable(width=False, height=False)
    dc_window.title('Discord')
    dc_window.config(bg='#2f3c42')

    
    update_pass_btn = Button(dc_window)
    
    show_pass_btn = Button(dc_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(dc_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=dc_window).start()

    dc_window.mainloop()

def ea_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global ea_window
    social_key = 'EA'
    ea_window = Tk()
    ea_window.geometry('300x400')
    ea_window.resizable(width=False, height=False)
    ea_window.title('EA App')
    ea_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(ea_window)
    
    show_pass_btn = Button(ea_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(ea_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=ea_window).start()

    ea_window.mainloop()

def epic_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global ep_window
    social_key = 'EPIC'
    ep_window = Tk()
    ep_window.geometry('300x400')
    ep_window.resizable(width=False, height=False)
    ep_window.title('Epic Games')
    ep_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(ep_window)
    
    show_pass_btn = Button(ep_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(ep_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=ep_window).start()

    ep_window.mainloop()

def ubi_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global ubi_window
    social_key = 'UBI'
    ubi_window = Tk()
    ubi_window.geometry('300x400')
    ubi_window.resizable(width=False, height=False)
    ubi_window.title('Ubisoft')
    ubi_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(ubi_window)
    
    show_pass_btn = Button(ubi_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(ubi_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=ubi_window).start()

    ubi_window.mainloop()

def tw_creds():
    
    global ask_for_pass
    global social_key
    global go_pass_btn
    global update_pass_btn
    global show_pass_btn
    global tw_window
    social_key = 'TW'
    tw_window = Tk()
    tw_window.geometry('300x400')
    tw_window.resizable(width=False, height=False)
    tw_window.title('Twitch')
    tw_window.config(bg='#2f3c42')

    
    
    update_pass_btn = Button(tw_window)
    
    show_pass_btn = Button(tw_window)

    show_pass_btn.config(text='Show Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12), 
                         command=show_password, state='normal')
    
    show_pass_btn.place(relx=0.5, rely=0.3, anchor='center')
    
    update_pass_btn = Button(tw_window)
    
    update_pass_btn.config(text='Update Password', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', compound='left',padx=5, cursor='hand2',font=('Helvetica', 12),
                           state='normal', command=update_password)
    
    update_pass_btn.place(relx=0.5, rely=0.5, anchor='center')
    

    show_pass_btn.bind('<Enter>', on_hover)
    show_pass_btn.bind('<Leave>', on_leave)
    

    update_pass_btn.bind('<Enter>', on_hover)
    update_pass_btn.bind('<Leave>', on_leave)

    
    Thread(target=tw_window).start()

    tw_window.mainloop()

resizer = image_resizer(40, 40)

igPhoto = resizer.resize('icons/instagram.png')

fbPhoto = resizer.resize('icons/facebook.png')

ytPhoto = resizer.resize('icons/youtube.png')

canvas = Canvas(window, width=820, height=820)
canvas.config(background='#2f3c42', relief='flat', highlightbackground='#2f3c42', highlightcolor='#2f3c42', highlightthickness=3)
canvas.place(relx=0.5, rely=0.5, anchor='center')

frame = Frame(canvas)

frame.config(bg='#2f3c42', width=600, height=200)

frame.place(x=120, rely=0.1)

ig_btn = Button(frame)

ig_btn.config(text='Instagram', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=igPhoto, compound='left',padx=5, cursor='hand2',
              command=instagram_creds, font=('Helvetica', 12))

ig_btn.place(relx=0.5, rely=0.5, anchor='center')


fb_btn = Button(frame)

fb_btn.config(text='Facebook', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=fbPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
              command=fb_creds)

fb_btn.place(relx=0.2, rely=0.5, anchor='center')


yt_btn = Button(frame)

yt_btn.config(text='YouTube', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=ytPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
               command=yt_creds)

yt_btn.place(relx=0.8, rely=0.5, anchor='center')

#==================================================================================================================

dcPhoto = resizer.resize('icons/discord.png')

twPhoto = resizer.resize('icons/twitch.png')

gitPhoto = resizer.resize('icons/github.png')

frame2 = Frame(canvas)

frame2.config(bg='#2f3c42', width=600, height=200)

frame2.place(x=120, rely=0.3)

dc_btn = Button(frame2)

dc_btn.config(text='Discord', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=dcPhoto, compound='left',padx=5,cursor='hand2', font=('Helvetica', 12),
               command=dc_creds)

dc_btn.place(relx=0.5, rely=0.5, anchor='center')


tw_btn = Button(frame2)

tw_btn.config(text='Twitch', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=twPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
               command=tw_creds)

tw_btn.place(relx=0.2, rely=0.5, anchor='center')


git_btn = Button(frame2)

git_btn.config(text='Github', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=gitPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
               command=git_creds)

git_btn.place(relx=0.8, rely=0.5, anchor='center')


#==================================================================================================================

epicPhoto = resizer.resize('icons/epicg.png')

eaPhoto = resizer.resize('icons/ea.png')

ubiPhoto = resizer.resize('icons/ubisoft.png')

frame3 = Frame(canvas)

frame3.config(bg='#2f3c42', width=600, height=200)

frame3.place(x=120, rely=0.5)

epic_btn = Button(frame3)

epic_btn.config(text='Epic Games', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=epicPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
                command=epic_creds)

epic_btn.place(relx=0.5, rely=0.5, anchor='center')


ea_btn = Button(frame3)

ea_btn.config(text='Ea App', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=eaPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
              command=ea_creds)

ea_btn.place(relx=0.2, rely=0.5, anchor='center')


ubi_btn = Button(frame3)

ubi_btn.config(text='Ubisoft', background='#2f3c42', fg='white', bd='1', highlightthickness='3', highlightcolor='white', highlightbackground='#2f3c42', relief='flat', image=ubiPhoto, compound='left',padx=5, cursor='hand2', font=('Helvetica', 12),
               command=ubi_creds)

ubi_btn.place(relx=0.8, rely=0.5, anchor='center')



if __name__ == '__main__':

    try:

        with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/websites.json', 'r') as f:
            pass
    
    except:
        
        with open(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/websites.json', 'w') as f:
            
            data = {}

            jsdata = json.dumps(data)

            f.write(jsdata)


    all_buttons =[ig_btn, fb_btn, yt_btn, dc_btn, git_btn, ea_btn, ubi_btn, epic_btn, tw_btn]
    
    try:
        with open(f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\generation.json', 'r') as f:
            
            LoginWindow()

    except:

        for btn in all_buttons:
            btn.config(state='disabled')
        
        SetPasswordWindow()

        password = grab_password()

        print(password)

        salt = generate_salt()

        save_salt(salt)

        key = generate_key(salt, password)

        save_key(key)

    for btn in all_buttons:
        btn.bind('<Enter>', on_hover)


    for btn in all_buttons:
    
        btn.bind('<Leave>', on_leave)


    target=window.mainloop()