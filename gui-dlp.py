import os, sys, subprocess, signal, webbrowser, time, threading, base64, datetime, pyperclip  #requests - future update
from decimal import *
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from functools import partial

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

def cookieButtonClicked():
    cookieButtonLocation = filedialog.askopenfilename()
    cookiesLocation.delete(0, "end")
    cookiesLocation.insert(0, cookieButtonLocation)

def tab2cookieButtonClicked():
    cookieButtonLocation = filedialog.askopenfilename()
    tab2cookiesLocation.delete(0, "end")
    tab2cookiesLocation.insert(0, cookieButtonLocation)

def nameboxAppear():
    global nameBox, nameUrlCheckBox, dateBox, folderChannelName
    if name_state.get():
        nameUrlCheckBox = Checkbutton(windowMain, text = "Include ID?", variable = hyperlink_state)
        nameUrlCheckBox.place(x = 160, y = 83)
        createToolTip(nameUrlCheckBox, text = "To include ID data in the\nvideo title, select this.")
        nameBox = Entry(windowMain, width = 35, textvariable = name_data)
        nameBox.place(x = 270, y = 85)
        createToolTip(nameBox, text = "Leave blank for default name, but\nwith the checkbox options applied.")
        dateBox = Checkbutton(windowMain, text = "Date First?", variable = date_state)
        dateBox.place(x = 160, y = 107)
        createToolTip(dateBox, text = "Add the upload date\nin front of the title.")
        folderChannelName = Checkbutton(windowMain, text = "Sort via Channel?", variable = channel_category_state)
        folderChannelName.place(x = 160, y = 132)
        createToolTip(folderChannelName, text = "Place video in a folder\nwith the channel name.")
    else:
        nameUrlCheckBox.destroy()
        nameBox.destroy()
        dateBox.destroy()
        folderChannelName.destroy()
        #hyperlink_state.set(0)
        #name_data.set("")
        #date_state.set(0)
        #channel_category_state.set(0)

def browserAppear():
    global radioBrave, radioChrome, radioChromium, radioEdge, radioFirefox, radioOpera, radioSafari, radioVivaldi, radioFile, browser_state, cookiesLocation
    if cookie_state.get():
        radioBrave = Radiobutton(tab1, text = "Brave", variable = browser_state, value = "brave", command = cookiesFileLocationBar)
        radioBrave.place(x = 280, y = 80)
        radioChrome = Radiobutton(tab1, text = "Chrome", variable = browser_state, value = "chrome", command = cookiesFileLocationBar)
        radioChrome.place(x = 340, y = 80)
        radioChromium = Radiobutton(tab1, text = "Chromium", variable = browser_state, value = "chromium", command = cookiesFileLocationBar)
        radioChromium.place(x = 410, y = 80)
        radioEdge = Radiobutton(tab1, text = "Edge", variable = browser_state, value = "edge", command = cookiesFileLocationBar)
        radioEdge.place(x = 280, y = 105)
        radioFirefox = Radiobutton(tab1, text = "Firefox", variable = browser_state, value = "firefox", command = cookiesFileLocationBar)
        radioFirefox.place(x = 340, y = 105)
        radioOpera = Radiobutton(tab1, text = "Opera", variable = browser_state, value = "opera", command = cookiesFileLocationBar)
        radioOpera.place(x = 410, y = 105)
        radioSafari = Radiobutton(tab1, text = "Safari", variable = browser_state, value = "safari", command = cookiesFileLocationBar)
        radioSafari.place(x = 280, y = 130)
        radioVivaldi = Radiobutton(tab1, text = "Vivaldi", variable = browser_state, value = "vivaldi", command = cookiesFileLocationBar)
        radioVivaldi.place(x = 340, y = 130)
        radioFile = Radiobutton(tab1, text = "Cookies File", variable = browser_state, value = "file", command = cookiesFileLocationBar)
        radioFile.place(x = 410, y = 130)
    else:
        radioBrave.destroy()
        radioChrome.destroy()
        radioChromium.destroy()
        radioEdge.destroy()
        radioFirefox.destroy()
        radioOpera.destroy()
        radioSafari.destroy()
        radioVivaldi.destroy()
        radioFile.destroy()
        try:
            cookiesLocation.destroy()
            cookiesBox.destroy()
        except Exception:
            pass
        browser_state = StringVar(windowMain, "brave")

def cookiesFileLocationBar():
    if browser_state.get() == "file": ################################## MAKE SURE COOKIES FILE CAN BE CHOSEN IN THE FINAL COMMAND
        global cookiesLocation, cookiesBox, browser_option_check
        cookiesLocation = Entry(tab1, width = 28, textvariable = cookies_data)
        cookiesLocation.place(x = 250, y = 155)
        createToolTip(fileLocation, text = "Enter the absolute path\nto the cookies file. Must\nbe in Netscape format.")
        cookiesBox = Button(tab1, text = "Destination", command = cookieButtonClicked)
        cookiesBox.place(x = 430, y = 152)
        createToolTip(cookiesBox, text = "Enter the absolute path\nto the cookies file.")
    else:
        try:
            cookiesBox.destroy()
        except NameError:
            pass
        try:
            cookiesLocation.destroy()
        except NameError:
            pass
        
    
