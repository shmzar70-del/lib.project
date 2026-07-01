# lib.install

Automatic Python Package Installer

---

## Description

`lib.install` is a lightweight Python module that automatically checks imported packages and installs missing dependencies using `pip`.

The goal is to let users run Python programs without manually installing required libraries.

---

## Features

- Automatically detects imported packages.
- Installs only missing packages.
- Skips packages already installed.
- Uses the current Python interpreter.
- Easy to integrate into any project.
- Lightweight and open source.

---

## Project Structure

```
project/
│
├── main.py
├── README.md
├── HELP.md
│
└── lib/
    ├── __init__.py
    └── install.py
```

---

## Usage

Import the installer before importing other packages.

```python
from lib.install import auto_install

auto_install()

import requests
import flask
import numpy
```

---

## Requirements

- Python 3.8+
- pip

---

## Future Plans

- Detect unknown packages.
- Ask user before installing suspicious modules.
- Support virtual environments.
- Generate requirements.txt automatically.
- Better error handling.

---

# فارسی

## معرفی

`lib.install` یک ماژول سبک برای پایتون است که کتابخانه‌های مورد نیاز برنامه را بررسی می‌کند و در صورت نصب نبودن، آن‌ها را به صورت خودکار توسط `pip` نصب می‌کند.

هدف این پروژه این است که اجرای برنامه برای کاربر ساده‌تر شود و نیازی به نصب دستی کتابخانه‌ها نباشد.

---

## قابلیت‌ها

- بررسی خودکار کتابخانه‌های Import شده
- نصب فقط کتابخانه‌های مورد نیاز
- نصب نکردن کتابخانه‌های موجود
- استفاده از همان نسخه Python در حال اجرا
- سبک و قابل استفاده در هر پروژه

---

## نحوه استفاده

در ابتدای برنامه بنویسید:

```python
from lib.install import auto_install

auto_install()
```

سپس کتابخانه‌های مورد نیاز را به صورت معمول Import کنید.

---

## نسخه

Version 1.0

---

## License

MIT License
