# Idea - 未来展望与学术研究

> 记录灵感、规划发展、沉淀思考，将零散的想法转化为系统的学术成果。

---

## 📁 目录结构

```
idea/
├── README.md                    # 本文件
├── academic-paper-writing/      # 论文写作 Skill
│   ├── SKILL.md                 # Skill 核心文档
│   ├── references/              # 参考资料
│   │   ├── citation-formats.md      # 引用格式指南
│   │   ├── docx-guide.md            # Word 文档处理
│   │   ├── paper-discussion-tips.md # 论文讨论技巧
│   │   └── paper-writing-en.md      # 英文写作指南
│   ├── scripts/                 # 实用脚本
│   │   ├── bib_formatter.py         # 参考文献格式化
│   │   ├── docx_word_count.py       # Word 字数统计
│   │   └── word_count.py            # 文本字数统计
│   └── assets/                  # 模板资源
│
└── future-vision/               # 未来展望与想法记录
    ├── README.md                # 使用指南
    ├── README-EN.md             # 英文版指南
    ├── ideas/                   # 想法与灵感
    │   ├── 2026-03-26-wireless-power-transmission.md
    │   ├── 2026-03-26-wireless-power-vision-v2.md
    │   ├── 2026-03-26-ambient-energy-direct-drive.md
    │   ├── 2026-03-26-aedd-ai-autonomy.md
    │   ├── 2026-03-26-global-energy-web-ai-civilization.md
    │   └── template-idea.md
    ├── research/                # 研究方向与论文
    │   ├── the-energy-civilization-paper.md      ⭐ 完整论文
    │   ├── ambient-energy-direct-drive-paper.md
    │   ├── aedd-ai-singularity-paper.md
    │   ├── global-energy-web-civilization-paper.md
    │   ├── wireless-power-network-research.md
    │   ├── wireless-power-future-paper.md
    │   └── template-research.md
    ├── goals/                   # 目标规划
    ├── reflections/             # 反思总结
    └── inspiration/             # 外部灵感
```

---

## 🌟 核心内容：能源文明论文系列

### 完整论文（推荐）

| 论文 | 主题 | 字数 |
|------|------|------|
| **[能源文明：从AEDD到星际社会](future-vision/research/the-energy-civilization-paper.md)** ⭐ | 三大支柱整合完整版 | ~22KB |

### 系列论文

| 论文 | 核心内容 | 状态 |
|------|---------|------|
| [AEDD技术原理](future-vision/research/ambient-energy-direct-drive-paper.md) | 环境能量直驱技术 | 完成 |
| [AEDD与AI自主](future-vision/research/aedd-ai-singularity-paper.md) | AI自主进化与奇点 | 完成 |
| [全球能量网络](future-vision/research/global-energy-web-civilization-paper.md) | 五层架构基础设施 | 完成 |

### 核心洞察

**能源文明三大支柱**：

```
AEDD（环境能量直驱）
    ↓ 使AI获得独立生存能力
GEW（全球能量网络）
    ↓ 提供泛在能源基础设施
EAS（能源自主系统）
    ↓ 实现星际开荒能力
    
结果：人类文明从0.7级跃迁到I型文明
```

**文明跃迁时间线**：
- 2025年：0.73级 → AEDD技术成熟
- 2030年：0.75级 → GEW开始建设
- 2040年：0.85级 → EAS在火星验证
- 2050年：0.95级 → GEW全球覆盖
- 2060年：1.0级  → **I型文明达成** 🎯

---

## 🛠️ 论文写作 Skill

位于 `academic-paper-writing/`，提供：

- **引用格式管理**：GB/T 7714、APA、MLA 等
- **Word 文档处理**：python-docx 指南和脚本
- **论文讨论技巧**：5个关键问题框架
- **字数统计工具**：支持 .txt、.md、.docx

使用方式：
```bash
# 统计 Word 论文字数
python academic-paper-writing/scripts/docx_word_count.py paper.docx

# 格式化参考文献
python academic-paper-writing/scripts/bib_formatter.py refs.txt gb7714
```

---

## 📝 使用流程

```
灵感/想法 → 记录到 ideas/ → 讨论完善 → 归纳到 research/ → 论文输出
```

1. **有灵感时**：在 `future-vision/ideas/` 创建新文件，快速记录
2. **想深入时**：在 `future-vision/research/` 展开论述，构建框架
3. **讨论后**：更新状态，整理结论
4. **成体系时**：使用 `academic-paper-writing` skill 输出正式论文

---

## 📄 文件命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 日期记录 | `YYYY-MM-DD-keyword.md` | `2026-03-26-ai-education.md` |
| 主题记录 | `topic-keyword.md` | `topic-machine-learning.md` |
| 论文草稿 | `draft-topic.md` | `draft-neural-networks.md` |

---

## 🌐 语言支持

- **中文**：主要记录和写作语言
- **English**：部分模板和论文提供英文版
- **bilingual**：双语并行记录

---

## 📚 参考资源

- [论文讨论技巧](academic-paper-writing/references/paper-discussion-tips.md)
- [引用格式指南](academic-paper-writing/references/citation-formats.md)
- [Word 处理指南](academic-paper-writing/references/docx-guide.md)

---

*创建时间：2026-03-26*
*最后更新：2026-03-26*
