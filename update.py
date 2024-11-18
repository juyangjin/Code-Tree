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
    content += "| 업로드 날짜 | 문제 폴더 | 파일 이름 | 링크 | 문제 설명 |\n"
    content += "| ---------- | --------- | --------- | ---- | --------- |\n"

    modified = False  # 파일이 수정되었는지 추적

    # 날짜 폴더(6자리 숫자) 내의 문제 폴더 탐색
    for root, dirs, files in os.walk("."):
        parent_dir = os.path.basename(root)
        # 6자리 숫자 날짜 폴더만 선택
        if not parent_dir.isdigit() or len(parent_dir) != 6:
            continue

        problem_folder_found = False  # 문제 폴더의 존재 여부
        problem_description = ""  # 문제 설명을 저장할 변수

        # 날짜 폴더 내의 문제 폴더 탐색
        for dir in dirs:
            # 문제 폴더가 있는지 확인
            problem_folder = os.path.join(root, dir)
            if os.path.isdir(problem_folder):
                problem_folder_found = True
                problem_description = ""  # 문제 설명을 초기화

                # 문제 폴더 내 README.md 파일에서 설명을 읽어옵니다.
                for file in os.listdir(problem_folder):
                    if file == "README.md":
                        with open(os.path.join(problem_folder, file), "r", encoding="utf-8") as f:
                            lines = f.readlines()
                            problem_description = "\n".join(lines[:5])  # 첫 5줄만 읽어오거나 적절히 조정
                        break

                # 문제 폴더 이름을 폴더 이름 그대로 사용
                folder_name = os.path.basename(problem_folder)
                folder_link = parse.quote(os.path.join(problem_folder, "README.md"))

                content += "| {} | [{}](#{}) | ".format(parent_dir, folder_name, folder_name)

                # .py 파일 목록 추가
                for file in os.listdir(problem_folder):
                    if file.endswith(".py"):  # .py 파일이 있을 경우
                        file_path = os.path.join(problem_folder, file)
                        content += "{} | [링크]({}) |\n".format(
                            file, parse.quote(file_path)
                        )
                    if file == "README.md":  # 문제 설명이 담긴 README.md 파일도 링크로 추가
                        file_path = os.path.join(problem_folder, file)
                        content += "README.md | [링크]({}) |\n".format(
                            parse.quote(file_path)
                        )

                # 문제 설명 추가
                content += "| {} |\n".format(problem_description)

                modified = True

        if not problem_folder_found:
            content += "| {} | 파일 없음 | - | - | - |\n".format(parent_dir)
            modified = True

    if modified:
        with open("README.md", "w") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")

if __name__ == "__main__":
    generate_readme()
