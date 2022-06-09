import webbrowser
import sys #for command line arguments
import pyperclip


# Check if command line arguments were passed. 
if len(sys.argv) > 1:
    # if Win+R: chap13a_gmap.py 870 Valencia St. -> sys.argv list: ['chap13a_gmap.py', '870', 'Valencia', 'St.']
    # join the list to get address, but not first argument which is filename. I.e. slice 1:end
    address = ' '.join(sys.argv[1:])
else:
    # else assume we want the clipboard text
    address = pyperclip.paste()


# This url works https://www.google.com/maps
#https://www.google.com/maps?q=870 valencia st. san francisco

# so we want to go to https://www.google.com/maps/place/<ADDRESS>
# opens default web browser
webbrowser.open('https://www.google.com/maps/place/' + address)

print(address)

