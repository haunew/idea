#!/usr/bin/env python3
"""
参考文献格式化工具
支持 GB/T 7714、APA、MLA 等格式转换
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Reference:
    """参考文献条目"""
    authors: List[str]
    year: str
    title: str
    source: str
    volume: str = ""
    issue: str = ""
    pages: str = ""
    doi: str = ""
    url: str = ""
    ref_type: str = "journal"  # journal, book, thesis, conference, online


def parse_reference(text: str) -> Optional[Reference]:
    """解析参考文献条目（简单启发式解析）"""
    # 尝试提取年份
    year_match = re.search(r'(\d{4})', text)
    year = year_match.group(1) if year_match else ""
    
    # 尝试提取作者（逗号或and/&分隔）
    author_part = text.split('.')[0] if '.' in text else text.split(',')[0]
    authors = [a.strip() for a in re.split(r',|\band\b|&', author_part) if a.strip()]
    
    # 尝试提取DOI
    doi_match = re.search(r'10\.\d{4,}/[^\s]+', text)
    doi = doi_match.group(0) if doi_match else ""
    
    # 尝试提取URL
    url_match = re.search(r'https?://[^\s]+', text)
    url = url_match.group(0) if url_match else ""
    
    return Reference(
        authors=authors,
        year=year,
        title=text,
        source="",
        doi=doi,
        url=url
    )


def format_gb7714(ref: Reference, index: int = 0) -> str:
    """格式化为 GB/T 7714 格式"""
    prefix = f"[{index}] " if index > 0 else ""
    authors = ", ".join(ref.authors)
    
    if ref.ref_type == "journal":
        return f"{prefix}{authors}. {ref.title}[J]. {ref.source}, {ref.year}, {ref.volume}({ref.issue}): {ref.pages}."
    elif ref.ref_type == "book":
        return f"{prefix}{authors}. {ref.title}[M]. {ref.source}, {ref.year}."
    elif ref.ref_type == "thesis":
        return f"{prefix}{authors}. {ref.title}[D]. {ref.source}, {ref.year}."
    else:
        return f"{prefix}{authors}. {ref.title}. {ref.source}, {ref.year}."


def format_apa(ref: Reference) -> str:
    """格式化为 APA 格式"""
    authors = ", ".join(ref.authors)
    if len(ref.authors) > 2:
        authors = ", ".join(ref.authors[:-1]) + ", & " + ref.authors[-1]
    
    base = f"{authors} ({ref.year}). {ref.title}"
    
    if ref.ref_type == "journal":
        base += f". {ref.source}, {ref.volume}({ref.issue}), {ref.pages}."
        if ref.doi:
            base += f" https://doi.org/{ref.doi}"
    else:
        base += f". {ref.source}."
    
    return base


def format_mla(ref: Reference) -> str:
    """格式化为 MLA 格式"""
    authors = ", ".join(ref.authors)
    
    if ref.ref_type == "journal":
        return f'"{ref.title}." {ref.source}, vol. {ref.volume}, no. {ref.issue}, {ref.year}, pp. {ref.pages}.'
    else:
        return f"{authors}. {ref.title}. {ref.source}, {ref.year}."


def process_bib_file(input_path: Path, output_format: str = "gb7714") -> str:
    """处理参考文献文件"""
    text = input_path.read_text(encoding='utf-8')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    results = []
    for i, line in enumerate(lines, 1):
        ref = parse_reference(line)
        if ref:
            if output_format == "gb7714":
                results.append(format_gb7714(ref, i))
            elif output_format == "apa":
                results.append(format_apa(ref))
            elif output_format == "mla":
                results.append(format_mla(ref))
            else:
                results.append(line)
        else:
            results.append(line)
    
    return '\n'.join(results)


def main():
    if len(sys.argv) < 2:
        print("用法: python bib_formatter.py <参考文献文件> [格式]")
        print("格式选项: gb7714 (默认), apa, mla")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    output_format = sys.argv[2] if len(sys.argv) > 2 else "gb7714"
    
    if not input_path.exists():
        print(f"错误: 文件不存在 {input_path}")
        sys.exit(1)
    
    result = process_bib_file(input_path, output_format)
    
    # 输出到文件
    output_path = input_path.with_suffix(f'.{output_format}.txt')
    output_path.write_text(result, encoding='utf-8')
    
    print(f"格式化完成！")
    print(f"格式: {output_format.upper()}")
    print(f"输出文件: {output_path}")
    print("\n预览:")
    print("-" * 50)
    print(result[:1000] + "..." if len(result) > 1000 else result)


if __name__ == '__main__':
    main()
