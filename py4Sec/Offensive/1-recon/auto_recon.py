#-*-coding:UTF-8 -*
#!/usr/bin/env python

"""
integrating nmap
s3blister
[hunter.io]

integrating bash command
bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
"""

import nmap
import optparse

def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*]", tgtHost, "tcp/"+tgtPort, state)

def main():
    parser = optparse.OptionParser('usage %prog '+\
                                   '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string',\
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',\
                      help='specify target port[s] separated by comma')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts[0] == None):
        print parser.usage
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()

"""
# Bash version
if [ $# -gt 2 ]; then
    echo "USAGE: .script.sh <domain>
    echo "Example: ./script.sh yahoo.com"
    exit(1)
fi

if [ ! -d "scans" ]; then
    mkdir scans
fi

if [ ! -d "eyewitness" ]; then
    mkdir eyewitness
fi

pwd=$(pwd)

echo "Gathering subdomains with sublist3r"
sublist3r -d $1 -o final.txt

echo $1 >> final.txt

echo "Compiling 3rd level domains..."
cat domain-test.txt | grep -Po  "(\w+\.\w+\.\w+)$" | sort -u >> third-level.txt

echo "Gathering full third-level domains with sublist3r"
for domain in $(cat third-level.txt); do sublit3r -d $domain -o thirdlevels/$domain.txt; cat thirdlevel/domain.txt | sort -u >> final.txt; done

if [ $# -eq 2 ]; then
    echo "Probing for alive third-levels..."
    cat final.txt | sort -u | grep -v $2 | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ":443" > probed.txt
else
    echo "Probing for alive third levels..."
    cat final.txt | sort -u | httprobe -s -p http:443 | sed 's/https\?:\/\///' | tr -d ":443" > probed.txt
fi

echo "scanning open ports"
nmap -iL probed.txt -T5 -oA scans/scanned.txt

echo "Running eyewitness..."
eyewitness -f $pwd/probed.txt -d $1 --all-protocols
mv /usr/share/eyewitness/$1 eyewitness/$1
"""

