# CTF_Challenges_Organizer

A small Python utility for organizing Capture The Flag challenge files into category folders.

## What it does

- Scans a base directory of challenge files
- Detects the category of each file using extension mapping
- Optionally inspects file headers for common challenge file formats
- Moves files into category folders such as `reverse`, `crypto`, `web`, `pwn`, `forensics`, `misc`, and `uncategorized`

## Categories

The script currently supports these categories:

- `reverse`
- `crypto`
- `web`
- `pwn`
- `forensics`
- `misc`
- `uncategorized`

## Installation

This script only depends on the Python standard library.

```bash
python3 --version
```

## Usage

Run the script from the repository directory, passing the base folder containing challenge files:

```bash
python3 file_manager.py /path/to/challenge/folder
```

The script will create category folders inside the provided directory and move files into the appropriate folders.

## Example

```bash
python3 file_manager.py ./challenges
```

If a file cannot be categorized automatically, the script prompts for a category choice.

## Notes

- The script currently uses extension-based detection first.
- It also inspects file headers for a few known binary formats such as ELF and PCAP.
- Files already inside category folders are skipped.

## Future improvements

- Add a `--dry-run` mode to preview changes without moving files
- Improve detection with more file signatures and metadata
- Add configuration support for custom categories and extensions
- Add logging and error handling for safer operation
- Add recursive folder scanning

## License

This repository is released under the MIT License. Feel free to adapt it for your own CTF workflow.
