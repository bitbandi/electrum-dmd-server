from setuptools import setup

setup(
    name="electrum-dmd-server",
    version="1.0",
    scripts=['run_electrum_dmd_server.py','electrum-dmd-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0'],
    package_dir={
        'electrumdmdserver':'src'
        },
    py_modules=[
        'electrumdmdserver.__init__',
        'electrumdmdserver.utils',
        'electrumdmdserver.storage',
        'electrumdmdserver.deserialize',
        'electrumdmdserver.networks',
        'electrumdmdserver.blockchain_processor',
        'electrumdmdserver.server_processor',
        'electrumdmdserver.processor',
        'electrumdmdserver.version',
        'electrumdmdserver.ircthread',
        'electrumdmdserver.stratum_tcp'
    ],
    description="Diamond Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="MIT Licence",
    url="https://github.com/bitbandi/electrum-dmd-server/",
    long_description="""Server for the Electrum Lightweight Diamond Wallet"""
)
