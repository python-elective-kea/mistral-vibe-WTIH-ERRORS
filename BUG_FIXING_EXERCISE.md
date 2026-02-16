# Mistral Vibe Bug Fixing Exercise

This document contains a series of bugs that have been intentionally introduced into the Mistral Vibe codebase for educational purposes. Each bug represents a different type of issue that developers commonly encounter.

## Bug List

### 1. Syntax Error (Obvious when running)
**File**: `vibe/core/utils.py`
**Line**: ~37
**Type**: Syntax Error
**Description**: Missing closing bracket in list definition
**How to find**: Try to import the module or run the application
**Fix**: Add the missing closing bracket

### 2. Logic Error (Found through testing)
**File**: `vibe/core/utils.py`
**Function**: `is_dangerous_directory()`
**Line**: ~127
**Type**: Logic Error
**Description**: Incorrect comparison operator (`!=` instead of `==`)
**How to find**: Run the test `tests/core/test_utils_dangerous_directory.py`
**Fix**: Change `if path != dangerous_path:` to `if path == dangerous_path:`

### 3. Style Violation (Found through linting)
**File**: `vibe/core/tools/builtins/bash.py`
**Function**: `_build_result()`
**Line**: ~285-289
**Type**: Style Violation
**Description**: Using old-style string formatting instead of f-strings
**How to find**: Run linter (e.g., `ruff`, `flake8`, `pylint`)
**Fix**: Replace `%` formatting with f-strings:
```python
# Before (incorrect):
error_msg = "Command failed: %r\n" % command
# After (correct):
error_msg = f"Command failed: {command!r}\n"
```

### 4. Runtime Error (Obvious when executing specific functionality)
**File**: `vibe/core/tools/builtins/read_file.py`
**Function**: `_read_file()`
**Line**: ~145-147
**Type**: Runtime Error (Division by Zero)
**Description**: Division by zero when reading empty files
**How to find**: Try to read an empty file using the `read_file` tool
**Fix**: Remove the division by zero code or add proper handling:
```python
# Remove these lines:
if len(lines_to_return) == 0:
    average_line_length = bytes_read / len(lines_to_return)
    print(f"Average line length: {average_line_length}")
```

### 5. Documentation Bug (Found through code review)
**File**: `vibe/core/tools/builtins/read_file.py`
**Function**: `_read_file()`
**Line**: ~122-134
**Type**: Documentation Error
**Description**: Incorrect docstring claiming function reads binary files
**How to find**: Read the docstring and compare with actual implementation
**Fix**: Correct the documentation:
```python
# Change:
# Note: This function actually reads binary files, but the documentation says it reads text files
# To:
# Note: This function reads text files using UTF-8 encoding.
```

### 6. Failing Test (Found when running tests)
**File**: `tests/core/test_utils_dangerous_directory.py`
**Test**: `test_system_directory_is_dangerous`
**Type**: Test Failure
**Description**: Test fails due to the logic bug in `is_dangerous_directory()`
**How to find**: Run `pytest tests/core/test_utils_dangerous_directory.py`
**Fix**: Fix the logic bug in `is_dangerous_directory()` (see Bug #2)

## How to Approach These Bugs

### For Students:
1. **Start with the obvious ones**: Try running the application to find syntax errors
2. **Run the tests**: Use `pytest tests/core/test_utils_dangerous_directory.py` to find logic errors
3. **Use linting tools**: Run `ruff check` or similar to find style violations
4. **Test specific functionality**: Try using the `read_file` tool on an empty file
5. **Review documentation**: Read docstrings carefully to find documentation bugs
6. **Fix one bug at a time**: Test after each fix to ensure you haven't introduced new issues

### For Instructors:
These bugs are designed to be:
- **Educational**: Each represents a common type of bug
- **Isolated**: Bugs don't interfere with each other
- **Realistic**: Similar to bugs found in real-world codebases
- **Fixable**: Each has a clear solution

## Verification

After fixing all bugs:
1. The application should start without syntax errors
2. All tests should pass: `pytest tests/core/test_utils_dangerous_directory.py -v`
3. Linting should pass: `ruff check vibe/core/utils.py vibe/core/tools/builtins/`
4. The `read_file` tool should work on empty files
5. Documentation should be accurate

## Additional Challenges (Optional)

For advanced students:
1. Write additional tests to cover edge cases
2. Improve the error handling in the `read_file` tool
3. Add input validation to prevent similar logic errors in the future
4. Create a custom linter rule to catch the style violation automatically