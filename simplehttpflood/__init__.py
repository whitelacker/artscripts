__all__ = ['requesthttp','socket_gen']
__version__ = '0.1'
__license__ = 'GPLv3'
__author__ = 'whitelacker'
__github__ = 'https://github.com/whitelacker/artscripts'

def main():
    for module in __all__:
        exec("import {}".format(module))

main()
