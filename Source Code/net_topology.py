from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

def create_topology():
    net = Mininet(controller=RemoteController, switch=OVSSwitch)

    # Create switches
    switch_1 = net.addSwitch('switch_1')
    switch_2 = net.addSwitch('switch_2')
    switch_3 = net.addSwitch('switch_3')
    switch_4 = net.addSwitch('switch_4')
    switch_5 = net.addSwitch('switch_5')

    # Create hosts
    host_1 = net.addHost('host_1')
    host_2 = net.addHost('host_2')
    host_3 = net.addHost('host_3')
    host_4 = net.addHost('host_4')

    # Create controllers
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

    # Open the Mininet CLI to interact with the network
    CLI(net)

    # Stop the network
    net.stop()

# Create the topology
create_topology()
