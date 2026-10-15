# Builds the two addition-facts games from src/facts-game.template.html.
# Run from the repo root: python3 scripts/build-facts.py
import json, os
here = 'src'
T = open(os.path.join(here, 'facts-game.template.html'), encoding='utf-8').read()
OUT = os.environ.get('OUT', 'games/')
games = {
 'addition-facts-within-12.html': dict(title='Fact Strategies: Adding Within 12', h1='Adding facts to 12', cfg=dict(MAX_SUM=12, STAGES=[
   dict(n=6, types=['zero','countOn'], maxSmall=2),
   dict(n=6, types=['doubles']),
   dict(n=6, types=['countOn','nearDoubles'], minSmall=3),
   dict(n=6, types=['makeTen']),
   dict(n=6, types=['any'], minSum=5)])),
 'addition-facts-within-18.html': dict(title='Fact Strategies: Adding Within 18', h1='Adding facts to 18', cfg=dict(MAX_SUM=18, STAGES=[
   dict(n=5, types=['countOn'], minSum=7),
   dict(n=6, types=['doubles'], minSum=10),
   dict(n=6, types=['nearDoubles'], minSum=9),
   dict(n=7, types=['makeTen'], minSum=11),
   dict(n=6, types=['any'], minSum=10)])),
}
for f, g in games.items():
    cfg = json.dumps(g['cfg']).replace('{"n"', '\n    {"n"').replace(']}', '\n  ]}')
    s = T.replace('__TITLE__', g['title']).replace('__H1__', g['h1']).replace('__CONFIG__', cfg)
    open(os.path.join(OUT, f), 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
