from setuptools import setup, find_packages


setup(
    name='aioredisqueue',
    version='0.1a',
    author='Konstantin Ignatov',
    author_email='kv@qrator.net',
    packages=find_packages(),
    install_requires=(
        'aioredis',
    ),
    extras_require={
        'dev': ['pytest'],
    },
    include_package_data = True,
)
