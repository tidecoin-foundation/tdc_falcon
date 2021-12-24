import setuptools
from setuptools import setup, Extension

tdc_falcon_module = Extension('tdc_falcon',
                            sources = [
                                       'src/codec.c',
                                       'src/common.c',
                                       'src/fft.c',
                                       'src/fpr.c',
                                       'src/keygen.c',
                                       'src/pqclean.c',
                                       'src/rng.c',
                                       'src/sign.c',
                                       'src/vrfy.c',
                                       'src/sha2.c',
                                       'src/randombytes.c',
                                       'src/fips202.c',
                                       'src/aes.c',                                       
                                       'src/module.c',                                       
                                       ],

                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.','src'])

setup (name = 'tdc_falcon',
       version = '1.0.1',
       author_email = 'tidecoins@protonmail.com',
       author = 'yarsawyer',
       url = 'https://github.com/yarsawyer/tdc_falcon',
       description = 'Falcon-512 bindings for TideCoin',
       package_dir={"": "src"},
       packages=setuptools.find_packages(where="src"),
       ext_modules = [tdc_falcon_module])
