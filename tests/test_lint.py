import subprocess
import unittest

class TestLinting(unittest.TestCase):
    def test_linting(self):
        # List of files to check
        files_to_lint = ["app.py", "synthscope.py"]

        # Run flake8 on each file
        for file in files_to_lint:
            with self.subTest(file=file):
                result = subprocess.run(
                    ["flake8", file],
                    capture_output=True,
                    text=True
                )
                self.assertEqual(
                    result.returncode, 0,
                    f"Linting errors in {file}:\n{result.stdout}"
                )

if __name__ == "__main__":
    unittest.main()