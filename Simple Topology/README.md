## Goal

Learn to build topologies, configure link parameters and troubleshooting tools.

## Overview
###### Important classes, methods, functions and variables to create the network topology

1. Topo: the base class for Mininet topologies
2. addSwitch(): adds a switch to a topology and returns the switch name
3. addHost(): adds a host to a topology and returns the host name
4. addLink(): adds a bidirectional link to a topology (and returns a link key, but this is not important). Links in Mininet are bidirectional unless noted otherwise.
5. Mininet: main class to create and manage a network
6. start(): starts your network
7. pingAll(): tests connectivity by trying to have all nodes ping each other
8. stop(): stops your network
9. net.hosts: all the hosts in a network
10. dumpNodeConnections(): dumps connections to/from a set of nodes.
11. setLogLevel( 'info' | 'debug' | 'output' ): set Mininet's

## Verification

1. **pingall** to ensure all hosts are reachable with 0% dropped.

2. **iperf** command to ensure the link parameters are enforced properly as in the given network topology   
_Iperf is a traffic generation / network performance measurement tool that can operate in client / server mode. The server mode operation will open a port and accept the incoming connection requests. Client mode operation will generate requests towards the Iperf server. We will be using this tool extensively for measuring the end-to-end network bandwidth._
