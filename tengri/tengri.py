__author__ = 'leonardo'

import boto3


class EC2Client:

    def __init__(self):
        """ Creates an EC2 client object

        :return:
        """
        self.ec2 = boto3.client('ec2')

    def list_instances(self, exclude=[]):
        """ List running instances based on a filter, example SSH Key name

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

    def stop_instances(self, exclude=[]):
        """ Stop instances that are not from basic infrastructure

        :return:
        """
        for instance in self.list_instances(exclude=exclude):
            print(instance['InstanceId'])
            if instance['State']['Name'] == 'running':
                self.ec2.stop_instances(InstanceIds=[instance['InstanceId']])
            else:
                print('Nothing to stop')


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
