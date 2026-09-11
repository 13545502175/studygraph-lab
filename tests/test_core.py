import json
from studygraph.io import load_nodes
from studygraph.graph import build_graph
from studygraph.recommend import recommend
def test_recommend_orders_low_mastery(tmp_path):
 p=tmp_path/'x.json'; p.write_text(json.dumps({'nodes':[{'id':'a','name':'A','prerequisites':[],'mastery':.9},{'id':'b','name':'B','prerequisites':['a'],'mastery':.1}]}))
 n=load_nodes(p); r=recommend(n,build_graph(n)); assert r[0]['id']=='b'
def test_cycle_rejected(tmp_path):
 p=tmp_path/'x.json'; p.write_text(json.dumps({'nodes':[{'id':'a','name':'A','prerequisites':['b'],'mastery':.5},{'id':'b','name':'B','prerequisites':['a'],'mastery':.5}]}))
 n=load_nodes(p)
 import pytest
 with pytest.raises(ValueError,match='cycle'): build_graph(n)
