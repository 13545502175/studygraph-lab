import csv, json
from pathlib import Path

def load_nodes(path):
    p=Path(path)
    if p.suffix.lower()=='.json':
        data=json.loads(p.read_text(encoding='utf-8'))
    elif p.suffix.lower()=='.csv':
        data=list(csv.DictReader(p.open(encoding='utf-8-sig', newline='')))
        for row in data: row['prerequisites']=[x.strip() for x in row.get('prerequisites','').split(';') if x.strip()]
    else: raise ValueError('Input must be .json or .csv')
    if isinstance(data,dict): data=data.get('nodes', data)
    validate_nodes(data); return data

def validate_nodes(nodes):
    if not isinstance(nodes,list) or not nodes: raise ValueError('nodes must be a non-empty list')
    ids=set()
    for i,n in enumerate(nodes):
        for key in ('id','name','mastery'):
            if key not in n: raise ValueError(f'row {i}: missing {key}')
        if n['id'] in ids: raise ValueError(f'duplicate node id: {n["id"]}')
        ids.add(n['id']); n['mastery']=float(n['mastery'])
        if not 0<=n['mastery']<=1: raise ValueError(f'{n["id"]}: mastery must be between 0 and 1')
        n.setdefault('prerequisites',[])
    for n in nodes:
        missing=set(n['prerequisites'])-ids
        if missing: raise ValueError(f'{n["id"]}: unknown prerequisite(s): {", ".join(sorted(missing))}')
    return nodes
