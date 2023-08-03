import os, sys, subprocess, signal, webbrowser, time, threading, base64
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

def thumbnailFormat():
    global ThumbFormatOptions
    OPTIONS = ["webp", "png", "jpg"]
    if thumbwrite_state.get():
        ThumbFormatOptions = OptionMenu(windowMain, thumbwrite_format_data, *OPTIONS)
        ThumbFormatOptions.grid(column = 3, row = 7)
        createToolTip(ThumbFormatOptions, text = "Select format to download thumbnail as.")
    else:
        ThumbFormatOptions.grid_forget()

def resolutionBoxAppear():
    global ResolutionBoxOptions
    OPTIONS = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
    if other_resolution_state.get():
        ResolutionBoxOptions = OptionMenu(windowMain, other_resolution_data, *OPTIONS)
        ResolutionBoxOptions.grid(column = 2, row = 11)
        createToolTip(ResolutionBoxOptions, text = "Not all resolutions are supported on every video.")
    else:
        ResolutionBoxOptions.grid_forget()

def encodingBoxAppear():
    global encodingBoxOptions
    OPTIONS = ["avi", "flv", "gif", "mkv", "mov", "mp4", "webm", "aac", "aiff", "alac", "flac", "m4a", "mka", "mp3", "ogg", "opus", "vorbis", "wav"]
    if other_encoding_state.get():
        encodingBoxOptions = OptionMenu(windowMain, other_encoding_data, *OPTIONS)
        encodingBoxOptions.grid(column = 1, row = 12)
        createToolTip(encodingBoxOptions, text = "Some other options may not work properly\ndepending on the file format chosen.")
    else:
        encodingBoxOptions.grid_forget()

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

def temp_textYin(e):
    dateEnterY.delete(0,"end")
def temp_textYout(e):
    if mm_year_data.get() == "":
        dateEnterY.insert(0,"YYYY")
def temp_textMin(e):
    dateEnterM.delete(0,"end")
def temp_textMout(e):
    if mm_month_data.get() == "":
        dateEnterM.insert(0,"MM")
def temp_textDin(e):
    dateEnterD.delete(0,"end")
def temp_textDout(e):
    if mm_day_data.get() == "":
        dateEnterD.insert(0,"DD")

def monitorTimeRange():
    global dateEnterY, dateEnterM, dateEnterD, text_1
    if monitor_mode_state.get():
        text_1 = Label(windowMain, text="Start Date")
        text_1.place(x=270, y=410)
        dateEnterY = Entry(windowMain, width = 5, textvariable = mm_year_data)
        dateEnterY.insert(0, "YYYY")
        dateEnterY.place(x = 250, y = 430)
        dateEnterY.bind("<FocusIn>", temp_textYin)
        dateEnterY.bind("<FocusOut>", temp_textYout)
        dateEnterM = Entry(windowMain, width = 4, textvariable = mm_month_data)
        dateEnterM.insert(0, "MM")
        dateEnterM.place(x = 285, y = 430)
        dateEnterM.bind("<FocusIn>", temp_textMin)
        dateEnterM.bind("<FocusOut>", temp_textMout)
        dateEnterD = Entry(windowMain, width = 4, textvariable = mm_day_data)
        dateEnterD.insert(0, "DD")
        dateEnterD.place(x = 314, y = 430)
        dateEnterD.bind("<FocusIn>", temp_textDin)
        dateEnterD.bind("<FocusOut>", temp_textDout)
    else:
        text_1.destroy()
        dateEnterY.place_forget()
        dateEnterY.delete(0,"end")
        dateEnterM.place_forget()
        dateEnterM.delete(0,"end")
        dateEnterD.place_forget()
        dateEnterD.delete(0,"end")



def checkGitHub():  
    webbrowser.open("https://github.com/Zeppelins-Forever/gui-dlp/releases", new = 0, autoraise = True)

def helpMenu():
    webbrowser.open("https://github.com/Zeppelins-Forever/gui-dlp/", new = 0, autoraise = True)
        

