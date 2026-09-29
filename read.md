```powershell
python -m pip install -r test1/requirements-test.txt
python -m playwright install chromium firefox webkit
python -m pytest test1/tests/test_login.py --username "<username>" --password "<password>" --browser chromium
```

Supported browser values: `chromium`, `firefox`, and `webkit`. Install the matching browser with `python -m playwright install <browser>` if you do not install all three above.