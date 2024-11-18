import os

def generate_readme():
    content = "# 코드트리 문제 풀이 목록\n"
    content += "| 날짜 | 문제 폴더 | 파일 이름 | 링크 |\n"
    content += "| ---- | -------- | -------- | ---- |\n"

    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".java", ".js")):
                file_path = os.path.join(root, file)
                content += f"| {root} | {file} | [링크]({file_path}) |\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
        print("README.md updated.")

if __name__ == "__main__":
    generate_readme()
