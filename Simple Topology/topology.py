#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCLink

def myNetwork():
    net = Mininet(topo = None, link=TCLink, build = False, ipBase = '10.0.0.0/8', autoStaticArp = True)
	
	#Adding Controllers
    info( '*** Adding controller\n' )
    c0 = net.addController('c0', controller = OVSController, port = 6633)
	
	#Adding Switches
    info( '*** Adding Switches\n ')
    s1 = net.addSwitch('s1',stp=True)
    s2 = net.addSwitch('s2',stp=True)
    s3 = net.addSwitch('s3',stp=True)
    s4 = net.addSwitch('s4',stp=True)
    s5 = net.addSwitch('s5',stp=True)
    s6 = net.addSwitch('s6',stp=True)
	
	
    info( '*** Adding hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')
    h4 = net.addHost('h4', ip='10.0.0.4')
    h5 = net.addHost('h5', ip='10.0.0.5')
    h6 = net.addHost('h6', ip='10.0.0.6')
    h7 = net.addHost('h7', ip='10.0.0.7')	
	
	#Adding Links
    info(' *** Adding Links\n ')
    net.addLink(h1,s1)
    net.addLink(h2,s2)
    net.addLink(h3,s5)
    net.addLink(h4,s5)
    net.addLink(h5,s6)
    net.addLink(h6,s4)
    net.addLink(h7,s4)
#------------------------------------------------------------------------------
    net.addLink(s1,s2, bw = 10 )
    net.addLink(s1,s3, bw = 10 )
    net.addLink(s2,s4, bw = 15 )
    net.addLink(s3,s4, bw = 5  )
    net.addLink(s4,s6, bw = 10 )
    net.addLink(s5,s6, bw = 5  )
    net.addLink(s1,s5, bw = 5  )
#------------------------------------------------------------------------------

    info('*** Starting Network \n')
    net.build()
    info('*** Starting Controllers\n')
    for controller in net.controllers:
        controller.start()
    info(' *** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])
    net.get('s5').start([c0])
    net.get('s6').start([c0])
	
   #Enable STP
    s1.cmd( 'ovs-vsctl set bridge s1 stp_enable = true' )
    s2.cmd( 'ovs-vsctl set bridge s2 stp_enable = true' )
    s3.cmd( 'ovs-vsctl set bridge s3 stp_enable = true' )
    s4.cmd( 'ovs-vsctl set bridge s4 stp_enable = true' ) 
    s5.cmd( 'ovs-vsctl set bridge s5 stp_enable = true' )
    s6.cmd( 'ovs-vsctl set bridge s6 stp_enable = true' )

    info( '**** Post Configure switches and hosts\n ')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topo = myNetwork()

