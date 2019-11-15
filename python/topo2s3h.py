import subprocess as sb
import os
print "Single Switch and 4 Hosts per switch topology"
print "Creation of topology"
os.system(" sudo mn --custom new_topo.py --topo MyTopo --mac --arp --switch ovsk --controller=remote")
