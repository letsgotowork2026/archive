# Switching

# Routing

# Default Gateway

# eth0 eth1 ...

ethernet + number N

이더넷 네트워크 인터페이스 카드 (NIC)

# `ip link`

호스트의 인터페이스를 나열하고 수정

# `ip addr`

인터페이스의 IP 주소를 설정

`ip addr add 192.168.1.10/24 dev eth0`

# `ip route`

`ip route add 192.168.1.0/24 via 192.168.2.1`

`cat /proc/sys/net/ipv4/ip_forward`

