# yt-to-drive

- A basic GUI for yt-dlp with Google Auth implementation
- Upload files and playlist to Google Drive automatically
- Automatically delete files after uploaded to drive (temp files)
- Users only need to authenticate once, after which their login will be stored locally

![](gui.jpg)

- Save to Drive: if checked, files will be uploaded to Google Drive (after user authenticates)
- Temp files: if checked, will delete local audio files after they are uploaded to Google Drive
- Playlist: if checked, will download the entire playlist. Otherwise, only a single item from the playlist will be downloaded
- Include index: if checked, the index in the playlist will be included in the filename (e.g. 1 - Darude-Sandstorm)

## How to use

- Install requirements

```
$ pip install -r requirements.txt
```

- Run using

```
$ python main.py
```

- Alternatively, downlaod from executable-file branch.

* Simply run yt-dlp.exe in dist/yt-to-drive, then run yt-to-drive.exe (in the same directory as yt-dlp.exe)
* You only need to run the yt-dlp once

## Future scope

- allow users to:

  - select directory to save files locally
  - select file output format

- conduct further testing.
