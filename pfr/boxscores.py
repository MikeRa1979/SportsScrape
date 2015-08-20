from bs4 import BeautifulSoup as _BeautifulSoup
import re as _re
import requests as _requests
from urlparse import urljoin as _urljoin

from pfr.players import getGamelogURL as _getGamelogURL
from pfr.utils import getHTML as _getHTML

_dateRegex = _re.compile(r'^\d{4}\-\d{2}\-\d{2}$')

def getBoxScoreURLs(playerURL, year):
    """Get list of box score URLs for a given player-season.

    :playerURL: absolute or relative URL for player
    :year: year for corresponding season in player-season.
    :returns: ["relative_box_score_URL"]

    """
    gamelogURL = _getGamelogURL(playerURL, year)
    html = _getHTML(gamelogURL)
    soup = _BeautifulSoup(html, 'lxml')
    bsURLs = [boxscore_a.get('href')
              for boxscore_a in 
              soup.select('table#stats a[href*="/boxscores/"]')
              if _re.match(_dateRegex, boxscore_a.string)
              ]
    return bsURLs
