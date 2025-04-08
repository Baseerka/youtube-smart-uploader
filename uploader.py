import json
import os
from api_uploader import upload_video
from selenium_uploader import upload_errorr

def upload(video_data):
    try:
        print(f"Uploading: {video_data['file']} using API...")
        upload_video(video_data)
    except Exception as e:
        print(f"API failed: {e}, using Selenium fallback...")
        upload_errorr(video_data)

def main():
    with open("config.json") as f:
        video_list = json.load(f)

    for video in video_list:
        if not os.path.exists(video['file']):
            print(f"Skipping missing file: {video['file']}")
            continue
        upload(video)

if __name__ == "__main__":
    main()