def errorCheck():
    if len(url_data.get()) == 0 and usrlist_state.get() == 0:
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
        return "error-no-DL-list"
    if monitor_mode_state.get():
        if not mm_year_data.get().isdigit() or not mm_month_data.get().isdigit() or not mm_day_data.get().isdigit():
            messagebox.showwarning("Warning", "Invalid characters in the date box.\nPlease use only numbers.")
            return "error-letters-in-date-box"
        if len(mm_year_data.get().replace(" ", "")) != 4 or len(mm_month_data.get().replace(" ", "")) != 2 or len(mm_day_data.get().replace(" ", "")) != 2:
            messagebox.showwarning("Warning", "Improper date format.\nPlease enter dates in YYYY MM DD format.\nEx. 2023 06 16")
            return "error-improper-date-format"
        dlBegin(1)
    else:
        dlBegin(0)

def monButtonStop(): 
    global stopMonitoring
    stopMonitoring = 1
    print("Stop Button Pressed, stopMonitoring =", stopMonitoring)

def dlBegin(monitor_mode):
    global downloading, shell_used, cmd_list
    cmd_list = ["yt-dlp"]
    if monitor_mode == 1:
        full_date = mm_year_data.get() + mm_month_data.get() + mm_day_data.get()
        cmd_list.append("--dateafter")
        cmd_list.append(full_date)
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
        else:
            # Only Custom Name
            dir_location += "/" + str(name_data.get())
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
        cmd_list.append("--convert-thumbnails")
        cmd_list.append(str(thumbwrite_format_data.get()))

    if thumbembed_state.get():
        cmd_list.append("--embed-thumbnail")

    if audio_state.get():
        cmd_list.append("-x")

    if usrlist_state.get():
        cmd_list.append("-a")
        cmd_list.append(usrlist_data.get())
    else:
        cmd_list.append(url_data.get())
    
    if subtitle_state.get():
        cmd_list.append("--all-subs")
    if subtitle_embed_state.get():
        cmd_list.append("--embed-subs")

    if allformats_state.get():
        cmd_list.append("-f")
        cmd_list.append("all")

    if other_resolution_state.get():
        cmd_list.append("-S")
        resolution_final = "res:" + other_resolution_data.get()
        cmd_list.append(resolution_final.replace("p" ,""))
    
    if other_encoding_state.get():
        cmd_list.append("--remux")
        cmd_list.append(other_encoding_data.get())
        cmd_list.append("--merge")
        cmd_list.append(other_encoding_data.get())

    print("\n", cmd_list, "\n")
    if monitor_mode_state.get():
        global stopMonitorButton
        dlButton.grid_forget()
        stopMonitorButton = Button(text = "Stop Monitoring", command = monButtonStop)
        stopMonitorButton.grid(column = 0, row = 20, pady = 5, sticky = "w")
        createToolTip(stopMonitorButton, text = "Finish current monitor cycle and\nend monitor mode. If you wish\nto download other videos while in\nmonitor mode, please launch\nanother instance of this program.")
        launchMonitorThread = threading.Thread(target = monitorThread, args = [cmd_list]) #launch new thread so download monitoring doesnt interfere with window processing.
        launchMonitorThread.start()
        return 0 

    if term_state.get():
        downloading = subprocess.Popen(cmd_list, shell=True)
        messagebox.showinfo("Download Status", "Download Starting")
        shell_used = True
    else:
        downloading = subprocess.Popen(cmd_list, shell=False)
        shell_used = False

def monitorThread(cmd_commands):
    global dlButton, stopMonitoring, mon_running
    mon_running = True
    if term_state.get():
        downloading = subprocess.Popen(cmd_list, shell=True)
    else:
        downloading = subprocess.Popen(cmd_list, shell=False)
    while not stopMonitoring:
        if downloading.poll() == None:
            print("Process is running!")
            print("Process ID:", downloading.pid)
            time.sleep(1)
            continue
        else:
            print("Restarting process.")
            if term_state.get():
                downloading = subprocess.Popen(cmd_list, shell=True)
                print("Process ID:", downloading.pid)
            else:
                downloading = subprocess.Popen(cmd_list, shell=False)
                print("Process ID:", downloading.pid)
    print("Stopped Monitoring")
    child_pid = downloading.pid
    print("Killing process ID:", downloading.pid)
    os.kill(child_pid, signal.SIGTERM)
    downloading.kill()
    stopMonitorButton.destroy()
    mon_running = False
    dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = errorCheck)
    dlButton.grid(column = 0, row = 20, sticky = "w")
    stopMonitoring = 0
    return
