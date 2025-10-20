import os, shutil
def setup_folders():
    for folder in ["downloads/temp", "downloads/audio", "downloads/video"]:
        os.makedirs(folder, exist_ok=True)
    return 0
def move_to_final(filepath, media_type):
    filename = os.path.basename(filepath)
    print(media_type)
    if (media_type == "audio"):
        dest_folder = "downloads/audio"
        print(dest_folder)
    elif (media_type == "video"):
        dest_folder = "downloads/video"
        print(dest_folder)
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
def cleanup_file():
    foldera = 'downloads/audio'
    folderv = 'downloads/video'
    for f in os.listdir(foldera):
        os.remove(os.path.join(f, foldera))
    for f in os.listdir(folderv):
        os.remove(os.path.join(f, folderv))
    return 0 