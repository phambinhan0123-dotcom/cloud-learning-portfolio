# Two-Subnet Networking Lab

A Cisco Packet Tracer lab connecting two IPv4 networks through 
a router, followed by connectivity testing and troubleshooting.

## Learning Background

Completed Cisco Networking Basics and applied the concepts 
in this lab.

## Network Design

| Network | Subnet | Default Gateway |
|---|---|---|
| LAN 1 | 192.168.10.0/24 | 192.168.10.1 |
| LAN 2 | 192.168.20.0/24 | 192.168.20.1 |

Each LAN contains two PCs connected through a switch.
The router connects the two LANs.

## What I Configured

- Static IPv4 addresses and subnet masks on the PCs
- Default gateways for communication between networks
- Router interface addresses and enabled interfaces

## Verification

- Used ping to test connectivity
- Used tracert to observe the path between networks
- Observed ARP and ICMP traffic in Simulation mode

## Troubleshooting Exercise

**Problem:** PC0 could communicate within its own subnet, 
but could not reach a PC on the other subnet.

**Cause:** PC0 had an incorrect default gateway.

**Fix:** Restored the correct gateway and repeated
the connectivity test successfully.

**Lesson:** Local communication can work even when the default gateway is incorrect. 
Communication with another network requires a reachable gateway and a valid return path.

## Evidence

[Download the Packet Tracer lab](two-subnet-lab.pkt)

Open the file in Cisco Packet Tracer.

## Scope

This lab demonstrates routing between two local networks. 
It does not demonstrate internet connectivity.
