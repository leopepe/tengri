import configparser


class Config:

    config = configparser.ConfigParser()
    config.sections()
    config.read('tengri.conf')
    exclude_list = config['DEFAULT']['exclude_list']
    instance_state = config['DEFAULT']['instance_state']

if __name__ == '__main__':
    config = Config()
    print(config.exclude_list, config.instance_state)
