from setuptools import setup

setup(
    name="filewatcher",
    version="0.3",
    py_modules=["filewatcher.filewatcher"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        filewatcher=filewatcher.filewatcher:main
    """,
)
