import string
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

main = "https://www.pikalytics.com/pokedex/vgc2018" #dat link
pokemon = []

s = ' !"#$%&()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~'; #things to remove

#poorly named variables
team = []
test = []
teamper = []
percent = []
combo = {}

final_team = []

#this begins the starting pokemon list generator portion of the code
uData = ureq(main)#pull html
html = uData.read()
page_soup = soup(html, "html.parser")

pokelist = page_soup.findAll("div", {"id": "mini_list_wrapper"})
pokelist = pokelist[0].findAll("div", {"id": "pokedex_wrapper"})
pokelist = pokelist[0].findAll("ul")
pokelist = pokelist[0].findAll("a")
for x in range(len(pokelist)):
    pokemon.append(pokelist[x]["data-name"])
#this concludes the starting pokemon list generator portion of the code


def pick_partner(final_team, combo):
    h = 0
    for key, val in combo.items():
        if float(val) > h and key not in final_team:
            h = float(val)
            NewGuy = key

    final_team.append(NewGuy)

    if len(final_team) < 6:
        pokemon_percent((main+"/"+NewGuy), final_team)

def pokemon_percent(pika, final_team):
    team = []
    teamper = []
    percent = []


    uData = ureq(pika)#pull html
    html = uData.read()
    page_soup = soup(html, "html.parser")

    stat = page_soup.findAll("div", {"class": "inline-block pokemon-stat-container"})
    teamlist = stat[2].findAll("div", {"class": "pokedex-category-wrapper"})
    teamwrapper = teamlist[0].findAll("div", {"id": "teammate_wrapper"})
    teamdiv = teamwrapper[0].findAll("div")
    teamrough = teamdiv[0].findAll("a", {"class": "teammate_entry pokedex-move-entry-new"})#whittle it down wo just the team mate data

    for x in range(5):
        team.append(teamrough[x]["data-name"]) #pull name data
        teamper.append(teamrough[x].findAll("div", {"style":"display:inline-block;float:right;"}))

    for x in range(5):
        for c in teamper[x]:
            for p in c:
                if p not in s:
                    p = p.replace("%", "")
                    percent.append(p) #pull percent data
    if len(final_team) == 1:
        for x in range(5):
            combo[team[x]] = percent[x] #put it in one readable dictionary
    else:
        for x in range(5):
            if team[x] in combo:
                combo[team[x]] = percent[x]
            else:
                combo[team[x]] = percent[x]

    pick_partner(final_team, combo)

for p in pokemon:
    final_team.append(p)
    pika = main+"/"+final_team[0]
    pokemon_percent(pika, final_team)
    print(final_team)
    final_team = []
