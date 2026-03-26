#!/usr/bin/env python3
"""
论文字数统计工具
统计论文字数、段落数、各章节字数分布
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


def count_words(text: str) -> dict:
    """统计文本字数信息"""
    # 中文字符
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
    # 英文单词
    english_words = len(re.findall(r'[a-zA-Z]+', text))
    # 数字
    numbers = len(re.findall(r'\d+', text))
    # 总字符数（不含空白）
    total_chars = len(re.sub(r'\s', '', text))
    
    return {
        'chinese_chars': chinese_chars,
        'english_words': english_words,
        'numbers': numbers,
        'total_chars': total_chars,
        'estimated_words': chinese_chars + english_words  # 估算总词数
    }


def analyze_structure(text: str) -> dict:
    """分析论文结构"""
    sections = defaultdict(str)
    current_section = '前言'
    
    # 常见章节标题模式
    section_patterns = [
        r'^[\s]*(?:摘要|Abstract)',
        r'^[\s]*(?:1|一|第一章)[、.\s]+(?:引言|Introduction|绪论)',
        r'^[\s]*(?:2|二|第二章)[、.\s]+(?:文献综述|Literature Review|相关研究)',
        r'^[\s]*(?:3|三|第三章)[、.\s]+(?:研究方法|Methodology|方法)',
        r'^[\s]*(?:4|四|第四章)[、.\s]+(?:结果|Results|实验结果)',
        r'^[\s]*(?:5|五|第五章)[、.\s]+(?:讨论|Discussion)',
        r'^[\s]*(?:6|六|第六章)[、.\s]+(?:结论|Conclusion|总结)',
        r'^[\s]*(?:参考文献|References)',
        r'^[\s]*(?:致谢|Acknowledgements)',
    ]
    
    lines = text.split('\n')
    for line in lines:
        is_section_header = False
        for pattern in section_patterns:
            if re.match(pattern, line, re.IGNORECASE):
                current_section = line.strip()
                is_section_header = True
                break
        if not is_section_header:
            sections[current_section] += line + '\n'
    
    return sections


def format_number(n: int) -> str:
    """格式化数字，添加千位分隔符"""
    return f"{n:,}"


def main():
    if len(sys.argv) < 2:
        print("用法: python word_count.py <论文文件路径>")
        print("支持格式: .txt, .md, .tex")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"错误: 文件不存在 {file_path}")
        sys.exit(1)
    
    text = file_path.read_text(encoding='utf-8')
    
    # 总体统计
    stats = count_words(text)
    
    print("=" * 50)
    print(f"📄 论文统计报告: {file_path.name}")
    print("=" * 50)
    print(f"中文字符数: {format_number(stats['chinese_chars'])}")
    print(f"英文单词数: {format_number(stats['english_words'])}")
    print(f"数字个数:   {format_number(stats['numbers'])}")
    print(f"总字符数:   {format_number(stats['total_chars'])}")
    print(f"估算总词数: {format_number(stats['estimated_words'])}")
    print("=" * 50)
    
    # 结构分析
    sections = analyze_structure(text)
    if len(sections) > 1:
        print("\n📊 各章节字数分布:")
        print("-" * 50)
        for section, content in sections.items():
            section_stats = count_words(content)
            print(f"{section[:30]:<30} {format_number(section_stats['estimated_words']):>10} 词")
        print("=" * 50)


if __name__ == '__main__':
    main()
