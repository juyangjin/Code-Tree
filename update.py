#!/usr/bin/env python

import os
from urllib import parse
import subprocess

HEADER = """#
# 코드트리 문제 풀이 목록

코드트리 실력진단  
[![코드트리 실력진단](https://banner.codetree.ai/v1/banner/wndid2008)](https://www.codetree.ai/profiles/wndid2008)

"""

def generate_readme():
    content = ""
    content += HEADER
    content += "## 🌳 코드트리 문제 목록\n"
    content += "| 업로드 날짜 | 문제 이름 | 링크 |\n"
    content += "| ---------- | -------- | ---- |\n"

    for root, dirs, files in os.walk("."):
        dirs.sort()

        # 최상위 폴더 제외
        if root == ".":
            continue

        # 업로드 날짜(6자리 숫자) 폴더인지 확인
        parent_dir = os.path.basename(root)
        if not parent_dir.isdigit() or len(parent_dir) != 6:
            continue

        # 문제 이름(하위 디렉토리) 탐색
        for sub_dir in dirs:
            problem_dir = os.path.join(root, sub_dir)
            for file in os.listdir(problem_dir):
                if file.endswith(('.py', '.cpp', '.java', '.txt')):  # 파일 필터링
                    file_path = os.path.join(problem_dir, file)
                    content += "| {} | {} | [링크]({}) |\n".format(
                        parent_dir, sub_dir, parse.quote(file_path)
                    )

    # README.md 파일 생성
    with open("README.md", "w") as fd:
        fd.write(content)

def git_commit_and_push():
    try:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "Update CodeTree problem list"], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Git 명령어 실패: {e}")

if __name__ == "__main__":
    generate_readme()
    git_commit_and_push()
