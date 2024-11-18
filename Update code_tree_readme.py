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

        # 문제 폴더 안에서 .py 파일과 README.md 찾기
        problem_folder_found = False  # 문제 폴더의 존재 여부
        problem_description = ""  # 문제 설명을 저장할 변수

        for file in files:
            if file == "README.md":  # 문제 폴더 내 README.md
                problem_folder_found = True
                # 문제 폴더 내 README.md 파일에서 설명을 읽어옵니다.
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    problem_description = "\n".join(lines[:5])  # 첫 5줄만 읽어오거나 적절히 조정
                break
            if file.endswith(".py"):  # .py 파일이 있으면 문제 폴더가 있다는 표시
                problem_folder_found = True

        # 문제 폴더가 있을 경우
        if problem_folder_found:
            # 원 폴더 이름을 사용하여 문제 폴더명을 표시하고, 해당 폴더로의 링크를 추가
            folder_name = os.path.basename(root)  # 폴더 이름을 그대로 사용
            folder_link = parse.quote(os.path.join(root, "README.md"))

            content += "| {} | [{}](#{}) | ".format(parent_dir, folder_name, folder_name)

            # .py 파일 및 README.md 추가
            for file in files:
                if file.endswith(".py"):  # .py 파일 목록 추가
                    file_path = os.path.join(root, file)
                    content += "{} | [링크]({}) |\n".format(
                        file, parse.quote(file_path)
                    )
                if file == "README.md":  # README.md 링크 추가
                    file_path = os.path.join(root, file)
                    content += "README | [링크]({}) |\n".format(
                        parse.quote(file_path)
                    )
            
            # 문제 설명 추가 (README.md에서 추출한 내용)
            content += "| {} |\n".format(problem_description)

            modified = True
        else:
            # 파일이 없거나 문제 폴더가 없으면 "파일 없음" 표시
            content += "| {} | 파일 없음 | - | - |\n".format(parent_dir)
            modified = True

    if modified:
        with open("README.md", "w") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")

if __name__ == "__main__":
    generate_readme()
