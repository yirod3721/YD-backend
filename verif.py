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
    with yt_dlp.YoutubeDL({'cookiefile': 'cookies.txt'}) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(url, download=False))

    # Extract available video resolutions
    video_formats = [
        {
            "id": f["format_id"],
            "ext": f.get("ext"),
            "resolution": f"{f.get('height')}p" if f.get("height") else "unknown",
            "fps": f.get("fps"),
            "vcodec": f.get("vcodec"),
            "filesize": f.get("filesize") or f.get("filesize_approx"),
        }
        for f in info.get("formats", [])
        if f.get("vcodec") != "none" and f.get("height")
    ]

    audio_formats = [
        {
            "id": f["format_id"],
            "ext": f.get("ext"),
            "acodec": f.get("acodec"),
            "abr": f.get("abr"),  # audio bitrate (in kbps)
            "filesize": f.get("filesize") or f.get("filesize_approx"),
        }
        for f in info.get("formats", [])
        if f.get("acodec") != "none" and f.get("vcodec") == "none"
    ]

    video_formats = sorted(video_formats, key=lambda x: int(x["resolution"].replace("p", "")) if x["resolution"] != "unknown" else 0)
    audio_formats = sorted(audio_formats, key=lambda x: x["abr"] or 0)

    data = {
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "duration": info.get("duration"),
        "thumbnail": info.get("thumbnail"),
        "video_formats": video_formats,
        "audio_formats": audio_formats,
    }
    cleanup_temp()
    return data

