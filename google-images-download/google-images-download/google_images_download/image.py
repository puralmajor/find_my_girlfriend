from sys import path
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"여자친구 엄지, 여자친구 유주, 여자친구 예린", "limit":200, "print_urls":True}
paths = response.download(arguments)
print(path)