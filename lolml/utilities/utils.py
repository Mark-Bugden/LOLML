import requests

from lolml import config


def getAPI_key() -> str:
    """Access the locally stored API key.

    The API key should be stored in a text file named "api_key.txt" in the project root
    directory.

    Returns:
        str: The API key as a string
    """
    f = open(config.API_KEY_PATH, "r")
    return f.read()


def get_config_patch():
    """Returns the patch version that is saved in the local config file."""
    return config.CONFIG_PATCH


def get_current_patch():
    """Returns the current patch in League of Legends."""

    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    resp = requests.get(url)
    list_of_patches = resp.json()

    return list_of_patches[0]


def check_config_patch(verbose: bool = True):
    """Checks if the config_patch value is up to date.

    Args:
        verbose: Prints details of the patch numbers if true.

    Returns:
        True if the patch value in the config file is up to date, false otherwise.
    """

    config_patch = get_config_patch()
    current_patch = get_current_patch()

    if config_patch == current_patch:
        if verbose:
            print("current_patch in config file is up to date.")
            print(f"config_patch: {config_patch:>10}")
        return True
    else:
        if verbose:
            print("config_patch is NO LONGER up to date!")
            print(f"config_patch: {config_patch:>12}")
            print(f"current_patch: {current_patch:>11}")
        return False
