import tkinter
import customtkinter
from pytube import YouTube


def startDownloadV():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        FinishLabel.configure(text="")
        video.download()
        FinishLabel.configure(text="Video Downloaded!")
    except:
        FinishLabel.configure(text="Download error", tex_color="red")


def startDownloadA():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="white")
        FinishLabel.configure(text="")
        audio.download()
        FinishLabel.configure(text="Audio Downloaded!")
    except:
        FinishLabel.configure(text="Download error", tex_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_compeletion / 100))


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("600x300")
app.title("youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finish Downloading
FinishLabel = customtkinter.CTkLabel(app, text="")
FinishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# Download Button
downloadV = customtkinter.CTkButton(app, text="Download Video", command=startDownloadV)
downloadV.pack(padx=10, pady=10)
downloadA = customtkinter.CTkButton(app, text="Download Audio", command=startDownloadA)
downloadA.pack(padx=10, pady=10)

# Run app
app.mainloop()
