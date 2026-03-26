---
name: academic-paper-writing
description: Comprehensive academic paper writing support including paper structure planning, literature review, methodology design, citation format management (APA/MLA/GB/T 7714), Word document processing, and paper discussion framework. Use when Kimi needs to help with academic paper writing, thesis writing, research reports, or any scholarly document creation.
---

# Academic Paper Writing

This skill provides comprehensive guidance for academic paper writing.

## Core Capabilities

### 1. Paper Structure Planning

**Standard Academic Paper Structure**:

```
Title
├── Abstract (200-300 words)
│   ├── Background (1-2 sentences)
│   ├── Methods (1-2 sentences)
│   ├── Results (2-3 sentences)
│   └── Conclusion (1-2 sentences)
│
├── Introduction
│   ├── Research background
│   ├── Literature review
│   ├── Research gap
│   ├── Research questions
│   └── Paper structure
│
├── Methods
│   ├── Research design
│   ├── Data collection
│   ├── Analysis methods
│   └── Ethical considerations
│
├── Results
│   ├── Objective presentation
│   ├── Tables and figures
│   └── Statistical analysis
│
├── Discussion
│   ├── Interpretation of results
│   ├── Comparison with literature
│   ├── Limitations
│   └── Future directions
│
├── Conclusion
│   ├── Main findings
│   ├── Theoretical contributions
│   └── Practical implications
│
└── References
```

### 2. Citation Format Management

**Common Citation Formats**:

| Format | Field | Example |
|--------|-------|---------|
| **APA 7th** | Social sciences | (Author, Year) |
| **MLA 9th** | Humanities | (Author Page) |
| **Chicago 17th** | History | Footnotes |
| **IEEE** | Engineering | [Number] |
| **GB/T 7714** | Chinese standards | [Number] |

**Quick Reference**: See [references/citation-formats.md](references/citation-formats.md)

### 3. Word Document Processing

**Using python-docx**:

```python
# Installation
pip install python-docx

# Read document
from docx import Document
doc = Document('paper.docx')

# Count words
total = sum(len(p.text) for p in doc.paragraphs)

# Modify content
for para in doc.paragraphs:
    if 'old text' in para.text:
        para.text = para.text.replace('old text', 'new text')

# Save
doc.save('modified_paper.docx')
```

**Scripts**:
- `scripts/word_count.py`: Count words in text files
- `scripts/docx_word_count.py`: Count words in Word documents
- `scripts/bib_formatter.py`: Format bibliography

### 4. Paper Discussion Framework

**5 Key Questions for Paper Development**:

1. **Technical Path Priority**
   - Near-term / Mid-term / Long-term?
   - Which path has the most potential?

2. **Core Argument Sharpness**
   - Gentle evolution vs. paradigm revolution?
   - How to balance rigor and impact?

3. **Counter-argument Response**
   - What are the main objections?
   - How to proactively acknowledge limitations?

4. **Killer Application Scenario**
   - Which scenario best illustrates the vision?
   - Most relatable to readers?

5. **Paper Positioning**
   - Review / Opinion / Technical / Predictive?
   - Target journal and audience?

**Common Pitfalls**:

| Pitfall | Solution |
|---------|----------|
| Jargon overload | Every term needs plain explanation |
| Over-promising | Use conditional statements and timelines |
| Ignoring limitations | Proactive Limitations section |
| Lack of comparison | Now vs. Future comparison tables |

## Writing Tips

### Title Writing
- Accurately summarize research content
- Avoid abbreviations and jargon
- Keep within 15-20 words

### Abstract Writing
- Background (1-2 sentences)
- Methods (1-2 sentences)
- Main results (2-3 sentences)
- Conclusion/Significance (1-2 sentences)

### Introduction Structure (Funnel)
1. Broad context → 2. Field status → 3. Research gap → 4. Research purpose → 5. Contributions

### Methods Section
- Sufficient detail for replication
- Use past tense
- State ethical approval (if human/animal subjects)
- Specify software versions

### Results vs. Discussion
- **Results**: Report facts only, no interpretation
- **Discussion**: Explain meaning, compare with literature, acknowledge limitations

## Journal Types and Requirements

| Type | Characteristics | Structure Focus |
|------|-----------------|-----------------|
| **Empirical Research** | Original data | IMRaD |
| **Review** | Systematic summary | Introduction-Literature-Discussion-Conclusion |
| **Methods Paper** | New method/tool | Method details, validation |
| **Case Study** | Specific instance | Background-Case-Analysis-Implications |
| **Theoretical Paper** | Conceptual framework | Literature-Theory building-Discussion |

## Bilingual Recording Tips

| Scenario | Recommendation |
|----------|---------------|
| Chinese native thinking | Record in Chinese first, translate when needed |
| English paper preparation | Use English templates directly |
| International collaboration | Use bilingual tags, parallel recording |
| Final paper output | Choose language based on target journal |

## Scripts Usage

```bash
# Count words in Word document
python scripts/docx_word_count.py paper.docx

# Format bibliography
python scripts/bib_formatter.py refs.txt apa

# Count words in text file
python scripts/word_count.py paper.txt
```

---

*Created: 2026-03-26*
*Version: v1.0 (English)*
