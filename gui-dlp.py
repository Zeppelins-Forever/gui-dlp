import os, sys, subprocess
from tkinter import *
from tkinter import filedialog, messagebox


#----------------------------------------------------
#credit and thanks to squareRoot17 from https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python for the code sample of this class.
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

#----------------------------------------------------

def fileButtonClicked():
    fileButtonLocation = filedialog.askdirectory()
    fileLocation.delete(0, "end")
    fileLocation.insert(0, fileButtonLocation)

def nameboxAppear():
    global nameBox, nameUrlCheckBox, dateBox
    if name_state.get():
        nameUrlCheckBox = Checkbutton(windowMain, text = "Include URL?", variable = hyperlink_state)
        nameUrlCheckBox.grid(column = 1, row = 2, sticky = "w")
        createToolTip(nameUrlCheckBox, text = "To include URL data in the\nvideo title, select this.")
        nameBox = Entry(windowMain, width = 40, textvariable = name_data)
        nameBox.grid(column = 2, row = 2, columnspan = 6, sticky = "w")
        createToolTip(nameBox, text = "Leave blank for default name, but\nwith the checkbox options applied.")
        dateBox = Checkbutton(windowMain, text = "Date first?", variable = date_state)
        dateBox.grid(column = 1, row = 3, sticky = "w")
        createToolTip(dateBox, text = "Add the upload date in front of the title.")
    else:
        nameUrlCheckBox.grid_forget()
        nameBox.grid_forget()
        dateBox.grid_forget()
        hyperlink_state.set(0)
        name_data.set("")
        date_state.set(0)

def browserAppear():
    global radioBrave, radioChrome, radioChromium, radioEdge, radioFirefox, radioOpera, radioSafari, radioVivaldi
    if cookie_state.get():
        radioBrave = Radiobutton(text = "Brave", variable = browser_state, value = "brave")
        radioBrave.grid(column = 2, row = 3, sticky = "w")
        radioChrome = Radiobutton(text = "Chrome", variable = browser_state, value = "chrome")
        radioChrome.grid(column = 3, row = 3, sticky = "w")
        radioChromium = Radiobutton(text = "Chromium", variable = browser_state, value = "chromium")
        radioChromium.grid(column = 4, row = 3, sticky = "w")
        radioEdge = Radiobutton(text = "Edge", variable = browser_state, value = "edge")
        radioEdge.grid(column = 2, row = 4, sticky = "w")
        radioFirefox = Radiobutton(text = "Firefox", variable = browser_state, value = "firefox")
        radioFirefox.grid(column = 3, row = 4, sticky = "w")
        radioOpera = Radiobutton(text = "Opera", variable = browser_state, value = "opera")
        radioOpera.grid(column= 4, row = 4, sticky = "w")
        radioSafari = Radiobutton(text = "Safari", variable = browser_state, value = "safari")
        radioSafari.grid(column = 2, row = 5, sticky = "w")
        radioVivaldi = Radiobutton(text = "Vivaldi", variable = browser_state, value = "vivaldi")
        radioVivaldi.grid(column = 3, row = 5, sticky = "w")
    else:
        radioBrave.grid_forget()
        radioChrome.grid_forget()
        radioChromium.grid_forget()
        radioEdge.grid_forget()
        radioFirefox.grid_forget()
        radioOpera.grid_forget()
        radioSafari.grid_forget()
        radioVivaldi.grid_forget()

def waitAppear():
    global numBox
    if wait_state.get():
        numBox = Spinbox(windowMain, from_= 1, to = 604800, wrap = True, width = 7, state = "readonly", textvariable = wait_num)
        numBox.grid(column = 1, row = 6, sticky = "w")
    else:
        numBox.grid_forget()

def userListAppear():
    global ulLocate, userFileButton
    if usrlist_state.get():
        ulLocate = Entry(windowMain, width = 43, textvariable = usrlist_data)
        ulLocate.grid(column = 0, row = 9, columnspan = 5)
        userFileButton = Button(windowMain, text = "File Location", fg = "blue", command = userListButton)
        userFileButton.grid(column = 4, row = 9, sticky = "w")
    else:
        ulLocate.grid_forget()
        userFileButton.grid_forget()


def userListButton():
    userButtonLocation = filedialog.askopenfilename()
    ulLocate.delete(0, "end")
    ulLocate.insert(0, userButtonLocation)


