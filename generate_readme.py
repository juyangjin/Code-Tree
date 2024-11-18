import os
from urllib.parse import quote
import re

# 복구된 헤더
HEADER = """#
# 코드트리 문제 풀이 목록
[![코드트리|실력진단-wndid2008](https://banner.codetree.ai/v1/banner/wndid2008)](https://www.codetree.ai/profiles/wndid2008)

## 🌳 코드트리 문제 목록
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

# 난이도와 이미지 링크 정의
DIFFICULTY_IMAGES = {
    "쉬움": "https://img.shields.io/badge/쉬움-%235cb85c.svg?for-the-badge",
    "보통": "https://img.shields.io/badge/보통-%23FFC433.svg?for-the-badge",
    "어려움": "https://img.shields.io/badge/어려움-%23D24D57.svg?for-the-badge"
}

# 난이도별 이모티콘
DIFFICULTY_EMOJIS = {
    "쉬움": "🟢",   # Green Circle
    "보통": "🟡",   # Yellow Circle
    "어려움": "🔴"   # Red Circle
}

def get_language_from_extension(file_name):
    """파일 확장자를 기반으로 언어 반환"""
    for language, ext in SUPPORTED_LANGUAGES.items():
        if file_name.lower().endswith(ext):
            return language
    return None

def extract_problem_difficulty(readme_path):
    """문제 폴더의 README.md에서 난이도 추출"""
    problem_difficulty = "쉬움"  # 기본 난이도는 쉬움으로 설정
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # 난이도 추출 (예: |난이도| 쉬움 |)
                if "|난이도|" in line:
                    match = re.search(r"\|난이도\| (.*?) \|", line)
                    if match:
                        problem_difficulty = match.group(1).strip()
    except Exception as e:
        print(f"Error reading {readme_path}: {e}")
    return problem_difficulty

def generate_readme():
    # 난이도별로 문제를 나누기 위한 딕셔너리
    problems_by_difficulty = {
        "쉬움": [],
        "보통": [],
        "어려움": []
    }

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
            problem_difficulty = extract_problem_difficulty(problem_readme) if os.path.exists(problem_readme) else "쉬움"

            # 난이도 이미지 링크 변환
            difficulty_image = DIFFICULTY_IMAGES.get(problem_difficulty, DIFFICULTY_IMAGES["쉬움"])

            # 날짜 및 문제 폴더
            problem_info = {
                "date": date_folder,
                "folder": problem_folder,
                "difficulty": problem_difficulty,
                "difficulty_image": difficulty_image,
                "path": problem_path
            }

            # 언어 탐색 (문제 폴더 안의 파일들을 통해 언어를 결정)
            found_language = None
            for file_name in os.listdir(problem_path):
                language = get_language_from_extension(file_name)
                if language:
                    found_language = language
                    break

            if found_language:
                problem_info["language"] = found_language
            else:
                problem_info["language"] = "알 수 없음"

            # 난이도별로 문제 분류
            problems_by_difficulty[problem_difficulty].append(problem_info)
            modified = True

    if modified:
        content = HEADER

        # 난이도별 문제 추가 (문제가 있을 경우에만 해당 난이도 섹션을 출력)
        for difficulty in ["쉬움", "보통", "어려움"]:
            if problems_by_difficulty[difficulty]:  # 해당 난이도에 문제가 있으면 출력
                # 난이도별 이모티콘 추가
                emoji = DIFFICULTY_EMOJIS[difficulty]
                content += f"### {emoji} {difficulty}\n"
                content += "| 업로드 날짜 | 문제 폴더 | 언어 | 링크 | 난이도 |\n"
                content += "| ----------- | --------- | ---- | ----- | ------- |\n"
                for problem in problems_by_difficulty[difficulty]:
                    content += f"| {problem['date']} | [{problem['folder']}]({quote(problem['path'])}) | {problem['language']} | [링크]({quote(problem['path'])}) | ![쉬움]({problem['difficulty_image']}) |\n"

        # 파일에 내용 저장
        with open("README.md", "w", encoding="utf-8") as fd:
            fd.write(content)
        print("README.md has been updated successfully.")
    else:
        print("No changes were made to README.md.")

if __name__ == "__main__":
    generate_readme()
