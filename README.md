# Achieveing_QoS_with_SDN

This is the term project for Network Programming course CMPE207

Introduction :

There are growing demand on automating networks using SDN, especially when it comes to QoS. In current IP networks, end users tend to change application level utilization from time to time. For example, If a company XYZ are using Webex as their conferencing software and for some reason they changed it to Zoom, now the network admin should go to every single device within the company IP network and change the QoS to allow Zoom to have higher priority than other traffic. The simple concept that the higher the priority of certain application traffic or certain device meaning the faster this traffic will be processed and pushed out. This is typically important in voice and interactive video. In this project we will create a GUI base control unit that we call “Controller” to push different types of configuration changes to an IP network, we will work on the QoS part at this stage. This will make management and day-to-day maintenance of this IP network easier and faster. The implementation will require us to separate control plane and data plane traffic. The QoS values and priorities are configured from the GUI where all the input will be stored in a JSON file and pushed down to the switches. 

For this project we created a virtual network using the 'Mininet' 

Mininet is a network emulator which creates a network of virtual hosts, switches, controllers, and links. 
Mininet hosts run standard Linux network software, and its switches support OpenFlow for highly flexible custom routing and Software-Defined Networking.

For the detailed information related to 'Mininet' follow the link below,

https://github.com/mininet/mininet/wiki/Documentation

To set up the enviroment you will need to download these following files individually.

The files include virtualization software, a SSH-capable terminal, an X server, and the VM image.

For Mac:
1. VirtualBox
2. Mininet VM
3. X11 Software (XQuartz)

Follow this link for step by step walkthrough

https://github.com/mininet/openflow-tutorial/wiki/Installing-Required-Software


For this project we have created a custom topology.

This topology includes 2 Switches, 3 Hosts and 1 Controller.

![](images/Untitled%20Diagram.png)

Steps to follow:

Set up SSH connection with the mininet VM from your local machine

Start the mininet VM

scp all the files in the projects 'python' folder into the 'mininet' directory of your mininet VM 

Mac users start the XQuartz once the mininet VM is up and running

Open three Terminal windows with XQuartz

SSH into the mininet from all the three terminal windows

In one of the terminal window type command 'cd mininet'

To start the custom topology use command 'sudo python topo2s3h.py'

This will start the topology

Type command 'pingall'

The hosts won't be able to ping each other as the switches don't have the forwarding information to route the packets

Type command 'exit' to stop the topology

Use command 'sudo mn -c' to clear the previous emulation

Now in the second terminal window type 'cd pox'

Then type the following command
'python pox.py log.level --DEBUG forwarding.l2_learning'

This will start the l2_learning switch

A layer 2 switch is a type of network switch or device that works on the data link layer (OSI Layer 2) and utilizes MAC Address to determine the path through where the frames are to be forwarded. It uses hardware based switching techniques to connect and transmit data in a local area network (LAN).

A layer 2 switch can also be referred to as a multiport bridge.

This allows the switches to have the forwarding information about each host inside the network.

Now follow the steps given above to start the topology again

perform pingall and the hosts will be able to ping each other

In the same window open the xterm for h1 h2 and h3
type 'xterm h1 h2 h3'

In window for h1 perform 'iperf -s'

In window for h2 perform 'iperf -c 10.0.0.1 -r'

Observe the traffic and bandwidth

Now we will apply the single QoS Queue.

In the third window opened initially run the 'qos1.py' script 'sudo python qos1.py'

This script will create single QoS with a single Queue (q0) on port s1-eth1

This will throttle all egress traffic (going out) on that port

The port s1-eth1 is the switch port linked to h1. 
Running iperf with h1 server, h2 client:
h2 → h1 (client to server) throttled to 4Mbit/s 
h1 → h2 (server to client) not throttled
This QoS is egress only i.e. when the switch is forwarding packets towards h1.
A side effect of this appears to be a reduction in the incoming bandwidth on that port, reduced almost by a third.
This is entirely a result of the bottleneck in the virtualised switch processing; later, a reduction in the link bandwidth is shown to relieve this bottleneck.

Now in the same terminal window as before run the script 'sudo python qos2.py'

Instead of applying QoS on queue 0 (default) on port s1-eth1, we will create two queues, one on which we enqueue traffic we want to pass unrestricted (at maximim bandwidth 1Gbit/s) and one on which we enqueue the traffic we want throttled to 4Mbit/s
