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
    """Fetch video metadata without downloading."""
    with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt'}) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(url, download=False))

    # Extract useful fields
    data = {
        'title': info.get('title'),
        'uploader': info.get('uploader'),
        'duration': info.get('duration'),           # seconds
        'thumbnail': info.get('thumbnail'),         # URL to image
    }
    cleanup_temp()
    return data

