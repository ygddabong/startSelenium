# Selenium Starter

A small browser-automation script with Selenium: it opens python.org, searches for a keyword, and clicks the first result.

Originally written in 2020 as a first Selenium exercise; updated in 2026.

## Tech stack

- Python 3.10+
- Selenium 4 (Selenium Manager downloads the matching ChromeDriver automatically)
- Explicit waits (`WebDriverWait` + `expected_conditions`)

## Getting started

Requires Google Chrome.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python search_demo.py                 # searches "selenium"
python search_demo.py django --headless
```

## 2026 update

- Selenium 3 → 4: `find_element(By..., ...)` instead of the removed `find_element_by_*` helpers
- Removed the committed macOS `chromedriver` binary and the hard-coded local path — Selenium Manager handles the driver now
- Switched the target from Google search (which blocks automated traffic with CAPTCHAs) to python.org's site search
- Added explicit waits, a `--headless` flag, and a query argument
- Added `requirements.txt` and `.gitignore`
