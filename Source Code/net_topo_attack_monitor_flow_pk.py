from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Create switches, hosts, and controllers
    switch_1 = net.addSwitch('switch_1')
    switch_2 = net.addSwitch('switch_2')
    switch_3 = net.addSwitch('switch_3')
    switch_4 = net.addSwitch('switch_4')
    switch_5 = net.addSwitch('switch_5')
    host_1 = net.addHost('host_1')
    host_2 = net.addHost('host_2')
    host_3 = net.addHost('host_3')
    host_4 = net.addHost('host_4')
    controller_1 = net.addController('controller_1')
    controller_2 = net.addController('controller_2')
    controller_3 = net.addController('controller_3')

    # Connect switches to controllers
    net.addLink(controller_1, switch_1)
    net.addLink(controller_1, switch_2)
    net.addLink(controller_2, switch_3)
    net.addLink(controller_2, switch_4)
    net.addLink(controller_3, switch_5)
    net.addLink(controller_3, switch_5)

    # Connect hosts to switches
    net.addLink(host_1, switch_5)
    net.addLink(host_2, switch_3)
    net.addLink(host_3, switch_3)
    net.addLink(host_4, switch_4)

    # Start the network
    net.start()

    # Start packet monitoring on switches
    switch_1.cmd('tcpdump -i switch_1-eth1 -w switch_1.pcap &')
    switch_2.cmd('tcpdump -i switch_2-eth1 -w switch_2.pcap &')
    switch_3.cmd('tcpdump -i switch_3-eth1 -w switch_3.pcap &')
    switch_4.cmd('tcpdump -i switch_4-eth1 -w switch_4.pcap &')
    switch_5.cmd('tcpdump -i switch_5-eth1 -w switch_5.pcap &')

    # Configure Host_1 to initiate DDoS attack on Host_4
    host_1.cmd('hping3 -c 10000 -i u1000 --rand-source 10.0.0.4')

    # Open the Mininet CLI to interact with the network
    CLI(net)

    # Stop packet monitoring
    switch_1.cmd('kill %tcpdump')
    switch_2.cmd('kill %tcpdump')
    switch_3.cmd('kill %tcpdump')
    switch_4.cmd('kill %tcpdump')
    switch_5.cmd('kill %tcpdump')

    # Stop the network
    net.stop()

# Create the topology and initiate DDoS attack
create_topology()
