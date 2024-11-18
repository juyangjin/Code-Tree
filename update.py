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
    return None  # 지원하지 않는 확장자

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

    for root, dirs, files in os.walk("."):
        parent_dir = os.path.basename(root)
        if not parent_dir.isdigit() or len(parent_dir) != 6:
            continue

        for folder in dirs:
            problem_path = os.path.join(root, folder)
            problem_readme = os.path.join(problem_path, "README.md")
            problem_description = extract_problem_description(problem_readme) if os.path.exists(problem_readme) else "문제 설명 없음"

            content += f"| {parent_dir} | [{folder}]({parse.quote(problem_path)}) | "

            # 지원 언어 파일 추가
            found_files = []
            for file_name in os.listdir(problem_path):
                language = get_language_from_extension(file_name)
                if language:
                    file_path = os.path.join(problem_path, file_name)
                    found_files.append((file_name, language, file_path))

            if found_files:
                for idx, (file_name, language, file_path) in enumerate(found_files):
                    # 첫 줄에는 문제 설명을 포함, 이후는 빈칸으로 처리
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
