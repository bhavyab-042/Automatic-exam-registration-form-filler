#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Dec 12, 2020 09:07:47 PM IST  platform: Windows NT

import sys
import mysql.connector
from mysql.connector import Error
import tkinter
import tkinter.messagebox as tkMessageBox
from subprocess import call

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_form_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    login_form_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    login_form_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def loginfun(self):
        try:
            username = self.useridtb.get('1.0', 'end')
            password = self.passwordtb.get('1.0', 'end')
            if(username=='admin@rvce\n'):
                if(password=='rvcepass\n'):
                    self.useridtb.delete("1.0","end")
                    self.passwordtb.delete("1.0","end")
                    call(["python", "collage_admin.py"])
                else:
                    tkMessageBox.showerror("Error", "Wrong PASSWORD...Please retry..")
            elif(username=='staff@rvce\n'):
                if(password=='rvcepass\n'):
                    self.useridtb.delete("1.0","end")
                    self.passwordtb.delete("1.0","end")
                    call(["python", "staff.py"])
                else:
                    tkMessageBox.showerror("Error", "Wrong PASSWORD...Please retry..")
            elif(username=='bank@rvce\n'):
                if(password=='rvcepass\n'):
                    self.useridtb.delete("1.0","end")
                    self.passwordtb.delete("1.0","end")
                    call(["python", "bank.py"])
                else:
                    tkMessageBox.showerror("Error", "Wrong PASSWORD...Please retry..")
            elif(username=='coordinator@rvce\n'):
                if(password=='rvcepass\n'):
                    self.useridtb.delete("1.0","end")
                    self.passwordtb.delete("1.0","end")
                    call(["python", "course_coordinator.py"])
                else:
                    tkMessageBox.showerror("Error", "Wrong PASSWORD...Please retry..")
            elif(username=='examdept@rvce\n'):
                if(password=='rvcepass\n'):
                    self.useridtb.delete("1.0","end")
                    self.passwordtb.delete("1.0","end")
                    call(["python", "exam_dept.py"])
                else:
                    tkMessageBox.showerror("Error", "Wrong PASSWORD...Please retry..")
            else:
                #sql_Query to find username
                print("username does not exist")
        except Exception:
            tkMessageBox.showerror("Error", "Please enter a valid USERNAME and PASSWORD")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1299x787+343+122")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Login Page")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.022, rely=0.037, relheight=0.933
                , relwidth=0.955)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.234, rely=0.368, height=47, width=199)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#c0c0c0")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''USER ID :''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.234, rely=0.518, height=47, width=195)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#c0c0c0")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''PASSWORD :''')

        self.useridtb = tk.Text(self.Frame1)
        self.useridtb.place(relx=0.435, rely=0.368, relheight=0.06
                , relwidth=0.278)
        self.useridtb.configure(background="white")
        self.useridtb.configure(font="TkTextFont")
        self.useridtb.configure(foreground="black")
        self.useridtb.configure(highlightbackground="#d9d9d9")
        self.useridtb.configure(highlightcolor="black")
        self.useridtb.configure(insertbackground="black")
        self.useridtb.configure(selectbackground="blue")
        self.useridtb.configure(selectforeground="white")
        self.useridtb.configure(wrap="word")

        self.Text1 = tk.Text(self.Frame1)
        self.Text1.place(relx=0.971, rely=1.038, relheight=0.183, relwidth=0.336)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.363, rely=0.218, height=47, width=284)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#0000ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''PLEASE LOGIN...!''')

        self.loginbtn = tk.Button(self.Frame1)
        self.loginbtn.place(relx=0.419, rely=0.695, height=33, width=136)
        self.loginbtn.configure(activebackground="#ececec")
        self.loginbtn.configure(activeforeground="#000000")
        self.loginbtn.configure(background="#d9d9d9")
        self.loginbtn.configure(disabledforeground="#a3a3a3")
        self.loginbtn.configure(foreground="#000000")
        self.loginbtn.configure(highlightbackground="#d9d9d9")
        self.loginbtn.configure(highlightcolor="black")
        self.loginbtn.configure(pady="0")
        self.loginbtn.configure(command=self.loginfun,text='''LOGIN''')

        self.passwordtb = tk.Text(self.Frame1)
        self.passwordtb.place(relx=0.435, rely=0.518, relheight=0.06
                , relwidth=0.273)
        self.passwordtb.configure(background="white")
        self.passwordtb.configure(font="TkTextFont")
        self.passwordtb.configure(foreground="black")
        self.passwordtb.configure(highlightbackground="#d9d9d9")
        self.passwordtb.configure(highlightcolor="black")
        self.passwordtb.configure(insertbackground="black")
        self.passwordtb.configure(selectbackground="blue")
        self.passwordtb.configure(selectforeground="white")
        self.passwordtb.configure(wrap="word")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.331, rely=0.054, height=35, width=355)
        self.Label2.configure(background="#00ff00")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''WELCOME TO AUTOMATIC EXAM FORM FILLER''')

if __name__ == '__main__':
    vp_start_gui()