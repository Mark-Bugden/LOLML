# ML project for predicting League of Legends matches

## Installation

1. First make sure that poetry is installed:

    pip install poetry

1. (Optional) If you would like the virtual environment folder to be located inside the repository directory, run the following:

    poetry config virtualenvs.in-project true

2. Clone the repo using your preferred method. Once the repo is cloned, cd to the repo directory. Create a virtual environment and install the required dependencies by running:

    poetry install

3. Once the project is installed, activate the virtual environment using:

    poetry shell


## API keys
Riot uses API keys to monitor and restrict access to their APIs. API keys are rate-limited and come in two different types: personal or development. For security reasons, the API key is stored in a text file "api_key.txt" in the project root directory and not pushed to GitHub. To use your own API key first obtain one from the Riot developer portal, then create the text file mentioned above save the api key in it. This is then accessed automatically by the ´getAPI_key´ function in ´lolml.utils.utilities´ when you run the functions in ´lolml.utils.api_calls´.

## Player IDs
Riot confusingly uses several different IDs for players, and different API endpoints require different IDs. The main ones in which we are interested are:
- riotID: The universal ID that Riot uses to track players across games. Each ID is unique, tied to a single email address, and divided into two parts. If your Riot ID is "EarlGreyTeemo#sip," for example, then your Game Name is "EarlGreyTeemo," and your tagline is "#sip".
    - Game Names must be 3–16 alphanumeric characters long and cannot be offensive or inappropriate. 
    - Taglines must be 3–5 alphanumeric characters long.
- PUUID: An internal ID used to identify players in some API calls.
- Summoner ID: An internal ID used to identify players in some API calls.

The following functions have been defined in lolml.utils.api_calls to make the transition between IDs easier:
- [x] get_PUUID_from_riotID()
- [x] get_riotID_from_PUUID()
- [x] get_summonerID_from_riotID()
- [x] get_riotID_from_summonerID()
- [x] get_PUUID_from_summonerID()
- [x] get_summonerID_from_PUUID()

## Scraping (ranked) LOL matches
Scraping League of Legends matches is somewhat difficult, as you need a match ID to obtain information from a specific match and there is no list of all matches in a given patch. Instead, we first scrape a list of summoners by looking at the league tables for a given league. For each summoner in the list, we obtain a list of match IDs played by that summoner. We then concatenate these lists and deduplicate so that we have a big list of match IDs which we can then use to scrape match information. 


## TO DO

- [ ] Convert to google-style docstrings
- [ ] Add docstrings to api calls
- [ ] Add exception messages (eg. if 403, check api key)
- [ ] Add type hints
- [ ] Add regions to api calls
- [ ] Add rate limits to api calls
- [ ] Write tests for ID api calls
- [x] Update .gitignore


## Developer notes:
def example_google_style():
    """This is an example of Google style.

    Some longer description of the function here, which goes on and on and on and on
    and on and on and on and on and on and on and on.

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        This is a description of what is returned.

    Raises:
        KeyError: Raises an exception.
    """
