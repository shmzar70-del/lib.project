# HELP - lib/install.py

## English

### What is this?

`lib/install.py` automatically checks the Python modules used by your program.

If a required package is missing, it installs it automatically using pip.

This allows your application to run without asking the user to manually install dependencies.

---

### Project Structure

```
project/
│
├── main.py
│
└── lib/
    ├── __init__.py
    └── install.py
```

---

### Usage

At the beginning of your main program:

```python
from lib.install import auto_install
auto_install()
```

Then import your modules normally.

Example:

```python
from lib.install import auto_install
auto_install()

import requests
import flask
import numpy
```

---

### Features

- Automatically scans imported modules.
- Detects missing packages.
- Installs only missing packages.
- Skips already installed packages.
- Uses the current Python interpreter.
- Future versions will ask before installing unknown packages.

---

# فارسی

## این فایل چیست؟

فایل `lib/install.py` به صورت خودکار کتابخانه‌های استفاده‌شده در برنامه را بررسی می‌کند.

اگر کتابخانه‌ای نصب نباشد، آن را با استفاده از pip نصب می‌کند.

به این ترتیب کاربر لازم نیست قبل از اجرای برنامه، کتابخانه‌ها را به صورت دستی نصب کند.

---

## ساختار پروژه

```
project/
│
├── main.py
│
└── lib/
    ├── __init__.py
    └── install.py
```

---

## نحوه استفاده

در ابتدای فایل اصلی برنامه بنویسید:

```python
from lib.install import auto_install
auto_install()
```

سپس کتابخانه‌های مورد نیاز را به صورت معمول import کنید.

مثال:

```python
from lib.install import auto_install
auto_install()

import requests
import flask
import numpy
```

---

## قابلیت‌ها

- بررسی خودکار importها
- تشخیص کتابخانه‌های نصب نشده
- نصب فقط کتابخانه‌های مورد نیاز
- نصب نکردن کتابخانه‌های موجود
- استفاده از همان نسخه Python که برنامه با آن اجرا شده است
- در نسخه‌های آینده، پرسیدن تأیید برای کتابخانه‌های ناشناخته

---

Version: 1.0
Project: lib.install