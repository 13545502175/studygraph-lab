# StudyGraph Lab 设计规格

## 目标

StudyGraph Lab 是一个面向学生的本地开源学习工具：用户导入知识点及其先修关系，工具构建知识图谱，用轻量图模型估计每个知识点的复习优先级，并生成可分享的 HTML 复习清单。首版不依赖云端 API，使用示例数据即可运行。

## 范围

- CSV 与 JSON 导入，字段包含 `id`、`name`、`prerequisites`、`mastery`。
- 输入校验：检测缺失字段、未知先修节点、循环关系和 mastery 越界。
- 基于邻接传播的轻量推荐模型；无 PyTorch 时提供确定性的加权基线。
- CLI：`validate`、`recommend`、`report` 三个命令。
- 输出排名 JSON 与单文件 HTML 报告，包含图谱统计、优先级、解释文字。
- 内置数学示例数据、快速开始文档、MIT 许可证和 GitHub Actions。

## 架构与数据流

`Input files -> loader/validator -> graph builder -> recommender -> JSON/HTML renderer`。

Python 包采用 `studygraph/` 分层：`io.py` 负责读取，`graph.py` 负责关系解析，`recommend.py` 负责评分，`report.py` 负责展示，`cli.py` 负责命令行编排。各模块通过普通字典和 dataclass 交互，便于学生阅读和替换模型。

## 评分逻辑

每个节点的复习分数由未掌握度、先修影响和后继影响组成：`0.6 * (1-mastery) + 0.25 * prerequisite_gap + 0.15 * downstream_count`，归一化到 0 到 1。输出同时包含分项分数和一句可读解释，避免把推荐当成不可解释的黑盒。

## 错误处理与验证

CLI 对输入错误返回非零退出码并指出行号或节点 ID；空图和只有一个节点的图也必须可运行。测试覆盖导入校验、循环检测、评分排序、报告生成和 CLI smoke test。CI 使用 Python 3.10–3.12 运行测试。

## 验收标准

新用户按 README 的三条命令可在本地生成推荐报告；示例数据输出至少 5 个节点、稳定排序和可打开的 HTML；测试全部通过；仓库首页能在 30 秒内说明用途、安装、示例和扩展方式。
