from tengri.tengri import EC2Client
from tengri.config import Config


def main():
    ec2 = EC2Client()
    config = Config()
    exclude_list = config.exclude_list
    instance_state = config.instance_state

    # List instances excluding a key name
    instances = ec2.list_instances(exclude=exclude_list)
    print('Instances: {0}'.format(instances))
    
    # Print Instance ids
    # for i in instances:
    #     print(i['InstanceId'])

    # Stop ONLY wanted instances
    # ec2.stop_all(exclude=exclude_list)


if __name__ == '__main__':
    main()