def tab2CookiesFileLocationBar():
    if tab2_cookies_state.get(): 
        global tab2cookiesLocation, tab2cookiesBox, tab2browser_option_check
        tab2cookiesLocation = Entry(tab2, width = 28, textvariable = tab2_cookies_data)
        tab2cookiesLocation.place(x = 250, y = 83)
        createToolTip(tab2cookiesLocation, text = "Enter the absolute path\nto the cookies file.")
        tab2cookiesBox = Button(tab2, text = "Destination", command = tab2cookieButtonClicked)
        tab2cookiesBox.place(x = 430, y = 80)
        createToolTip(tab2cookiesBox, text = "Enter the absolute path\nto the cookies file.")
    else:
        tab2cookiesLocation.destroy()
        tab2cookiesBox.destroy()

def waitAppear():
    global numBox
    if wait_state.get():
        numBox = Spinbox(tab1, from_= 1, to = 604800, wrap = True, width = 7, state = "readonly", textvariable = wait_num)
        numBox.place(x = 160, y = 155)
    else:
        numBox.destroy()

def thumbnailFormat():
    global ThumbFormatOptions
    OPTIONS = ["webp", "png", "jpg"]
    if thumbwrite_state.get():
        ThumbFormatOptions = OptionMenu(tab1, thumbwrite_format_data, *OPTIONS)
        ThumbFormatOptions.place(x = 320, y = 178)
        createToolTip(ThumbFormatOptions, text = "Select format to download thumbnail as.")
    else:
        try:
            ThumbFormatOptions.destroy()
        except NameError:
            pass

def resolutionBoxAppear():
    global ResolutionBoxOptions
    OPTIONS = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
    if other_resolution_state.get():
        ResolutionBoxOptions = OptionMenu(tab1, other_resolution_data, *OPTIONS)
        ResolutionBoxOptions.place(x = 320, y = 278)
        createToolTip(ResolutionBoxOptions, text = "Not all resolutions are supported on every video.")
    else:
        ResolutionBoxOptions.destroy()

def encodingBoxAppear():
    global encodingBoxOptions
    OPTIONS = ["avi", "flv", "gif", "mkv", "mov", "mp4", "webm", "aac", "aiff", "alac", "flac", "m4a", "mka", "mp3", "ogg", "opus", "vorbis", "wav"]
    if other_encoding_state.get() and audio_state.get() == 0:
        encodingBoxOptions = OptionMenu(tab1, other_encoding_data, *OPTIONS)
        encodingBoxOptions.place(x = 160, y = 302)
        createToolTip(encodingBoxOptions, text = "Some other options may not work properly\ndepending on the file format chosen.")
    else:
        try:
            encodingBoxOptions.destroy()
        except:
            pass

def userListAppear():
    global ulLocate, userFileButton
    if usrlist_state.get():
        ulLocate = Entry(tab1, width = 43, textvariable = usrlist_data)
        ulLocate.place(x = 155, y = 233)
        userFileButton = Button(tab1, text = "File Location", command = userListButton)
        userFileButton.place(x = 420, y = 229)
    else:
        ulLocate.destroy()
        userFileButton.destroy()


def userListButton():
    userButtonLocation = filedialog.askopenfilename()
    ulLocate.delete(0, "end")
    ulLocate.insert(0, userButtonLocation)

def temp_textYin(e):
    dateEnterY.delete(0,"end")
def temp_textYout(e):
    today = datetime.date.today()
    if mm_year_data.get() == "":
        dateEnterY.insert(0, today.strftime('%Y'))
def temp_textMin(e):
    dateEnterM.delete(0,"end")
def temp_textMout(e):
    today = datetime.date.today()
    if mm_month_data.get() == "":
        dateEnterM.insert(0, today.strftime('%m'))
def temp_textDin(e):
    dateEnterD.delete(0,"end")
def temp_textDout(e):
    today = datetime.date.today()
    if mm_day_data.get() == "":
        dateEnterD.insert(0, today.strftime('%d'))

def monitorTimeRange():
    global dateEnterY, dateEnterM, dateEnterD, text_1
    today = datetime.date.today()
    if monitor_mode_state.get():
        text_1 = Label(tab1, text="Start Date")
        text_1.place(x=253, y=410)
        dateEnterY = Entry(tab1, width = 4, textvariable = mm_year_data)
        dateEnterY.insert(0, today.strftime('%Y'))
        dateEnterY.place(x = 249, y = 430)
        createToolTip(dateEnterY, text = "YYYY/MM/DD format. Be sure to include zeros.\nex. 2000/01/23, not 2000/1/23.")
        dateEnterY.bind("<FocusIn>", temp_textYin)
        dateEnterY.bind("<FocusOut>", temp_textYout)
        dateEnterM = Entry(tab1, width = 2, textvariable = mm_month_data)
        dateEnterM.insert(0, today.strftime('%m'))
        dateEnterM.place(x = 279, y = 430)
        createToolTip(dateEnterM, text = "YYYY/MM/DD format. Be sure to include zeros.\nex. 2000/01/23, not 2000/1/23.")
        dateEnterM.bind("<FocusIn>", temp_textMin)
        dateEnterM.bind("<FocusOut>", temp_textMout)
        dateEnterD = Entry(tab1, width = 2, textvariable = mm_day_data)
        dateEnterD.insert(0, today.strftime('%d'))
        dateEnterD.place(x = 297, y = 430)
        createToolTip(dateEnterD, text = "YYYY/MM/DD format. Be sure to include zeros.\nex. 2000/01/23, not 2000/1/23.")
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
    if os.path.isfile("help/GUI-DLP-help.html"):
        filename = 'file:///'+os.getcwd()+'/help/GUI-DLP-help.html'
        webbrowser.open_new_tab(filename)
    else:
        webbrowser.open("https://github.com/Zeppelins-Forever/gui-dlp/", new = 0, autoraise = True)
        
