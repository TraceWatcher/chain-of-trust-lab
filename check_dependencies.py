from pathlib import Path
import re
import sys

ALLOWED_PACKAGES = {"requests"}

for line in Path("requirements.txt").read_text().splitlines():
    line = line.strip()

    if not line or line.startswith("#"):
        continue

    match = re.fullmatch(
        r"([A-Za-z0-9_.-]+)==([A-Za-z0-9_.!+*-]+)",
        line
    )

    if not match:
        print(f"[BLOCKED] Unsupported requirement: {line}")
        sys.exit(1)

    package = re.sub(r"[-_.]+", "-", match.group(1)).lower()

    if package not in ALLOWED_PACKAGES:
        print(f"[BLOCKED] Untrusted dependency: {package}")
        sys.exit(1)

    print(f"[OK] Approved dependency: {package}")

print("[PASS] Dependency policy satisfied")
