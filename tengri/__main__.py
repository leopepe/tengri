from tengri.tengri import EC2Client


def main():
    ec2 = EC2Client()
    exclude = ['deployer_key', 'blabla_key']

    # List instances excluding a key name
    instances = ec2.list_instances(exclude=exclude)

    # Do not exclude key name
    instances = ec2.list_instances()

    # Print Instance ids
    for i in instances:
        print(i['InstanceId'])

    # Stop ONLY wanted instances
    ec2.stop_instances(exclude=['deployer_key'])


if __name__ == '__main__':
    main()
