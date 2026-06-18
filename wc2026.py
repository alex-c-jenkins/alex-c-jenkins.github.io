#!/usr/bin/env python
import json
import numpy as np
from datetime import datetime
from os import system

system('claudinho --json --no-color --flavor off table > assets/json/wc2026.json')

with open('assets/json/wc2026.json', 'r') as f:
    data = json.load(f)['tables']

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
    '🇵🇹🇺🇸🇦🇹🇧🇦🇪🇨🇮🇶', '🇫🇷🇺🇾🇵🇦🇸🇳🇪🇬🇯🇴', '🇩🇪🇧🇪🇰🇷🇸🇪🇮🇷🇸🇦', '🇧🇷🇭🇷🇨🇮🇹🇳🇬🇭🇨🇻', '🇪🇸🇯🇵🇨🇭🇦🇺🇿🇦🇶🇦', '🇳🇱🇨🇦🏴󠁧󠁢󠁳󠁣󠁴󠁿🇲🇽🇺🇿🇳🇿', '🏴󠁧󠁢󠁥󠁮󠁧󠁿🇳🇴🇨🇴🇵🇾🇩🇿🇨🇼', '🇦🇷🇲🇦🇹🇷🇨🇿🇨🇩🇭🇹'])
played = np.zeros(len(names))
won = np.zeros(len(names))
drawn = np.zeros(len(names))
lost = np.zeros(len(names))
goaldiff = np.zeros(len(names))
scores = np.zeros(len(names))

for group in data:
    for team in group['standings']:
        idx = np.where(teams == team['team']['code'])[0][0]
        played[idx] += team['played']
        won[idx] += team['won']
        drawn[idx] += team['drawn']
        lost[idx] += team['lost']
        goaldiff[idx] += team['goalDiff']
        scores[idx] += team['won'] + 0.5 * team['drawn']

ids = np.argsort(-goaldiff)
names = names[ids]
teams = teams[ids]
flags = flags[ids]
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
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

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
    '| Name | Teams | Score | Played | Won | Drawn | Lost | Goal Diff |\n')
file.write(
    '|------|-------|-------|--------|-----|-------|------|-----------|\n')
for i in range(len(names)):
    file.write(
        f'| {names[i]} | {flags[i]} | **{scores[i]:.1f}** | {int(played[i])} | {int(won[i])} | {int(drawn[i])} | {int(lost[i])} | {int(goaldiff[i])} |\n')
file.close()