########################################################################################################### Tab 2 functions
def tab2AddRetryStream():
    global tab2checkFrequency
    if tab2_wait_state.get():
        tab2checkFrequency = Checkbutton(tab2, text = "Check More Often?", variable = tab2_frequency_state, command = tab2chooseTime)
        tab2checkFrequency.place(x = 159, y = 130)
        createToolTip(tab2checkFrequency, text = "By default, ytarchive will wait until the video\nis scheduled to start to begin checking. This option\nwill make ytarchive check the video at a specific\nfrequency (in seconds) instead.")
    else:
        tab2checkFrequency.destroy()
        tab2_frequency_state.set(0)
        try:
            tab2numBox.destroy()
        except NameError:
            pass

def tab2chooseTime():
    global tab2numBox
    if tab2_frequency_state.get():
        tab2numBox = Spinbox(tab2, from_= 1, to = 604800, wrap = True, width = 7, state = "readonly", textvariable = tab2_wait_num)
        tab2numBox.place(x = 300, y = 132)
    else:
        tab2numBox.destroy()

def tab2qualityChoice():
    global tab2ResolutionBoxOptions
    OPTIONS = ["2160p60", "2160p", "1440p60", "1440p", "1080p60", "1080p", "720p60", "720p", "480p", "360p", "240p", "144p"]
    if tab2_quality_state.get():
        tab2ResolutionBoxOptions = OptionMenu(tab2, tab2_other_resolution_data, *OPTIONS)
        tab2ResolutionBoxOptions.place(x = 160, y = 205)
        createToolTip(tab2ResolutionBoxOptions, text = "Not all resolutions are supported on every video.")
    else:
        try:
            tab2ResolutionBoxOptions.destroy()
        except NameError:
            pass

def copyCommand():
    final_command = dlBegin(show_command=True)
    final_command = " ".join(final_command)
    print(final_command)
    pyperclip.copy(final_command)

###########################################################################################################################

def errorCheck():
    if len(url_data.get()) == 0 and usrlist_state.get() == 0:
        messagebox.showwarning("Warning", "The URL field is empty!")
        return "error-URL"
    #future update
    """
    URL_request = requests.get(url_data.get())
    if "Video unavailable" in URL_request.text:
        messagebox.showwarning("Warning", "That is not a valid URL!")
        return "error-invalid-url"
    """
    if len(dl_data.get()) == 0:
        messagebox.showwarning("Warning", "The destination field is empty!")
        return "error-destination"
    if name_state.get() and (len(name_data.get()) == 0 and not hyperlink_state.get() and not date_state.get() and not channel_category_state.get()):
        messagebox.showwarning("Warning", "The Custom Name field is empty and no additional settings are selected!\nPlease uncheck it, check a name option, or enter a name.")
        return "error-name"
    if tabControl.index("current") == 0:
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
            dlBegin()
        else:
            dlBegin()
    elif tabControl.index("current") == 1:
        if tab2_cookies_state.get() and tab2_cookies_data.get() == "":
            messagebox.showwarning("Warning", "Please fill in cookie data\nor uncheck cookie option.")
        else:
            dlBegin()

def monButtonStop(): 
    global stopMonitoring
    stopMonitoring = 1
    print("Stop Button Pressed, stopMonitoring =", stopMonitoring)

def dlBegin(show_command=False): #### 0 = no monitor mode, 1 = monitor mode
    global downloading, shell_used, cmd_list, stopMonitorButton, tab2stopMonitorButton
    if tabControl.index("current") == 0: ################################ yt-dlp
        cmd_list = ["yt-dlp"]
    if tabControl.index("current") == 1: ################################ ytarchive
        cmd_list = ["ytarchive"]
