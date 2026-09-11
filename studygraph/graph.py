def build_graph(nodes):
    graph={n['id']:list(n.get('prerequisites',[])) for n in nodes}
    state={}
    def visit(x):
        if state.get(x)==1: raise ValueError(f'cycle detected at {x}')
        if state.get(x)==2: return
        state[x]=1
        for p in graph[x]: visit(p)
        state[x]=2
    for x in graph: visit(x)
    return graph
