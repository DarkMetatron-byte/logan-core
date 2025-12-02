import sys
import re
import os

VALID_SUFFIXES = [r"-un\b", r"-ta\b", r"-im\b", r"-ex\b"]
IGNORE_PATTERNS = [r"^//", r"^\[", r"^\s*$"] 

def is_valid_line(line, line_num):
    for pattern in IGNORE_PATTERNS:
        if re.search(pattern, line):
            return True, ""
    has_token = False
    for suffix in VALID_SUFFIXES:
        if re.search(suffix, line):
            has_token = True
            break
    if not has_token:
        if '"' in line and ":" in line:
            return True, ""
        return False, f"Line {line_num}: No valid LOGAN suffix found -> {line.strip()}"
    return True, ""

def lint_file(filepath):
    print(f"🔍 Linting: {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            errors = []
            for i, line in enumerate(f, 1):
                valid, msg = is_valid_line(line, i)
                if not valid:
                    errors.append(msg)
            if errors:
                print(f"❌ Found {len(errors)} errors:")
                for e in errors: print(e)
            else:
                print("✅ LOGAN Syntax Valid.")
    except FileNotFoundError:
        print(f"❌ Error: File not found: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python linter.py <path_to_file.logan>")
    else:
        lint_file(sys.argv[1])