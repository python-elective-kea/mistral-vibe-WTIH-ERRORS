from pathlib import Path
import tempfile
import pytest

from vibe.core.utils import is_dangerous_directory


class TestDangerousDirectory:
    """Test the is_dangerous_directory function."""
    
    def test_home_directory_is_dangerous(self):
        """Test that home directory is correctly identified as dangerous."""
        home_dir = Path.home()
        is_dangerous, reason = is_dangerous_directory(home_dir)
        assert is_dangerous is True
        assert "home directory" in reason
    
    def test_system_directory_is_dangerous(self):
        """Test that system directories are correctly identified as dangerous."""
        # This test will fail due to the logic bug we introduced
        system_dir = Path("/usr")
        is_dangerous, reason = is_dangerous_directory(system_dir)
        assert is_dangerous is True  # This will fail because of our bug
        assert "System usr folder" in reason
    
    def test_safe_directory_is_not_dangerous(self):
        """Test that safe directories are not identified as dangerous."""
        with tempfile.TemporaryDirectory() as temp_dir:
            safe_dir = Path(temp_dir)
            is_dangerous, reason = is_dangerous_directory(safe_dir)
            assert is_dangerous is False
            assert reason == ""
    
    def test_current_directory_when_in_home(self):
        """Test behavior when current directory is home."""
        # Change to home directory for test
        original_cwd = Path.cwd()
        try:
            home_dir = Path.home()
            # Note: We can't actually change directory in some test environments
            # So we'll test with the home directory path directly
            is_dangerous, reason = is_dangerous_directory(home_dir)
            assert is_dangerous is True
        finally:
            # No need to change back since we didn't actually change
            pass