import ast
import subprocess
import sys
import importlib.util

# نام‌هایی که جزو کتابخانه استاندارد هستند و نباید نصب شوند
IGNORE = {
    "os", "sys", "time", "math", "json", "random", "re",
    "pathlib", "threading", "subprocess", "socket",
    "tempfile", "shutil", "logging", "datetime",
    "collections", "itertools", "functools", "typing",
    "asyncio", "sqlite3", "hashlib", "base64", "csv",
    "configparser", "urllib", "http", "email", "xml",
    "zipfile", "tarfile", "argparse"
}


def installed(name):
    return importlib.util.find_spec(name) is not None


def install(pkg):
    print(f"[INSTALL] {pkg}")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        pkg
    ])


def check():
    main = sys.modules["__main__"]

    if not hasattr(main, "__file__"):
        return

    with open(main.__file__, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    modules = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                modules.add(n.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                modules.add(node.module.split(".")[0])

    modules -= IGNORE
    modules.discard("lib")

    for m in sorted(modules):
        if installed(m):
            continue

        ans = input(f"کتابخانه '{m}' نصب نیست. نصب شود؟ (y/n): ")

        if ans.lower() == "y":
            try:
                install(m)
            except Exception as e:
                print("خطا:", e)


check()