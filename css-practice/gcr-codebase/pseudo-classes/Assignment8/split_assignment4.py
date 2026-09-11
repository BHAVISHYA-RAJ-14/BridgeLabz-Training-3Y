import re
from pathlib import Path

base = Path(r"c:\Users\BHAVISHYA RAJ\Desktop\BridgeLabz-Training-3Y\css-practice\gcr-codebase\pseudo-classes\Assignment8")
sol_file = base / "sol.html"
combined_file = base / "all-questions.html"

if combined_file.exists():
    combined_file.unlink()
    print(f"Removed: {combined_file.name}")

text = sol_file.read_text(encoding="utf-8").replace("\r\n", "\n")

if 'content = """' in text:
    text = text.split('content = """', 1)[1]
    if text.endswith('"""'):
        text = text[:-3]

text = re.sub(r"\n\s*[-]{3,}\s*\n", "\n", text)

pattern = re.compile(r"(?ms)^###\s*(\d+)\.\s*([^\n]+)\s*\n(.*?)(?=^###\s*\d+\.\s*|\Z)")

created = []
for _, file_name, content in pattern.findall(text):
    safe_name = file_name.strip()
    body = content.strip()
    if not safe_name:
        continue
    (base / safe_name).write_text(body + "\n", encoding="utf-8")
    created.append(safe_name)
    print(f"Created: {safe_name}")

print("Done. Files created:", ", ".join(created))