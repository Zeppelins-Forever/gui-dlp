# gui-dlp

This is a GUI front-end application for yt-dlp. You must already 
have yt-dlp (and its dependencies, such as ffmepg) installed and in 
the system PATH Environment. (Settings > System > About > Advanced 
System Settings > Advanced tab > Environment Variables > Double-
click "Path" under System Variables > make a new path to the folder 
where you placed yt-dlp (and do the same for ffmpeg, if you haven't 
already after downloading yt-dlp)).

This presently does not have all of the features available in the 
terminal, so I wouldn't recommend using it if you need more 
technically specific options.

You can run it as a python script just fine, or if you want to 
convert this into a Windows executable, I would recommend the tool 
auto-py-to-exe (https://pypi.org/project/auto-py-to-exe/), or just
use one of my releases.

It is designed with Windows in mind (Linux and macOS not thoroughly 
tested). For experimental Linux users, you may have to install "Tk"
(Tkinter module for Python) before running the python3 script. A 
couple of features may not work exactly as intended in Linux (terminal
window not showing with download progress), but core functionality may
still be intact. Not thoroughly tested, however, so beware of bugs.

--------------------------------------------------------------------

<details>
<summary><h2>Documentation</h2></summary>
<br>
        <h3><u id="1-yt-dlp-options">yt-dlp options</u></h3>
        <p>
            yt-dlp is meant for videos uploaded to a variety of platforms. If you want to download scheduled or active
            YouTube streams, I would recommend ytarchive, but yt-dlp usually works too. ytarchive can begin recording
            from the beginning of the stream, even if started midway though.<br>
            It can be found at <a href="https://github.com/yt-dlp/yt-dlp">https://github.com/yt-dlp/yt-dlp</a>
        </p>
        <br>
        <u id="1-url-for-media-source">URL for media source</u>
        <p>Enter the source URL of the desired video (or channel, or playlist, etc.)</p>
        <br>
        <u id="1-destination">Destination</u>
        <p>Enter the absolute, not relative, path to the folder you wish to download the video to. If Custom Name > Sort
            via Channel is selected, it will place the channel folder here and the downloaded video within it.</p>
        <br>
        <u id="1-custom-name">Custom Name</u>
        <p>
            Provides options to customize the output name of the video from the default of “[title] [video ID]”. If this
            is selected, but the options are left in their default state (Include URL, Date First, and Sort via Channel
            are unchecked and the rename box is empty), the download will not be allowed to proceed. If Custom Name is
            selected, it functionally treats your video title as blank until other customizations are selected.<br>
            This is the order in which these option appear in the final downloaded file name:<br>
            [channel] / [upload date] [title] [video ID].extension
        </p>
        <u style="margin-left: 50px;" id="1-include-id">Include ID</u>
        <p style="margin-left: 50px;">An option which only appears when Custom Name is selected. Adds the video ID to
            the video name itself, after the title, if the video has one. Recommended if using <a
                href="#1-custom-name-box">Custom Name Box</a> in conjunction with <a href="#1-download-list">Download
                List</a>.</p>
        <br>
        <u style="margin-left: 50px;" id="1-date-first">Date First</u>
        <p style="margin-left: 50px;">An option which only appears when Custom Name is selected. Adds the date of upload
            to the beginning of the video title, in YYYYMMDD format.</p>
        <br>
        <u style="margin-left: 50px;" id="1-sort-via-channel">Sort via Channel</u>
        <p style="margin-left: 50px;">An option which only appears when Custom Name is selected. Places the downloaded
            video inside of a folder named after the channel of the video source. Destination would then indicate the
            location of the channel folder not the video itself.</p>
        <br>
        <u style="margin-left: 50px;" id="1-custom-name-box">Custom Name Box</u>
        <p style="margin-left: 50px;">An option which only appears when Custom Name is selected. You can change the
            title of the video itself, replacing the default video title with a title of choice. (Ex, downloading a
            YouTube video titled “Yee” from channel “revergo”, with Custom Name, Include ID, Date First, and Sort via
            Channel selected, and typing “funny video” in the name box will result in a file titled “20120229 funny
            video q6EoRBvdVPQ.webm” within the folder “revergo”.) Do not include the file extension.</p>
        <br>
        <u id="1-use-cookies">Use Cookies</u>
        <p>Cookies allow certain data to be pulled from the browser, such as logins saved to the browser, which can
            allow downloading paywalled content, as long as you could access this data through the browser.</p>
        <u style="margin-left: 50px;" id="1-browser-choices">Browser Choices</u>
        <p style="margin-left: 50px;">This pulls cookies automatically from one of the available browsers. If <a
                href="#1-cookies-file">Cookies File</a> is chosen from these options, it will open the Cookies File box,
            downloading from a cookies file instead of pulling directly from a browser.</p>
        <br>
        <u style="margin-left: 50px;" id="1-cookies-file">Cookies File</u>
        <p style="margin-left: 50px;">This allows you to select a file containing cookies data (text files are typically
            a good choice) in Netscape format. Use the absolute, not relative, path to the file. The EditThisCookie <a
                href="https://www.editthiscookie.com/">https://www.editthiscookie.com/</a> browser extension, for
            example, allows copying your browser cookies to your clipboard (it will have to be configured to use the
            Netscape format), which you can paste into a text file. Said text file can then be used as the cookies file
            for this option.</p>
        <br>
        <u id="1-download-description">Download Description</u>
        <p>This option downloads the description of the video source, if one is available, to a separate file.</p>
        <br>
        <u id="1-download-comments">Download Comments</u>
        <p>This option downloads comments from the video source, if comments are available, to a separate file.</p>
        <br>
        <u id="1-wait-for-video">Wait for Video</u>
        <p>This option can be used when a video has an associated URL and is scheduled to release in the future, but is
            not released yet (ex. YouTube videos having waiting rooms to start). This will continue to check the video
            every 15 seconds by default, but can be adjusted as desired.</p>
        <br>
        <u id="1-embed-thumbnail">Embed Thumbnail</u>
        <p>This option will embed the video thumbnail in the downloaded file itself. Depending on the file format, the
            embedded thumbnail may or may not display on certain operating systems due to not having the proper codecs.
            MP4 is generally reliable in that regard.</p>
        <br>
        <u id="1-write-thumbnail">Write Thumbnail</u>
        <p>This option, in addition to downloading the video itself, writes the thumbnail to a separate file. The three
            file types available to be selected are WEBP, PNG, and JPG; yt-dlp defaults to webp.</p>
        <br>
        <u id="1-audio-only">Audio Only</u>
        <p>This option only downloads the audio of the video source.</p>
        <br>
        <u id="1-skip-video">Skip Video</u>
        <p>This option only downloads other selected attributed, but not the video itself. (Ex. If Download Comments,
            Write Thumbnail, and Skip Video are selected, only the comments and thumbnail would be downloaded, but not
            the video itself.)</p>
        <br>
        <u id="1-download-list">Download List</u>
        <p>This option lets you download multiple videos from a list in an external text file. In the external text
            file, enter one URL per line, and provide the absolute file path to the file in the Download List box.</p>
        <br>
        <u id="1-download-subs">Download Subs</u>
        <p>This will download all available subtitles to an external file, if any are available, which can later be used
            by programs such as VLC to view subtitles in a video.</p>
        <br>
        <u id="1-embed-subs">Embed Subs</u>
        <p>This will embed all available subtitles within the downloaded video itself, rather than downloading them
            separately.</p>
        <br>
        <u id="1-all-formats">All Formats</u>
        <p>This will download all available file types of the available video.</p>
        <br>
        <u id="1-non-highest-quality">Non-highest Quality</u>
        <p>Specify a particular resolution to download at. The available resolutions to download at via yt-dlp are
            2160p, 1440p, 1080p, 720p, 480p, 360p, 240p, and 144p. <a href="#1-audio-only">Audio Only</a> takes
            precedence.</p>
        <br>
        <u id="1-non-default-encoding">Non-default Encoding</u>
        <p>This option allows you to select how the downloaded video should be encoded, and does not filter by if you
            are downloading only audio, audio and video, or any other options, so select carefully. MKV, WEBM, and MP4
            are the most commonly used options, so limit yourself to these if you are uncertain as to which formats you
            may want for videos. For Audio Only downloads, try M4A, MP4, or WAV.</p>
        <br>
        <u id="1-hide-terminal">Hide Terminal</u>
        <p>By default, when the program is run, a terminal window appears which will show the status and progress of the
            download. It is not generally recommend to check this, as doing so will prevent you from being able to kill
            a non-<a href="#1-monitor-mode">Monitor Mode</a> process if needed, nor see the status of the download.</p>
        <br>
        <u id="1-monitor-mode">Monitor Mode</u>
        <p>Monitor mode in yt-dlp mode is not a command supported with yt-dlp traditionally. The closes thing it has is
            Wait for Video, which allows it to wait on a video waiting room, but it cannot monitor a channel for new
            uploads. GUI-DLP attempts to add this functionality to yt-dlp by continuously running yt-dlp on a particular
            target. If a “/videos” or “/live” tab on YouTube is used instead of an individual video URL, yt-dlp will
            continuously read through each video available for the URL. Which videos will be downloaded can be filtered
            by date using the <a href="#1-start-date">Start Date</a> function. This also works for non-YouTube URLs, so
            long as new videos are shown in the same place and can be read by yt-dlp. This feature can additionally be
            used as a way to simply download all videos after a certain date, if you cancel Monitor Mode after the
            downloads are complete.</p>
        <u style="margin-left: 50px;" id="1-start-date">Start Date</u>
        <p style="margin-left: 50px;">Auto-fills the current date. Used to limit which videos in Monitor Mode will be
            downloaded, and will download anything after the given date. If monitoring a video that is scheduled to
            begin in the future, use the date that the waiting room was created (or before), not the date it is
            scheduled to release.</p>
        <br>
        <u id="1-help">Help</u>
        <p>
            Opens this document if it is detected, or the main GitHub page for GUI-DLP.<br>
            <a
                href="https://github.com/Zeppelins-Forever/gui-dlp/tree/main">https://github.com/Zeppelins-Forever/gui-dlp/tree/main</a>
        </p>
        <br>
        <u id="1-update">Update</u>
        <p>
            Opens the GitHub releases page for GUI-DLP, easily allowing you to download the most current version of this
            program. Auto-updates are not supported.<br>
            <a
                href="https://github.com/Zeppelins-Forever/gui-dlp/releases">https://github.com/Zeppelins-Forever/gui-dlp/releases</a>
        </p>
        <br>
        <h3><u id="2-ytarchive-options">ytarchive options</u></h3>
        <p>
            ytarchive is designed for YouTube specifically, and can only download actively running or scheduled live
            videos, and it downloads from the very beginning, even when starting midway through the stream. For anything
            already uploaded, or if you wish to only download the current moment of a stream and nothing before, use
            yt-dlp.<br>
            It can be found at <a href="https://github.com/Kethsar/ytarchive">https://github.com/Kethsar/ytarchive</a>"
        </p>
        <br>
        <u id="2-url-for-media-source">URL for media source</u>
        <p>See <a href="#1-url-for-media-source">yt-dlp > URL for Media Source</a></p>
        <br>
        <u id="2-destination">Destination</u>
        <p>See <a href="#1-destination">yt-dlp > Destination</a></p>
        <br>
        <u id="2-custom-name">Custom Name</u>
        <p>See <a href="#1-custom-name">yt-dlp > Custom Name</a></p>
        <br>
        <u id="2-cookies-file">Cookies File</u>
        <p>ytarchive does not support <a href="#1-browser-choices">Cookies from Browser</a> like yt-dlp does, so a
            cookies file must be used.</p>
        <br>
        <u id="2-download-description">Download Description</u>
        <p>See <a href="#1-download-description">yt-dlp > Download Description</a></p>
        <br>
        <u id="2-wait-for-video">Wait for Video</u>
        <p>yt-dlp and ytarchive have slightly different methods for waiting for a video to start, which is why ytarchve
            has more waiting options available in GUI-DLP. The Wait for Video option causes ytarchive to wait for the
            time which the video is scheduled to start before checking again. May not catch if the scheduled start time
            is moved forward.</p>
        <u style="margin-left: 50px;" id="2-check-more-often">Check more often</u>
        <p style="margin-left: 50px;">Rather than only waiting for the time the video is scheduled to start, it will
            repeatedly poll the time until the video starts, the time between checks being however many seconds are
            selected.</p>
        <br>
        <u id="2-write-thumbnail">Write Thumbnail</u>
        <p>See <a href="#1-write-thumbnail">yt-dlp > Write Thumbnail</a>, but without the option for choosing the
            written thumbnail format.</p>
        <br>
        <u id="2-embed-thumbnail">Embed Thumbnail</u>
        <p>See <a href="#1-embed-thumbnail">yt-dlp > Embed Thumbnail</a></p>
        <br>
        <u id="2-audio-only">Audio Only</u>
        <p>See <a href="#1-audio-only">yt-dlp > Audio Only</a></p>
        <br>
        <u id="2-non-highest-quality">Non-highest Quality</u>
        <p>Different qualities available through ytarchive that aren’t available through yt-dlp. All options available
            are 2160p60, 2160p, 1440p60, 1440p, 1080p60, 1080p, 720p60, 720p, 480p, 360p, 240p, 144p. <a
                href="#2-audio-only">Audio Only</a> takes precedence over any quality chosen.</p>
        <br>
        <u id="2-encode-as-mkv">Encode as MKV</u>
        <p>ytarchive has fewer video encoding options than yt-dlp. By default, it downloads all videos as MP4, but this
            option will make it use MKV instead.</p>
        <br>
        <u id="2-separate-audio">Separate Audio</u>
        <p>Saves a copy of the audio to a separate file along with the full download.</p>
        <br>
        <u id="2-hide-terminal">Hide Terminal</u>
        <p>See <a href="#1-hide-terminal">yt-dlp > Hide Terminal</a></p>
        <br>
        <u id="2-monitor-mode">Monitor Mode</u>
        <p>Different than <a href="#1-monitor-mode">yt-dlp Monitor Mode</a>, ytarchive has a built in option to monitor
            YouTube channels. While GUI-DLP’s yt-dlp monitor mode can potentially work on a wider range of video
            sources, it is less reliable. If you want to monitor a YouTube channel, though, ytarchive Monitor Mode is
            highly recommended over yt-dlp. It must use a “/videos” or “/streams” tab, otherwise it will not work.</p>
        <br>
        <u id="2-help">Help</u>
        <p>See <a href="#1-help">yt-dlp > help</a></p>
        <br>
        <u id="2-update">Update</u>
        <p>See <a href="#1-update">yt-dlp > update</a></p>
</details>
