import os 

def rename_fun(path_directory,d_path):

    # To check a directory
    if not path_directory:
        print("❌ Path is not found!")
        return
    
    print("✅ Path is Successfully Connected")
    
    # extentsion to storing a set
    extention = set()

    # Iterate a every file 
    for file in os.listdir(path_directory):
        ext = os.path.splitext(file)[1][1:]
        if ext:
            extention.add(ext)
        else:
            extention.add("no extention")    

    # To creation of formate based rename a file
    for extent in extention:
        for index,files in enumerate(os.listdir(path_directory)):
            ext_file = os.path.splitext(files)[1][1:] or "no extension"
            if extent == ext_file  :

                # starting location
                starting_loc = os.path.join(path_directory,files)

                # check whether staring location in same
                if os.path.isfile(starting_loc):

                    # destination of file renamed
                    destin = os.path.join(d_path,f"something{index}.{extent}")
                    os.renames(starting_loc,destin)
                    print("✅ Successfully rename the files")

                    
if __name__ == "__main__":
    dire_path = r""  # file location
    destination_rename_file = r"" # rename file location
    rename_fun(dire_path,destination_rename_file)
