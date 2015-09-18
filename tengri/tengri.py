import boto3


class EC2Client:

    def __init__(self):
        """ Creates an EC2 client object

        :return:
        """
        self.ec2 = boto3.client('ec2')

    def list_instances(self, exclude=[], state='Running'):
        """ List all instances which key pair name is not on the exclude list

        :param exclude: list of keynames to exclude, default is empty list
        :return: instances list
        :rtype: list
        """
        reservations = self.ec2.describe_instances()['Reservations']
        instances = []
        for reservation in reservations:
            # print(reservation['Instances'])
            for instance in reservation['Instances']:
                if instance['KeyName'] not in exclude:
                    instances.append(instance)

        return instances

    def stop_all(self, exclude=[]):
        """ Stop all instances which key pair name is not on the exclude list

        :return:
        """
        for instance in self.list_instances(exclude=exclude):
            # print(instance['InstanceId'])
            if instance['State']['Name'] == 'running':
                self.ec2.stop_all(InstanceIds=[instance['InstanceId']])
            else:
                print('Nothing to stop')


if __name__ == '__main__':
    ec2 = EC2Client()
    exclude_list = ['deployer_key', 'blabla_key']

    # List instances excluding a key name
    instances = ec2.list_instances(exclude=exclude_list)

    # Do not exclude key name
    instances = ec2.list_instances()

    # Print Instance ids
    for i in instances:
        print(i['InstanceId'])

    # Stop ONLY wanted instances
    ec2.stop_all(exclude=exclude_list)
