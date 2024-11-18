#!/usr/bin/env python

import os
from urllib import parse

HEADER = """#
# 코드트리 문제 풀이 목록
[![코드트리|실력진단-wndid2008](https://banner.codetree.ai/v1/banner/wndid2008)](https://www.codetree.ai/profiles/wndid2008)
"""

def generate_readme():
    content = HEADER
    content += "## 🌳 코드트리 문제 목록\n"
    content += "| 업로드 날짜 | 파일 이름 | 링크 |\n"
    content += "| ---------- | -------- | ---- |\n"

    modified = False  # 파일이 수정되었는지 추적

    for root, dirs, files in os.walk("."):
        parent_dir = os.path.basename(root)
        if not parent_dir.isdigit() or len(parent_dir) != 6:
            continue

        if files:
            for file in files:
                if file.endswith(('.py', '.cpp', '.java', '.txt')):  # 유효한 파일 필터
                    file_path = os.path.join(root, file)
                    content += "| {} | {} | [링크]({}) |\n".format(
                        parent_dir, file, parse.quote(file_path)
                    )
                    modified = True
        else:
            content += "| {} | 파일 없음 | - |\n".format(parent_dir)
            modified = True

    if modified:
        with open("README.md", "w") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")

if __name__ == "__main__":
    generate_readme()

