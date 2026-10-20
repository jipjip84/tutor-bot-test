"""Build tutorbot.html by inlining the course data into src/app.html."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
from course import build  # noqa: E402

data = json.dumps(build(), ensure_ascii=False).replace("</", "<\\/")
html = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
(ROOT / "tutorbot.html").write_text(html.replace("__COURSE_JSON__", data), encoding="utf-8")
print("Wrote tutorbot.html")
