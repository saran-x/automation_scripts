import os
import shutil
import logging

# logging file creating for monitoring a automation scripts

logging.basicConfig(
    filename = "automation.log",
    level = logging.INFO,
    format = "%(actime)s - %(levelname)s - %(message)s"
)

# moving to one direction into another direction
def files_moving(path_s,detination_d):
    
    # Checking a path is avalable
    if not path_s:
        print("❌ Path is not found!")

    print("✅ path is connected successfully")

    try:
        for files in os.listdir(path_s):
            # staring a path file to initiated
            starting = os.path.join(path_s,files)

            if os.path.isfile(starting):
                destination_copy = os.path.join(detination_d,files)
                # copy the file into another path
                shutil.copy(starting,destination_copy)
                logging.info(f"File is successfully backed{files}")
    except Exception :
        logging.error(f"File is backup is failed{files  }")


if __name__ == "__main__":
    path_s = r"" # paste your location
    detination_d = r"" # paste your destination

    files_moving(path_s,detination_d)
