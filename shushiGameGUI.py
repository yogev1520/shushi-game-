from multiprocessing import Event
import time
import PySimpleGUI as sg
import shushiGame

#layout  contin elements mining (button, text, menu .... )
layout = [

    [sg.Text("<<< bot made by >>> ")],
    [sg.Text("<<< Yogev Shushan >>>")],
    [sg.Button("Close"),sg.Button("createFood")],
    [sg.Button("openGameView"),sg.Button("skipAdds")],
    [sg.Button("picCoin")],
    [sg.Button("Food1"),sg.Button("Food2")],
    [sg.Button("Food3"),sg.Button("Food4")],
    [sg.Button("Food5"),sg.Button("Food6")],
    [sg.Button("Food7"),sg.Button("Food8")]
]

#window settings and display
window = sg.Window("shushiGameBot",layout,location=(1030,70),keep_on_top=True, element_padding=(1,1))

#loop thet hold the gui fonctions and connecte the > button ("name") < and events 

while True:
    event, values = window.Read(timeout=10)#read from window
    if event == sg.WIN_CLOSED or event == "Close" :
        break
    elif event == "openGameView":
        shushiGame.openBrowser()
    elif event == "skipAdds":
        shushiGame.skipAdds()
    elif event == "picCoin":
        shushiGame.picCoin()
    elif event == "Food1":
        shushiGame.onigiri()
        print("food1")
    elif event == "Food2":
        shushiGame.roe_maki()
    elif event == "createFood":
        shushiGame.CreateFood()
    elif event == "Food3":
        shushiGame.gunkan_maki()
    elif event == "Food4":
        print("event food4")
        shushiGame.sake_roll()
    elif event == "Food5":
        print("event food5")
        shushiGame.unagi_nigiri()
    elif event == "Food6":
        shushiGame.california_Roll()
    elif event == "Food7":
        shushiGame.Ebi_nigiri()
    elif event == "Food8":
        shushiGame.ringu_maki()
    else: {}
        
