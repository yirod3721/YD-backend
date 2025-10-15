import yt_dlp, os
def video_download(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url)
            filepath = ydl.prepare_filename(info)
            filepath = os.path.splitext(filepath)[0] + '.mp4'
            print(f"Path is {filepath}")
            return filepath
    except:
        with yt_dlp.utils.DownloadError as e:
            print("ERROR", e)
            return 1



def audio_download(url):
    ydl_opts = {
        'format': 'bestaudio[abr>=192]/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',

            }
        ]
    }
    ydl_opt_audio = {
        'writethumbnail': True,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }, 
        {
          'key': 'FFmpegMetadata',
          'add_metadata': True,

        },
        {'key': 'EmbedThumbnail'},]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opt_audio) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url)
            filepath = ydl.prepare_filename(info)
            filepath = os.path.splitext(filepath)[0] + '.mp3'
            print(f"Path is {filepath}")
            return filepath
    except yt_dlp.utils.DownloadError as e:
        print("Download Utils", e)
        return 1

