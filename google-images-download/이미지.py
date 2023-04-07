from google_images_download import google_images_download
 
import ssl  # ssl Error 발생 시
ssl._create_default_https_context = ssl._create_unverified_context  
 
 
def imageCrawling(keyword, dir):
    response = google_images_download.googleimagesdownload()
 
    arguments = {"keywords":keyword,      # 검색 키워드
                 "limit":100,             # 크롤링 이미지 수
                 "print_urls":True,       # 이미지 url 출력
                 "no_directory":True,     # 
                 'output_directory':dir}  # 크롤링 이미지를 저장할 폴더
 
    paths = response.download(arguments)
    print(paths)
 
imageCrawling('cat','/Users/aaron/Desktop/test/')
