import os
from urllib import parse

HEADER = """#
# 코드트리 문제 풀이 목록
[![코드트리|실력진단-wndid2008](https://banner.codetree.ai/v1/banner/wndid2008)](https://www.codetree.ai/profiles/wndid2008)
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
        if file_name.endswith(ext):
            return language
    return None

def extract_problem_description(readme_path):
    """문제 폴더의 README.md에서 문제 설명 추출"""
    problem_description = ""
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("# "):  # 문제 제목
                    problem_description += line.replace("# ", "").strip() + " "
                if line.startswith("|유형|"):  # 표 시작
                    problem_description += "\n" + "".join(lines[lines.index(line):])
                    break
    except Exception as e:
        print(f"Error reading {readme_path}: {e}")
    return problem_description.strip()

def generate_readme():
    content = HEADER
    content += "## 🌳 코드트리 문제 목록\n"
    content += "| 업로드 날짜 | 문제 폴더 | 파일 이름 | 언어 | 링크 | 문제 설명 |\n"
    content += "| ----------- | --------- | --------- | ---- | ----- | --------- |\n"

    modified = False

    # 날짜 폴더를 탐색
    for date_folder in sorted(os.listdir(".")):
        if not date_folder.isdigit() or len(date_folder) != 6:
            continue

        date_path = os.path.join(".", date_folder)

        # 문제 폴더 탐색
        for problem_folder in os.listdir(date_path):
            problem_path = os.path.join(date_path, problem_folder)
            if not os.path.isdir(problem_path):
                continue

            problem_readme = os.path.join(problem_path, "README.md")
            problem_description = extract_problem_description(problem_readme) if os.path.exists(problem_readme) else "문제 설명 없음"

            # 날짜 및 문제 폴더
            content += f"| {date_folder} | [{problem_folder}]({parse.quote(problem_path)}) | "

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
                        content += f"{file_name} | {language} | [링크]({parse.quote(file_path)}) | {problem_description} |\n"
                    else:
                        content += f"| | | {file_name} | {language} | [링크]({parse.quote(file_path)}) | |\n"
            else:
                content += "- | - | - | - |\n"

            modified = True

    if modified:
        with open("README.md", "w", encoding="utf-8") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")
