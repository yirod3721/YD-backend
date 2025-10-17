import os, shutil
def setup_folders():
    for folder in ["downloads/temp", "downloads/audio", "downloads/video"]:
        os.makedirs(folder, exist_ok=True)
    return 0
def move_to_final(filepath, media_type):
    filename = os.path.basename(filepath)
    if media_type == "audio":
        dest_folder = "downloads/audio"
    elif media_type == "video":
        dest_folder == "downloads/video"
    else:
        print("INVALID PATH")
        return 1
    final_path = os.path.join(dest_folder, filename)
    shutil.move(filepath, final_path)
    return final_path
def cleanup_temp():
    temp_folder = 'downloads/temp'
    for f in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, f))
    return 0