from setuptools import setup,find_packages

setup(
    name               = 'sd_embed'
    , version          = '1.240707.2'
    , license          = 'Apache License'
    , author           = "Andrew Zhu"
    , author_email     = 'xhinker@hotmail.com'
    , packages         = find_packages('src')
    , package_dir      = {'': 'src'}
    , url              = 'https://github.com/xhinker/sd_embed'
    , keywords         = 'diffusers stable-diffusion embedding'
    , install_requires = [
        'torch'
        , 'transformers'
        , 'diffusers'
        , 'lark'
    ]
    , include_package_data=True
)
