import os
import setuptools

# Check if README.md exists and read it
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "A small python package for CNN app"

__version__ = "0.0.0"
REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_USER_NAME = "Ommuddaiah16"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "igomprakash@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
