## **1.General Information**
### Endpoint URL: https://fantasy.premierleague.com/api/bootstrap-static/
### Sections:
* #### **events**: Basic information for every gameweek such as average score, highest score, top scoring manager etc.
* #### **game_settings**
* #### **phases**: Different phases of the game.
* #### **teams**: Information about the current Premier League Clubs.
* #### **total_players**: Total number of FPL managers.
* #### **elements**: Information of all FPL assets.
* #### **element_types**: Dictionary with player positions (GK, DEF, MID, FWD).

## **2.Fixtures**
### Endpoint URL: https://fantasy.premierleague.com/api/fixtures/
### Sections:
* #### **event**: Refers to the event id in events section of /bootstrap-static endpoint.
* #### **team_a** & **team_h**: Refers to the team id in the teams section of the /bootstrap-static endpoint.
* #### **team_h_difficulty** & **team_a_difficulty**: the FDP value as calculated by FPL.
* #### **stats**: A list of match facts that affects the points scored by individual footballers.

## **3.Players' Detailed Data**
### Endpoint URL: https://fantasy.premierleague.com/api/element-summary/{element_id}/
### Sections:
* #### **fixtures**: A player's remaining fixtures.
* #### **history**: A player's history.
* #### **history**: A player's previous seasons and seasonal stats.

## **4.Gameweek Live Data**
### Endpoint URL: https://fantasy.premierleague.com/api/event/{event_id}/live/
#### Returns a list of a player's information in a specified gameweek.
### Sections:
* #### **id**: Refers to the element id from bootstrap-statis data.
* #### **stats**: A player's match stats for the specific gameweek.
* #### **explain**: Breakdown of a player's points for the specific gameweek.



