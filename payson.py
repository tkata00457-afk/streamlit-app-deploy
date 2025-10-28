import sys
from datetime import datetime

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(f"Hello, {name}!")
    print(f"実行中のPython: {sys.executable}")
    print(f"バージョン: {sys.version.split()[0]}")
    print(f"時刻: {datetime.now():%Y-%m-%d %H:%M:%S}")

if __name__ == "__main__":
    main()