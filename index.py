import ffmpeg

inputPath = './medias/input/input.mp4'
inputPath2 = './medias/input/input2.mp4'
outputPath = './medias/output/output.mp4'
overlayPath = './medias/assets/overlay.png'

in_file = ffmpeg.input(inputPath)
overlay_file = ffmpeg.input(overlayPath)

(
    ffmpeg
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .overlay(overlay_file.hflip())
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output(outputPath)
    .run()
)
