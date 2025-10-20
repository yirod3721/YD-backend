import yt_dlp, os
from file_manager import move_to_final, cleanup_temp
def video_download(url):
    temp_out = 'downloads/temp/%(title)s.%(ext)s'
    ydl_opts = {
        'format': 'mp4',
        'cookiefile': 'cookies.txt',
        'outtmpl': temp_out
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filepath_ = ydl.prepare_filename(info)
            print(f"filepath1 is {filepath_}")
            filepath_ = os.path.splitext(filepath_)[0] + '.mp4'
            print(f"Path2 is {filepath_}")
            final_path = move_to_final(filepath_, 'video')
            print(f"filepath2 is {filepath_}")
            return final_path
    except:
        with yt_dlp.utils.DownloadError as e:
            print("ERROR", e)
            return 1



def audio_download(url):
    temp_out = 'downloads/temp/%(title)s.%(ext)s'
    ydl_opt_audio = {
        'writethumbnail': True,
        'outtmpl': temp_out,
        'cookiefile': 'cookies.txt',
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
            info = ydl.extract_info(url, download=True)  # download + metadata in one
            filepath = ydl.prepare_filename(info)
            filepath = os.path.splitext(filepath)[0] + ".mp3"
            print(f"Path is {filepath}")
            final_path  = move_to_final(filepath, 'audio')
            print(f"final path is {final_path}")
            return final_path
    except yt_dlp.utils.DownloadError as e:
        print("Download Utils", e)
        return 1

