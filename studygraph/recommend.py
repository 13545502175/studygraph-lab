def recommend(nodes, graph, limit=None):
    by={n['id']:n for n in nodes}; downstream={x:0 for x in graph}
    for ps in graph.values():
        for p in ps: downstream[p]+=1
    result=[]
    for n in nodes:
        gap=sum(1-by[p]['mastery'] for p in graph[n['id']])/max(1,len(graph[n['id']]))
        down=downstream[n['id']]/max(1,len(nodes)-1)
        un=1-n['mastery']; score=.6*un+.25*gap+.15*down
        result.append({'id':n['id'],'name':n['name'],'score':round(score,4),'mastery':n['mastery'],'prerequisite_gap':round(gap,4),'downstream_impact':round(down,4),'explanation':f"复习{name if (name:=n['name']) else n['id']}：当前掌握度 {n['mastery']:.0%}。"})
    return sorted(result,key=lambda x:(-x['score'],x['id']))[:limit] if limit else sorted(result,key=lambda x:(-x['score'],x['id']))
