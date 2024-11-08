from setuptools import setup, find_packages

setup(
    name="math-quiz",
    version="0.1",
    description="A simple math quiz game with random math problems",
    author="Anish Adgaonkar",
    packages=find_packages(),
    install_requires=[],  # List any dependencies here (if required)
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
