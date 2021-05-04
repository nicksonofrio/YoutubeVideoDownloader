from tkinter import *
from pytube import YouTube
from tkinter.scrolledtext import *
import sys

#Method used to download a single youtube video given a url
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    download_to_directory = str(directory.get())
    #given a specific directory the video will be downloaded there. otherwise it downloads in the same directory the script exists
		if download_to_directory != '':
			video.download(r'' + download_to_directory)
		else:
			video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 650 , y = 190)  

#Method used to download multiple youtube videos in a list given their urls
def MultiDownloader():
	#grab all of the input text from start to finish
    result=multi_link_enter.get(1.0, 'end-1c')
    #remove new lines from string and replace with commas
    remove_new_lines = result.replace('\n',',')
    #separate into a list based on commas
    list_of_links = remove_new_lines.split(",")
    i = 0
    while i < len(list_of_links):
    	url = list_of_links[i]
    	i = i + 1
    	print(url)
    	if url != '':
    		url_format = YouTube(url)
    		video = url_format.streams.first()
    		download_to_directory = str(directory.get())
    		#given a specific directory the video will be downloaded there. otherwise it downloads in the same directory the script exists
    		if download_to_directory != '':
    			video.download(r'' + download_to_directory)
    		else:
    			video.download()
    		
    Label(root, text ="Downloaded Videos", font = 'arial 15').place(x= 32 , y = 500) 

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


root.mainloop()
