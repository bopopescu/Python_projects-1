import youtube_dl as ud
import subprocess

#https://www.youtube.com/watch?v=fCmm8toLtkA&t=443s


print("===========Youtube Downloader===========")
choice = int(input("1. Download movie \n2. Download playlist \3Download audio"))
if choice == 1:
    url = input("Enter url of moovie")
elif choice == 2:
    url = input("Enter url of playlist")
                
def youtub_loader():
    exit = True
    While not exit:  
        command = "youtube-dl " + url + " -c"
        call(command.split(), shell=False)
        from subprocess import call

youtub_loader()



