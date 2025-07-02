import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'https?://(?:www\.)?youtube\.com/embed/(.+)"',s.strip(),re.IGNORECASE):
        return "https://youtu.be/"+match.group(1)
    else:
        return None
    

if __name__ == "__main__":
    main()
