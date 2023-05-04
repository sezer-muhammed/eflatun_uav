
from setuptools import setup, find_packages

setup(
    name="eflatun_uav",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        
    ],
    extras_require={{
        "dev": [
            "pytest",
        ],
    }},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    author="",
    author_email="",
    description="",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    url="",
    project_urls={{
        "Bug Tracker": "",
        "Documentation": "",
        "Source Code": "",
    }},
)
