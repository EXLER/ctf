# Nmap Cheatsheet

## Target Specification

| Switch    | Example                      | Description              |
| --------- | ---------------------------- | ------------------------ |
|           | nmap 192.168.1.1             | Scan a single IP         |
|           | nmap 192.168.1.1 192.168.2.1 | Scan specific IPs        |
|           | nmap 192.168.1.1-254         | Scan a range             |
|           | nmap scanme.nmap.org         | Scan a domain            |
| -iL       | nmap -iL targets.txt         | Scan using CIDR notation |
| -iR       | nmap -iR 100                 | Scan 100 random IPs      |
| --exclude | nmap --exclude 192.168.1.1   | Exclude listed hosts     |

## Scan Techniques

| Switch | Example              | Description                                            |
| ------ | -------------------- | ------------------------------------------------------ |
| -sS    | nmap 192.168.1.1 -sS | TCP SYN port scan (Default)                            |
| -sT    | nmap 192.168.1.1 -sT | TCP connect port scan (Default without root privilege) |
| -sU    | nmap 192.168.1.1 -sU | UDP port scan                                          |
| -sA    | nmap 192.168.1.1 -sA | TCP ACK port scan                                      |
| -sW    | nmap 192.168.1.1 -sW | TCP Window port scan                                   |
| -sM    | nmap 192.168.1.1 -sM | TCP Maimon port scan                                   |

## Host Discovery

| Switch | Example                        | Description                                     |
| ------ | ------------------------------ | ----------------------------------------------- |
| -sL    | nmap 192.168.1.1-3 -sL         | No scan. List targets only                      |
| -sn    | nmap 192.168.1.1/24 -sn        | Disable port scanning                           |
| -Pn    | nmap 192.168.1.1-5 -Pn         | Disable host discovery. Port scan only          |
| -PS    | nmap 192.168.1.1-5 -PS22-25,80 | TCP SYN discovery on port x. Port 80 by default |
| -PA    | nmap 192.168.1.1-5 -PA22-25,80 | TCP ACK discovery on port x. Port 80 by default |
| -PU    | nmap 192.168.1.1-5 -PU53       | UDP discovery on port x. Port 40125 by default  |
| -PR    | nmap 192.168.1.1-1/24 -PR      | ARP discovery on local network                  |
| -n     | nmap 192.168.1.1 -n            | Never do DNS resolution                         |

## Port Specification

| Switch      | Example                             | Description                                                           |
| ----------- | ----------------------------------- | --------------------------------------------------------------------- |
| -p          | nmap 192.168.1.1 -p 21              | Port scan for port x                                                  |
| -p          | nmap 192.168.1.1 -p 21-100          | Port range                                                            |
| -p          | nmap 192.168.1.1 -p U:53,T:21-25,80 | Port scan multiple TCP and UDP ports                                  |
| -p-         | nmap 192.168.1.1 -p-                | Scan all ports                                                        |
| -p          | nmap 192.168.1.1 -p http,https      | Port scan from service name                                           |
| -F          | nmap 192.168.1.1 -F                 | Fast scan. Scan 100 most common ports                                 |
| --top-ports | nmap 192.168.1.1 --top-ports 2000   | Scan top 2000 ports                                                   |
| -p-65535    | nmap 192.168.1.1 -p-65535           | Leaving off initial port makes the scan start at port 1               |
| -p0-        | nmap 192.168.1.1 -p0-               | Leaving off end port in range makes the scan go through to port 65535 |

## Service/Version Detection

### Service Detection

| Switch                  | Example                                | Description                                                                |
| ----------------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| -sV                     | nmap 192.168.1.1 -sV                   | Attemps to determine the version of the service running on port            |
| -sV --version-intensity | nmap 192.168.1.1 --version-intensity 8 | Intensity level 0 to 9. Higher number increases possibility of correctness |
| -sV --version-light     | nmap 192.168.1.1 --version-light       | Enable light mode. Lower possibility of correctness. Faster                |
| -sV --version-all       | nmap 192.168.1.1 --version-all         | Enable intensity level 9. Higher possibility of correctness. Slower        |

### OS detection

| Switch            | Example                            | Description                                                                                          |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| -O                | nmap 192.168.1.1 -O                | Remote OS detection using TCP/IP stack fingerprinting                                                |
| -O --osscan-limit | nmap 192.168.1.1 -O --osscan-limit | If at least one open and one closed TCP port are not found it will not try OS detection against host |
| -O --osscan-guess | nmap 192.168.1.1 -O --oscan-guess  | Makes Nmap guess more aggressively                                                                   |
| -O --max-os-tries | nmap 192.168.1.1 --max-os-tries 1  | Set the maximum number x of OS detection tries against a target                                      |
| -A                | nmap 192.168.1.1 -A                | Enable OS detection, version detection, script scanning, and traceroute                              |

## Timing and Performance

| Switch | Example              | Description                                                                                |
| ------ | -------------------- | ------------------------------------------------------------------------------------------ |
| -T0    | nmap 192.168.1.1 -T0 | Paranoid (0) Intrustion Detection System evasion                                           |
| -T1    | nmap 192.168.1.1 -T1 | Sneaky (1) Intrusion Detection System evasion                                              |
| -T2    | nmap 192.168.1.1 -T2 | Polite (2) slows down the scan to use less bandwidth and use less target machine resources |
| -T3    | nmap 192.168.1.1 -T3 | Normal (3) which is default speed                                                          |
| -T4    | nmap 192.168.1.1 -T4 | Aggressive (4) speeds up scans; assumes you are on a reasonably fast and reliable network  |
| -T5    | nmap 192.168.1.1 -T5 | Insane (5) speeds up scans; assumes you are on an extraordinarily fast network             |


