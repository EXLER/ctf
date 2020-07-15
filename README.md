# ctf
🏴‍☠️ Tools, scripts and other stuff helpful in CTF challenges.

## Recon

| Name | Description | Usage |
| --- | --- | --- |
| Recon-ng | Conduct open source web-based reconnaissance quickly and thoroughly | [Github](https://github.com/lanmaster53/recon-ng) |
| sherlock | Find social media accounts by username | [Github](https://github.com/sherlock-project/sherlock) |
| nmap | Port scanning & network exploration | [Official Site](https://nmap.org/) |
| Gobuster | Brute force directories and files names on servers | [Github](https://github.com/OJ/gobuster) |
| LinEnum | Local Linux enumeration & privilege escalation checking  | [Github](https://github.com/rebootuser/LinEnum) |

## Attacks

| Name | Description | Usage |
| --- | --- | --- |
| bettercap | WiFi, BLE, wireless HID, Ethernet toolset | [Documentation](https://www.bettercap.org/) |

## Exploits

Find software exploits on [Exploit Database](https://www.exploit-db.com/).

| Name | Description | Usage |
| --- | --- | --- |
| pwntools | CTF framework and exploit development library | [Documentation](http://docs.pwntools.com/en/stable/) |

## Reverse engineering

| Name | Description | Usage | Notes |
| --- | --- | --- | --- |
| Ghidra | Software reverse engineering suite of tools | [Official Site](https://ghidra-sre.org/) | |
| strings | Display printable strings in files | `sudo apt install binutils` | |
| hexdump | Dump file contents as hexadecimal values | Pre-installed | `hexdump -C` shows hex and ASCII side-by-side |
| gdb | GNU debugger | `sudo apt install gdb` | Plugins: [pwndbg](https://github.com/pwndbg/pwndbg), [GDB dashboard](https://github.com/cyrus-and/gdb-dashboard) |
| ltrace | Library call tracer | `sudo apt install ltrace` | |
| uncompyle6 | Translate Python bytecode (`.pyc`) into Python code | [PyPI](https://pypi.org/project/uncompyle6/) | |

### Shellcode

Shellcode is a small piece of code used as the payload in the exploitation of a software vulnerability.

* Shellcodes database - [shell-storm.org](http://shell-storm.org/shellcode/)
* Shellcode generation using `pwntools` - [Documentation](https://docs.pwntools.com/en/stable/shellcraft.html)

### Random values

When the seed is not given for the rand method, the seed will always be starting on 1. Therefore rand will always give the same answer when the method in only called once in the program.

Not every OS/system has the same implementation of the rand function. Therefore you need to determine which random value will be generated on the server.

## Web

| Name | Description | Usage |
| --- | --- | --- |
| ZAP | Web application security scanner | [Official Site](https://www.zaproxy.org/) |
| Nikto2 | Web server scanner which performs comprehensive tests | [Github](https://github.com/sullo/nikto) |
| WPScan | WordPress vulnerability scanner | [Official Site](https://wpscan.org/) |
| sqlmap | Automatic SQL injection and database takeover tool | [Github](https://github.com/sqlmapproject/sqlmap) |

## Networking

| Name | Description | Usage |
| --- | --- | --- |
| WireShark | Examine packets in a network and in `.pcap` files | [Official Site](https://www.wireshark.org/) |
| NetworkMiner | Extract files, images and other useful data from `.pcap` files | [Official Site](https://www.netresec.com/index.ashx?page=NetworkMiner) |

## Esoteric Languages

| Name | Description | Usage |
| --- | --- | --- |
| Try It Online | Online interpreter that has tons of esoteric languages | [tio.run](https://tio.run/) |

### Piet

A graphical programming language in which programs look like abstract paintings. It uses 20 colors, of which 18 are related cyclically through a lightness cycle and a hue cycle.

* Interpreter: [npiet](https://www.bertnase.de/npiet/)

## Steganography

| Name | Description | Usage |
| --- | --- | --- |
| steghide | Hide and extract data from image and audio files | [SourceForge](http://steghide.sourceforge.net/) |
| StegCracker | Brute-force utility to uncover hidden data inside files | [Github](https://github.com/Paradoxis/StegCracker) |
| stegsolve.jar | View through different renditions of an image | [Direct Download](http://www.caesum.com/handbook/Stegsolve.jar) |
| OpenStego | Hiding data and invisible file watermarking | [Official Site](https://www.openstego.com/) |
| Steganography Online | Message decoding service for low-hanging-fruits | [Website](http://stylesuxx.github.io/steganography/)

## Android

| Name | Description | Usage |
| --- | --- | --- |
| Apktool | Reverse engineer Android APK files | [Official Site](https://ibotpeaches.github.io/Apktool/) |
| JADX | Dex to Java decompiler | [Github](https://github.com/skylot/jadx) |
| dex2jar | Generate `.jar` file from `.dex` | [Github](https://github.com/pxb1988/dex2jar) |
| Frida | Reverse engineering toolkit for iOS and Android | [Official Site](https://frida.re)

## Passwords

| Name | Description | Usage |
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

| Name | Description | Usage |
| --- | --- | --- |
| binwalk | Analyzing, reverse engineering, and extracting firmware images | [Github](https://github.com/ReFirmLabs/binwalk) |
| TestDisk | Data recovery software, useful for `.img` or `.dd` files | [Official Site](https://www.cgsecurity.org/wiki/TestDisk) |
| FotoForensics | Forensic analysis on images | [Website](http://fotoforensics.com/)

### Magic numbers

The starting values that identify a file format. These are often crucial for programs to properly read a certain file type, so they must be correct. If some files are acting strangely, try verifying their magic number with a trusted list of file signatures.

* Magic numbers on Wikipedia: [Wikipedia](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files)
* List of file signatures: [Wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)

## Cryptography

### Caesar Cipher

Classic shift cipher. Below is a bash one-liner using `caesar` (from package `bsdgames`) to try all shift positions.

```bash
$ cipher='jeoi{geiwev_gmtliv_ws_svmkmrep}' ; for i in {0..25}; do echo $cipher | caesar $i; done
```

### Vigenère Cipher

Vigenère cipher has several Caesar ciphers in sequence with different shift values. 

* Cipher explanation - [Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Description)
* Online cipher analysis & cracking - [f00l.de](http://f00l.de/hacking/vigenere.php)

### Frequency analysis

Frequency analysis is a technique used to break classical ciphers. Frequency analysis is based on the fact that, in any given stretch of written language, certain letters and combinations of letters occur with varying frequencies.

* Online frequency analysis - [dcode.fr](https://www.dcode.fr/frequency-analysis)

## Substitution cipher

Substitution cipher is a method of encrypting by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution. 

* Online cipher solver - [quipqiup.com](https://quipqiup.com/)
