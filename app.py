from flask import Flask, request, jsonify, send_file,Response
from flask_cors import CORS, cross_origin
from downloader import video_download, audio_download, progress_data
from verif import data_fetch, is_valid_youtube
from file_manager import setup_folders, cleanup_temp
import json
import os
app = Flask(__name__)
CORS(app)
@app.route('/downloads', methods=['POST'])
#@cross_origin()
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
        print("APP MP4 ON")
        return video_download(url)
    else:
        return None  # handle invalid format gracefully

@app.route('/verification', methods=['POST'])
#@cross_origin()
def url_verif():
    data = request.get_json()
    if not data or not 'url' in data:
        return jsonify({'error': 'Please provide a URL'}), 400
    url = data['url']
    if not is_valid_youtube(url):
        print("Invalid url detected")
        return jsonify({'error': 'URL is not valid'}), 400
    try:
        video_info = data_fetch(url)
    except:
        with Exception as E:
            return jsonify({'error': f'Failed to fetch video data: {str(E)}'}), 500
    return jsonify(video_info)
    
@app.route('/progress_stream')
def progress_stream():
    def generate():
        last = None
        while True:
            if progress_data != last:
                json_data = json.dumps(progress_data)
                yield f"data: {json_data}\n\n"
                last = progress_data.copy()
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    setup_folders()
    cleanup_temp()
    app.run(host='0.0.0.0', threaded=True, )
    