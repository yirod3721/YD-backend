from flask import Flask, request, jsonify, send_file
from downloader import video_download, audio_download  # your own module
import os
app = Flask(__name__)

@app.route('/downloads', methods=['POST'])
def handle_post_request():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400

    url = data.get('url')
    format_ = data.get('format')

    if not url or not format_:
        return jsonify({'error': 'Please provide both "url" and "format"'}), 400

    # Download the file
    print(f"format is {format_}")
    filepath = Download(url, format_)

    if not filepath or not os.path.exists(filepath):
        return jsonify({'error': 'Download failed or file missing'}), 500
    if not os.path.exists(filepath):
        return jsonify({'error': f'File {filepath} does not exist'}), 500
    print("Serving file:", filepath)
    print("Exists:", os.path.exists(filepath))



    # MUST return the file to avoid None
    return send_file(
        filepath,
        as_attachment=True,
        download_name=os.path.basename(filepath),
        mimetype='audio/mpeg' if format_ == 'mp3' else 'video/mp4'
    )


def Download(url, format_):
    if format_ == 'mp3':
        print("APP MP3 ON")
        return audio_download(url)
    elif format_ == 'mp4':
        return video_download(url)
    else:
        return None  # handle invalid format gracefully


if __name__ == '__main__':
    app.run(debug=True)
