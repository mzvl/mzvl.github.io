import os
import json
from datetime import datetime

MD_DIR = 'p'
OUTPUT_FILE = 'list.json'

def get_md_list():
    result = []
    for fname in os.listdir(MD_DIR):
        if fname.lower().endswith('.md'):
            path = os.path.join(MD_DIR, fname)
            mtime = os.path.getmtime(path)
            date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            result.append([fname, date_str])
    result.sort(key=lambda x: x[1], reverse=True)  # 按日期降序
    return result

def write_json(data):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    md_list = get_md_list()
    write_json(md_list)
    print(f'{OUTPUT_FILE} updated with {len(md_list)} entries.')
