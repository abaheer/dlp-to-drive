# dlp-to-drive

- A basic GUI for yt-dlp with Google Authentication implementation using PyDrive
  - Upload files and playlists to Google Drive automatically
  - Automatically delete files after uploaded to Google Drive
  - Store credentials locally to instantly upload to Google Drive
  - Support for invalid filename characters (e.g. \*/!?)

![](gui.jpg)

- **Playlist**: if checked, will download the entire playlist.
- **Include index**: if checked, the index in the playlist will be included in the filename.
- **Save to Drive**: if checked, files will be uploaded to linked Google Drive account.
- **Temp files**: if checked, local audio files are deleted after they are uploaded to Google Drive.
- **.wav**: Coverts the file to .wav, otherwise it will remain in original format (e.g. opus).

## How to use

You will need to have [ffmpeg](https://ffmpeg.org/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file) installed and added to PATH or in the same directory as main.py.

- Install requirements:

```
$ pip install -r requirements.txt
```

- Run using:

```
$ python main.py
```

To use Google Drive functionality, you will need to generate a client_secret and client_id and add those to the settings.yaml file. For more information, check the [documentation](https://developers.google.com/people/quickstart/python#set_up_your_environment).

## Future scope

- Use mutithreaded approach to stop window from freezing while running
- Add progress bar
- Select directory to save files locally
- Select output file format
- Allow user to queue multiple links
- Conduct further testing
