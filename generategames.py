f = open("games.csv","r")
lines = f.readlines()
f.close()

dictnames = lines[0].replace('\n','').split(',')

games = []
for l in lines[1:]:
    game = {}
    for i,info in enumerate(l.replace('\n','').split(",")):
        if not info: continue
        game[dictnames[i]] = info
    games.append(game)




def putinto(parent, child, var="$content"):
    return parent.replace(var, child)

def has(g, what):
    return what in g and g[what]

CARD_BACKGROUND = "background-size: cover; background-position: center center; background-image: url(/images/$content); background-repeat: no-repeat"

GAME_CARD = "<div class=\"col-md-6\"><div style=\"$style\" class=\"game-card card mb-4 shadow-sm\">$content</div></div>"

NAME = "<p class=\"h3 game-name\" style=\"color: #fff\">$content</p>"

CARD_BODY = "<div class=\"card-body\"><div>$content</div></div>"

TEXT_CONTENT = "<div class=\"text-content\">$content</div>"

PLATFORM = "<i style=\"\" class=\"platform fab fa-$content\"></i>"

LANGUAGE = "<i class=\"devicon devicon-$content\"></i>"

ICON = "<img src=\"/images/$content\" />"

LDJAM_LINK ="<a href=\"$content\" role=\"button\" class=\"btn btn-secondary\"><i class=\"fa fa-trophy\"></i> LD Entry</a>"

PLAY_LINK ="<a href=\"$content\" role=\"button\" class=\"btn btn-secondary\"><i class=\"fab fa-google-play\"></i> Google Play</a>"

ITCHIO_LINK ="<a href=\"$content\" role=\"button\" class=\"btn btn-secondary\"><i class=\"fab fa-itch-io\"></i> itch.io</a>"

GITHUB_LINK ="<a href=\"$content\" role=\"button\" class=\"btn btn-secondary\"><i class=\"fab fa-github\"></i> GitHub</a>"

GAMES = """---
layout: default
---
<article class="post">

  <header class="post-header">
    <h1 class="post-title">Games</h1>
  </header>

  <style type="text/css">
    img {width: 5em; height: 5em;  margin-top: 1.25rem; margin-left: 1.25rem;}
    .platform {
        color: white;
        font-size: 32pt;
        position: absolute; right: 1.25rem; top: 1.25rem;
     }
    .devicon {
        position: absolute; right: 1.25rem; top: calc(1.75rem + 32pt);
        font-size: 32pt;
        color: white;
     }
    .game-card {
        min-height: 16em;
    }
    @media screen and (min-width: 992px) {
        .game-card {
            min-height: 20em;
            border-radius: 0.3em;
        }
        img {width: 6em; height: 6em; margin-top: 1.25rem; margin-left: 1.25rem;}
    }
    .game-name {
        text-shadow: 1px 1px 3px rgba(10, 10, 10, 0.8);
        font-weight: bold;
        font-family: Jost, sans-serif;
    }
    .card-body a.btn, .card-body a.btn:hover {
        background-color: rgb(230, 230, 230);
        color: #111;
        margin: 2px;
    }
    .card-body > div {
        position:absolute; bottom: 1.25rem;
    }

    ul.profilelinks {
        margin-top: 8px;
        margin-bottom: 8px;
        margin-left: 2px;
        margin-right: 2px;
        text-align: right;
        list-style-type: none;
        display: block;
    }

    ul.profilelinks li {
        display: inline;
    }

    ul.profilelinks li a {
        color: white;
    }

    ul.profilelinks li a:hover {
        color: #cba;
        transition: 0.25s 0.25s ease-in color;
    }
  </style>

  <ul class="profilelinks">
    <li><a href="https://furfel.itch.io" target="_blank" role="button" class="btn btn-secondary"><i class="fab fa-itch-io"></i> itch.io</a></li>
    <li><a href="https://play.google.com/store/apps/dev?id=8056970146235984514" target="_blank" role="button" class="btn btn-secondary"><i class="fab fa-google-play"></i> Google Play</a></li>
    <li><a href="https://github.com/furfel" target="_blank" role="button" class="btn btn-secondary"><i class="fab fa-github"></i> GitHub</a></li>
  </ul>

  <div class="post-content">
    <h3 id="here-is-the-list-of-my-games-for-android">Here is the list of some of my works:</h3>
    <div class="containter">
        <div class="row">
            $games
        </div>
    </div>
  </div>

</article>"""

gameshtml = ""

for g in games:
    content = ''
    card_body = ''
    bg = ''
    if has(g, 'Screenshot'):
        bg = putinto(CARD_BACKGROUND, g['Screenshot'])
    if has(g, 'Icon'):
        content += putinto(ICON, g['Icon'])
    if has(g, 'Platform'):
        content += putinto(PLATFORM, g['Platform'])
    if has(g, 'Language'):
        content += putinto(LANGUAGE, g['Language'])

    if has(g, 'Name'):
        card_body += putinto(NAME, g['Name'])
    
    if has(g, 'play_link'):
        card_body += putinto(PLAY_LINK, g['play_link'])

    if has(g, 'github_link'):
        card_body += putinto(GITHUB_LINK, g['github_link'])

    if has(g, 'itchio_link'):
        card_body += putinto(ITCHIO_LINK, g['itchio_link'])

    if has(g, 'ldjam_link'):
        card_body += putinto(LDJAM_LINK, g['ldjam_link'])

    content += putinto(CARD_BODY, card_body)
    if not card_body:
        continue

    game_card = putinto(GAME_CARD, content)
    game_card = putinto(game_card, bg, '$style')
    if card_body and content:
        gameshtml += game_card

html = open("_layouts/games.html", "w")
games = putinto(GAMES, gameshtml, '$games')
html.write(games)
html.close()
    


import json
print(json.dumps(games))
        
        
