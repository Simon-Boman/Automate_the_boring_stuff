import os
#dry run - comment out the actual delete call, just print and test if e.g. typo
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)