####################################################################### Applies to all tabs
    #dir_location = '''"'''
    if name_state.get() and len(name_data.get()) > 0:
        dir_location = str(dl_data.get())
        if channel_category_state.get():
            #[Channel]/
            dir_location += "/%(channel)s"
        if hyperlink_state.get() and not date_state.get():
            #Custom Name [hyperlink].[extension]
            dir_location += "/" + str(name_data.get()) + " %(id)s"
        elif date_state.get() and not hyperlink_state.get():
            #[date] Custom Name.[extension]
            dir_location += "/%(upload_date)s " + str(name_data.get()) 
        elif hyperlink_state.get() and date_state.get():
            #[date] Custom Name [hyperlink].[extension]
            dir_location += "/%(upload_date)s " + str(name_data.get()) + " %(id)s"
        else:
            # Only Custom Name
            dir_location += "/" + str(name_data.get())
    elif name_state.get() and len(name_data.get()) == 0:
        dir_location = str(dl_data.get())
        if channel_category_state.get():
            #[Channel]/
            dir_location += "/%(channel)s"
        if hyperlink_state.get() and not date_state.get():
            #[Default Name] [hyperlink].[extension]
            dir_location += "/%(title)s %(id)s"
        elif date_state.get() and not hyperlink_state.get():
            #[date] [Default Name].[extension]
            dir_location += "/%(upload_date)s %(title)s"
        elif hyperlink_state.get() and date_state.get():
            #[date] [Default Name] [hyperlink].[extension]
            dir_location += "/%(upload_date)s %(title)s %(id)s"
        else:
            dir_location += "/%(title)s"
    else:
        dir_location = str(dl_data.get())
        if channel_category_state.get():
            dir_location += "/%(channel)s"
        dir_location += "/%(title)s %(id)s"
    #dir_location += '''"'''
    cmd_list.append("-o")
    if show_command == False:
        cmd_list.append(str(dir_location))
    else:
        cmd_list.append('''"''' + str(dir_location) + '''"''')
    

    if description_state.get():
        cmd_list.append("--write-description")

    #########################################################################################
    if tabControl.index("current") == 0: ############################################################### yt-dlp
        if monitor_mode_state.get():
            full_date = mm_year_data.get() + mm_month_data.get() + mm_day_data.get()
            cmd_list.append("--dateafter")
            cmd_list.append(full_date)
        
        if cookie_state.get() and browser_state.get() != "file":
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
        elif cookie_state.get() and browser_state.get() == "file":
            cmd_list.append("--cookies")
            if show_command == False:
                cmd_list.append(cookies_data.get())
            else:
                cmd_list.append('''"''' + str(cookies_data.get()) + '''"''')
        
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
        
        if skip_vid_state.get():
            cmd_list.append("--skip-download")

        if usrlist_state.get():
            cmd_list.append("-a")
            if show_command == False:
                cmd_list.append(usrlist_data.get())
            else:
                cmd_list.append('''"''' + str(usrlist_data.get()) + '''"''')
        else:
            cmd_list.append(url_data.get())
        
        if subtitle_state.get():
            cmd_list.append("--all-subs")
        if subtitle_embed_state.get():
            cmd_list.append("--embed-subs")

        if allformats_state.get():
            cmd_list.append("-f")
            cmd_list.append("all")

        if other_resolution_state.get() and audio_state.get() == 0:
            cmd_list.append("-S")
            resolution_final = "res:" + other_resolution_data.get()
            cmd_list.append(resolution_final.replace("p" ,""))
        
        if other_encoding_state.get():
            cmd_list.append("--remux")
            cmd_list.append(other_encoding_data.get())
            cmd_list.append("--merge")
            cmd_list.append(other_encoding_data.get())

        if monitor_mode_state.get():
            if show_command == False:
                print("\n", cmd_list, "\n")
                dlButton.destroy()
                stopMonitorButton = Button(text = "  Stop Monitoring  ", command = monButtonStop)
                stopMonitorButton.place(x = 5, y = 500)
                createToolTip(stopMonitorButton, text = "Kill the monitor mode process, interrupting downloads.\nIf you wish to download other videos while in monitor\nmode, please launch another instance of this program.")
                launchMonitorThread = threading.Thread(target = monitorThread, args = [cmd_list]) #launch new thread so download monitoring doesnt interfere with window processing.
                launchMonitorThread.start()
                return 0 
            else:
                return cmd_list
