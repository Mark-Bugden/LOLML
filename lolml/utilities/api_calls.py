import requests

from lolml.utilities import utils

# Patch related API calls


# ID Related API calls
########################
# API calls: 1
def get_PUUID_from_riotID(gameName, tagLine):
    """Get PUUID from the RiotID.

    When querying for a player by their riotID, the gameName and tagLine
    query params are required.

    Args:
        gameName: gameName of the account
        tagLine: tagLine of the account

    Returns
        PUUID: the PUUID associated to the given riotID
    """

    base_api_url = (
        "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"
    )
    api_url = base_api_url + gameName + "/" + tagLine
    resp = requests.get(api_url + "?api_key=" + utils.getAPI_key())
    account_info = resp.json()
    PUUID = account_info["puuid"]

    return PUUID


# API calls: 1
def get_riotID_from_PUUID(PUUID):
    """Get RiotID from the PUUID.

    Args:
        PUUID: The PUUID for the player whose account info you want

    Returns:
        gameName, tagLine: The components of the riotID associated to the given PUUID.
    """
    base_api_url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/"
    api_url = base_api_url + PUUID
    resp = requests.get(api_url + "?api_key=" + utils.getAPI_key())
    account_info = resp.json()
    gameName = account_info["gameName"]
    tagLine = account_info["tagLine"]

    return gameName, tagLine


# API calls: 1
def get_summonerID_from_PUUID(PUUID):
    """Get summonerID from PUUID"""

    base_api_url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"
    api_url = base_api_url + PUUID
    resp = requests.get(api_url + "?api_key=" + utils.getAPI_key())
    account_info = resp.json()
    summonerID = account_info["id"]
    return summonerID


# API calls: 1
def get_PUUID_from_summonerID(summonerID):
    """ """
    base_api_url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/"
    api_url = base_api_url + summonerID
    resp = requests.get(api_url + "?api_key=" + utils.getAPI_key())
    account_info = resp.json()
    PUUID = account_info["puuid"]
    return PUUID


# API calls: 2
def get_summonerID_from_riotID(gameName, tagLine):
    """ """
    PUUID = get_PUUID_from_riotID(gameName, tagLine)
    summonerID = get_summonerID_from_PUUID(PUUID)
    return summonerID


# API calls: 2
def get_riotID_from_summonerID(summonerID):
    """"""
    PUUID = get_PUUID_from_summonerID(summonerID)
    riotID = get_riotID_from_PUUID(PUUID)
    return riotID

