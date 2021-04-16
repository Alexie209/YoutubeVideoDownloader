from tkinter import *
from pytube import YouTube


#this project needs pytube package
#design
root = Tk()
root.geometry('600x400')
root.resizable(1, 1)
root.title("Youtube Video Downloader made by Alexie")

Label(root, text='Start Downloading Youtube Videos', font='Helvetica 20').pack()

#link set-up
link = StringVar()

Label(root, text='Insert your Youtube link:', font='Times 15').pack()
link_enter = Entry(root, width=80, textvariable=link).pack()


def Download():
    '''
    It downloads a video by link
    :return:
    '''
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='Times 30').pack()


Label(root, text=' ')
Button(root, text='DOWNLOAD', font='Times 20 bold', bg='pale violet red', padx=2, command=Download).pack()

root.mainloop()
