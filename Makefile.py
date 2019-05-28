import os
import argparse



parser = argparse.ArgumentParser(description='My example explanation')

parser.add_argument('cmd', default=None, type=str)
args = parser.parse_args()


def makemigrations():
    db_change = bool(os.system('python manage.py makemigrations'))
    if db_change:
        os.system('python manage.py migrate')


if args.cmd == 'db':
    makemigrations()

if args.cmd == 'install':
    os.system('pip install -r requirements.txt')
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
    os.system('sudo apt-get install redis-server')
    os.system('sudo systemctl enable redis-server.service')


