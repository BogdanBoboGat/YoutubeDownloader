from tkinter import *
from backEnd import *

def createGUI():
    backgroundColor = '#FFD2B1'
    buttonColor = '#FFB199'

    # reset command
    def resetGUI():
        nameVideo.config(text='')
        lengthVideo.config(text='')
        audioButton.config(bg=buttonColor)
        videoButton.config(bg=buttonColor)
        downloadButton.config(bg=buttonColor)
        downloadStatus.config(text='')
    
    # exit command
    def exitGUI():
        gui.destroy()

    # get info of video command
    def getURL():
        URL = entryURL.get()
        if checkNetwork():
            if checkVideoURL(URL):
                title, length = videoInfo(str(URL))
                downloadButton.config(bg = 'green')
                nameVideo.config(text=title)
                lengthVideo.config(text=str(length // 60) + ' minutes, ' + str(length % 60) + ' seconds')
            
            else:
                downloadButton.config(bg = 'red')
                nameVideo.config(text='Not Found')
                lengthVideo.config(text='0 minutes, 0 seconds')
        else:
            nameVideo.config(text='No Internet Connection')    

    # commands for format buttons
    def audioCommand():
        audioButton.config(bg='green')
        videoButton.config(bg=buttonColor)
    
    def videoCommand():
        videoButton.config(bg='green')
        audioButton.config(bg=buttonColor)

    # download video
    def downloadVideo():
        audioFormat = audioButton['bg'] == 'green'
        videoFormat = videoButton['bg'] == 'green'
        
        if checkNetwork():
            # URL unselected 
            if downloadButton['bg'] == buttonColor:
                downloadStatus.config(text='Insert URL')
            
            # bad URL
            elif downloadButton['bg'] == 'red':
                downloadStatus.config(text='Video Not Found')
    
            # format unselected
            elif downloadButton['bg'] == 'green' and not audioFormat and not videoFormat:
                downloadStatus.config(text='Choose Format')
            
            # download URL
            elif downloadButton['bg'] == 'green' and (audioFormat or videoFormat):
                URL = entryURL.get()
                downloadURL(URL, audioFormat, videoFormat)
                downloadStatus.config(text='Download Completed')
        else:
            downloadButton.config(bg='red')
            downloadStatus.config(text='No Internet')

    # init GUI
    gui = Tk(className=' Youtube Downloader')
    gui.geometry('800x600')
    gui.configure(bg=backgroundColor)
    gui.resizable(False, False)
    iconImage = PhotoImage(file='photos/iconImage.png')
    gui.iconphoto(False, iconImage)
    
    # background
    background = PhotoImage(file='photos/background.png')
    bgLabel = Label(gui, image=background, bd=0)
    bgLabel.place(x=0, y=0)
    
    # reset button
    resetImage = PhotoImage(file='photos/reset.png')
    resetButton = Button(gui, width=60, height=60, image=resetImage, bg=backgroundColor, activebackground=backgroundColor, bd=0, command=resetGUI)
    resetButton.place(relx=0.01, rely=0.01)

    # exit button
    exitImage = PhotoImage(file='photos/exit.png')
    exitButton = Button(gui, width=60, height=60, image=exitImage, bg=backgroundColor, activebackground=backgroundColor, bd=0, command=exitGUI)
    exitButton.place(relx=0.92, rely=0.01)

    # logo
    logo = PhotoImage(file='photos/ceva.png')
    Label(gui, image=logo, bg=backgroundColor).place(relx=0.26, rely=0.09)
    Label(gui, text='Downloader', fg=backgroundColor, font='Roboto 15 bold', bg='#E62117').place(relx=0.555, rely=0.336)

    # URL field
    Label(gui, text='URL', font='Roboto 20 bold', bg=backgroundColor).place(relx=0.20, rely=0.42) # 0.23
    entryURL = Entry(gui, font=('Helvetica', 20), width=27, bd=0, bg=buttonColor)
    entryURL.place(relx=0.29, rely=0.42)
    
    # enter button
    enterImage = PhotoImage(file='photos/enter.png')
    enterButton = Button(gui, width=50, height=50, image=enterImage, bg=backgroundColor, activebackground=backgroundColor, bd=0, command=getURL)
    enterButton.place(relx=0.81, rely=0.405)
    
    # info fields
    Label(gui, text='Name:', font='Roboto 15 bold', bg=backgroundColor).place(relx=0.22, rely=0.53)
    Label(gui, text='Duration:', font='Roboto 15 bold', bg=backgroundColor).place(relx=0.22, rely=0.57)
    
    nameVideo = Label(gui, text='', width=51, font='Roboto 13 bold', bg=backgroundColor)
    nameVideo.place(relx=0.30, rely=0.535)
    lengthVideo = Label(gui, text='', width=48, font='Roboto 13 bold', bg=backgroundColor)
    lengthVideo.place(relx=0.34, rely=0.575)

    # format buttons + labels
    Label(gui, text='Format', font='Roboto 16 bold', bg=backgroundColor).place(relx=0.19, rely=0.821)

    audioButton = Button(gui, text='Audio', font='Roboto 14 bold', bg=buttonColor, bd=0, activebackground=backgroundColor, command=audioCommand)
    audioButton.place(relx=0.19, rely=0.887)
    videoButton = Button(gui, text='Video', font='Roboto 14 bold', bg=buttonColor, bd=0, activebackground=backgroundColor, command=videoCommand)
    videoButton.place(relx=0.32, rely=0.887)

    # download button + label
    downloadButton = Button(gui, width=10, height=2, text='Download', font='Roboto 15 bold', bg=buttonColor, bd=0, activebackground=backgroundColor, command=downloadVideo)
    downloadButton.place(relx=0.613, rely=0.84)
    downloadStatus = Label(gui, text='', font='Roboto 15 bold', bg=backgroundColor, width=16)
    downloadStatus.place(relx=0.565, rely=0.78)

    gui.mainloop()