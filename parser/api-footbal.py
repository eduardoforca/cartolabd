import requests
from datetime import datetime
import os
from urllib.request import urlopen
import random
api_token = ''
def save_teams(teams):
    for team in teams:
        img = urlopen(team['logo']).read()
        image_path = str(team['team_id']) + '.png'
        with open(image_path, 'wb') as out:
            out.write(img)
        image_filename = os.path.basename(image_path)
        to_post = {
            'crest': (image_filename, open(image_path, 'rb'))
        }
        response = requests.post('http://157.230.153.79/v1/realClub/',
                                 files=to_post, data={'nome': team['name'], 'short_name': (team['name'][0:3]).upper()})
        print(response.status_code)

def fetch_teams_from_api():
    response = requests.get("http://157.230.153.79/v1/realClub/")
    return response.json()

def fetch_players_from_api():
    response = requests.get("http://157.230.153.79/v1/player/")
    return response.json()

def fetch_matches_from_api():
    response = requests.get("http://157.230.153.79/v1/match/")
    return response.json()

def fetch_matches():
    response = requests.get("https://api-football-v1.p.rapidapi.com/v2/fixtures/league/357",
        headers={
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
            "X-RapidAPI-Key": api_token
        }
    )
    data = response.json()
    return data['api']['fixtures']

def fetch_teams():
    response = requests.get("https://api-football-v1.p.rapidapi.com/v2/teams/league/357",
      headers={
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
        "X-RapidAPI-Key": api_token
      }
    )

    data = response.json()
    return data['api']['teams']
def save_matches(matches, teams):
    error = []
    for match in matches:
        to_post = {
            'datetime': datetime.fromtimestamp(match['event_timestamp']),
            'home_score': match['goalsHomeTeam'],
            'away_score': match['goalsAwayTeam'],
            '_round': match['round'][17:],
            'home_club': next((x['id'] for x in teams if (x['nome']).upper() == (match['homeTeam']['team_name']).upper()), 0),
            'away_club': next((x['id'] for x in teams if (x['nome']).upper() == (match['awayTeam']['team_name']).upper()), 0)
        }
        response = requests.post('http://157.230.153.79/v1/match/',
                                 data=to_post)
        print(response.status_code)
        if response.status_code != 201:
            error.append(response)
    if error:
        import ipdb; ipdb.set_trace()

def convertPosition(pos):
    if (pos == 'G') or (pos == 'Goalkeeper'):
        return 1
    elif (pos == 'D') or (pos == 'Defender'):
        return 2
    elif (pos == 'M') or (pos == 'Midfielder'):
        return 3
    elif (pos == 'A') or (pos == 'Attacker'):
        return 4
    else:
        return None
def convertEvent(type, detail):
    if type == 'Goal':
        if (detail == 'Own Goal'):
            return 3
        else:
            return 16
    elif type == 'Card':
        if (detail == 'Yellow Card'):
            return 4
        else:
            return 5
    else:
        return None
def fetch_players(teams, api_teams):
    error = []
    for team in teams:
        response = requests.get("https://api-football-v1.p.rapidapi.com/v2/players/team/{}/2019".format(team['team_id']),
            headers={
                "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
                "X-RapidAPI-Key": api_token
            }
        )
        data = response.json()
        for player in data['api']['players']:
            if player['league'] != 'Serie A':
                continue
            to_post = {
                'nome': player['player_name'],
                'club': next((x['id'] for x in api_teams if (x['nome']).upper() == (player['team_name']).upper()), 0),
                'position': convertPosition(player['position'])
            }
            response = requests.post('http://157.230.153.79/v1/player/',
                                     data=to_post)
            print(response.status_code)
            if response.status_code != 201:
                error.append(response)
    if error:
        import ipdb; ipdb.set_trace()

def fetch_events(matches, api_matches, api_players, api_teams):
    all_players = {}
    error = []
    for match in matches:
        if match['statusShort'] != 'FT':
            continue
        response = requests.get("https://api-football-v1.p.rapidapi.com/v2/events/{}".format(match['fixture_id']),
          headers={
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
            "X-RapidAPI-Key": api_token
          }
        )
        data = response.json()
        home_team = next((x for x in api_teams if (x['nome']).upper() == (match['homeTeam']['team_name']).upper()), None)
        away_team = next((x for x in api_teams if (x['nome']).upper() == (match['awayTeam']['team_name']).upper()), None)
        match_round = next((x['_round'] for x in api_matches if (x['away_club'] == away_team['id']) and (x['home_club'] == home_team['id'])), 0)
        events = {}
        for event in data['api']['events']:
            if event['player_id'] in all_players:
                plr = all_players[event['player_id']]
            else:
                response = requests.get("https://api-football-v1.p.rapidapi.com/v2/players/player/{}/2019".format(event['player_id']),
                    headers={
                        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
                        "X-RapidAPI-Key": api_token
                    }
                )
                data2 = response.json()
                if 'players' in data2['api'] and data2['api']['results'] > 0:
                    plr = next((x for x in data2['api']['players'] if x['league'] == 'Serie A'), data2['api']['players'][0])
                else:
                    continue
                all_players[event['player_id']] = plr
            if (match['homeTeam']['team_id'] == event['team_id']):
                club_id = home_team['id']
            else:
                club_id = away_team['id']
            player_id = next((x['id'] for x in api_players if ((x['nome']).upper() == (plr['player_name']).upper()) and (x['club'] == club_id)), 0)
            if player_id == 0:
                to_post = {
                    'nome': plr['player_name'],
                    'club': club_id,
                    'position': convertPosition(plr['position'])
                }
                response = requests.post('http://157.230.153.79/v1/player/',
                                         data=to_post)
                if response.status_code == 201:
                    data3 = response.json()
                    print('added player {}'.format(data3['id']))
                    api_players.append(data3)
                    player_id = data3['id']
            event_id = convertEvent(event['type'], event['detail'])
            if event_id:
                if not (player_id in events):
                    events[player_id] = {}
                if not (event_id in events[player_id]):
                    events[player_id][event_id] = {
                        'player': player_id,
                        'stat': event_id,
                        '_round': match_round,
                        'amount': 1
                    }
                else:
                    events[player_id][event_id]['amount'] = events[player_id][event_id]['amount'] + 1
        for player in events:
            for event in events[player]:
                response = requests.post('http://157.230.153.79/v1/playerStats/',
                                         data=events[player][event])
                print(response.status_code)
                print(response.json())
                if response.status_code != 201:
                    error.append(response)
    if error:
        import ipdb; ipdb.set_trace()

def generatePlayerPrice(api_players):
    for player in api_players:
        if player['id'] < 631:
            continue
        last_price = int(random.normalvariate(7, 5))
        if (last_price < 1):
            last_price = 1 - last_price
        for round in range(1, 10):
            data = {
                'price': last_price,
                'player': player['id'],
                '_round': round
            }
            last_price += int(random.normalvariate(0, 2))
            if (last_price < 1):
                last_price = 1 - last_price
            response = requests.post('http://157.230.153.79/v1/playerPrice/',
                                     data=data)
            print(response.status_code)
            print(response.json())
            if response.status_code != 201:
                error.append(response)


if __name__ == '__main__':
    # teams = fetch_teams()
    # save_teams(teams)
    # api_teams = fetch_teams_from_api()
    # matches = fetch_matches()
    # save_matches(api_teams)
    # api_matches = fetch_matches_from_api()
    # fetch_players(teams, api_teams)
    api_players = fetch_players_from_api()
    # fetch_events(matches, api_matches, api_players, api_teams)
    generatePlayerPrice(api_players)
