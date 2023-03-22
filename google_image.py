import simple_image_download.simple_image_download as simp


my_downloader = simp.Downloader()
# Change Directory
my_downloader.directory = 'pictures/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)
my_downloader.download('mister obama', limit=4, verbose=True)