import argparse,json
from .io import load_nodes
from .graph import build_graph
from .recommend import recommend
from .report import render_html
def main(argv=None):
    p=argparse.ArgumentParser(prog='studygraph'); sub=p.add_subparsers(dest='cmd',required=True)
    for c in ('validate','recommend','report'):
        q=sub.add_parser(c); q.add_argument('input'); q.add_argument('-o','--output'); q.add_argument('-n','--limit',type=int)
    a=p.parse_args(argv); nodes=load_nodes(a.input); graph=build_graph(nodes)
    if a.cmd=='validate': print(f'Valid graph: {len(nodes)} nodes, {sum(map(len,graph.values()))} prerequisite edges'); return 0
    items=recommend(nodes,graph,a.limit)
    if a.cmd=='recommend': out=json.dumps(items,ensure_ascii=False,indent=2)
    else: out=render_html(items)
    if a.output: open(a.output,'w',encoding='utf-8').write(out)
    else: print(out)
    return 0
