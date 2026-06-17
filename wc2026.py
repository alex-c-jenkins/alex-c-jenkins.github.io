#!/usr/bin/env python
import json
import numpy as np
from os import system

system('claudinho --json --no-color --flavor off table > fwc2026.json')

with open('fwc2026.json', 'r') as f:
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

ids = goaldiff.argsort()[::-1]
names = names[ids]
teams = teams[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

ids = won.argsort()[::-1]
names = names[ids]
teams = teams[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]

ids = scores.argsort()[::-1]
names = names[ids]
teams = teams[ids]
played = played[ids]
won = won[ids]
drawn = drawn[ids]
lost = lost[ids]
goaldiff = goaldiff[ids]
scores = scores[ids]
