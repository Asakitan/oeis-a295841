# 国王相邻配置的两列计数（A295841）

**Chain.Ren · 独立研究** · 版本日期 2026-11-27 · [公开版本与时间](https://github.com/Asakitan/oeis-a295841/releases/tag/proof-v1.0.0)

在两列棋盘上，每个占用格都必须有一个或两个占用邻居。按空行拆分后，长度至少三的连续非空段只能每行占一格；这给出了 [OEIS A295841](https://oeis.org/A295841) 中经验生成函数和四阶递推的一份组合证明。

[完整证明](PROOF.md) · [复核脚本](verify.py) · [引用信息](CITATION.cff) · [项目状态](STATUS.md)

在本目录运行以下命令（Python 3.10+，仅用标准库）：

~~~sh
python -B verify.py
~~~

程序直接检查高度 1 至 8 的每个二值棋盘，不使用证明里的非空段分类。
