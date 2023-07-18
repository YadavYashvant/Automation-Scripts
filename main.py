from pytube import YouTube
# from pytube import YouTube
link = str(input("Enter Video link: "))
video_download = YouTube(link)
videos = video_download.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter index: "))
videos[strm].download()
print("Downloaded Succesfully!")