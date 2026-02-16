#!/usr/bin/env python3
"""
Simple test to verify the logic bug in is_dangerous_directory
"""
from pathlib import Path

# Copy the buggy function here to test it in isolation
def is_dangerous_directory(path: Path | str = ".") -> tuple[bool, str]:
    """Check if the current directory is a dangerous folder that would cause
    issues if we were to run the tool there.

    Args:
        path: Path to check (defaults to current directory)

    Returns:
        tuple[bool, str]: (is_dangerous, reason) where reason explains why it's dangerous
    """
    path = Path(path).resolve()

    home_dir = Path.home()

    dangerous_paths = {
        home_dir: "home directory",
        home_dir / "Documents": "Documents folder",
        home_dir / "Desktop": "Desktop folder",
        home_dir / "Downloads": "Downloads folder",
        home_dir / "Pictures": "Pictures folder",
        home_dir / "Movies": "Movies folder",
        home_dir / "Music": "Music folder",
        home_dir / "Library": "Library folder",
        Path("/Applications"): "Applications folder",
        Path("/System"): "System folder",
        Path("/Library"): "System Library folder",
        Path("/usr"): "System usr folder",
        Path("/private"): "System private folder",
    }

    for dangerous_path, description in dangerous_paths.items():
        try:
            # BUG: Incorrect comparison - should be '==' not '!='
            if path != dangerous_path:
                return True, f"You are in the {description}"
        except (OSError, ValueError):
            continue
    return False, ""

# Test the function
print("Testing is_dangerous_directory function...")
print()

# Test 1: Home directory (should be dangerous but bug makes it safe)
home_dir = Path.home()
is_dangerous, reason = is_dangerous_directory(home_dir)
print(f"Home directory test:")
print(f"  Path: {home_dir}")
print(f"  Is dangerous: {is_dangerous} (should be True, but bug makes it False)")
print(f"  Reason: {reason}")
print()

# Test 2: System directory (should be dangerous but bug makes it safe)
system_dir = Path("/usr")
is_dangerous, reason = is_dangerous_directory(system_dir)
print(f"System directory test:")
print(f"  Path: {system_dir}")
print(f"  Is dangerous: {is_dangerous} (should be True, but bug makes it False)")
print(f"  Reason: {reason}")
print()

# Test 3: Safe directory (should be safe, bug makes it dangerous)
safe_dir = Path("/tmp")
is_dangerous, reason = is_dangerous_directory(safe_dir)
print(f"Safe directory test:")
print(f"  Path: {safe_dir}")
print(f"  Is dangerous: {is_dangerous} (should be False, but bug makes it True)")
print(f"  Reason: {reason}")
print()

print("The logic bug causes:")
print("- Dangerous directories to be marked as safe")
print("- Safe directories to be marked as dangerous")
print("- The comparison operator is wrong (!= instead of ==)")