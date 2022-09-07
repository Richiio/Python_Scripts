#Python scripts to aid you download PDF Scripts from the internet
import urllib.request
url = input("Enter link to download PDF")
Name = input("Enter a name for the PDF file: ")
FileName = Name + ".pdf"
urllib.request.urlretrieve(url, FileName)