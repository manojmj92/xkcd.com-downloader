Python script to download all pictures from xkcd.com

Script downloads all images to folder names "xkcd".

It automatically checks the number of images in the folder with the total number of comics
available, and starts downloading only if they are not equal.

Incase the execution of script stopped in between, the script resumes from the next file
in xkcd archives. It does not download duplicates.

Add a shortcut to your startup folder to check and download updates from xkcd

Dependencies:

BeautifulSoup 4