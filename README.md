# Cisco-Project-CrazyDriveZrt
Complex enterprise network project including VLANs, VTP, EtherChannel, STP, OSPF (IPv4/IPv6), HSRP and GRE tunnel. Configured Cisco devices, ASA firewall (NAT), Linux &amp; Windows servers (AD, DNS, DHCP). Automated backups using Python (Netmiko).

## Documentation

- Full project presentation: docs/Bemutato.pptx

 ## Network Topology

![Topology](topology/network_topology.png)

## Automation Script (Python - Netmiko)

This script connects to Cisco devices via SSH and automatically saves their running configuration.

### Features
- Connects to network devices using SSH
- Executes basic commands (e.g. show running-config)
- Saves configuration to a local file
- Uses Netmiko for automation

### Usage
1. Enter device IP address
2. Script connects and retrieves configuration
3. Backup file is saved locally

### Note
Default credentials and IP must be modified before use.
