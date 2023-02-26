pytest -v -n=2 --html=Reports\report.html testCases/test_login.py
pytest -v -n=2 --html=Reports\report.html testCases/test_login.py --browser firefox

pytest -v -m "sanity" --html=./Reports/report.html testCases/
pytest -v -m "sanity and regression" --html=./Reports/report.html testCases/