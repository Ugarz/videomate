#!/bin/bash
ffmpeg -f concat -i ./medias/input/compressed/mp4/video_files.txt -c copy ./medias/output/out.mp4