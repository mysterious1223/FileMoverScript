import os
import sys
import shutil  

if(len(sys.argv) >=1 and len(sys.argv) <= 2):
    print("invalid param")
    sys.exit()
   
#path
EndDirectory = sys.argv [2]
SourceDirectory = sys.argv [1]
IncludeFoldersFlag = False
MoveSubFolders = False

print ("[-] Copying from "+SourceDirectory)
print ("[-] To "+EndDirectory)
try:
    #include files in subfolders
    if (sys.argv [3] == '-F'):
        print ("[-] Including sub folders")
        IncludeFoldersFlag = True
    elif (sys.argv [3] == '-sF'):
        print ("[-] Including sub folders")
        print ("[-] moving sub folders")
        MoveSubFolders = True
        IncludeFoldersFlag = True
    else:
        print ("[!] Invalid argument")
        sys.exit()
except:
    print ("[!] Sub folders ignored")

def getDirectoryFromPath (CurrentSourceDirectory, mainSource):

    return CurrentSourceDirectory.replace (mainSource, '')

def CreateMissingDirectories (CurrentSourceDirectory, SourceDirectory, EndDirectory):
    
    Folders =  getDirectoryFromPath (CurrentSourceDirectory, SourceDirectory).split ("/")
    currentPathBuild = ""
    for folder in Folders:
        currentPathBuild += folder + "/"
        if (folder != ""):
            if not (os.path.exists(EndDirectory + '/' + currentPathBuild)):
                #print ("[debug] missing folder : " + currentPathBuild)
                #print ("[debug] new  : " + currentPathBuild + " -> " + EndDirectory + '/' + currentPathBuild )
                os.mkdir (EndDirectory + '/' + currentPathBuild)
                print ("[+] New directory created")
def copy_file_over (filename, CurrentSourceDirectory):

    if (CurrentSourceDirectory != SourceDirectory):
        #print ("[debug] Detected a sub directory! ->> " +CurrentSourceDirectory)

        #print ("[debug] " + getDirectoryFromPath (CurrentSourceDirectory, SourceDirectory))

        # we will need recursion or loop to make all directories?
        #move sub folders too
        if (MoveSubFolders):
            CreateMissingDirectories (CurrentSourceDirectory, SourceDirectory, EndDirectory)
            shutil.copy (CurrentSourceDirectory + '/' + filename, EndDirectory +'/' + getDirectoryFromPath (CurrentSourceDirectory, SourceDirectory) + '/' +filename)

        shutil.copy (CurrentSourceDirectory + '/' + filename, EndDirectory +'/' +filename)
    else:
        shutil.copy (CurrentSourceDirectory + '/' + filename, EndDirectory+ '/' +filename)

    print ("[+] Copied -" + CurrentSourceDirectory + '/' + filename +" ------> "+ EndDirectory+"/" +filename)



def ProcessMove (CurrentSourceDirectory):

    for filename in os.listdir (CurrentSourceDirectory):
        
        #process the move
        if (os.path.isfile (CurrentSourceDirectory + '/' + filename)):
            #do something
            print ("[-] copying : ["+filename+']')
            copy_file_over (filename, CurrentSourceDirectory)

        elif (IncludeFoldersFlag == True):
            print ("[++] Processing Sub Directory")
            ProcessMove (CurrentSourceDirectory + '/' + filename)
        else:
            print ('['+filename+']' + " is not a file... ")


ProcessMove (SourceDirectory)

#for filename in os.listdir (SourceDirectory):

    #do something
 #   print ("[-] copying : ["+filename+']')

    

    #process the move
  #  if (os.path.isfile (SourceDirectory + '/' + filename)):

   #     copy_file_over (filename)

    #elif (IncludeFoldersFlag == True):
        #print ('['+filename+']' + " is not a file... ")
    #else:
     #   print ('['+filename+']' + " is not a file... ")
