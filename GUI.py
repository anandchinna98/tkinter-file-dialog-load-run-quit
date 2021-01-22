import tkinter as tk
from tkinter import filedialog, messagebox, ttk ,Frame
from threading import Thread
import time
import os
import tkinter.messagebox       
import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

# Setting icon of master window
root.geometry("500x500") 
root.pack_propagate(False)
root.resizable(0, 0) 

#  TreeView
frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.place(height=250, width=500)

#  open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, rely=0.55, relx=0)

# process_frame
process_frame = tk.LabelFrame(root, text="Process")
process_frame.place(height=100,width=400 , rely=0.75 , relx=0)


# Buttons
button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.65, relx=0.30)


# file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)


## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) 
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 

#function for file and load

def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("csv files", "*.csv"),("All Files", "*.*")))
    label_file["text"] = filename
    return None

def Load_excel_data():
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f" {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) 

    df_rows = df.to_numpy().tolist() 
    for row in df_rows:
        tv1.insert("", "end", values=row) 

    

#function for main.py intergeration

def helloCallBack():
    messagebox.askquestion("Info panel", "Are you sure?")
    os.system('main.py')
    messagebox.showinfo("Info","completed sucessfully")
button11 = tk.Button(root, text ="RUN", command = helloCallBack)
button11.place(x=25, y=410)



def helloCallBack():
    messagebox.askquestion("askquestion", "Are you sure?")
    print("hello")
    messagebox.showinfo("Info","processing...")
button11 = tk.Button(root, text ="RUN", command = helloCallBack)
button11.place(x=25, y=410)


# Button for closing 
def Close(): 
    root.destroy() 
exit_button = tk.Button(root, text="QUIT", width=4, height=2 ,command=Close) 
exit_button.place(x=440 ,y=410)

#data clear form 
def clear_data():
    tv1.delete(*tv1.get_children())
    return None

#tool title and running page
root.title("SEO TOOl".center(110))
root.mainloop()

