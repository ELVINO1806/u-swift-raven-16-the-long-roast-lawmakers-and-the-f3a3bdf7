import os
TEXT = "They passed a law on algorithms they cannot explain, then spent an hour asking an intern to turn the bill into a PDF."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as handle:
    handle.write(TEXT)