########################################################################## ytarchive (tab2)
    if tabControl.index("current") == 1:
        if tab2_wait_state.get():
            if tab2_frequency_state.get():
                cmd_list.append("--retry-stream")
                cmd_list.append(str(tab2_wait_num.get()))
            else:
                cmd_list.append("-w")
        else:
            if tab2_monitor_mode_state.get() == 0:
                cmd_list.append("--no-wait")
            else:
                cmd_list.append("--monitor-channel")
        if tab2_separate_audio_state.get():
            cmd_list.append("--separate-audio")
        if tab2_cookies_state.get():
            cmd_list.append("-c")
            if show_command == False:
                cmd_list.append(tab2_cookies_data.get())
            else:
                cmd_list.append('''"''' + tab2_cookies_data.get() + '''"''')
        if tab2_mkv_state.get():
            cmd_list.append("--mkv")
        if tab2_thumbwrite_state.get():
            cmd_list.append("--write-thumbnail")
        if tab2_thumbembed_state.get():
            cmd_list.append("-t")
        cmd_list.append(url_data.get())

        if tab2_quality_state.get() == 0 and tab2_audio_only_state.get() == 0:
            cmd_list.append("best")
        elif tab2_quality_state.get() and tab2_audio_only_state.get() == 0:
            t2_quality_choice = str(tab2_other_resolution_data.get()) + "/best"
            cmd_list.append(str(t2_quality_choice))
        else: #tab2_audio_only_state.get():
            cmd_list.append("audio_only/best")

        if tab2_monitor_mode_state.get():
            if show_command == False:
                print("\n", cmd_list, "\n")
                dlButton.destroy()
                tab2stopMonitorButton = Button(text = "Stop Monitoring", command = monButtonStop)
                tab2stopMonitorButton.place(x = 5, y = 500)
                createToolTip(tab2stopMonitorButton, text = "Kill the monitor mode process early, interrupting downloads.\nIf you wish to download other videos while in monitor\nmode, please launch another instance of this program.")
                tab2launchMonitorThread = threading.Thread(target = tab2monitorThread, args = [cmd_list]) #launch new thread so download monitoring doesnt interfere with window processing.
                tab2launchMonitorThread.start()
                return 0 
            else:
                return cmd_list
        ################ --monitor-channel - launch it as a new thread, similar to normal monitor mode.
        
##########################################################################
    print("\n", cmd_list, "\n")
    if term_state.get():
        if show_command == False:
            log = open('log.txt', 'w')
            cmd_string = " ".join(cmd_list)
            log.write(cmd_string)
            downloading = subprocess.Popen(cmd_list, shell=True)
            messagebox.showinfo("Download Status", "Download Starting")
            #for line in downloading.stdout:  ##### eventually write to terminal and to text log file
            #    print(line, "\n")
            #    log.write(str(line))
            shell_used = True
        else:
            return cmd_list
    else:
        if show_command == False:
            log = open('log.txt', 'w')
            cmd_string = " ".join(cmd_list)
            log.write(cmd_string)
            downloading = subprocess.Popen(cmd_list, shell=False)
            #for line in downloading.stdout:
            #    print(line, "\n")
            #    log.write(str(line))
            shell_used = False
        else:
            return cmd_list

###### Tab1 monitor mode
def monitorThread(cmd_commands):
    global dlButton, stopMonitoring, mon_running
    mon_running = True
    if term_state.get():
        log = open('log.txt', 'w')
        cmd_string = " ".join(cmd_list)
        log.write(cmd_string)
        downloading = subprocess.Popen(cmd_list, shell=True)
        #for line in downloading.stdout:
        #    print(line, "\n")
        #    log.write(str(line))   
    else:
        log = open('log.txt', 'w')
        cmd_string = " ".join(cmd_list)
        log.write(cmd_string)
        downloading = subprocess.Popen(cmd_list, shell=False)
        #for line in downloading.stdout:
        #    print(line, "\n")
        #    log.write(str(line))
    print_count = 0
    getcontext().prec = 15
    while not stopMonitoring:
        if downloading.poll() == None:
            print_count += Decimal(0.3)
            if print_count % Decimal(15) == 0:
                print("Process ID:", downloading.pid, "has been running for", print_count, "seconds.")
            time.sleep(0.3)
            continue
        else:
            print("Restarting process.")
            restart_count = 0
            while not stopMonitoring and restart_count <= 15:
                restart_count += Decimal(0.3)
                time.sleep(0.3)
            if term_state.get():
                log = open('log.txt', 'w')
                cmd_string = " ".join(cmd_list)
                log.write(cmd_string)
                downloading = subprocess.Popen(cmd_list, shell=True)
                print("Process ID:", downloading.pid)
                #for line in downloading.stdout:
                #    print(line, "\n")
                #    log.write(str(line)) 
            else:
                log = open('log.txt', 'w')
                cmd_string = " ".join(cmd_list)
                log.write(cmd_string)
                downloading = subprocess.Popen(cmd_list, shell=False)
                print("Process ID:", downloading.pid)
                #for line in downloading.stdout:
                #    print(line, "\n")
                #    log.write(str(line))
    print("Stopped Monitoring")
    child_pid = downloading.pid
    print("Killing process ID:", downloading.pid)
    try:
        os.kill(child_pid, signal.SIGTERM)
    except Exception:
        print("Process Kill Exception")
        pass
    stopMonitorButton.destroy()
    mon_running = False
    dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = errorCheck)
    dlButton.place(x = 5, y = 500)
    stopMonitoring = 0
    return

