import configparser
from os import path


class Config:

    fname = 'tengri.conf'
    config = configparser.ConfigParser()
    config.sections()

    if path.isfile(fname):
        config.read(fname)
    elif path.isfile('~/' + fname):
        config.read('~/' + fname)
    elif path.isfile('/tmp/' + fname):
        config.read('/tmp/' + fname)

    exclude_list = config['DEFAULT']['exclude_list']
    instance_state = config['DEFAULT']['instance_state']

if __name__ == '__main__':
    config = Config()
    print(config.exclude_list, config.instance_state)
