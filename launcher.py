import os
os.system("pip install requests")
os.system("cls")
import requests
import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser
import shutil

app_VERSION = '1.1'

application_get_url = "https://unerasable.github.io/application.json"


window = tkinter.Tk()
window.title("Erased Launcher")
window.geometry("500x500")
window.resizable(0, 0)

window.configure(background='#282c34')
def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_application_get_url():
    request = requests.get(application_get_url)
    data = check_valid_status_code(request)
    return data
app_URL=get_application_get_url()

checkAppVer = f"{app_URL['erasedLauncher']['version']}"
icon_url = f"{app_URL['erasedLauncher']['appIcon']}"
r = requests.get(icon_url)
with open(f"ErasedLauncherIcon.ico",'wb') as f:
    f.write(r.content)
window.iconbitmap('ErasedLauncherIcon.ico')
def download_ErasedRPG():
    application_URL = f"{app_URL['erasedRPG']['downloadURL']}"
    application_NAME = f"{app_URL['erasedRPG']['name']}"
    install_Location = instLoc.get()
    try:
        if install_Location == "":
            install_Location = f"./{application_NAME}/"
            os.mkdir(install_Location)
        else:
            install_Location = f"{install_Location}/{application_NAME}/"
            os.mkdir(install_Location)
    
        r = requests.get(application_URL)
        with open(f"{install_Location}{application_NAME}.exe",'wb') as f:
            f.write(r.content)
        original = f"{install_Location}{application_NAME}.exe"
        target = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/{application_NAME}.exe"
        shutil.copyfile(original, target)
        # add a message box to say that the application has been downloaded
        messagebox.showinfo("Application Downloaded", "The application has been downloaded to the specified location")
    except Exception as e:
        print(e)
        #message box to say that the application could not be downloaded
        messagebox.showerror("Application Download Error", f"The application could not be downloaded.\n{e}")
def download_ProcastinatorMotivator():
    application_URL = f"{app_URL['procastinatorMotivator']['downloadURL']}"
    application_NAME = f"{app_URL['procastinatorMotivator']['name']}"
    install_Location = instLoc.get()
    try:
        if install_Location == "":
            install_Location = f"./{application_NAME}/"
            os.mkdir(install_Location)
        else:
            install_Location = f"{install_Location}/{application_NAME}/"
            os.mkdir(install_Location)
    
        r = requests.get(application_URL)
        with open(f"{install_Location}{application_NAME}.exe",'wb') as f:
            f.write(r.content)
        original = f"{install_Location}{application_NAME}.exe"
        target = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/{application_NAME}.exe"
        shutil.copyfile(original, target)
        # add a message box to say that the application has been downloaded
        messagebox.showinfo("Application Downloaded", "The application has been downloaded to the specified location")
    except Exception as e:
        print(e)
        #message box to say that the application could not be downloaded
        messagebox.showerror("Application Download Error", f"The application could not be downloaded.\n{e}")

def download_ApplicationRPC():
    application_URL = f"{app_URL['applicationRPC']['downloadURL']}"
    application_NAME = f"{app_URL['applicationRPC']['name']}"
    install_Location = instLoc.get()
    try:
        
        if install_Location == "":
            install_Location = f"./{application_NAME}/"
            os.mkdir(install_Location)
        else:
            install_Location = f"{install_Location}/{application_NAME}/"
            os.mkdir(install_Location)
    
        r = requests.get(application_URL)
        with open(f"{install_Location}{application_NAME}.exe",'wb') as f:
            f.write(r.content)
        original = f"{install_Location}{application_NAME}.exe"
        target = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/{application_NAME}.exe"
        shutil.copyfile(original, target)
        # add a message box to say that the application has been downloaded
        messagebox.showinfo("Application Downloaded", "The application has been downloaded to the specified location")
    except Exception as e:
        print(e)
        #message box to say that the application could not be downloaded
        messagebox.showerror("Application Download Error", f"The application could not be downloaded.\n{e}")


if checkAppVer == app_VERSION:
    # add a lable to the window
    label = tkinter.Label(window, text="Erased Launcher is up to date", bg='#282c34', fg='#00ff00')
    label.pack()
    # install Location
    inst = tkinter.Label(window, text="Install Location", bg='#282c34', fg='#00ff00')
    inst.pack()
    instLoc = tkinter.Entry(window)
    instLoc.pack()
    # add an empty label
    empty = tkinter.Label(window, text="", bg='#282c34', fg='#00ff00')
    empty.pack()
    # download button
    downloadErasedRPG = tkinter.Button(window, text="Download Erased RPG",bg='#a2a6c2', fg='#282c34', command=lambda: download_ErasedRPG())
    downloadErasedRPG.pack()
    # add a empty label
    emptyLabel1 = tkinter.Label(window, text="", bg='#282c34', fg='#00ff00')
    emptyLabel1.pack()
    # downloadProcastinatorMotivator
    downloadProcastinatorMotivator = tkinter.Button(window, text="Download Procastinator Motivator",bg='#a2a6c2', fg='#282c34', command=lambda: download_ProcastinatorMotivator())
    downloadProcastinatorMotivator.pack()
    # add a empty label
    emptyLabel = tkinter.Label(window, text="", bg='#282c34', fg='#00ff00')
    emptyLabel.pack()
    # downloadApplicationRPC
    downloadApplicationRPC = tkinter.Button(window, text="Download Application RPC",bg='#a2a6c2', fg='#282c34', command=lambda: download_ApplicationRPC())
    downloadApplicationRPC.pack()
else:
    # add a lable to the window
    label = tkinter.Label(window, text="Erased Launcher is outdated", bg='#282c34', fg='#ff0000')
    label.pack()
    # add a button to the window
    button = tkinter.Button(window, text="Update", bg='#282c34', fg='#00ff00', command=lambda: webbrowser.open("http://github.com/Unerasable/ErasedLauncher"))
    button.pack()


window.mainloop()