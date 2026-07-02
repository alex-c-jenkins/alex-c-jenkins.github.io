import numpy as np
from datetime import datetime
from json import load, loads
from os import chdir, getcwd
from subprocess import call, check_output

cwd = getcwd()
chdir('/Users/alex/Documents/Work/alex-c-jenkins.github.io/')

# set up standings
names = np.array([
    'Alex', 'Bryony', 'Dad', 'George', 'Mum', 'Sandra', 'Saskia', 'Stuart'])
teams = np.array([
    ['POR', 'USA', 'AUT', 'BIH', 'ECU', 'IRQ'],
    ['FRA', 'URU', 'PAN', 'SEN', 'EGY', 'JOR'],
    ['GER', 'BEL', 'KOR', 'SWE', 'IRN', 'KSA'],
    ['BRA', 'CRO', 'CIV', 'TUN', 'GHA', 'CPV'],
    ['ESP', 'JPN', 'SUI', 'AUS', 'RSA', 'QAT'],
    ['NED', 'CAN', 'SCO', 'MEX', 'UZB', 'NZL'],
    ['ENG', 'NOR', 'COL', 'PAR', 'ALG', 'CUW'],
    ['ARG', 'MAR', 'TUR', 'CZE', 'COD', 'HAI']])
flags = np.array([
    ['🇵🇹', '🇺🇸', '🇦🇹', '🇧🇦', '🇪🇨', '🇮🇶'],
    ['🇫🇷', '🇺🇾', '🇵🇦', '🇸🇳', '🇪🇬', '🇯🇴'],
    ['🇩🇪', '🇧🇪', '🇰🇷', '🇸🇪', '🇮🇷', '🇸🇦'],
    ['🇧🇷', '🇭🇷', '🇨🇮', '🇹🇳', '🇬🇭', '🇨🇻'],
    ['🇪🇸', '🇯🇵', '🇨🇭', '🇦🇺', '🇿🇦', '🇶🇦'],
    ['🇳🇱', '🇨🇦', '🏴󠁧󠁢󠁳󠁣󠁴󠁿', '🇲🇽', '🇺🇿', '🇳🇿'],
    ['🏴󠁧󠁢󠁥󠁮󠁧󠁿', '🇳🇴', '🇨🇴', '🇵🇾', '🇩🇿', '🇨🇼'],
    ['🇦🇷', '🇲🇦', '🇹🇷', '🇨🇿', '🇨🇩', '🇭🇹']])
eliminated = np.array([
    [False, False, False, True, True, True],
    [False, True, True, True, False, True],
    [True, False, True, True, True, True],
    [False, False, True, True, False, False],
    [False, True, False, False, True, True],
    [True, False, True, False, True, True],
    [False, False, False, False, False, True],
    [False, False, True, True, True, True]])
played = np.zeros(len(names))
won = np.zeros(len(names))
drawn = np.zeros(len(names))
lost = np.zeros(len(names))
goaldiff = np.zeros(len(names))
scores = np.zeros(len(names))

# refresh group stage data
with open('assets/json/wc2026.json', 'r') as f: old_data = load(f)['tables']
call('/opt/homebrew/bin/node '
     + '/opt/homebrew/lib/node_modules/@claudinho/cli/dist/index.js '
     + '--json --no-color --flavor off table > assets/json/wc2026.json',
     shell=True)
with open('assets/json/wc2026.json', 'r') as f: data = load(f)['tables']
if data != old_data:
    call('git commit -m "Update WC2026 groups table" assets/json/wc2026.json',
         shell=True)

# process group stage data
for group in data:
    for team in group['standings']:
        idx = np.where(teams == team['team']['code'])[0][0]
        played[idx] += team['played']
        won[idx] += team['won']
        drawn[idx] += team['drawn']
        lost[idx] += team['lost']
        goaldiff[idx] += team['goalDiff']
        scores[idx] += team['won'] + 0.5 * team['drawn']

# process knockout stage data
for matchid in range(760486, 760518):
    matchdata = check_output('/opt/homebrew/bin/node '
        + '/opt/homebrew/lib/node_modules/@claudinho/cli/dist/index.js '
        + '--json --no-color --flavor off match ' + str(matchid), shell=True)
    matchdata = loads(matchdata)['match']
    if matchdata['status'] == 'FT':
        player1 = np.where(teams == matchdata['home']['code'])[0][0]
        team1 = np.where(teams == matchdata['home']['code'])[1][0]
        player2 = np.where(teams == matchdata['away']['code'])[0][0]
        team2 = np.where(teams == matchdata['away']['code'])[1][0]
        played[player1] += 1
        played[player2] += 1
        home = matchdata['score']['home']
        away = matchdata['score']['away']
        #print(matchdata['home']['code'], home, away, matchdata['away']['code'])
        if home > away:
            won[player1] += 1
            lost[player2] += 1
            scores[player1] += 1
            eliminated[player2][team2] = True
        elif home < away:
            lost[player1] += 1
            won[player2] += 1
            scores[player2] += 1
            eliminated[player1][team1] = True
        elif matchid in [760488, 760489]:
            lost[player1] += 1
            won[player2] += 1
            scores[player2] += 1
            eliminated[player1][team1] = True
        goaldiff[player1] += home - away
        goaldiff[player2] += away - home

# update standings (sort by goal difference, then wins, then scores)
ids = np.argsort(-goaldiff)
names = names[ids]
teams = teams[ids]
flags = flags[ids]
eliminated = eliminated[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

ids = np.argsort(-won)
names = names[ids]
teams = teams[ids]
flags = flags[ids]
eliminated = eliminated[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

ids = np.argsort(-scores)
names = names[ids]
teams = teams[ids]
flags = flags[ids]
eliminated = eliminated[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

# update standings page
with open('_pages/wc2026.md', 'r') as f:
    old_standings = f.readlines()[9:]

file = open('_pages/wc2026.md', 'w')
file.write('---\n')
file.write('layout: page\n')
file.write('title: Jenkins World Cup Sweepstake 2026\n')
file.write('permalink: /wc2026/\n')
file.write('nav: false\n')
file.write('---\n')
file.write('\n')
file.write('Table last updated at '
            + datetime.now().strftime("%H:%M")
            + ' on ' + datetime.now().strftime("%d %B %Y") + '\n')
file.write('\n')
file.write(
    '| Name | Teams | Remaining | Score | Played | Won | Drawn | Lost | Goal Diff |\n')
file.write(
    '|------|-------|-----------|-------|--------|-----|-------|------|-----------|\n')
for i in range(len(names)):
    file.write(
        f'| {names[i]} | {''.join(flags[i])} | {''.join(flags[i][~eliminated[i]])} | **{scores[i]:.1f}** '
        + f'| {int(played[i])} | {int(won[i])} | {int(drawn[i])} '
        + f'| {int(lost[i])} | {int(goaldiff[i])} |\n')
file.close()

with open('_pages/wc2026.md', 'r') as f:
    standings = f.readlines()[9:]

if standings != old_standings:
    call('git commit -m "Update WC2026 standings" _pages/wc2026.md', shell=True)
    call('git push', shell=True)

chdir(cwd)
