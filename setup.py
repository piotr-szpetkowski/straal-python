from setuptools import find_packages, setup

setup(
    name="straal",
    version="0.1.0",
    author="Piotr Szpetkowski",
    url="https://github.com/piotr-szpetkowski/straal-python",
    description="Python client for Straal Payments API",
    packages=find_packages(),
    install_requires=["requests>=2.22.0"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
