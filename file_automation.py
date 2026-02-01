import os
import shutil

# core function logic
def automation_files(paths_dir):
    
    # To check a path is found or not found
    if not os.path.exists(paths_dir): 
        print("❌ Path is not found!")
        return
    
    print("✅ Path is found ")
    
    # To store a all extension 
    extentions_formate = set()

    # To collect a all files

    for files in os.listdir(paths_dir):
        ex_name = os.path.splitext(files)[1][1:] # To remove the dot
        
        # To store a extenstion
        if ex_name:
            extentions_formate.add(ex_name)

    # To create a folder
    for formate in extentions_formate:
        create_folder = os.path.join(paths_dir,formate)
        os.makedirs(create_folder,exist_ok = True) # To create a folder if already exist skip to creating a folder

    # To moving a files an inside the destination
    for file in os.listdir(paths_dir):
        # To initiating a staring location
        staring_paths = os.path.join(paths_dir,file)

        # Checking a path inside of file
        if os.path.isfile(staring_paths):

            file_ext = os.path.splitext(file)[1][1:] or "no extention"

            # Destination for file extension based
            destination = os.path.join(paths_dir,file_ext)

            # To moving a final destination
            shutil.move(staring_paths,destination)

            print("✅ Successfully automating a files")


if __name__ == "__main__":
    directory_paths = '' # Paste yours path
    
    # core function call
    automation_files(directory_paths)
