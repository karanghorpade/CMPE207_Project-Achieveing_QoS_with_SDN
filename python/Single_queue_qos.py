import subprocess as sb
import os
print "Single Queue QoS applied to the topology"

os.system("sudo ovs-vsctl -- set Port s1-eth1 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=1000000000 queues=0=@q0 -- --id=@q0 create Queue other-config:min-rate=4000000 other-config:max-rate=4000000")
