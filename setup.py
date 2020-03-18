
from setuptools import setup

with open('README.md', 'r') as f:
    README = f.read()

setup(
    name='vlawyer',
    packages=['vlawyer'],
    version='0.2',
    license='gpl-3.0',
    description='An unofficial vjudge.net statistics API',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Raheeb Hassan',
    author_email='raheeb@myself.com',
    url='https://github.com/hoenchioma/vlawyer',
    keywords=['vjudge', 'virtualjudge', 'competitive-programming', 'contest'],
    install_requires=['requests'], # package dependencies
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.5',
)
