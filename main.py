import threading
import tkinter as tk
import random, time, pyautogui, webbrowser

stop_program = False

def run_popup():
    def on_close():
        global stop_program
        stop_program = True
        popup.destroy()

    popup = tk.Tk()
    popup.title("Popup")
    popup.geometry("300x200")
    popup.protocol("WM_DELETE_WINDOW", on_close)

    popup.mainloop()

def main_program():
    while not stop_program:
        print("Program is running...")


        movies = ["The Office"]

        #SHOWS & URLS
        #"Chowder","Legend of Korra","The Office"
        Chowder = []
        Legend_Of_Korra = []
        The_Office_Season1 = []
        The_Office_Season2 = []
        The_Office_Season3 = []



        firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'


        searchLocation = [263,105]#[763,105]
        playLocation = [1082,648]
        restartTime = 660#1440#30#1440


        def opencloseURL(url):
            webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
            webbrowser.get('firefox').open_new(url)



            time.sleep(8)
            pyautogui.moveTo(playLocation) #start video
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.press('f')
            pyautogui.moveTo(10,10)



            time.sleep(restartTime) #VIDEO TIME UNTIL CLOSING/PLAYING NEXT
            pyautogui.press('escape')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(0.5)
            #pyautogui.hotkey('ctrl', 'w')
            time.sleep(1.5) #RESTART & PLAY NEXT





        time.sleep(5)
        #print("Program Running")

        while False: #URL COPY PASTE THING
            #Click URL
            pyautogui.moveTo(searchLocation)
            pyautogui.click()
            #COPY
            pyautogui.hotkey('ctrl','a')
            pyautogui.hotkey('ctrl','c')
            #ALT TAB TO CODE
            pyautogui.hotkey('alt','tab')
            #"" > PASTE > "" > ,
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','z')
            time.sleep(0.5)
            pyautogui.write("'")
            time.sleep(0.5)
            pyautogui.hotkey('ctrl','v')
            time.sleep(0.5)
            pyautogui.write("',")
            #ALT TAB
            print("Click Now")
            time.sleep(3)
            #REPEAT


        while True:
            firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            showChoice = random.choice(movies)
            if showChoice == "Chowder":
                url = random.choice(Chowder)
            if showChoice == "Legend of Korra":
                url = random.choice(Legend_Of_Korra)
            if showChoice == "The Office":
                officeSeasons = []
                officeSeasons.extend(The_Office_Season1)
                officeSeasons.extend(The_Office_Season2)
                officeSeasons.extend(The_Office_Season3)
                url = random.choice(officeSeasons)
            if showChoice == "Bojack Horseman":
                bojackSeasons = []
                bojackSeasons.extend(Bojack_Season1)
                bojackSeasons.extend(Bojack_Season2)
                url = random.choice(bojackSeasons)
                
            opencloseURL(url)



# Create and start the popup thread
popup_thread = threading.Thread(target=run_popup)
#popup_thread.start() ####<<<<<<<

# Run the main program
main_program()

# Wait for the popup thread to finish
#popup_thread.join() ####<<<<<<<
