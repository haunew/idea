# Word 文档处理指南 (.docx)

## 概述

Microsoft Word (.docx) 是学术论文最常用的文件格式，几乎所有期刊和高校都接受 Word 投稿。

## 使用 python-docx 处理 Word

### 安装

```bash
pip install python-docx
```

### 基本操作

#### 1. 读取文档

```python
from docx import Document

# 打开文档
doc = Document('paper.docx')

# 读取所有段落
for para in doc.paragraphs:
    print(para.text)

# 读取所有表格
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)
```

#### 2. 创建新文档

```python
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# 添加标题
title = doc.add_heading('论文标题', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 添加摘要
abstract = doc.add_heading('摘要', level=1)
p = doc.add_paragraph()
p.add_run('这里是摘要内容...').italic = True

# 添加正文
doc.add_heading('1. 引言', level=1)
doc.add_paragraph('这是引言段落...')

# 保存
doc.save('new_paper.docx')
```

#### 3. 修改现有文档

```python
from docx import Document

doc = Document('paper.docx')

# 修改段落文本
for para in doc.paragraphs:
    if '旧文本' in para.text:
        para.text = para.text.replace('旧文本', '新文本')

# 添加新段落
doc.add_paragraph('这是新增的段落')

# 在特定位置插入（需要遍历找到位置）
for i, para in enumerate(doc.paragraphs):
    if para.text.startswith('参考文献'):
        # 在参考文献前插入新段落
        doc.paragraphs[i]._element.addprevious(
            Document().add_paragraph('新增内容')._element
        )

doc.save('modified_paper.docx')
```

### 样式设置

```python
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 设置字体
run = paragraph.add_run('文本')
run.font.name = 'Times New Roman'
run.font.size = Pt(12)
run.font.bold = True
run.font.color.rgb = RGBColor(0, 0, 0)

# 段落对齐
paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 居中
paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY  # 两端对齐

# 行距
paragraph.paragraph_format.line_spacing = 1.5

# 首行缩进
paragraph.paragraph_format.first_line_indent = Inches(0.5)
```

### 处理页眉页脚

```python
# 添加页眉
header = doc.sections[0].header
header_para = header.paragraphs[0]
header_para.text = "论文标题"
header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 添加页脚（页码）
footer = doc.sections[0].footer
footer_para = footer.paragraphs[0]
footer_para.text = "第 X 页"
```

## 论文字数统计（Word 版）

```python
from docx import Document
import re

def count_words_docx(filepath):
    doc = Document(filepath)
    
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    text = '\n'.join(full_text)
    
    # 中文字符
    chinese = len(re.findall(r'[\u4e00-\u9fff]', text))
    # 英文单词
    english = len(re.findall(r'[a-zA-Z]+', text))
    
    return {
        'chinese_chars': chinese,
        'english_words': english,
        'total': chinese + english
    }

# 使用
stats = count_words_docx('paper.docx')
print(f"中文字符: {stats['chinese_chars']}")
print(f"英文单词: {stats['english_words']}")
print(f"总词数: {stats['total']}")
```

## Word 论文排版规范

### 页面设置
- **纸张**：A4 (210mm × 297mm)
- **页边距**：上下 2.54cm，左右 3.17cm（或按学校要求）
- **行距**：1.5 倍或 2 倍行距

### 字体字号

| 元素 | 中文字体 | 英文字体 | 字号 |
|------|----------|----------|------|
| 标题 | 黑体 | Arial | 二号/16pt |
| 一级标题 | 黑体 | Arial | 三号/15pt |
| 二级标题 | 楷体 | Arial | 四号/14pt |
| 正文 | 宋体 | Times New Roman | 小四/12pt |
| 图表标题 | 黑体 | Arial | 五号/10.5pt |

### 段落格式
- **对齐**：正文两端对齐，标题居中
- **缩进**：首行缩进 2 字符
- **段间距**：段前 0，段后 0 或 6pt

## 与 LaTeX 对比

| 特性 | Word | LaTeX |
|------|------|-------|
| 学习曲线 | 低 | 高 |
| 公式排版 | 一般 | 优秀 |
| 版本控制 | 困难 | 容易 |
| 协作编辑 | 方便 | 需工具支持 |
| 排版稳定性 | 易错乱 | 稳定 |
| 期刊模板 | 部分提供 | 普遍提供 |

## 推荐场景

**使用 Word：**
- 人文社科论文
- 需要频繁与他人协作修改
- 导师要求使用 Word
- 公式较少的论文

**使用 LaTeX：**
- 理工科论文（大量公式）
- 计算机科学（代码排版）
- 数学、物理等学科
- 期刊提供 LaTeX 模板
