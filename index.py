import os
import subprocess
import datetime

media_in='./medias/input/'
media_out= './medias/output/'


subprocess.run(["bash", "./clean.sh"])


# Look for zip and unzip it
for subdirs, dirs, files in os.walk(media_in):
    for file in files:
        print(subdirs + file)
        extension=os.path.splitext(file)[-1].lower()
        if extension == ".zip":
            print("found a zip")
            subprocess.run('unzip ./medias/input/archive.zip -d ./medias/input', shell=True)

# Compress video files
for subdirs, dirs, files in os.walk(media_in):
    for file in files:
        print(subdirs + file)
        extension=os.path.splitext(file)[-1].lower()
        if not os.path.exists(subdirs + "/compressed"):
            os.makedirs(subdirs + "/compressed")
        if extension == ".mov":
            if not os.path.exists(subdirs + "/compressed/mov/"):
                os.makedirs(subdirs + "/compressed/mov/")
            cmd='ffmpeg -i ' + media_in + file + ' -vcodec libx264 -crf 22 ' + media_in + 'compressed/' + extension.replace(".","") + "/" + "compressed_" + file
            print("compressing.." + file)
            subprocess.run(cmd, shell=True)
        elif extension == ".mp4":
            if not os.path.exists(subdirs + "/compressed/mp4/"):
                os.makedirs(subdirs + "/compressed/mp4/")
            cmd='ffmpeg -i ' + media_in + file + ' -vcodec libx264 -crf 22 ' + media_in + 'compressed/' + extension.replace(".","") + "/" + "compressed_" + file
            print("compressing.." + cmd)
            subprocess.run(cmd, shell=True)

video_files='./medias/input/compressed/mp4/video_files.txt'

# list all videos in a text file
if os.path.exists(video_files):
    print('Remove old video_files and create new video_files')
    os.remove(video_files)

print('Create video_files list for you')
with open(video_files, 'a') as f:
    for root, directories, files in os.walk('./medias/input/compressed/mp4', topdown=False):
        for name in files:
            extension=os.path.splitext(name)[-1].lower()
            if extension == ".mp4":
                f.write("file '" + name + "'" + "\n")
print("List video files ready")

subprocess.run('ffmpeg -f concat -i video_files -c copy ./medias/output/out.mp4')
# subprocess.run(["bash", "./medias/input/build_video.sh"])