| Switch                                                | Example input    | Description                                                   |
| ----------------------------------------------------- | ---------------- | ------------------------------------------------------------- |
| --host-timeout `<time>`                               | 1s; 4m; 2h       | Give up on target after this long                             |
| --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout | 1s; 4m; 2h       | Specifies probe round trip time                               |
| --min-hostgroup/max-hostgroup `<size>`                | 50; 1024         | Parallel host scan group sizes                                |
| --min-parallelism/max-parallelism `<numprobes>`       | 10; 1            | Probe parallelization                                         |
| --scan-delay/--max-scan-delay `<time>`                | 20ms; 2s; 4m; 5h | Adjust delay between probes                                   |
| --max-retries `<tries>`                               | 3                | Specify the maximum number of port scan probe retransmissions |
| --min-rate `<number>`                                 | 100              | Send packets no slower than `<number>` per second             |
| --max-rate `<number>`                                 | 100              | Send packets no faster than `<number>` per second             |

## NSE Scripts

| Switch           | Example                                                                   | Description                                                             |
| ---------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| --script default | nmap 192.168.1.1 --script default                                         | Scan with default NSE scripts. Considered useful for discovery and safe |
| --script         | nmap 192.168.1.1 --script=banner                                          | Scan with a single script. Example *banner*                             |
| --script         | nmap 192.168.1.1 --script=http*                                           | Scan with a wildcard. Example *http*                                    |
| --script         | nmap 192.168.1.1 --script=http,banner                                     | Scan with multiple scripts. Example *http* and *banner*                 |
| --script         | nmap 192.168.1.1 --script "not intrusive"                                 | Scan default, but remove intrusive scripts                              |
| --script-args    | nmap --script snmp-sysdescr --script-args snmpcommunity=admin 192.168.1.1 | NSE script with arguments                                               |

### Useful NSE script examples

| Command                                                                                                              | Description                                    |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| nmap -Pn --script=http-sitemap-generator scanme.nmap.org                                                             | HTTP sitemap generator                         |
| nmap -n -Pn -p 80 --open -sV -vvv --script=banner,http-title -iR 1000                                                | Fast search for random web servers             |
| nmap -Pn --script=dns-brute domain.com                                                                               | Brute forces DNS hostnames guessing subdomains |
| nmap -n -Pn -vv -O -sV --script=smb-enum*,smb-ls,smb-mbenum,smb-os-discovery,sms-s*,smb-vuln*,smbv2* -vv 192.168.1.1 | Safe SMB scripts to run                        |
| nmap --script=whois* domain.com                                                                                      | WHOIS query                                    |
| nmap -p80 --script=http-unsafe-output-escaping scanme.nmap.org                                                       | Detect cross site scripting vulnerabilities    |
| nmap -p80 --script=http-sql-injection scanme.nmap.org                                                                | Detect SQL injection vulnerabilities           |

## Firewall / IDS Evasion and Spoofing

| Switch        | Example                                                                        | Description                                                              |
| ------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| -f            | nmap 192.168.1.1 -f                                                            | Requested scan use tiny fragmented IP packets. Harder for packet filters |
| --mtu         | nmap 192.168.1.1 --mtu 32                                                      | Set your own offset size                                                 |
| -D            | nmap -D 192.168.1.101,192.168.1.102 192.168.1.1                                | Send scans from spoofed IPs                                              |
| -S            | nmap -S www.microsoft.com www.facebook.com                                     | Scan Facebook from Microsoft (-e eth0 -Pn may be required)               |
| -g            | nmap -g 53 192.168.1.1                                                         | Use given source port number                                             |
| --proxies     | nmap --proxies http://192.168.1.101:8080,http://192.168.1.102:8080 192.168.1.1 | Relay connections through HTTP/SOCKS4 proxies                            |
| --data-length | nmap --data-length 200 192.168.1.1                                             | Appends random data to sent packets                                      |


## Output

| Switch          | Example                                          | Description                                                            |
| --------------- | ------------------------------------------------ | ---------------------------------------------------------------------- |
| -oN             | nmap 192.168.1.1 -oN normal.file                 | Normal output                                                          |
| -oX             | nmap 192.168.1.1 -oX xml.file                    | XML output                                                             |
| -oG             | nmap 192.168.1.1 -oG grep.file                   | Grepable output                                                        |
| -oA             | nmap 192.168.1.1 -oA results                     | Output in the three major formats at once                              |
| -oG -           | nmap 192.168.1.1 -oG -                           | Grepable output to stdout. -oN -, -oX - also usable                    |
| --append-output | nmap 192.168.1.1 -oN normal.file --append-output | Append to normal output file instead of overwriting                    |
| -v              | nmap 192.168.1.1 -v                              | Increase the verbosity level (use -vv or more for greater effect)      |
| -d              | nmap 192.168.1.1 -d                              | Increase debugging level (use -dd or more for greater effect)          |
| --reason        | nmap 192.168.1.1 --reason                        | Display the reason a port is in a particular state, same output as -vv |
| --open          | nmap 192.168.1.1 --open                          | Only show open (or possibly open) ports                                |
| --packet-trace  | nmap 192.168.1.1 -T4 --packet-trace              | Show all packets sent and received                                     |
| --iflist        | nmap --iflist                                    | Shows the host interfaces and routes                                   |
| --resume        | nmap --resume results.xml                        | Resume an aborted scan                                                 |

## Misc

| Switch | Example                      | Description          |
| ------ | ---------------------------- | -------------------- |
| -6     | nmap -6 2607:f0d0:1002:51::4 | Enable IPv6 scanning |
