from setuptools import find_packages, setup

requires = ["google-auth", "gspread", "requests"]

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="gssetting",
    version="0.0.1",
    description="Load setting value from Google Sheets",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="deresmos",
    author_email="deresmos@google.com",
    url="https://github.com/deresmos/gssetting",
    python_requires=">=3.7",
    packages=find_packages(),
    include_package_data=False,
    keywords=["tools"],
    license="MIT License",
    install_requires=requires,
)
