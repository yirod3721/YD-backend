import yt_dlp
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
            return 0
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
            return 0, filepath
    except yt_dlp.utils.DownloadError as e:
        print("Download Utils", e)
        return 1

