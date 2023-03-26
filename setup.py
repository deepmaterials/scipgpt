import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scigpt",
    version="2023.3.24",
    author="Kamal Choudhary",
    author_email="writetokamal.1989@gmail.com",
    description="scigpt",
    install_requires=[
        "numpy>=1.22.0",
        "scipy>=1.6.3",
        "jarvis-tools>=2021.07.19",
        "openai",
        "chemnlp",
        "matplotlib>=3.4.1",
        "flake8>=3.9.1",
        "pycodestyle>=2.7.0",
        "pydocstyle>=6.0.0",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepmaterials/scipgpt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
