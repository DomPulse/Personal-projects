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

all_teams = []
showdown_comp = []
used_items = []

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
    teamrough = teamdiv[0].findAll("a", {"class": "teammate_entry pokedex-move-entry-new"})#whittle it down to just the team mate data

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
    all_teams.append(final_team)
    final_team = []
    combo = {}

def add_item(item, n, inlist, p):
    pika = "https://www.pikalytics.com/pokedex/vgc2018/" + p + "/"

    uData = ureq(pika)#pull html
    html = uData.read()
    page_soup = soup(html, "html.parser")

    item = page_soup.findAll("div", {"class": "inline-block pokemon-stat-container"})
    item = item[3].findAll("div", {"class": "pokedex-category-wrapper"})
    item = item[0].findAll("div", {"id": "items_wrapper"})
    item = item[0].findAll("div")
    item = item[0].findAll("div", {"class": "pokedex-move-entry-new"})
    item = item[n].findAll("div", {"style": "display:inline-block;"})
    item = str(item)
    item = item.split('>')
    item = item[1].split('<')
    item = item[0]
    if item not in inlist:
        inlist.append(item)
        return(item)
    else:
        n+=1
        return(add_item(item, n, inlist, p))

def add_abil(p):
    pika = "https://www.pikalytics.com/pokedex/vgc2018/" + p + "/"

    uData = ureq(pika)#pull html
    html = uData.read()
    page_soup = soup(html, "html.parser")

    abil = page_soup.findAll("div", {"class": "inline-block pokemon-stat-container"})
    abil = abil[4].findAll("div", {"class": "pokedex-category-wrapper"})
    abil = abil[0].findAll("div")
    abil = abil[1].findAll("div", {"class": "pokedex-move-entry-new"})
    abil = abil[0].findAll("div", {"style": "margin-left:10px;display:inline-block;"})
    abil = str(abil)
    abil = abil.split('>')
    abil = abil[1].split('<')
    abil = abil[0]
    return(abil)

def add_ev_and_nat(p):
    pika = "https://www.pikalytics.com/pokedex/vgc2018/" + p + "/"

    uData = ureq(pika)#pull html
    html = uData.read()
    page_soup = soup(html, "html.parser")

    ev_and_nat = page_soup.findAll("div", {"class": "inline-block pokemon-stat-container"})
    ev_and_nat = ev_and_nat[5].findAll("div", {"class": "pokedex-category-wrapper"})
    ev_and_nat = ev_and_nat[0].findAll("div", {"id": "spread_wrapper"})
    ev_and_nat = ev_and_nat[0].findAll("div")
    ev_and_nat = ev_and_nat[0].findAll("div", {"class": "pokedex-move-entry-new"})
    nat = ev_and_nat[0].findAll("div", {"style": "margin-left:10px;display:inline-block;"})
    ev = ev_and_nat[0].findAll("div", {"style": "display:inline-block;"})

    nat = str(nat[0])
    nat = nat.split(">")
    nat = nat[1]
    nat = nat.split("<")
    nat = nat[0]
    evfinal = ""
    stat = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]
    for n in range(len(ev)):
        x = str(ev[n])
        x = x.split(">")
        x = x[1]
        x = x.split("<")
        x = x[0]
        x = x.replace("/", "")
        evfinal += x + " " + stat[n] + " "
        if n < 5:
            evfinal  +=  "/" + " "

    return(evfinal, nat)

def add_moves(p):
    move_list = []
    pika = "https://www.pikalytics.com/pokedex/vgc2018/" + p + "/"

    uData = ureq(pika)#pull html
    html = uData.read()
    page_soup = soup(html, "html.parser")

    moves = page_soup.findAll("div", {"class": "inline-block pokemon-stat-container"})
    moves = moves[1].findAll("div", {"class": "pokedex-category-wrapper"})
    moves = moves[0].findAll("div", {"id": "moves_wrapper"})
    moves = moves[0].findAll("div")
    moves = moves[0].findAll("div", {"class": "pokedex-move-entry-new"})
    for m in range(0, 4):
        move = moves[m].findAll("div", {"style": "margin-left:10px;display:inline-block;color:#333;"})
        move = moves
        move = move[m]
        move = move.findAll("div", {"style": "margin-left:10px;display:inline-block;color:#333;"})
        move[0] = str(move[0])
        move = move[0].split(">")
        move = move[1]
        move = move.split("<")
        move = move[0]
        move_list.append(move)

    return(move_list)
def add_info(new_team, showdown_comp):
    showdown_comp.append("=== [gen7vgc2018] ===")
    showdown_comp.append(" ")
    inlist = []
    for p in new_team:

        item = "item"
        n = 0
        item = add_item(item, n, inlist, p)

        np = p
        if np == "Tapu%20Lele":
            np = "Tapu Lele"
        elif np == "Tapu%20Fini":
            np = "Tapu Fini"
        elif np == "Tapu%20Bulu":
            np = "Tapu Bulu"
        elif np == "Tapu%20Koko":
            np = "Tapu Koko"

        showdown_comp.append(np + " " + "@" + " " + item)

        ability = add_abil(p)
        showdown_comp.append("Ability: " + ability)

        showdown_comp.append("Level: 50")

        evs, nat = add_ev_and_nat(p)
        showdown_comp.append("EVs: " + evs)
        showdown_comp.append(nat + " " + "Nature")

        move1, move2, move3, move4 = add_moves(p)
        showdown_comp.append("- " + move1)
        showdown_comp.append("- " + move2)
        showdown_comp.append("- " + move3)
        showdown_comp.append("- " + move4)

        showdown_comp.append(" ")

    showdown_comp.append(" ")

def showdown(all_teams, showdown_comp):
    for x in range(len(all_teams)):
        add_info(all_teams[x], showdown_comp)

showdown(all_teams, showdown_comp)
for x in showdown_comp:
    print(x)
