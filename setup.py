from setuptools import setup

setup(
    name="nereea",
    version="0.1.0",
    description="# NEREEA: Named Entity Recognition Extensive Error Analysis",
    url="https://github.com/fvillena/nereea",
    author="Fabián Villena",
    author_email="fvillena@proton.me",
    license="BSD 2-clause",
    packages=["nereea"],
    install_requires=[
        "seqeval",
        "setuptools>=24.2.0",
    ],
    python_requires=">=3.10",
    extras_require={"dev": ["ipykernel==6.25.2"]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
