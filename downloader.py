import yt_dlp, os
from file_manager import move_to_final, cleanup_temp
def video_download(url):
    temp_out = 'downloads/temp/%(title)s.%(ext)s'
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': temp_out
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url)
            filepath = ydl.prepare_filename(info)
            filepath = os.path.splitext(filepath)[0] + '.mp4'
            print(f"Path is {filepath}")
            final_path = move_to_final(filepath, 'video')
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
            final_path  = move_to_final(filepath, 'audio')
            return final_path
    except yt_dlp.utils.DownloadError as e:
        print("Download Utils", e)
        return 1

