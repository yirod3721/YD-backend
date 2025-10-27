import yt_dlp
from file_manager import cleanup_temp
def is_valid_youtube(url):
    """Check if a URL points to a valid YouTube video."""
    opts = {
        'cookiefile': 'cookies.txt'
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.extract_info(url, download=False)
        return True
    except yt_dlp.utils.DownloadError:
        return False


def data_fetch(url):
    #Fetch video metadata without downloading.
    verif_opts = {
        'quiet': True,
        'skip_download': True

    }
    with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt'}) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(url, download=False))
    video_resolution = sorted({
        f"{f.get('height')}p"
        for f in info.get("formats", [])
        if f.get("vcodec") != "none" and f.get("height")
    }, key=lambda x: int(x.replace("p", "")))

    audio_resolution = sorted({
        f"{f.get('abr')}kbps"
        for f in info.get("formats", [])
        if f.get("acodec") != "none" and f.get("abr")
    }, key=lambda x: float(x.replace("kbps", "")))


    # Extract useful fields
    data = {
        'title': info.get('title'),
        'uploader': info.get('uploader'),
        'duration': info.get('duration'),           # seconds
        'thumbnail': info.get('thumbnail'),         # URL to image
        'video_resolution': video_resolution,
        'audio_resolution': audio_resolution,
    }
    cleanup_temp()
    return data

