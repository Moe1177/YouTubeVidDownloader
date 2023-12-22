from pytube import YouTube

def download_video(url, desination):
    try:
        video = YouTube(url)
        yd = video.streams.get_highest_resolution()
        print("Downloading...")
        yd.download(desination)
        print(f"Download complete! Saved at {desination}")
    # Catches any unexpected errors when downloading
    except Exception as err:
        print(f"An error has occured: {err}")

if __name__ == "__main__":
    # Amount of videos they download
    count = 1

    url = input("Enter a YouTube link you would like to download: ")
    destination_path = input("Enter your destination path: ")
    
    download_video(url, destination_path)

    while True:
        link = input("\nEnter another YouTube video link you would like to download (exit): ")
        
        # Breaks out loop if user exits
        if link == "exit":
            print("Enjoy your " + str(count) + " YouTube video(s)")
            break

        download_video(link, destination_path)
        count += 1

