#!/usr/bin/env python

import os
from urllib import parse

HEADER = """#
# 코드트리 문제 풀이 목록
"""

def generate_readme():
    content = HEADER
    content += "## 🌳 코드트리 문제 목록\n"
    content += "| 업로드 날짜 | 파일 이름 | 링크 |\n"
    content += "| ---------- | -------- | ---- |\n"

    for root, dirs, files in os.walk("."):
        # 현재 디렉토리가 날짜 형식의 디렉토리인지 확인
        parent_dir = os.path.basename(root)
        if not parent_dir.isdigit() or len(parent_dir) != 6:
            continue  # 6자리 숫자가 아니면 스킵

        # 파일 목록 정리
        if files:
            for file in files:
                if file.endswith(('.py', '.cpp', '.java', '.txt')):  # 유효한 파일 필터
                    file_path = os.path.join(root, file)
                    content += "| {} | {} | [링크]({}) |\n".format(
                        parent_dir, file, parse.quote(file_path)
                    )
        else:
            # 파일이 없는 경우
            content += "| {} | 파일 없음 | - |\n".format(parent_dir)

    # README.md 파일 생성
    with open("README.md", "w") as fd:
        fd.write(content)
    print("README.md has been updated successfully.")

if __name__ == "__main__":
    generate_readme()
