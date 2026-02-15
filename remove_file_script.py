import os
import shutil

# file remove function
def file_remove(path_r):
    # Checking the path is here
    if not os.path.exists(path_r):
        print("❌ Path is not found!")
        return
    
    print("✅ Path is connected successfully")

    for files in os.listdir(path_r):
        location_file = os.path.join(path_r,files)
        os.remove(location_file)

        print("✅ Successfully file was removed")

# folder remove function
def folder_remove(path_r):
    shutil.rmtree(path_r)
    print("✅ Folder is successfully removed")

if __name__ == "__main__":
    path_r = r""  # Paste the path what you remove
    choice = input("Enter what you remove file or Complete folder : ").lower().strip()
    if choice == "file":
        file_remove(path_r)
    else:
        folder_remove(path_r)