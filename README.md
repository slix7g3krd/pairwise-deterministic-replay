# pairwise-deterministic-replay

同一段回放跑两次，第 300 帧开始角色位置分叉，浮点累加顺序随并行归约变化；随机数种子按端生成，两边第一次掉落就不同；物理子步按渲染帧数切，帧率波动时步长跟着变；遍历哈希表决定伤害结算顺序，每次都不一样；并行求和把浮点结果按线程完成顺序合并；输入采样时间戳带抖动，回放重放时按键落在不同 tick；AI 决策读了 wall clock，同一录像在不同机器上走不同分支；浮点 denormal 模式两端不一致，极小速度被冲成零；回放记录丢帧后没补空输入，后续整段错位；快照间隔太长，分叉后无法定位首个不同帧；碰撞查询顺序依赖 broadphase 构建，重建后结果变。gameplay/deterministic_replay.py 是核心，tests/test_deterministic_replay.py 15个红。要修的是：固定归约顺序；种子由录像写入并按 tick 派生；物理固定步长加 accumulator；结算按稳定 id 排序；并行结果按索引合并；输入按 tick 对齐采样；AI 禁用 wall clock；统一浮点环境；丢帧补空输入；缩短快照间隔并记录首异帧；broadphase 顺序稳定化。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
