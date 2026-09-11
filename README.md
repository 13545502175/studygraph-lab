# StudyGraph Lab

> 用知识图谱生成可解释的复习优先级。

把知识点之间的先修关系变成一份可解释的复习计划。适合学生做课程复习，也适合作为图机器学习入门项目。

## 5 分钟运行

```bash
python -m pip install -e .
python -m studygraph validate examples/math.json
python -m studygraph recommend examples/math.json -o recommendations.json
python -m studygraph report examples/math.json -o review.html
```

打开 `review.html` 即可看到按优先级排序的复习清单。输入 JSON 的每个节点包含 `id`、`name`、`prerequisites`（ID 数组）和 0 到 1 的 `mastery`。

## 为什么有用

分数结合当前未掌握度、先修薄弱程度和对后续知识点的影响，并输出解释文字。模型是确定性的，方便课堂演示、复现和改造。

## 开发

```bash
python -m pytest -q
```

MIT License。欢迎提交新的学科示例和评分策略。

## Python API

```python
from studygraph import load_nodes, build_graph, recommend
nodes = load_nodes("examples/math.json")
plan = recommend(nodes, build_graph(nodes), limit=3)
```
