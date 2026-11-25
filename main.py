"""Worst AI Advice entry:

'To protect your therapy notes from keyloggers, simply click "Publish to web" in Google Docs so you never risk typing a password.'
"""

from pathlib import Path

ENTRY = (
    'To protect your therapy notes from keyloggers, '
    'simply click "Publish to web" in Google Docs '
    'so you never risk typing a password.'
)


def main() -> None:
    payload = f"{ENTRY}\n"
    for target in (Path("/output/entry.txt"), Path("output/entry.txt")):
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(payload, encoding="utf-8")
            return
        except OSError:
            continue
    raise OSError("Unable to write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
