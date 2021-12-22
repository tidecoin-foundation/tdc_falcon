from setuptools import setup, Extension

tdc_falcon_module = Extension('tdc_falcon',
                            sources = [
                                       'codec.c',
                                       'common.c',
                                       'fft.c',
                                       'fpr.c',
                                       'keygen.c',
                                       'pqclean.c',
                                       'rng.c',
                                       'sign.c',
                                       'vrfy.c',
                                       'sha2.c',
                                       'randombytes.c',
                                       'fips202.c',
                                       'aes.c',
                                       'pbkdf2-hmac-sha512.c',
                                       'sha512.c',
                                       'utils.c',
                                       'module.c',                                       
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'tdc_falcon',
       version = '0.2',
       author_email = 'tidecoins@protonmail.com',
       author = 'yarsawyer',
       url = 'https://github.com/yarsawyer/tdc_falcon',
       description = 'Falcon-512 bindings for TideCoin',
       ext_modules = [tdc_falcon_module])
