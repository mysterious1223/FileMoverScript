import os
import sys
import shutil  

if(len(sys.argv) < 2):
    print("invalid param")
    sys.exit()
   
#path
EndDirectory = sys.argv [2]
SourceDirectory = sys.argv [1]

print ("Copying from "+SourceDirectory)
print ("To "+EndDirectory)



def copy_file_over (filename):
    shutil.copy (SourceDirectory + '/' + filename, EndDirectory+ '/' +filename)
    print ("Copyied -" + SourceDirectory + '/' + filename +" ------> "+ EndDirectory+ '/' +filename)

for filename in os.listdir (SourceDirectory):

    #do something
    print ("copying : ["+filename+']')

    

    #process the move
    if (os.path.isfile (SourceDirectory + '/' + filename)):

        copy_file_over (filename)
    else:
        print ('['+filename+']' + " is not a file...")