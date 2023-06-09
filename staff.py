#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Dec 17, 2020 01:47:04 PM IST  platform: Windows NT

import sys
import pymongo
from bson import ObjectId
import mysql.connector
from mysql.connector import Error
from fpdf import FPDF
import tkinter
import tkinter.messagebox as tkMessageBox

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

import staff_support
teacher="ab"

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    staff_support.init(root, top)
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
    staff_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def searchcourse(self):
        try:
            inputcc = self.staffccodetb.get('1.0', 'end')
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='aef_database',
                                                     user='root',
                                                     password='toor')
                #sql_select_Query = "select name from student where usn='input'" # sql command q is assign to query variable
                q="select course_title from course where course_code='"+input+"'"
                sql_select_Query=q
                cursor = connection.cursor()
                cursor.execute(sql_select_Query)
                records = cursor.fetchall()
                self.staffctlb.delete(0, self.staffctlb.size())
                if(cursor.rowcount==0):
                    connection.close()
                    cursor.close()
                    connection = mysql.connector.connect(host='localhost',
                                                         database='aef_database',
                                                         user='root',
                                                         password='toor')
                    q="select lcourse_title from lab_course where lcourse_code='"+input+"'"
                    sql_select_Query=q
                    cursor = connection.cursor()
                    cursor.execute(sql_select_Query)
                    records = cursor.fetchall()
                    self.staffctlb.delete(0, self.staffctlb.size())
                    if(cursor.rowcount==0):
                        tkMessageBox.showerror("Error", "This course does not exist in the database")
                    else:
                        for i in range(0, (cursor.rowcount)):
                            self.staffctlb.insert(i, records[i])
                        teacher="present"
                else:
                    for i in range(0, (cursor.rowcount)):
                        self.staffctlb.insert(i, records[i])
                    teacher="present"
            except Exception:
                tkMessageBox.showerror("Error", "Could not reach the server at the movement..please try later..")
            finally:
                if (connection.is_connected()):
                    connection.close()
                    cursor.close()
        except Exception:
            tkMessageBox.showerror("Error", "please enter correct course code you are teaching..")


    def attinfo(self):
        if(teacher == 'ab'):
            tkMessageBox.showerror("Error", "Please enter your course code.. and press Search Button..")
        else:
            #mongoDB code to store attendance
            usn = self.usntb.get('1.0', 'end')
            usn=str.rstrip(usn)
            attendance=self.attendancetb.get('1.0', 'end')
            attendance=str.rstrip(attendance)
            attendance=int(attendance)
            connection=pymongo.MongoClient('localhost', 27017)

            database = connection['aef_database']

            collection = database['student_info']
            collection.update_one({'USN': usn}, {"$set":{'Attendance':attendance}}, upsert=True)
            
            
            
            tkMessageBox.showerror("Success", "Successfully Updated attendance information")
    def logoutfun(self):
        quit()

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1184x759+354+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Staff")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.034, rely=0.04, relheight=0.929, relwidth=0.941)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.314, rely=0.057, height=26, width=442)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#00ff00")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''WELCOME BACK ! - TEACHER''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.224, rely=0.241, height=26, width=183)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ENTER COURSE CODE :''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.215, rely=0.567, height=26, width=182)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''ENTER STUDENT USN :''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.206, rely=0.681, height=26, width=202)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ATTENDACE SHORTAGE :''')

        self.staffccodetb = tk.Text(self.Frame1)
        self.staffccodetb.place(relx=0.422, rely=0.241, relheight=0.048
                , relwidth=0.201)
        self.staffccodetb.configure(background="white")
        self.staffccodetb.configure(font="TkTextFont")
        self.staffccodetb.configure(foreground="black")
        self.staffccodetb.configure(highlightbackground="#d9d9d9")
        self.staffccodetb.configure(highlightcolor="black")
        self.staffccodetb.configure(insertbackground="black")
        self.staffccodetb.configure(selectbackground="blue")
        self.staffccodetb.configure(selectforeground="white")
        self.staffccodetb.configure(wrap="word")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.709, rely=0.241, height=33, width=76)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.searchcourse,text='''Search''')

        self.staffctlb = tk.Listbox(self.Frame1)
        self.staffctlb.place(relx=0.206, rely=0.369, relheight=0.068
                , relwidth=0.654)
        self.staffctlb.configure(background="white")
        self.staffctlb.configure(disabledforeground="#a3a3a3")
        self.staffctlb.configure(font="TkFixedFont")
        self.staffctlb.configure(foreground="#000000")
        self.staffctlb.configure(highlightbackground="#d9d9d9")
        self.staffctlb.configure(highlightcolor="black")
        self.staffctlb.configure(selectbackground="blue")
        self.staffctlb.configure(selectforeground="white")

        self.staffusntb = tk.Text(self.Frame1)
        self.staffusntb.place(relx=0.395, rely=0.567, relheight=0.048
                , relwidth=0.228)
        self.staffusntb.configure(background="white")
        self.staffusntb.configure(font="TkTextFont")
        self.staffusntb.configure(foreground="black")
        self.staffusntb.configure(highlightbackground="#d9d9d9")
        self.staffusntb.configure(highlightcolor="black")
        self.staffusntb.configure(insertbackground="black")
        self.staffusntb.configure(selectbackground="blue")
        self.staffusntb.configure(selectforeground="white")
        self.staffusntb.configure(wrap="word")

        self.staffastb = tk.Text(self.Frame1)
        self.staffastb.place(relx=0.395, rely=0.667, relheight=0.048
                , relwidth=0.12)
        self.staffastb.configure(background="white")
        self.staffastb.configure(font="TkTextFont")
        self.staffastb.configure(foreground="black")
        self.staffastb.configure(highlightbackground="#d9d9d9")
        self.staffastb.configure(highlightcolor="black")
        self.staffastb.configure(insertbackground="black")
        self.staffastb.configure(selectbackground="blue")
        self.staffastb.configure(selectforeground="white")
        self.staffastb.configure(wrap="word")

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.512, rely=0.667, relheight=0.044
                , relwidth=0.101)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''(Yes/No)''')
        self.Message1.configure(width=115)

        self.updatebtn = tk.Button(self.Frame1)
        self.updatebtn.place(relx=0.422, rely=0.894, height=33, width=126)
        self.updatebtn.configure(activebackground="#ececec")
        self.updatebtn.configure(activeforeground="#000000")
        self.updatebtn.configure(background="#d9d9d9")
        self.updatebtn.configure(disabledforeground="#a3a3a3")
        self.updatebtn.configure(foreground="#000000")
        self.updatebtn.configure(highlightbackground="#d9d9d9")
        self.updatebtn.configure(highlightcolor="black")
        self.updatebtn.configure(pady="0")
        self.updatebtn.configure(command=self.attinfo,text='''UPDATE''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.063, rely=0.383, height=26, width=143)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Course Tittle :''')

        self.logoutbtn = tk.Button(self.Frame1)
        self.logoutbtn.place(relx=0.871, rely=0.028, height=33, width=96)
        self.logoutbtn.configure(activebackground="#ececec")
        self.logoutbtn.configure(activeforeground="#000000")
        self.logoutbtn.configure(background="#d9d9d9")
        self.logoutbtn.configure(disabledforeground="#a3a3a3")
        self.logoutbtn.configure(foreground="#000000")
        self.logoutbtn.configure(highlightbackground="#d9d9d9")
        self.logoutbtn.configure(highlightcolor="black")
        self.logoutbtn.configure(pady="0")
        self.logoutbtn.configure(command=self.logoutfun,text='''LOGOUT''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.278, rely=0.766, height=26, width=121)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''REMARKS :''')

        self.remarkstb = tk.Text(self.Frame1)
        self.remarkstb.place(relx=0.395, rely=0.766, relheight=0.048
                , relwidth=0.514)
        self.remarkstb.configure(background="white")
        self.remarkstb.configure(font="TkTextFont")
        self.remarkstb.configure(foreground="black")
        self.remarkstb.configure(highlightbackground="#d9d9d9")
        self.remarkstb.configure(highlightcolor="black")
        self.remarkstb.configure(insertbackground="black")
        self.remarkstb.configure(selectbackground="blue")
        self.remarkstb.configure(selectforeground="white")
        self.remarkstb.configure(wrap="word")

if __name__ == '__main__':
    vp_start_gui()
