from setuptools import setup, find_packages

setup(
    name='tts-voice-cloning',
    version='1.0.0',
    author='Souporno Chakraborty',
    author_email='soupornochakraborty40@gmail.com',
    description='A Python package for text-to-speech voice cloning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Tirthaboss/Python-TTS---Voice-Cloning_Module/#readme',
    packages=find_packages(),
    install_requires=[
        'torch',
        'librosa',
        'numpy',
        'soundfile',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
