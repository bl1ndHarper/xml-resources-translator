import sys

def print_status(line_num, total, text, status):
    sys.stdout.write(f"\r🔄 Line {line_num}/{total} | {status}: {text[:60]}...   ")
    sys.stdout.flush()
