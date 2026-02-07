import os
import shutil

def back_up(f_path,d_path):
    
    # To check path is available
    if not os.path.exists(f_path):
        print("❌ Path is not found!")
        return
    print("✅ Path is connected successfully")

    # Iteration of all files to each files to copy a destination
    for files in os.listdir(f_path):
        # starting a path 
        starting = os.path.join(f_path,files)
        if os.path.isfile(starting):
            # destination for backup
            destination = os.path.join(d_path,files)

            # copy to the files in destination
            shutil.copy(starting,destination)
            print("✅ successfully backup  ")
if __name__ == "__main__":
    f_path = r"" # To paste the files paths
    d_path = r"" # Backup desination of the paths
    back_up(f_path,d_path)