"""
def on_closing():

    if mon_running:
        if messagebox.askokcancel("Quit", "Monitor is still running.\nDo you want to end monitor mode and quit?"):
            windowMain.destroy()
    else:
        windowMain.destroy()
"""
def windowIcon(windowName):
    icon = """ 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
    """
    icondata= base64.b64decode(icon)
    ## The temp file is icon.ico
    tempFile= "icon.ico"
    iconfile= open(tempFile,"wb")
    ## Extract the icon
    iconfile.write(icondata)
    iconfile.close()
    windowName.wm_iconbitmap(tempFile)
    ## Delete the tempfile
    os.remove(tempFile)


windowMain = Tk()
windowMain.title("GUI-DLP v1.2.0")
windowMain.geometry("510x500")
windowMain.resizable(False, False)
windowIcon(windowMain)


url_data = StringVar(windowMain, "")
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
thumbwrite_format_data = StringVar(windowMain, "webp")
thumbembed_state = IntVar(windowMain, 0)
other_resolution_state = IntVar(windowMain, 0)
other_resolution_data = StringVar(windowMain, "1080p")
other_encoding_state = IntVar(windowMain, 0)
other_encoding_data = StringVar(windowMain, "mkv")
audio_state = IntVar(windowMain, 0)

usrlist_state = IntVar(windowMain, 0)
usrlist_data = StringVar(windowMain, "")

subtitle_state = IntVar(windowMain, 0)
subtitle_embed_state = IntVar(windowMain, 0)
allformats_state = IntVar(windowMain, 0)

################################################ Window Starts Here ################################################

term_state = IntVar(windowMain, 0)
monitor_mode_state = IntVar(windowMain, 0)
mm_year_data = StringVar(windowMain, "")
mm_month_data = StringVar(windowMain, "")
mm_day_data = StringVar(windowMain, "")

stopMonitoring = 0


mediaSource = Entry(windowMain, width = 60, textvariable = url_data)
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

customNameCheck = Checkbutton(text = "Custom Name?", variable = name_state, command = nameboxAppear)
customNameCheck.grid(column = 0, row = 2, sticky = "w")
createToolTip(customNameCheck, "Set a custom name for the downloaded file.\nDO NOT INCLUDE FILE EXTENSION!\nIf you are downloading a playlist, check 'Include URL?',\notherwise the videos will overwrite themselves.")

cookiesCheck = Checkbutton(text = "Use Cookies?", variable = cookie_state, command = browserAppear)
cookiesCheck.grid(column = 0, row = 3, sticky = "w")
createToolTip(cookiesCheck, text = "Import cookies from your browser of choice.\nMay be needed for paywalled content.")

descriptionCheck = Checkbutton(text = "Download\nDescription?", variable = description_state)
descriptionCheck.grid(column = 0, row = 4, sticky = "w")
createToolTip(descriptionCheck, text = "Write the video description to a seperate file.")

commentsCheck = Checkbutton(text = "Download\nComments?", variable = comments_state)
commentsCheck.grid(column = 0, row = 5, sticky = "w")
createToolTip(commentsCheck, text = "Download stream comments to a seperate infojson file.")

waitCheck = Checkbutton(text = "Wait for Video?", variable = wait_state, command = waitAppear)
waitCheck.grid(column = 0, row = 6, sticky = "w")
createToolTip(waitCheck, text = "If the video is scheduled but\nnot started yet, use this to retry\nplaying the video after the selected\nnumber of seconds.")

writeThumbnail = Checkbutton(text = "Write\nThumbnail?", variable = thumbwrite_state, command = thumbnailFormat)
writeThumbnail.grid(column = 0, row = 7, sticky = "w")
createToolTip(writeThumbnail, text = "Download the thumbnail as\na separate image file.") \

