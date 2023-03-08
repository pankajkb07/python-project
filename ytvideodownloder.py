# Program to download youtube vidoes
 
# Importing the module
import pytube 
 
# Taking input the link
link = input('Enter url here : ')
 
# Using the module to download the video
video = pytube.YouTube(link)
 
#promt to make sure that the download is complete
print("Downloaded Successfully, ",link)