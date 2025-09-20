from setuptools import setup, find_packages

setup(
    name='saAam-core',
    version='1.0.0',
    description='SaAaM-Core: Conscious World Engine for Dynamic Games.',
    author='SaAaM LLC',
    author_email='your_email@example.com',
    url='https://github.com/your_repo/saAam-core',  # Replace with private repo URL
    packages=find_packages(),
    install_requires=[
        'torch',
        'transformers',
        'numpy',
        'networkx',
        'pygame',
        'pyyaml',
        'cryptography',
        'mediapipe'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Proprietary',
        'Programming Language :: Python :: 3.8',
        'Topic :: Games/Entertainment :: Simulation'
    ],
    python_requires='>=3.8',
)
