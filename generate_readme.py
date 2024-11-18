import os
from urllib.parse import quote
import re

# 복구된 헤더
HEADER = """#
# 코드트리 문제 풀이 목록
[![코드트리|실력진단-wndid2008](https://banner.codetree.ai/v1/banner/wndid2008)](https://www.codetree.ai/profiles/wndid2008)

## 🌳 코드트리 문제 목록
| 업로드 날짜 | 문제 폴더 | 파일 이름 | 언어 | 링크 | 문제 설명 |
| ----------- | --------- | --------- | ---- | ----- | --------- |
"""

SUPPORTED_LANGUAGES = {
    "Python": ".py",
    "Java": ".java",
    "C++": ".cpp",
    "JavaScript": ".js",
    "C": ".c",
    "Ruby": ".rb",
    "Go": ".go",
    "Kotlin": ".kt",
    "Swift": ".swift",
    "Rust": ".rs"
}

def get_language_from_extension(file_name):
    """파일 확장자를 기반으로 언어 반환"""
    for language, ext in SUPPORTED_LANGUAGES.items():
        if file_name.lower().endswith(ext):
            return language
    return None

def extract_problem_info(readme_path):
    """문제 폴더의 README.md에서 유형과 문제 난이도 추출"""
    problem_type = "유형 없음"
    problem_difficulty = "난이도 없음"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # 유형 및 난이도 추출 (예: |유형| Novice Low / 출력 / 변수 값 변경 |)
                if line.startswith("|유형|"):
                    match = re.search(r"\|유형\| (.*?) \|", line)
                    if match:
                        problem_type = match.group(1).strip()

                elif line.startswith("|난이도|"):
                    match = re.search(r"\|난이도\| (.*?) \|", line)
                    if match:
                        problem_difficulty = match.group(1).strip()
    except Exception as e:
        print(f"Error reading {readme_path}: {e}")
    return problem_type, problem_difficulty

def generate_readme():
    content = HEADER

    modified = False

    # 날짜 폴더 탐색
    for date_folder in sorted(os.listdir(".")):
        date_path = os.path.join(".", date_folder)
        if not date_folder.isdigit() or len(date_folder) != 6 or not os.path.isdir(date_path):
            continue

        # 날짜 폴더 안의 문제 폴더 탐색
        for problem_folder in os.listdir(date_path):
            problem_path = os.path.join(date_path, problem_folder)
            if not os.path.isdir(problem_path):  # 문제 폴더가 아니면 스킵
                continue

            problem_readme = os.path.join(problem_path, "README.md")
            problem_type, problem_difficulty = extract_problem_info(problem_readme) if os.path.exists(problem_readme) else ("유형 없음", "난이도 없음")

            # 날짜 및 문제 폴더
            content += f"| {date_folder} | [{problem_folder}]({quote(problem_path)}) | "

            # 파일 탐색
            found_files = []
            for file_name in os.listdir(problem_path):
                language = get_language_from_extension(file_name)
                if language:
                    file_path = os.path.join(problem_path, file_name)
                    found_files.append((file_name, language, file_path))

            if found_files:
                for idx, (file_name, language, file_path) in enumerate(found_files):
                    if idx == 0:
                        content += f"{file_name} | {language} | [링크]({quote(file_path)}) | {problem_type} / {problem_difficulty} |\n"
                    else:
                        content += f"| | | {file_name} | {language} | [링크]({quote(file_path)}) | |\n"
            else:
                content += "- | - | - | - |\n"

            modified = True

    if modified:
        with open("README.md", "w", encoding="utf-8") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")

if __name__ == "__main__":
    generate_readme()
