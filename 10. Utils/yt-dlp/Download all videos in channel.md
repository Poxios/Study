```cmd
yt-dlp -f "bv*[height>=720]+ba" --embed-thumbnail --embed-metadata --download-archive CHANNEL_NAME_HERE.txt https://www.youtube.com/c/CHANNEL_NAME_HERE/videos -o '%(channel)s/%(title)s.%(ext)s'
```