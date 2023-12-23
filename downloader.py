from pytube import YouTube
import tkinter
import customtkinter
import threading

def download_video():
    try:
        videoLink = link.get()
        # Disable the download button while downloading
        download.configure(state=tkinter.DISABLED)
        
        # Start the download in a separate thread
        download_thread = threading.Thread(target=download_video_thread, args=(videoLink,))
        download_thread.start()
    except Exception as err:
        downloadInfo.configure(text=f"An error has occurred: {err}", text_color="red")

def download_video_thread(videoLink):
    try:
        yt_Object = YouTube(videoLink)
        yd = yt_Object.streams.get_highest_resolution()
        title.configure(text = yt_Object.title, text_color = "black")
        downloadInfo.configure(text = "Download Complete!", text_color = "green")
        yd.download()
    except Exception as err:
        # Update the downloadInfo label from the main thread
        downloadInfo.configure(text=f"An error has occurred: {err}", text_color="red")
    finally:
        # Re-enable the download button after the download is complete or an error occurs
        app.after(0, lambda: download.configure(state=tkinter.NORMAL))


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text = "Insert a YouTube link")
title.pack(padx = 10, pady = 10)

# Link Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url)
link.pack()

# Download Information
downloadInfo = customtkinter.CTkLabel(app, text = "")
downloadInfo.pack()

# Download Button
download = customtkinter.CTkButton(app, text = "Download", command = download_video)
download.pack(padx = 10, pady = 10)

# Run app
app.mainloop()



    
        

