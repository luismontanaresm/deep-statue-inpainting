import os
import threading
import urllib.request
import json
from unsplash_links import links as unsplash_links

DEST_PATH = f'{os.getcwd()}/raw_data/unsplash_statues/'
os.mkdir(DEST_PATH)

def download_image(url, dest):
    urllib.request.urlretrieve(url, dest)

def download_images(urls, dest):
    downloads = list()
    for idx, image_url in enumerate(urls):
        download = threading.Thread(target=download_image, args=(image_url, DEST_PATH+f'{idx:04d}.jpg'))
        download.start()
    
    for download in downloads:
        download.join()

