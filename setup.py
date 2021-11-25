import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setup(
    name='pycodon',
    version='0.1.1',
    python_requires='>=3.8.0',
    description='read DNA sequences',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/tikeeva/pycodon',
    author=['ETikeeva', 'DMalakhova', 'DZanadvornykh'],
    author_email='tikeeva_es@mail.ru',
    license='MIT',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.8',

    ],
    packages=find_packages(exclude=('scripts',)),
    include_package_data=True, 
    entry_points={
        "console_scripts": []}
    
)