import ast
import subprocess
import sys
import importlib.util

# Standard library modules (do not install)
IGNORE = {
    "os", "sys", "time", "math", "json", "random", "re",
    "pathlib", "threading", "subprocess", "socket",
    "tempfile", "shutil", "logging", "datetime",
    "collections", "itertools", "functools", "typing",
    "asyncio", "sqlite3", "hashlib", "base64", "csv",
    "configparser", "urllib", "http", "email", "xml",
    "zipfile", "tarfile", "argparse"
}

# Import name -> pip package name
PACKAGE_MAP = {
    "cv2": "opencv-python",
    "PIL": "Pillow",
    "bs4": "beautifulsoup4",
    "Crypto": "pycryptodome",
    "yaml": "PyYAML",
    "sklearn": "scikit-learn",
    "serial": "pyserial",
    "dns": "dnspython",
    "OpenSSL": "pyOpenSSL",
    "Image": "Pillow"
}


def installed(name):
    """Return True if the module is installed."""
    return importlib.util.find_spec(name) is not None


def install(package):
    """Install package using pip."""
    print(f"[INSTALL] Installing '{package}'...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        package
    ])

    print(f"[OK] '{package}' installed successfully.")


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

    for module in sorted(modules):

        if installed(module):
            continue

        package = PACKAGE_MAP.get(module, module)

        print(f"\n[INFO] Missing module : {module}")

        if package != module:
            print(f"[INFO] Suggested pip package : {package}")

        answer = input(f"Install '{package}'? (y/n): ").strip().lower()

        if answer == "y":
            try:
                install(package)
            except Exception as e:
                print(f"[ERROR] Unable to install '{package}'.")
                print(e)
        else:
            print(f"[SKIPPED] '{package}'")


check()
