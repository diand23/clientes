from setuptools import setup, find_packages

setup(
    name="Generador_contrasenas",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'generar-contrasena = Generador_contrasenas.contrasenas:main',
        ],
    },
    install_requires=[],
    author="Diandra",
    author_email="diandmcm@gmail.com",
    description="Una librería que genere contraseñas seguras y aleatorias.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/diand23/Generador_contrasenas",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 