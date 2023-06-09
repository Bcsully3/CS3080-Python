"""
Homework 6 exercise 3
Brendan Sullivan
4/11/23
This program allows user to save multiple items to the clipboard by saving
them under keywords. You can save the current contents of the clipboard
under a keyword and then recall those contents by using the keyword, and
have multiple keywords each corresponding with different things to be
put on the clipboard.
"""
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close

