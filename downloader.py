from pytube import YouTube
import tkinter, customtkinter, threading
from tkinter import filedialog

def save_file():
    #Ask user the directory
    global folder 
    folder = filedialog.askdirectory()

    return folder

def download_video():
    try:
        videoLink = link.get()
        # Disable the download button while downloading
        download.configure(state=tkinter.NORMAL)
        
        # Start the download in a separate thread
        download_thread = threading.Thread(target=download_video_thread, args=(videoLink,))
        downloadInfo.configure(text = "Downloading...", text_color = "blue")
        download_thread.start()
    except Exception as err:
        downloadInfo.configure(text=f"An error has occurred: {err}", text_color= "red")

def download_video_thread(videoLink):
    global folder
    try:
        # Creates YouTube Object and how we want to download it
        yt_Object = YouTube(videoLink)
        yd = yt_Object.streams.get_highest_resolution()
        title.configure(text = yt_Object.title, text_color = "black")
        downloadInfo.configure(text = "Download Complete!", text_color = "green")
        
        yd.download(output_path = folder)
    except Exception as err:
        # Update the downloadInfo label from the main thread
        downloadInfo.configure(text=f"An error has occurred: {err}", text_color = "red")

if __name__ == "__main__":
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

    # Save As Button
    save_as = customtkinter.CTkButton(app, text = "Save as", command = save_file)
    save_as.pack(padx = 10)

    # Download Button
    download = customtkinter.CTkButton(app, text = "Download", command = download_video)
    download.pack(padx = 10, pady = 10)

    # Run app
    app.mainloop()



    
        

