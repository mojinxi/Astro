import os

folder = r'C:\Astro\src\content\blog'

for filename in os.listdir(folder):
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 如果内容已经以 --- 开头，则跳过（但你的情况不是，所以会进入 else）
    if content.strip().startswith('---'):
        print(f'跳过 {filename}，已有分隔符')
        continue
    
    # 强制添加 --- 包裹
    # 注意：原内容可能没有开头的 ---，我们直接在最前面加上 --- 和换行，并在最后加上 ---
    new_content = '---\n' + content + '\n---'
    
    # 修正 date: 后面缺少空格的问题（可选，但有助于解析）
    # 将 date:2021 替换为 date: 2021
    import re
    new_content = re.sub(r'(date):(\S)', r'\1: \2', new_content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'已修复 {filename}')