import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


version = "0.0.0"    
REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "rudravaidya"
SRC_REPO = "textSummarizer"


setuptools.setup(
    name = SRC_REPO,
    version = version,
    author = AUTHOR_USER_NAME,
    description = "A small python package for text summarization",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)