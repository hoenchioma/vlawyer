
from distutils.core import setup

setup(
    name='vlawyer',
    packages=['vlawyer'],
    version='0.1',
    license='gpl-3.0',
    description='An unofficial vjudge.net statistics API',
    author='Raheeb Hassan',
    author_email='raheeb@myself.com',
    url='https://github.com/hoenchioma/vlawyer',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['vjudge', 'virtualjudge', 'competitive-programming', 'contest'],
    install_requires=['requests'], # package dependencies
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3.0',
        # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
