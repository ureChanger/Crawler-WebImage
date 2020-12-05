import requests
from PIL import Image
import os
import io
import hashlib

def persist_image(folder_path, url):
    
    try:
        image_content = requests.get(url).content
    
    except Exception as e:
        print("ERROR - Could not download {url} - {e}")
        
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10]+'.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print("SUCCESS - saved {url} - as {file_path}".format(url=url, file_path=file_path))
    
    except Exception as e:
        print("ERROR - Could not save {url} - {e}".format(url=url, e=e))