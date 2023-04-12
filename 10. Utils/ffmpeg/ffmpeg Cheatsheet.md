## Adjust video speed
```
ffmpeg -i input.mp4 -filter_complex "[0:v]setpts=PTS/1.5[v];[0:a]atempo=1.5[a]" -map "[v]" -map "[a]" output.mp4
```
* Change value of `atempo`.

## webm to mp4
```
ffmpeg -i video.webm video.mp4
```