###### Tab2 monitor mode
def tab2monitorThread(cmd_commands):
    global dlButton, stopMonitoring, mon_running, tab2stopMonitorButton
    stopMonitoring = 0
    mon_running = True
    if term_state.get():
        log = open('log.txt', 'w')
        cmd_string = " ".join(cmd_list)
        log.write(cmd_string)
        downloading = subprocess.Popen(cmd_list, shell=True)
        #for line in downloading.stdout:
        #    print(line, "\n")
        #    log.write(str(line))
    else:
        log = open('log.txt', 'w')
        cmd_string = " ".join(cmd_list)
        log.write(cmd_string)
        downloading = subprocess.Popen(cmd_list, shell=False)
        #for line in downloading.stdout:
        #    print(line, "\n")
        #    log.write(str(line))
    print_count = 0
    getcontext().prec = 15
    while not stopMonitoring and downloading.poll() == None:
        print_count += Decimal(0.3)
        if print_count % Decimal(15) == 0:
            print("Process ID:", downloading.pid, "has been running for", print_count, "seconds.")
        time.sleep(0.3)
    print("Stopped Monitoring")
    child_pid = downloading.pid
    print("Killing process ID:", downloading.pid)
    try:
        os.kill(child_pid, signal.SIGTERM)
    except Exception:
        print("Process Kill Exception, perhaps process died on its own?")
        pass
    tab2stopMonitorButton.destroy()
    mon_running = False
    dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = errorCheck)
    dlButton.place(x = 5, y = 500)
    return

################### For future updates
""" 
def on_closing():

    if mon_running:
        if messagebox.askokcancel("Quit", "Monitor is still running.\nDo you want to end monitor mode and quit?"):
            windowMain.destroy()
    else:
        windowMain.destroy()
"""
######################################

def windowIcon(windowName):
    try:
        icon = """ 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
        """
        icondata= base64.b64decode(icon)
        ## The temp file is icon.ico
        tempFile = "icon.ico"
        iconfile = open(tempFile,"wb")
        ## Extract the icon
        iconfile.write(icondata)
        iconfile.close()
        windowName.wm_iconbitmap(tempFile)
        ## Delete the tempfile
        os.remove(tempFile)
    except Exception:
        pass


################################################ Window Starts Here ################################################


windowMain = Tk()
windowMain.title("GUI-DLP v2.0.0")
windowMain.geometry("510x535")
windowMain.resizable(False, False)
windowIcon(windowMain)
tabControl = ttk.Notebook(windowMain)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text = "   yt-dlp   ")
tabControl.add(tab2, text = " ytarchive ")
tabControl.pack(expand = 1, pady = 5, fill = "both")



url_data = StringVar(windowMain, "")
dl_data = StringVar(windowMain, "")
name_state = IntVar(windowMain, 0)
name_data = StringVar(windowMain, "")
date_state = IntVar(windowMain, 0)
channel_category_state = IntVar(windowMain, 0)
hyperlink_state = IntVar(windowMain, 0)
cookie_state = IntVar(windowMain, 0)
cookies_data = StringVar(windowMain, "")
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
skip_vid_state = IntVar(windowMain, 0)

usrlist_state = IntVar(windowMain, 0)
usrlist_data = StringVar(windowMain, "")

subtitle_state = IntVar(windowMain, 0)
subtitle_embed_state = IntVar(windowMain, 0)
allformats_state = IntVar(windowMain, 0)

term_state = IntVar(windowMain, 0)
monitor_mode_state = IntVar(windowMain, 0)
mm_year_data = StringVar(windowMain, "")
mm_month_data = StringVar(windowMain, "")
mm_day_data = StringVar(windowMain, "")

############################# Tab 2 Variables
tab2_cookies_state = IntVar(windowMain, 0)
tab2_cookies_data = StringVar(windowMain, "")
tab2_wait_state = IntVar(windowMain, 0)
tab2_frequency_state = IntVar(windowMain, 0)
tab2_wait_num = IntVar(windowMain, 15)
tab2_thumbwrite_state = IntVar(windowMain, 0)
tab2_thumbembed_state = IntVar(windowMain, 0)
tab2_audio_only_state = IntVar(windowMain, 0)
tab2_quality_state = IntVar(windowMain, 0)
tab2_other_resolution_data = StringVar(windowMain, "1080p")
tab2_monitor_mode_state = IntVar(windowMain, 0)
tab2_mkv_state = IntVar(windowMain, 0)
tab2_separate_audio_state = IntVar(windowMain, 0)
#############################################

stopMonitoring = 0
browser_option_check = 0
cmd_list = []

##############################################################################
############################################################################## Assets on all tabs
mediaSource = Entry(windowMain, width = 60, textvariable = url_data)
mediaSource.place(x = 6, y = 33)
createToolTip(mediaSource, text = "Enter the URL of the Youtube video, Twitch\nstream, etc, that you want to download. You\ncan download individual videos or playlists.")

mediaSourceText = Label(windowMain, text = "URL for media source")
mediaSourceText.place(x = 375, y = 32)

fileLocation = Entry(windowMain, width = 60, textvariable = dl_data)
fileLocation.place(x = 6, y = 58)
createToolTip(fileLocation, text = "Enter the absolute path\nto where you want the\nvideo to be downloaded to\n(or use the 'Destination' button).")

fileButton = Button(windowMain, text = "       Destination       ", fg = "blue", command = fileButtonClicked)
fileButton.place(x = 378, y = 55)
createToolTip(fileButton, text = "Enter the absolute path\nto where you want the\nvideo to be downloaded to\n(or use the 'Destination' button).")

dlButton = Button(windowMain, text = "     Begin Download     ", fg = "dark green", background = "light gray", command = errorCheck)
dlButton.place(x = 5, y = 500)

