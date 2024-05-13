# This script checks the local data directory for the patch's folder, and if it does not exist it downloads the relevant patch data. 
# Defaults to the patch given in the local config file, but if the patch is out of date it will ask the user to confirm.
import os 
import shutil

import requests

from lolml.utilities import utils
from lolml.config import PATCHES_DIR


def check_data_dir_for_patch(patch: str):
    """Checks the local data directory for the patch folder.

    Args:
        patch: The patch number

    Returns:
        True if the data directory already exists, False if it does not.
    """
    return os.path.isdir(PATCHES_DIR / f"dragontail-{patch}")



def download_patch_data(patch: str):
    """Downloads the data for the given patch."""

    download_url = f"https://ddragon.leagueoflegends.com/cdn/dragontail-{patch}.tgz"
    r = requests.get(download_url)  
    with open(PATCHES_DIR / f"dragontail-{patch}.tgz", 'wb') as f:
        f.write(r.content)

    return None

def unzip_patch_data(patch: str):
    """Unzips the saved file."""
    tgz_path = PATCHES_DIR / f"dragontail-{patch}.tgz"
    target_dir = PATCHES_DIR / f"dragontail-{patch}"
    shutil.unpack_archive(tgz_path, target_dir)

def remove_zip_file(patch: str):
    """Removes the downloaded zip file once it has been unzipped"""
    tgz_path = PATCHES_DIR / f"dragontail-{patch}.tgz"
    os.remove(tgz_path)


def main():
    # Check latest patch and if it is out of date, ask the user to confirm. 
    if not utils.check_config_patch(verbose=False):
        config_patch = utils.get_config_patch()
        current_patch = utils.get_current_patch()
        print(f"The config patch ({config_patch}) is out of date! The current LoL patch is {current_patch}\n")
        patch_confirm = input("Would you like to download the config patch or the current patch? Type 'config' to select the config patch, or 'current' to select the current patch: ")
        if patch_confirm == "config":
            patch = config_patch
            print(f"Patch {patch} selected.")
        elif patch_confirm == "current":
            patch = current_patch
            print(f"Patch {patch} selected.")
        else:
            print("No valid response detected. Please restart script.")
            exit()
    else: 
        patch = utils.get_config_patch()
        print(f"Current patch is: {patch}")

    # Check if the patch directory exists.
    if check_data_dir_for_patch(patch):
        print("Patch directory already exists! If you want it to be downloaded again, delete the patch directory and restart the script.")
        exit()
    else:
        print(f"Downloading patch {patch}...")
        download_patch_data(patch)
        print("Patch downloaded!")

    # Unzip the patch
    print("Unzipping patch data")
    unzip_patch_data(patch)
    print("Patch data unzipped")

    # Remove zip file
    print("Cleaning up directory")
    remove_zip_file(patch)
    print("Directory cleaned up!")

    print("Patch data downloaded!")

    exit()


if __name__ == '__main__':
    main()