from setuptools import setup

setup(
    name="pson",
    version="1.0.0",
    py_modules=["pson"],
    description="Advanced JSON creator and reader",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pson=pson:cli"
        ]
    },
)