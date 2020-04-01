# ctf
🏴‍☠️ Tools, scripts and other stuff helpful in CTF challenges.

## Recon

| Name | Description | Website |
| --- | --- | --- |
| Recon-ng | Conduct open source web-based reconnaissance quickly and thoroughly | [Github](https://github.com/lanmaster53/recon-ng) |
| ZAP | Web application security scanner | [Official Site](https://www.zaproxy.org/) |
| sherlock | Find social media accounts by username | [Github](https://github.com/sherlock-project/sherlock) |
| nmap | Port scanning & network exploration | [Official Site](https://nmap.org/) |
| Gobuster | Brute force directories and files names on servers | [Github](https://github.com/OJ/gobuster) |
| LinEnum | Local Linux enumeration & privilege escalation checking  | [Github](https://github.com/rebootuser/LinEnum) |

## Attacks

| Name | Description | Website |
| --- | --- | --- |
| bettercap | WiFi, BLE, wireless HID, Ethernet toolset | [Documentation](https://www.bettercap.org/) |

## Exploits

Find software exploits on [Exploit Database](https://www.exploit-db.com/).

| Name | Description | Website |
| --- | --- | --- |
| pwntools | CTF framework and exploit development library | [Documentation](http://docs.pwntools.com/en/stable/) |

## Reverse engineering

| Name | Description | Website |
| --- | --- | --- |
| Ghidra | Software reverse engineering suite of tools | [Official Site](https://ghidra-sre.org/) |

## Web

| Name | Description | Website |
| --- | --- | --- |
| Nikto2 | Web server scanner which performs comprehensive tests | [Github](https://github.com/sullo/nikto) |
| WPScan | WordPress vulnerability scanner | [Official Site](https://wpscan.org/) |
| sqlmap | Automatic SQL injection and database takeover tool | [Github](https://github.com/sqlmapproject/sqlmap) |



## Networking

| Name | Description | Website |
| --- | --- | --- |
| WireShark | Examine packets in a network and in `.pcap` files | [Official Site](https://www.wireshark.org/) |
| NetworkMiner | Extract files, images and other useful data from `.pcap` files | [Official Site](https://www.netresec.com/index.ashx?page=NetworkMiner) |

## Esoteric Languages

| Name | Description | Website |
| --- | --- | --- |
| Try It Online | Online interpreter that has tons of esoteric languages | [tio.run](https://tio.run/) |

### Piet

A graphical programming language in which programs look like abstract paintings. It uses 20 colors, of which 18 are related cyclically through a lightness cycle and a hue cycle.

* Interpreter: [npiet](https://www.bertnase.de/npiet/)

## Steganography

| Name | Description | Website |
| --- | --- | --- |
| StegCracker | Brute-force utility to uncover hidden data inside files | [Github](https://github.com/Paradoxis/StegCracker) |
| stegsolve.jar | View through different renditions of an image | [Direct Download](http://www.caesum.com/handbook/Stegsolve.jar) |
| OpenStego | Hiding data and invisible file watermarking | [Official Site](https://www.openstego.com/) |

## Android

| Name | Description | Website |
| --- | --- | --- |
| Apktool | Reverse engineer Android APK files | [Official Site](https://ibotpeaches.github.io/Apktool/) |
| dex2jar | Generate `.jar` file from `.dex` | [Github](https://github.com/pxb1988/dex2jar) |

## Passwords

| Name | Description | Website |
| --- | --- | --- |
| Patator | Multi-purpose brute forcer | [Github](https://github.com/lanjelot/patator) |
| John the Ripper | Password cracker | [Official Site](https://www.openwall.com/john/) |
| Hashcat | Password cracker/recovery | [Official Site](https://hashcat.net/hashcat/) |

### Dictionary attacks

* Wordlists for dictionary attacks: [github.com/berzerk0/Probable-Wordlists](https://github.com/berzerk0/Probable-Wordlists)
* Password & other types of wordlists: [github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)

## Programming Languages

### PHP

#### Magic Hashes

Common vulnerability in PHP that fakes hash "collisions" where the == operator falls short in PHP type comparison, thinking everything that follows 0e is considered scientific notation (and therefore 0).

* More information: [github.com/spaze/hashes](https://github.com/spaze/hashes)

## Forensics

| Name | Description | Website |
| --- | --- | --- |
| binwalk | Analyzing, reverse engineering, and extracting firmware images | [Github](https://github.com/ReFirmLabs/binwalk) |
| TestDisk | Data recovery software, useful for `.img` or `.dd` files | [Official Site](https://www.cgsecurity.org/wiki/TestDisk)

### Magic numbers

The starting values that identify a file format. These are often crucial for programs to properly read a certain file type, so they must be correct. If some files are acting strangely, try verifying their magic number with a trusted list of file signatures.

* Magic numbers on Wikipedia: [Wikipedia](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files)
* List of file signatures: [Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
