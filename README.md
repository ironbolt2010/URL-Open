# URL-Open
This is a URL opener that can be imported
# USAGE:
  from main.py import URLOpener #import the URLOpener class
  URLOpener.open(URLS = ['https://github.com' , 'https://some_other_website.io' , ARGS = ['-load'] , filename = 'URLS.txt'])
The URLS list takes all the necessary URLS to open
The ARGS list has only 2 recognized elements:
    '-read' this will look for a file in the current directory.The filename is the string thet you pass to the 'filename' variable.After the file is found,it will load the URLS in the file.
    
