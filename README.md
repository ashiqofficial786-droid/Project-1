# GUVI Website Tests

This project automatically tests the GUVI website (guvi.in) to make sure 
things like login, signup, and logout are working properly.

Built with Python + Playwright + pytest.

# What's inside
- `config.py` — website URL and login details
- `pages/` — one file per webpage (home page, login page, etc.)
- `tests/` — the actual test cases
- `utils/logger.py` — saves logs to a file so you can check what happened

# How to set it up (only once)

1. Install the required packages:

   pip install -r requirements.txt
   playwright install

2. Add your GUVI login details:

   cp .env.example .env

   Then open `.env` and fill in your email and password.

 How to run the tests


pytest --html=reports/report.html --self-contained-html -v


This runs all the tests and creates a report you can open in your browser at 
`reports/report.html`.

# Good to know

- If you don't add login details in `.env`, the login and logout tests 
  will just be skipped instead of failing — that's normal.
- GUVI's website changes sometimes. If a test suddenly fails, it's often 
  because a button or element on the site changed. Just check the site 
  in your browser (right-click → Inspect) and update the matching selector 
  in the `pages/` folder.