def dlBegin():
    cmd_list = ["yt-dlp"]
    if len(url_state.get()) == 0 and usrlist_state.get() == 0:
        messagebox.showwarning("Warning", "The URL field is empty!")
        return "error-URL"
    if len(dl_data.get()) == 0:
        messagebox.showwarning("Warning", "The destination field is empty!")
        return "error-destination"
    if name_state.get() and ( len(name_data.get()) == 0 and not hyperlink_state.get() and not date_state.get() ):
        messagebox.showwarning("Warning", "The Custom Name field is empty and no additional settings are selected!\nPlease uncheck it, check a name option, or enter a name.")
        return "error-name"
    if usrlist_state.get() and len(usrlist_data.get()) == 0:
        messagebox.showwarning("Warning", "The DL List field is empty!\nPlease uncheck it or enter a file location.")
    

    if name_state.get() and len(name_data.get()) > 0:
        dir_location = str(dl_data.get())
        if hyperlink_state.get() and not date_state.get():
            #Custom Name [hyperlink].[extension]
            dir_location += "/" + str(name_data.get()) + " [%(id)s].%(ext)s"
        elif date_state.get() and not hyperlink_state.get():
            #[date] Custom Name.[extension]
            dir_location += "/%(upload_date)s " + str(name_data.get()) + ".%(ext)s"
        elif hyperlink_state.get() and date_state.get():
            #[date] Custom Name [hyperlink].[extension]
            dir_location += "/%(upload_date)s " + str(name_data.get()) + " [%(id)s].%(ext)s"
    elif name_state.get() and len(name_data.get()) == 0:
        dir_location = str(dl_data.get())
        if hyperlink_state.get() and not date_state.get():
            #[Default Name] [hyperlink].[extension]
            dir_location += "/%(title)s [%(id)s].%(ext)s"
        elif date_state.get() and not hyperlink_state.get():
            #[date] [Default Name].[extension]
            dir_location += "/%(upload_date)s %(title)s.%(ext)s"
        elif hyperlink_state.get() and date_state.get():
            #[date] [Default Name] [hyperlink].[extension]
             dir_location += "/%(upload_date)s %(title)s [%(id)s].%(ext)s"
    else:
        dir_location = str(dl_data.get())
        dir_location += "/%(title)s [%(id)s].%(ext)s"
    cmd_list.append("-o")
    cmd_list.append(str(dir_location))
    
    if cookie_state.get():
        cmd_list.append("--cookies-from-browser")
        if browser_state.get() == "brave":
            cmd_list.append("brave")
        elif browser_state.get() == "chrome":
            cmd_list.append("chrome")
        elif browser_state.get() == "chromium":
            cmd_list.append("chromium")
        elif browser_state.get() == "edge":
            cmd_list.append("edge")
        elif browser_state.get() == "firefox":
            cmd_list.append("firefox")
        elif browser_state.get() == "opera":
            cmd_list.append("opera")
        elif browser_state.get() == "safari":
            cmd_list.append("safari")
        elif browser_state.get() == "vivaldi":
            cmd_list.append("vivaldi")
    
    if description_state.get():
        cmd_list.append("--write-description")
    
    if comments_state.get():
        cmd_list.append("--write-comments")

    if wait_state.get():
        cmd_list.append("--wait-for-video")
        cmd_list.append(str(wait_num.get()))

    if thumbwrite_state.get():
        cmd_list.append("--write-thumbnail")

    if thumbembed_state.get():
        cmd_list.append("--embed-thumbnail")

    if audio_state.get():
        cmd_list.append("-x")

    if usrlist_state.get():
        cmd_list.append("-a")
        cmd_list.append(usrlist_data.get())
    else:
        cmd_list.append(url_state.get())

    if term_state.get():
        downloading = subprocess.Popen(cmd_list, shell=True)
        messagebox.showinfo("Download Status", "Download Starting")

    else:
        downloading = subprocess.Popen(cmd_list, shell=False)




windowMain = Tk()
windowMain.title("yt-dlp Manger")
windowMain.geometry("500x500")
windowMain.iconbitmap("gui-dlp.ico")

url_state = StringVar(windowMain, "")
dl_data = StringVar(windowMain, "")
name_state = IntVar(windowMain, 0)
name_data = StringVar(windowMain, "")
date_state = IntVar(windowMain, 0)
hyperlink_state = IntVar(windowMain, 0)
cookie_state = IntVar(windowMain, 0)
browser_state = StringVar(windowMain, "brave")
description_state = IntVar(windowMain, 0)
comments_state = IntVar(windowMain, 0)
wait_state = IntVar(windowMain, 0)
wait_num = IntVar(windowMain, 15)
thumbwrite_state = IntVar(windowMain, 0)
thumbembed_state = IntVar(windowMain, 0)
audio_state = IntVar(windowMain, 0)