helpButton = Button(windowMain, text = "   Help   ", command = helpMenu)
helpButton.place(x = 450, y = 470)
createToolTip(helpButton, text = "Open the README page\non GitHub for detailed\ninfo about each option.")

updateButton = Button(windowMain, text = "Update?", command = checkGitHub)
updateButton.place(x = 450, y = 500)
createToolTip(updateButton, text = "Open the GitHub Releases\npage to manually check\nfor updates.")

customNameCheck = Checkbutton(windowMain, text = "Custom Name?", variable = name_state, command = nameboxAppear)
customNameCheck.place(x = 1, y = 83)
createToolTip(customNameCheck, "Set a custom name for the downloaded file.\nDO NOT INCLUDE FILE EXTENSION! If you\nare downloading a playlist, check 'Include ID?',\nelse the videos may overwrite themselves.\nThe default name is [Video title] [Video ID].")

showTerm = Checkbutton(windowMain, text = "Hide Terminal?", variable = term_state)
showTerm.place(x = 140, y = 500)
createToolTip(showTerm, text = "The process typically opens a terminal to display progress. Select this to prevent it.\nHiding is not recommended for monitor mode, as it allows you to kill the process in the\nterminal window immediatly, if desired. Also not recommended for non-default encoding\nand non-highest resolution, as you will not see if download failures take place.")

descriptionCheck = Checkbutton(windowMain, text = "Download Description?", variable = description_state)
descriptionCheck.place(x = 1, y = 133)
createToolTip(descriptionCheck, text = "Write the video description to a separate file.")

commandShow = Button(windowMain, text = "Copy?", command = copyCommand)
commandShow.place(x = 320, y = 500)
createToolTip(commandShow, text = "Copy the current configuration to your clipboard.")

# Potentially add an option to add or remove the ToolTips?

##################################################################################################
##################################################################################################


##################################################################################################
############################################################################################ Tab 1
cookiesCheck = Checkbutton(tab1, text = "Use Cookies?", variable = cookie_state, command = browserAppear)
cookiesCheck.place(x = 0, y = 80)
createToolTip(cookiesCheck, text = "Import cookies from your browser of choice.\nMay be needed for paywalled content.")

commentsCheck = Checkbutton(tab1, text = "Download Comments?", variable = comments_state)
commentsCheck.place(x = 0, y = 130)
createToolTip(commentsCheck, text = "Download stream comments to a separate infojson file.")

waitCheck = Checkbutton(tab1, text = "Wait for Video?", variable = wait_state, command = waitAppear)
waitCheck.place(x = 0, y = 155)
createToolTip(waitCheck, text = "If the video is scheduled but not\nstarted yet, use this to retry playing\nthe video after the selected number\nof seconds.")

writeThumbnail = Checkbutton(tab1, text = "Write Thumbnail?", variable = thumbwrite_state, command = thumbnailFormat)
writeThumbnail.place(x = 160, y = 180)
createToolTip(writeThumbnail, text = "Download the thumbnail\nas a separate image file.")

embedThumbnail = Checkbutton(tab1, text = "Embed Thumbnail?", variable = thumbembed_state)
embedThumbnail.place(x = 0, y = 180)
createToolTip(embedThumbnail, text = "Embed the thumbnail as the\ndownloaded video's thumbnail.")

audioOnly = Checkbutton(tab1, text = "Audio Only?", variable = audio_state)
audioOnly.place(x = 0, y = 205)
createToolTip(audioOnly, text = "Only download the source's audio.")

skipVid = Checkbutton(tab1, text = "Skip Video?", variable = skip_vid_state)
skipVid.place(x = 160, y = 205)
createToolTip(skipVid, text = "Download all other selected options,\nbut skip downloading the video itself.")

downloadList = Checkbutton(tab1, text = "Download List?", variable = usrlist_state, command = userListAppear)
downloadList.place(x = 0, y = 230)
createToolTip(downloadList, text = "If you have a list of URLs to download\n(separated by a new line in a text doc),\nuse this to download videos from that\ndocument's data. This takes priority\nover the URL field.")

downloadSubs = Checkbutton(tab1, text = "Download Subs?", variable = subtitle_state)
downloadSubs.place(x = 0, y = 255)
createToolTip(downloadSubs, text = "Download All Available subtitle options for a video.")

embedSubs = Checkbutton(tab1, text = "Embed Subs?", variable = subtitle_embed_state)
embedSubs.place(x = 160, y = 255)
createToolTip(embedSubs, text = "Embed all available subtitle options for a video.")

downloadAllFormats = Checkbutton(tab1, text = "All Formats?", variable = allformats_state)
downloadAllFormats.place(x = 0, y = 280)
createToolTip(downloadAllFormats, text = "Download all file types available.")

otherResolution = Checkbutton(tab1, text = "Non-highest Quality?", variable = other_resolution_state, command = resolutionBoxAppear)
otherResolution.place(x = 160, y = 280)
createToolTip(otherResolution, text = "Choose a resolution to download the video\nat that is not the default highest.")

