from tkinter import *
from pytube import YouTube
from tkinter.scrolledtext import *
from tkinter import filedialog

#Method used to download a single youtube video given a url
def Downloader():
    val = generalDownload(str(link.get()))
    if val == 1:
        Label(root, text ='Download Successful', font = 'arial 20').place(x= 200 , y = 700) 
    else:
        Label(root, text ='Download Unsuccessful', font = 'arial 20').place(x= 200 , y = 700) 

#Method used to download multiple youtube videos in a list given their urls
def MultiDownloader():
    #grab all of the input text from start to finish
    result=multi_link_enter.get(1.0, 'end-1c')
    #remove new lines from string and replace with commas
    remove_new_lines = result.replace('\n',',')
    #separate into a list based on commas
    list_of_links = remove_new_lines.split(",")
    i = 0
    total = 0
    success_total = 0
    while i < len(list_of_links):
        url = list_of_links[i]
        i = i + 1
        if url != '':
            total = total + 1
            val = generalDownload(url)
            success_total = success_total + val
    display_text = '{} out of {} videos downloaded successfully.'.format(success_total, total)
    Label(root, text =display_text, font = 'arial 20').place(x= 200 , y = 700)            
        

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    file = open(filename,"r")
    lines = file.readlines()
    total = 0
    success_total = 0
    for line in lines:
        if line != '':
            total = total + 1
            line = line.replace(',','')
            val = generalDownload(line)
            success_total = success_total + val
    display_text = '{} out of {} videos downloaded successfully.'.format(success_total, total)
    Label(root, text=display_text, font = 'arial 20').place(x= 200 , y = 700) 

def generalDownload(url_string):
    try:
        url =YouTube(url_string)
        video = url.streams.first()
        download_to_directory = str(directory.get())
        #given a specific directory the video will be downloaded there. otherwise it downloads in the same directory the script exists
        if download_to_directory != '':
                video.download(r'' + download_to_directory)
        else:
                video.download()
        return 1
    except:
        return 0



#create the pop up window
root = Tk()
root.geometry('1000x1000')
root.resizable(0,0)
root.title("Youtube Video Downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

#controls the directory input and display
directory = StringVar()
Label(root, text = 'Specify Directory', font = 'arial 15 bold').place(x= 32 , y = 60)
directory_entered = Entry(root, width = 70,textvariable = directory).place(x = 32, y = 90)

#controls the single youtube download and display
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 32 , y = 160)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 190)

#controls multiple youtube video url input and display
multi_line_link = StringVar()
Label(root, text = 'Paste Multiple Links Here Separated By Commas:', font = 'arial 15 bold').place(x= 32 , y = 300)
#doing this in 2 lines to prevent none error on multi_link_enter
multi_link_enter=Text(root, height=10)
multi_link_enter.place(x=32, y=350)

#download buttons
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=500 ,y = 190)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = MultiDownloader).place(x=700 ,y = 350)
Button(root,bg = 'pale violet red', text='Download Videos By File', font = 'arial 15 bold', command=UploadAction).place(x=32,y=600)

root.mainloop()