embedThumbnail = Checkbutton(text = "Embed?", variable = thumbembed_state)
embedThumbnail.grid(column = 1, row = 7, sticky = "w")
createToolTip(embedThumbnail, text = "Embed the thumbnail as the\ndownloaded video's thumbnail.")

audioOnly = Checkbutton(text = "Audio Only?", variable = audio_state)
audioOnly.grid(column = 0, row = 8, sticky = "w")
createToolTip(audioOnly, text = "Only download the source's audio.")

downloadList = Checkbutton(text = "DL List?", variable = usrlist_state, command = userListAppear)
downloadList.grid(column = 0, row = 9, sticky = "w")
createToolTip(downloadList, text = "If you have a list of URLs to download\n(separated by a new line in a text doc),\nuse this to download videos from that\ndocument's data. This takes priority\nover the URL field.")

downloadSubs = Checkbutton(text = "Subtitles?", variable = subtitle_state)
downloadSubs.grid(column = 0, row = 10, sticky = "w")
createToolTip(downloadSubs, text = "Download all available subtitle options for a video.")

downloadAllFormats = Checkbutton(text = "All Formats?", variable = allformats_state)
downloadAllFormats.grid(column = 0, row = 11, sticky = "w")
createToolTip(downloadAllFormats, text = "Download all file types available.")

otherResolution = Checkbutton(text = "Non-highest\nresolution?", variable = other_resolution_state, command = resolutionBoxAppear)
otherResolution.grid(column = 1, row = 11, sticky = "w")
createToolTip(otherResolution, text = "Choose a resolution to download the video\nat that is not the default highest.")

otherEncoding = Checkbutton(text = "Non-default\nencoding?", variable = other_encoding_state, command = encodingBoxAppear)
otherEncoding.grid(column = 0, row = 12, sticky = "w")
createToolTip(otherEncoding, text = "Choose an format to encode the video\nas instead of using the default.")

embedSubs = Checkbutton(text = "Embed?", variable = subtitle_embed_state)
embedSubs.grid(column = 1, row = 10, sticky = "w")
createToolTip(embedSubs, text = "Embed all available subtitle options for a video.")

windowMain.rowconfigure(18, weight = 1)

dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = errorCheck)
dlButton.grid(column = 0, row = 20, sticky = "w", padx = 2)

showTerm = Checkbutton(text = "Hide terminal?", variable = term_state)
showTerm.grid(column = 1, row = 20, sticky = "w")
createToolTip(showTerm, text = "The process typically opens a terminal to display progress. Select this to prevent it.\nHiding is not recommended for monitor mode, as it allows you to kill the process in the\nterminal window immediatly, if desired. Also not recommended for non-default encoding\nand non-highest resolution, as you will not see if download failures take place.")

monitorModeCheck = Checkbutton(text = "Monitor\nMode", variable = monitor_mode_state, command = monitorTimeRange)
monitorModeCheck.grid(column = 2, row = 20, sticky = "w")
createToolTip(monitorModeCheck, text = "Monitor video source for new uploads. Used to monitor a\nsource of videos, not a specific video. For example, to monitor\na YouTube channel for new uploads in the 'videos' tab, enter\n'https://www.youtube.com/[channel name]/videos'\nIf you want to monitor streams, use the '/streams' link.\nThe same concept applies to other sites that yt-dlp supports.")

helpButton = Button(text = "   Help   ", command = helpMenu)
helpButton.grid(column = 4, row = 19, pady = 5, sticky = "e")
createToolTip(helpButton, text = "Open the README page\non GitHub for detailed\ninfo about each option.")

updateButton = Button(text = "Update?", command = checkGitHub)
updateButton.grid(column = 4, row = 20, sticky = "e")
createToolTip(updateButton, text = "Open the GitHub Releases\npage to manually check\nfor updates.")

#windowMain.protocol("WM_DELETE_WINDOW", on_closing)  ###### For future updates
windowMain.mainloop()
