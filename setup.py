from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crm_app",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'crm-app = crm_app.main:main',
        ],
    },
    install_requires=[
        'mysql-connector-python',
    ],
    author="Diandra",
    author_email="diandmcm@gmail.com",
    description="Un sistema CRM simple que maneja usuarios y facturas con SQL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diand23/crm_app",  # actualiza si usas otro nombre
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