otherEncoding = Checkbutton(tab1, text = "Non-default Encoding?", variable = other_encoding_state, command = encodingBoxAppear)
otherEncoding.place(x = 0, y = 305)
createToolTip(otherEncoding, text = "Choose an format to encode the video\nas instead of using the default.")

tab1.rowconfigure(18, weight = 1)

tab2mediaSourceText = Label(tab2, text = "Download with ytarchive")
tab2mediaSourceText.place(x = 5, y = 450)
createToolTip(tab2mediaSourceText, text = "ytarchive is meant to be used with active or scheduled livestreams\non YouTube only. It cannot be used on other platforms, or completed\nstreams or videos. Use yt-dlp for uploaded videos.")

monitorModeCheck = Checkbutton(tab1, text = "Monitor\nMode?", variable = monitor_mode_state, command = monitorTimeRange)
monitorModeCheck.place(x = 245, y = 464)
createToolTip(monitorModeCheck, text = "Monitor video source for new uploads. Used to monitor a\nsource of videos, not a specific video. For example, to monitor\na YouTube channel for new uploads in the 'videos' tab, enter\n'https://www.youtube.com/[channel name]/videos'\nIf you want to monitor streams, use the '/streams' link.\nThe same concept applies to other sites that yt-dlp supports.")
##################################################################################################
##################################################################################################


##################################################################################################
################################################################################################## Tab 2
tab2Cookies = Checkbutton(tab2, text = "Cookies File?", variable = tab2_cookies_state, command = tab2CookiesFileLocationBar)
tab2Cookies.place(x = 0, y = 80)
createToolTip(tab2Cookies, text = "ytarchive cannot pull cookies from the browser,\nso instead, select a cookies file if content you\nwish to access is paywalled. Must first access\nit through the browser you pull cookies from.")

tab2Wait = Checkbutton(tab2, text = "Wait for Video?", variable = tab2_wait_state, command = tab2AddRetryStream) ### Add command(s) to show option for --retry-stream [seconds]
tab2Wait.place(x = 0, y = 130)
createToolTip(tab2Wait, text = "If the video is scheduled but\nnot started yet, use this to\nwait until the video starts to\ncheck again.") ##### finish this next!!!!

tab2writeThumbnail = Checkbutton(tab2, text = "Write Thumbnail?", variable = tab2_thumbwrite_state, command = thumbnailFormat)
tab2writeThumbnail.place(x = 160, y = 155)
createToolTip(tab2writeThumbnail, text = "Download the thumbnail\nas a separate image file.")

tab2embedThumbnail = Checkbutton(tab2, text = "Embed Thumbnail?", variable = tab2_thumbembed_state)
tab2embedThumbnail.place(x = 0, y = 155)
createToolTip(tab2embedThumbnail, text = "Embed the thumbnail as the\ndownloaded video's thumbnail.")

tab2audioOnly = Checkbutton(tab2, text = "Audio Only?", variable = tab2_audio_only_state) 
tab2audioOnly.place(x = 0, y = 180)
createToolTip(tab2audioOnly, text = "Download only the audio of the livestream.")

tab2vidQuality = Checkbutton(tab2, text = "Non-highest Quality?", variable = tab2_quality_state, command = tab2qualityChoice) 
tab2vidQuality.place(x = 0, y = 205)
createToolTip(tab2vidQuality, text = "ytarchive will choose the highest quality by default.\nChoose a different quality to download at. If the chosen\resolution isn't available, highest quality will be chosen.\n'Audio only' overrides this option.")

tab2mkvOption = Checkbutton(tab2, text = "Encode as MKV?", variable = tab2_mkv_state)
tab2mkvOption.place(x = 0, y = 230)
createToolTip(tab2mkvOption, text = "Encode the downloaded video in MKV format.\nIgnored when using 'Audio only'.")

tab2separateAudio = Checkbutton(tab2, text = "Separate Audio?", variable = tab2_separate_audio_state)
tab2separateAudio.place(x = 0, y = 255)
createToolTip(tab2separateAudio, text = "Save the audio to a separate file,\nsimilar to when downloading audio_only,\nalongside the final muxed file.")

mediaSourceText = Label(tab1, text = "Download with yt-dlp")
mediaSourceText.place(x = 5, y = 450)
createToolTip(mediaSourceText, text = "yt-dlp is meant for videos uploaded to a variety of platforms. If you want\nto download scheduled or active YouTube streams, I would recommend\nytarchive, but yt-dlp usually works too. ytarchive can begin recording\nfrom the beginning of the stream, even if started midway though.")

tab2monitorModeCheck = Checkbutton(tab2, text = "Monitor\nMode?", variable = tab2_monitor_mode_state)
tab2monitorModeCheck.place(x = 245, y = 464)
createToolTip(tab2monitorModeCheck, text = "ytarchive monitor mode is much more stable, and more recommended than yt-dlp\nmonitor mode. Use this to monitor a YouTube channel for new uploads.\nUse a '/videos' or '/streams' URL.")
##################################################################################################
##################################################################################################

#windowMain.protocol("WM_DELETE_WINDOW", on_closing)  ###### For future updates
windowMain.mainloop()
