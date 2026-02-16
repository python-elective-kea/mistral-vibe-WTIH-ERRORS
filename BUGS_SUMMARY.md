# Summary of Intentionally Introduced Bugs

This document provides a quick reference to all the bugs that have been intentionally introduced into the Mistral Vibe codebase for educational purposes.

## Bug Inventory

### 1. Syntax Error
- **Location**: `vibe/core/utils.py:37`
- **Type**: Missing closing bracket
- **Impact**: Prevents module from being imported
- **Line**: `KNOWN_TAGS = [CANCELLATION_TAG, TOOL_ERROR_TAG, VIBE_STOP_EVENT_TAG, VIBE_WARNING_TAG`

### 2. Logic Error  
- **Location**: `vibe/core/utils.py:127`
- **Type**: Incorrect comparison operator
- **Impact**: `is_dangerous_directory()` returns wrong results
- **Line**: `if path != dangerous_path:` (should be `==`)

### 3. Style Violation
- **Location**: `vibe/core/tools/builtins/bash.py:285-289`
- **Type**: Old-style string formatting
- **Impact**: Violates modern Python style guidelines
- **Lines**: Using `%` formatting instead of f-strings

### 4. Runtime Error
- **Location**: `vibe/core/tools/builtins/read_file.py:145-147`
- **Type**: Division by zero
- **Impact**: Crashes when reading empty files
- **Lines**: Division by `len(lines_to_return)` when list is empty

### 5. Documentation Bug
- **Location**: `vibe/core/tools/builtins/read_file.py:122-134`
- **Type**: Incorrect docstring
- **Impact**: Misleading documentation
- **Lines**: Claims function reads binary files when it reads text files

### 6. Failing Test
- **Location**: `tests/core/test_utils_dangerous_directory.py`
- **Type**: Test failure due to logic bug
- **Impact**: Test suite fails
- **Test**: `test_system_directory_is_dangerous`

## Files Modified

1. `vibe/core/utils.py` - Syntax error + Logic error
2. `vibe/core/tools/builtins/bash.py` - Style violation
3. `vibe/core/tools/builtins/read_file.py` - Runtime error + Documentation bug
4. `tests/core/test_utils_dangerous_directory.py` - New test file (will fail)
5. `test_logic_bug.py` - Standalone test script (for verification)

## Files Created

1. `BUG_FIXING_EXERCISE.md` - Comprehensive guide for students
2. `BUGS_SUMMARY.md` - This quick reference
3. `tests/core/test_utils_dangerous_directory.py` - Test file that demonstrates the bug
4. `test_logic_bug.py` - Standalone verification script

## How to Verify Bugs Exist

1. **Syntax Error**: Try to import any module from `vibe.core`
   ```bash
   python -c "from vibe.core.utils import KNOWN_TAGS"
   ```

2. **Logic Error**: Run the standalone test
   ```bash
   python test_logic_bug.py
   ```

3. **Style Violation**: Run linter
   ```bash
   ruff check vibe/core/tools/builtins/bash.py
   ```

4. **Runtime Error**: Try to read an empty file (after fixing syntax error)
   ```bash
   touch empty_file.txt
   # Then use vibe to read it
   ```

5. **Documentation Bug**: Read the docstring and compare with implementation

6. **Failing Test**: Run the test (after fixing syntax error)
   ```bash
   pytest tests/core/test_utils_dangerous_directory.py -v
   ```

## Expected Behavior After Fixes

- All modules import successfully
- `is_dangerous_directory()` returns correct results
- Linter passes without style violations
- Empty files can be read without crashes
- Documentation accurately describes the function
- All tests pass

## Educational Objectives

These bugs demonstrate:
- Common types of errors in Python development
- Different methods for discovering bugs (runtime, testing, linting, review)
- Importance of writing tests
- Value of code reviews and linting
- Need for accurate documentation