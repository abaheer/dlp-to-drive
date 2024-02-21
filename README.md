# yt-to-drive

- A basic GUI for yt-dlp with Google Authentication implementation using PyDrive
  - Upload files and playlist to Google Drive automatically
  - Automatically delete files after uploaded to drive
  - Users only need to authenticate once, after which their login will be stored locally

![](gui.jpg)

- Playlist: if checked, will download the entire playlist. Otherwise, only a single item from the playlist will be downloaded
- Include index: if checked, the index in the playlist will be included in the filename (e.g. 1 - Darude-Sandstorm)
- Save to Drive: if checked, files will be uploaded to Google Drive (after user authenticates)
- Temp files: if checked, will delete local audio files after they are uploaded to Google Drive

## How to use

- Install requirements (run cmd as administrator)

```
$ pip install -r requirements.txt
```

- Run using

```
$ python main.py
```

## Alternatively, download from executable-file branch.

- Simply run yt-dlp.exe in dist/yt-to-drive
- Run yt-to-drive.exe in dist/yt-to-drive to open the GUI (you can make a shortcut to this file)
- You only need to run the yt-dlp once

## Future scope

- allow users to:

  - select directory to save files locally
  - select output file format
  - allow user to queue multiple links

- conduct further testing.
