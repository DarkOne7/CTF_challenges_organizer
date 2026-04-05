import os
import shutil
import argparse


BASE_DIR = "."

parser = argparse.ArgumentParser(description="Organize CTF challenge files into categories.")
parser.add_argument("base_dir", default=BASE_DIR, help="Base directory for the challenges.")
BASE_DIR = parser.parse_args().base_dir

CATEGORIES = ["reverse", "crypto", "web", "pwn", "forensics", "misc", "uncategorized"]

# extension-based detection
EXTENSION_MAP = {
    "reverse": [".exe", ".elf", ".bin", ".out"],
    "crypto": [".enc", ".pem", ".der"],
    "web": [".php", ".html", ".js"],
    "forensics": [".pcap", ".pcapng", ".dd", ".img", ".mem"],
    "misc": [".txt", ".md"]
}

def detect_by_extension(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, exts in EXTENSION_MAP.items():
        if ext in exts:
            return category
    return None

def detect_by_content(filepath):
    try:
        with open(filepath, "rb") as f:
            header = f.read(8)

        # ELF binary
        if header.startswith(b"\x7fELF"):
            return "reverse"

        # ZIP 
        if header.startswith(b"PK"):
            return None  # zip files could be anything

        # PCAP
        if header.startswith(b"\xd4\xc3\xb2\xa1") or header.startswith(b"\xa1\xb2\xc3\xd4"):
            return "forensics"

        # PNG (maybe stego)
        if header.startswith(b"\x89PNG"):
            return "misc"

    except:
        pass

    return None

def ask_user(item_name):
    print(f"\n[?] Could not categorize: {item_name}")
    print("Choose category:")
    for c, category in enumerate(CATEGORIES):
        print(f"{c + 1}. {category}")

    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)
        
        except:
            pass

        print("Invalid choice, try again.")

def get_category(item_path, item_name):
    # try extension
    category = detect_by_extension(item_name)
    if category:
        return category
    
     # try content (only for files)
    if os.path.isfile(item_path):
        category = detect_by_content(item_path)
        if category:
            return category

    # ask user
    return ask_user(item_name)

def organize():
    for item in os.listdir(BASE_DIR):
        item_path = os.path.join(BASE_DIR, item)

        if not os.path.exists(item_path):
            continue

        # skip already categorized folders
        if item in CATEGORIES:
            continue

        category = get_category(item_path, item)

        target_dir = os.path.join(BASE_DIR, category)
        os.makedirs(target_dir, exist_ok=True)

        target_path = os.path.join(target_dir, item)

        print(f"[+] Moving {item} -> {category}/")
        shutil.move(item_path, target_path)

if __name__ == "__main__":
    organize()