N = '\n'


def create_file():
    try:
        with open('/Users/montekkundan/Downloads/coding/defisherpa/dynamic_web_check/smoke/test_example.py', 'w') as f:
            f.write(f'# imports{N}')
            f.write(f'from FUNCTIONS.helper import Checker{N}')
            f.write(f'import json{N}')
            f.write(f'from utilites.logfile import Logclass{N}')
            f.write(f'import pytest{N}')
            f.write(f'{N}')
            f.write(f'{N}')
            f.write(f'# test case{N}')
            f.write(f'def test_check(browser):{N}')
            f.write(f'    logger = Logclass(){N}')
            f.write(f'    log = logger.getLogs(){N}')
            f.write(f'    log.info("This test is now running"){N}')
            f.write(f'    run = Checker("", browser){N}')
            f.write(f'    ####{N}')
            f.write(f'    # your code here{N}')
            f.write(f'    ###{N}')
            f.write(f'    run.end(){N}')

        print("File created!")
    except FileNotFoundError:
        print("The 'smoke' directory does not exist")