usrlist_state = IntVar(windowMain, 0)
usrlist_data = StringVar(windowMain, "")

term_state = IntVar(windowMain, 0)



mediaSource = Entry(windowMain, width = 60, textvariable = url_state)
mediaSource.grid(padx = 5, pady = 10, columnspan = 4)
createToolTip(mediaSource, text = "Enter the URL of the Youtube video, Twitch\nstream, etc, that you want to download. You\ncan download individual videos or playlists.")

mediaSourceText = Label(windowMain, text = "URL for media source")
mediaSourceText.grid(column = 4, row = 0)

fileLocation = Entry(windowMain, width = 60, textvariable = dl_data)
fileLocation.grid(padx = 5, pady = 10, columnspan = 4)
createToolTip(fileLocation, text = "Enter the absolute path\nto where you want the\nvideo to be downloaded to\n(or use the 'Destination' button).")

fileButton = Button(windowMain, text = "     Destination     ", fg = "blue", command = fileButtonClicked)
fileButton.grid(column = 4, row = 1)
createToolTip(fileButton, text = "Enter the absolute path\nto where you want the\nvideo to be downloaded to\n(or use the 'Destination' button).")

customNameCheck = Checkbutton(text = "Custom name?", variable = name_state, command = nameboxAppear)
customNameCheck.grid(column = 0, row = 2, sticky = "w")
createToolTip(customNameCheck, "Check this if you want to set a custom name for the\ndownloaded file. DO NOT INCLUDE FILE EXTENSION!\n If you are downloading a playlist, check 'Include URL?',\notherwise the videos will overwrite themselves.")

cookiesCheck = Checkbutton(text = "Use cookies?", variable = cookie_state, command = browserAppear)
cookiesCheck.grid(column = 0, row = 3, sticky = "w")
createToolTip(cookiesCheck, text = "Select this to import cookies from\nyour browser of choice. May\nbe needed for paywalled content.")

descriptionCheck = Checkbutton(text = "Download description?", variable = description_state)
descriptionCheck.grid(column = 0, row = 4, sticky = "w")
createToolTip(descriptionCheck, text = "Select this to write the video\ndescription to a seperate file.")

commentsCheck = Checkbutton(text = "Download comments?", variable = comments_state)
commentsCheck.grid(column = 0, row = 5, sticky = "w")
createToolTip(commentsCheck, text = "Select this to download stream comments\nto a seperate infojson file.")

waitCheck = Checkbutton(text = "Wait for video?", variable = wait_state, command = waitAppear)
waitCheck.grid(column = 0, row = 6, sticky = "w")
createToolTip(waitCheck, text = "If the video is scheduled but\nnot started yet, use this to retry\nplaying the video after the selected\nnumber of seconds.")

writeThumbnail = Checkbutton(text = "Write thumbnail?", variable = thumbwrite_state)
writeThumbnail.grid(column = 0, row = 7, sticky = "w")
createToolTip(writeThumbnail, text = "Select this to download the\nthumbnail as a separate\nimage file.")

embedThumbnail = Checkbutton(text = "Embed?", variable = thumbembed_state)
embedThumbnail.grid(column = 1, row = 7, sticky = "w")
createToolTip(embedThumbnail, text = "Select this to embed the\nthumbnail as the downloaded\nvideo's thumbnail.")

audioOnly = Checkbutton(text = "Audio only?", variable = audio_state)
audioOnly.grid(column = 0, row = 8, sticky = "w")
createToolTip(audioOnly, text = "Select this if you only wish to\ndownload the source's audio.")

downloadList = Checkbutton(text = "DL List?", variable = usrlist_state, command = userListAppear)
downloadList.grid(column = 0, row = 9, sticky = "w")
createToolTip(downloadList, text = "If you have a list of URLs to download\n(separated by a new line in a text doc),\nuse this to download videos from that\ndocument's data. This takes priority\nover the URL field.")

windowMain.rowconfigure(19, weight = 1)

dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = dlBegin)
dlButton.grid(column = 0, row = 20, sticky = "w")

showTerm = Checkbutton(text = "Hide terminal?", variable = term_state)
showTerm.grid(column = 1, row = 20, sticky = "w")
createToolTip(showTerm, text = "Select this to hide the process run\nin a terminal, such as CMD. Otherwise,\nit will be shown.")

windowMain.mainloop()
