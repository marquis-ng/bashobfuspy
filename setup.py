from setuptools import setup

setup(name="bashobfuspy",
    version = "1.0",
    description = "Bash obfuscator written in Python",
    author = "Marquis",
    url = "https://github.com/marquis-ng/bashobfuspy",
    packages = ["bashobfuspy"],
    entry_points = {
        "console_scripts": ["bashobfuspy=bashobfuspy:_main"]
    },
    extras_require = {
        "full": ["shtab"]
    }
)
