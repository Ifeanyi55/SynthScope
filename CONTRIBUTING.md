# Contributing to SynthScope

First off—thank you for considering contributing to **SynthScope**! 🎉  
We welcome contributions of all kinds: bug reports, feature suggestions, documentation improvements, and of course, code contributions.  

---

## 📜 Code of Conduct
This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).  
By participating, you agree to uphold this code and foster a welcoming and respectful community.

---

## 🙌 How You Can Contribute
- ⭐ Star the repo to show your support.
- 🐞 Report bugs.
- 💡 Suggest new features or enhancements.
- 📝 Improve documentation.
- 🔧 Submit pull requests with code improvements or fixes.

---

## 🐛 Reporting Bugs
When reporting a bug, please:
1. Search [existing issues](../../issues) to avoid duplicates.
2. Open a new issue with:
   - **Title**: Clear and descriptive (e.g., _“Speech output fails on macOS”_).
   - **Description**: What happened vs. what you expected.
   - **Steps to reproduce**: So we can replicate the issue.
   - **Environment details**: OS, Python version, SynthScope version.
   - **Additional context**: Logs, screenshots, or error messages.

Example:


**Title**: No audio output in French locale
**Steps to reproduce**:
1. Run `python app.py`
2. Select French language
3. Perform a search
**Expected**: French audio narration
**Actual**: Silent output
**Environment**: Windows 11, Python 3.11

---

## 💡 Suggesting Enhancements
When proposing a new feature:
- **Title**: One-line summary (e.g., _“Add support for dark mode UI”_).
- **Motivation**: Why this is valuable.
- **Proposed solution**: How it should work.
- **Alternatives considered**: Optional but helpful.

---

## 👩‍💻 Your First Code Contribution
1. **Fork** the repository.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/SynthScope.git
   cd SynthScope
   ```
3. **Create a branch**:
   ```bash
   git checkout -b feature/my-feature
   ```
4. **Set up your environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. **Make your changes**:
   - Follow coding style (PEP8).
   - Add docstrings and comments where useful.
6. **Test your changes**:
   ```bash
   pytest tests/
   ```
   Or, if no test suite exists, verify manually by running:
   ```bash
   python app.py
   ```
7. **Commit your work**:
   ```bash
   git add .
   git commit -m "Add feature: description of change"
   ```
8. **Push to your fork**:
   ```bash
   git push origin feature/my-feature
   ```
9. **Open a Pull Request** on the main repo:
   - Describe your changes clearly.
   - Link any related issues.
   - Be responsive to reviewer feedback.

---

## 🔄 Pull Request Guidelines
- Keep PRs small and focused for easier review.
- Use clear commit messages (imperative mood: *“Fix bug”*, not *“Fixed bug”*).
- Document any new functionality in `README.md` or inline docstrings.
- Add/update tests where applicable.
- Ensure code runs without errors before submitting.

---

## 🎨 Style Guidelines
- **Python Code**: Follow [PEP8](https://peps.python.org/pep-0008/).
- **Linting**: Use `flake8` before committing.
- **Docstrings**: Follow Google-style or NumPy-style docstrings.
- **Commit Messages**:
  - `fix: ...` → for bug fixes
  - `feat: ...` → for new features
  - `docs: ...` → for documentation changes
  - `refactor: ...` → for code refactoring

---

## 📚 Additional Resources
- [SynthScope Repository](https://github.com/Ifeanyi55/SynthScope)
- [Issues](../../issues) — open bugs or feature requests
- [Pull Requests](../../pulls) — active contributions
- [Contributor Covenant](https://www.contributor-covenant.org/)

---

## 🎉 Final Note
Every contribution—big or small—makes **SynthScope** better.  
Thank you for helping build a tool that combines **web search, image generation, and audio narration** into one experience! 🚀
