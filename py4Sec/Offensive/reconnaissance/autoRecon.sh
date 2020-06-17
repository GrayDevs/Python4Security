#!/bin/bash

#####################################################################################################
# Requirement: sublist3r, eyewitness, httprobe, nmap
#
# Description: Exemple de script d'automatisation des tâches de reconnaissance
#   1. Récupère les domaines et sous domaines à l'aide de sublist3r
#   2. Vérifier que les sites sont actifs
#   3. Prend des captures d'écran des différents sites rencontrées grâce à eyewitness
# Param: domain: <str> - un nom de domaine, ex: utt.fr; ttu.ee;
#####################################################################################################


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
