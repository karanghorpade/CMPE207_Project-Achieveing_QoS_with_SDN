# CMPE207_Project-Achieveing_QoS_with_SDN

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
