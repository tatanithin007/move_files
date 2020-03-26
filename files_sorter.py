from os import listdir
from os.path import isfile, join
import shutil

mypath='/Users/apple/Downloads/'
dest_pdf='/Users/apple/Downloads/PDFS/'
dest_img='/Users/apple/Downloads/images/'
dest_dmg='/Users/apple/Downloads/DMGS/'
dest_zip='/Users/apple/Downloads/ZIPS/'
dest_docs='/Users/apple/Downloads/docs/'
dest_json='/Users/apple/Downloads/JsonAndHtml/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    if i[-3:].lower()== 'pdf':
        shutil.move(mypath+i,dest_pdf+i)
    elif i[-3:].lower()== 'img' or i[-3:].lower()== 'png' or i[-4:].lower()== 'jpeg' or i[-3:].lower()== 'jpg' or i[-3:].lower()== 'gif':
        shutil.move(mypath + i, dest_img + i)
    elif i[-3:].lower()== 'dmg':
        shutil.move(mypath + i, dest_dmg + i)
    elif i[-3:].lower()== 'zip':
        shutil.move(mypath + i, dest_zip + i)
    elif i[-4:].lower() == 'docx' or i[-3:].lower() == 'csv' or i[-4:].lower() == 'xlsx' or i[-3:].lower() == 'txt' or i[-3:].lower() == 'doc' or i[-3:].lower() == 'ppt':
        shutil.move(mypath + i, dest_docs + i)
    elif i[-4:].lower()== 'json' or i[-4:].lower()== 'html':
        shutil.move(mypath + i, dest_json + i)



