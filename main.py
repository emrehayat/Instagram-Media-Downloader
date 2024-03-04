import instaloader
from tkinter import *

ig = instaloader.Instaloader()

window = Tk()
window.title("Instagram Media Downloader")
window.minsize(width=900, height=300)
window.config(bg="#A75816")

my_label = Label(text="ENTER THE USERNAME: ", font=("Times New Roman", 24, "bold"), bg="white", fg="#A75816")
my_label.place(x=250, y=50)

user_name_entry = Entry(width=75)
user_name_entry.place(x=220, y=125)

def click_button():
    try:
        username = user_name_entry.get()
        ig.download_profile(username, profile_pic_only=False)
        final_label = Label(text="Download completed!", fg="green", bg="white", font=("Times New Roman", 12, "bold"))
        final_label.place(x=375, y=225)
    except instaloader.InstaloaderException as e:
        final_label = Label(text="Download failed!", fg="red", bg="white", font=("Times New Roman", 12, "bold"))
        final_label.place(x=390, y=225)
        error_label = Label(text=str(e), fg="red", bg="white", font=("Times New Roman", 12, "bold"))
        error_label.pack(side = BOTTOM)

my_button = Button(text="Download the media", font=("Times New Roman", 12, "bold"), command=click_button)
my_button.place(x=375, y=175)

window.mainloop()