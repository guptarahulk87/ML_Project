from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).parent
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")


setup(
    name="ml-project",
    version="0.1.0",
    description="Starter scaffold for a machine learning project",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "seaborn",
    ],
    python_requires=">=3.10",
)
