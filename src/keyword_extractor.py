"""Simple keyword extraction prototype for resume/JD matching."""

from collections import Counter
import re


STOPWORDS = {
    "and", "the", "for", "with", "you", "our", "are", "will", "this", "that",
    "from", "your", "have", "has", "to", "of", "in", "a", "an", "or", "as",
}


def extract_keywords(text: str, top_n: int = 30) -> list[tuple[str, int]]:
    words = re.findall(r"[A-Za-z][A-Za-z+#.]*", text.lower())
    words = [word for word in words if word not in STOPWORDS and len(word) > 2]
    return Counter(words).most_common(top_n)


if __name__ == "__main__":
    sample = "Data analyst internship requiring SQL, Python, Excel, dashboards, and stakeholder communication."
    for keyword, count in extract_keywords(sample):
        print(f"{keyword}: {count}")
