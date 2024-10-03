import glob
import subprocess
import os
from PyPDF2 import PdfReader as reader

## Creates necessary Folders
if len(glob.glob('Reformatted_Cards')) == 0:
    subprocess.run('mkdir Reformatted_Cards', check = True, shell=True)
if len(glob.glob('Original_Cards')) == 0:
    subprocess.run('mkdir Original_Cards', check = True, shell=True)
    raise SystemExit('Please import cards into "Original_Cards"')

unformatted_cards = glob.glob('./Original_Cards/*.pdf')

## Spaces cause formatting errors down the line
for filename in unformatted_cards:
    os.rename(filename, filename.replace(" ", "-"))

## Reinitializing variable
unformatted_cards = glob.glob('./Original_Cards/*pdf')

for card in unformatted_cards:
    the_file = reader(card)
    box = the_file.pages[0].mediabox
    if box.width/72>=16:
        subprocess.run('pdfposter -s0.5 '+card +" "+'./Reformatted'+card[10:], check = True, shell=True)
    else:
        try:
            subprocess.run('pdfposter -s1 '+card +" "+'./Reformatted'+card[10:], check = True, shell=True)
        except:
            print('Error found - did you "pip install pdftools.pdfposter"?')
            break
