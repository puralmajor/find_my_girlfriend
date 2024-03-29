import sys
import argparse
import requests
from PIL import Image, ImageFilter
import glob
import os

API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
# 아래 My Kakao api key, 본인 계정의 API 키로 변경해서 사용하세요.
MYAPP_KEY = '####'

def detect_face(filename):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'file' : open(filename, 'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.height)
        h = int(face['h']*image.height)
        box = image.crop((x,y,x+w, y+h))
        # 모자이크 강도를 조절하려면 사이즈를 조절하세요.
        box = box.resize((20,20), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))
    return image



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mosaic all of faces.')
    parser.add_argument('-f', '--folder', type=str, nargs='?', default="./.",
                        help='image file to hide faces', required = True)
    args = parser.parse_args()
    # Make files lists
    files = glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.png')
    # make loop
    for i in files:
        head, tail = os.path.split(i)
        try:
            detection_result = detect_face(i)
            image = mosaic(i, detection_result)           
            image.save(head+'mosaic_'+tail,'JPEG')
            print('! Add mosaic on : ' + tail)
        except:
            print('! Face does not detected on : ' + tail) 
    
    print('!!  All process finished  !!')
