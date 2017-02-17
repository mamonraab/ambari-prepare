from subprocess import call
import urllib2
import urlparse

class mamonSetupMe:
    def __init__(self, filememo):
        self.file = filememo

    def start(self):
        network = raw_input('Do you want me to setup your Netowrk ip and host :')
        if network =='y':
            self.setNetwork()
        host = raw_input('Do you want me to host :')
        if host=='y':
            hostname = raw_input('what is your host:')
            networkhost='''NETWORKING=yes
HOSTNAME='''+hostname+''''''
            file_mamon = open('/etc/sysconfig/network','w')
            file_mamon.write(networkhost)
            file_mamon.close()
            print 'done change host name'
        prepare = raw_input('Do you want me to prepare these server for ambari :')
        if prepare=='y':
            self.prepare()


    def prepare(self):
        url = self.file
        parsurl = urlparse.urlparse(url)
        if bool(parsurl.scheme):
            files = urllib2.urlopen(self.file)
        else:
            with open(self.file) as fil:
                files = fil.readlines()
        for line in files:
            wordlist = line.split()
            print 'iam goining to do these cmd '+line+' /n'
            try:
                call(wordlist)
            except Exception as e:
                print e
            finally:
                print 'going next'
        print 'done prepare these box'
    def setNetwork(self):
        dev = raw_input('device name :')
        ip = raw_input('ip you want :')
        sub = raw_input('sub net:')
        gateway = raw_input('gateway :')
        netinfo ='''DEVICE='''+dev+'''
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=no
BOOTPROTO=static
IPADDR='''+ip+'''
NETMASK='''+sub+'''
GATEWAY='''+gateway+''''''
        netfile = '/etc/sysconfig/network-scripts/ifcfg-'+dev
        file_mamon = open(netfile,'w')
        file_mamon.write(netinfo)
        file_mamon.close()
        call(['service','network','restart'])
        print 'done interface setup'
        call(['ifconfig',dev])




i = mamonSetupMe('./memo.txt')
i.start()
