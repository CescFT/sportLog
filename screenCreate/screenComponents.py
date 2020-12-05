import tkinter as tk
from tkinter import ttk
import os
import sys
import functools
from eventListeners.buttonListeners import *

def setPositionOfElementsInFrame(dictParams):
    if dictParams['positionFrame'] == 'top':
        frameButtons = tk.Frame(master=dictParams['frame'])
        labelInfoTop = tk.Label(master=dictParams['frame'], text="Sistema de control de rutina esportiva. Aquí podràs veure els logs que insertis")
        labelInfoTop.pack(padx=5, pady=20)

        buttonReminders = generateButtonReminders({
            'screen': dictParams['screen'],
            'frame': frameButtons
        })
                
        buttonStatistics = generateStatisticsButton({
            'screen': dictParams['screen'],
            'frame': frameButtons
        })

        buttonListReminders = generateButtonListReminders({
            'screen': dictParams['screen'],
            'frame': frameButtons
        })
        
        buttonReminders.pack(padx=5, pady=5, side="left")
        buttonStatistics.pack(padx=5, pady=5, side="left")
        buttonListReminders.pack(padx=5, pady=5, side="left")
        frameButtons.pack()
    
    elif dictParams['positionFrame'] == 'bottom':
        frameTree = tk.Frame(master=dictParams['frame'])
        frameButtonsLogActions = tk.Frame(master=dictParams['frame'])
        labelInfoDB = tk.Label(master=dictParams['frame'], text="Accions log:")
        labelInfoDB.pack()

        tree = ttk.Treeview(frameTree)

        buttonCreate = generateCreateButton({
            'frame': frameButtonsLogActions,
            'screen': dictParams['screen']
        })

        buttonEditLog = generateEditLogButton({
            'screen': dictParams['screen'],
            'frame': frameButtonsLogActions,
            'treeView': tree
        })

        buttonDeleteLog = generateDeleteLogButton({
            'screen': dictParams['screen'],
            'frame': frameButtonsLogActions,
            'treeView': tree
        })

        buttonCreate.pack(side="left", padx=5, pady=5)
        buttonEditLog.pack(side="left", padx=5, pady=5)
        buttonDeleteLog.pack(side="left", padx=5, pady=5)
        frameButtonsLogActions.pack()

        tree["columns"] = ("C1", "C2", "C3", "C4")
        tree.column("#0", width=60, minwidth=60, stretch=tk.NO)
        tree.column("C1", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C2", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C3", width=200, minwidth=200, stretch=tk.NO)
        tree.column("C4", width=200, minwidth=200, stretch=tk.NO)
        tree.heading("#0", text="ID", anchor=tk.W)
        tree.heading("C1", text="Esport", anchor=tk.W)
        tree.heading("C2", text="Durada", anchor=tk.W)
        tree.heading("C3", text="Dia esport", anchor=tk.W)
        tree.heading("C4", text="Dificultat", anchor=tk.W)

        
        for i in range(20):
            tree.insert("", i, text="Log {}".format(i), values=("esport","durada","diaesport", "dificultat"))
        
        vsb = ttk.Scrollbar(frameTree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        

        tree.pack(side="left", expand=True)
        vsb.pack(side='right', fill='y')
        frameTree.pack(padx=5, pady=5)
        

def getProgramIcon():
    basedir = os.path.dirname(sys.modules['__main__'].__file__)
    for root, dirs, files in os.walk(basedir):
        if "logoLogsSport.ico" in files:
            return os.path.join(root, "logoLogsSport.ico")
    return ""

def generateButtonListReminders(configParams):
    buttonListReminders = tk.Button(master=configParams['frame'], text="Llistar recordatoris")
    buttonListReminders['command'] = functools.partial(buttonListRemindersListener ,configParams['screen'], buttonListReminders)
    return buttonListReminders

def generateButtonReminders(configParams):
    buttonCreateReminder = tk.Button(master=configParams['frame'], text="Crear recordatori")
    buttonCreateReminder['command'] = functools.partial(buttonCreateReminderListener ,configParams['screen'], buttonCreateReminder)
    return buttonCreateReminder

def generateStatisticsButton(configParams):
    buttonStatistics = tk.Button(master=configParams['frame'], text="Estadístiques")
    buttonStatistics['command'] = functools.partial(buttonStatisticsListener ,configParams['screen'], buttonStatistics)
    return buttonStatistics

def generateEditLogButton(configParams):
    buttonEditLog = tk.Button(master=configParams['frame'], text="Editar log(s)")
    buttonEditLog['command'] = functools.partial(buttonEditLogListener ,configParams['screen'], buttonEditLog, configParams['treeView'])
    return buttonEditLog

def generateDeleteLogButton(configParams):
    buttonDeleteLog = tk.Button(master=configParams['frame'], text="Eliminar log")
    buttonDeleteLog['command'] = functools.partial(buttonDeleteLogListener ,configParams['screen'], buttonDeleteLog, configParams['treeView'])
    return buttonDeleteLog

def generateCreateButton(configParams):
    buttonCreateLog = tk.Button(master = configParams['frame'], text="Crear Log")
    buttonCreateLog['command'] = functools.partial(buttonCreateListener,configParams['screen'], buttonCreateLog)
    return buttonCreateLog

def generateFrames(screen):
    frame_buttons = tk.Frame(master=screen, height=100)
    frame_logs = tk.Frame(master=screen, height=477)

    return {'frameButtons':frame_buttons, 'frameLogs':frame_logs}

def setWindowAttributes():
    root = tk.Tk()
    root.geometry("1000x500")
    root.minsize(890, 400)
    programIcon = getProgramIcon()
    if programIcon:
        root.iconbitmap(programIcon)
    root.winfo_toplevel().title("Sport log - CONTROL DE LA RUTINA ESPORTIVA")
    return root

def executeScreen(tkScreen):
    tkScreen.mainloop()

def packFrames(elementsToShow):
    for elementName, elementToPack in elementsToShow.items():
        elementToPack.pack(fill=tk.BOTH, side=tk.TOP, expand=True)