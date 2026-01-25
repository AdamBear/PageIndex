import json
import sys

def print_tree(structure, indent=0, prefix=""):
    """打印树状结构"""
    for i, node in enumerate(structure):
        is_last = i == len(structure) - 1
        current_prefix = "└── " if is_last else "├── "
        print(f"{prefix}{current_prefix}{node['title']} (p.{node['start_index']}-{node['end_index']})")

        if 'nodes' in node and node['nodes']:
            child_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(node['nodes'], indent + 1, child_prefix)

# 读取结果文件
with open('results/four-lectures_structure.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"文档: {data['doc_name']}")
print(f"总节点数: {len(data['structure'])}")
print("\n树状结构:")
print_tree(data['structure'])