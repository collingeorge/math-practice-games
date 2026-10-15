# Builds the three operation games from src/operation-game.template.html.
# Run from the repo root: python3 scripts/build-operations.py
import json
T=open('src/operation-game.template.html', encoding='utf-8').read()
games = {
 'subtract-within-1000.html': dict(title='Take It Away: Subtraction Within 1,000', h1='Take it away', emoji='🧮', cfg=dict(OP='-', MODEL='blocks', STAGES=[
   dict(n=5, a=[3,3], b=[2,3], reg=[0,0], maxTop=999),
   dict(n=7, a=[3,3], b=[2,3], cols=[0], maxTop=999),
   dict(n=6, a=[3,3], b=[2,3], cols=[1], maxTop=999),
   dict(n=7, a=[3,3], b=[2,3], cols=[0,1], maxTop=999),
   dict(n=3, a=[3,3], b=[2,3], reg=[1,2], zeros=True, maxTop=999),
   dict(n=2, special='fromPower', k=3)])),
 'add-within-1-million.html': dict(title='Add It Up: Addition Within 1,000,000', h1='Add it up: big numbers', emoji='🚀', cfg=dict(OP='+', MODEL='disks', STAGES=[
   dict(n=3, a=[6,6], b=[5,6], reg=[0,0], maxTop=999999),
   dict(n=4, a=[6,6], b=[5,6], reg=[1,1], maxTop=999999),
   dict(n=5, a=[6,6], b=[5,6], reg=[2,3], maxTop=999999),
   dict(n=4, a=[6,6], b=[6,6], reg=[4,5], maxTop=999999),
   dict(n=2, a=[6,6], b=[3,5], reg=[1,3], zeros=True, maxTop=999999),
   dict(n=2, special='toPower', k=6)])),
 'subtract-within-1-million.html': dict(title='Take It Away: Subtraction Within 1,000,000', h1='Take it away: big numbers', emoji='🚀', cfg=dict(OP='-', MODEL='disks', STAGES=[
   dict(n=3, a=[6,6], b=[5,6], reg=[0,0], maxTop=999999),
   dict(n=4, a=[6,6], b=[5,6], reg=[1,1], maxTop=999999),
   dict(n=5, a=[6,6], b=[5,6], reg=[2,3], maxTop=999999),
   dict(n=6, a=[6,6], b=[4,6], reg=[1,4], zeros=True, maxTop=999999),
   dict(n=2, special='fromPower', k=6)])),
}
for f,g in games.items():
    cfg=json.dumps(g['cfg'], indent=2).replace('\n','\n  ')
    s=T.replace('__TITLE__',g['title']).replace('__H1__',g['h1']).replace('__EMOJI__',g['emoji']).replace('__CONFIG__',cfg)
    open('games/'+f, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
