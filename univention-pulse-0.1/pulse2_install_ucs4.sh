#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# debconf
#run-parts ${SCRIPT_DIR}/debconf

# Define packages to install
PULSE_DEPS='python-netaddr createrepo'
MMC='mmc-agent mmc-web-base python-mmc-base mmc-web-dashboard python-mmc-dashboard'
PULSE2='atftpd openbsd-inetd pulse2 dnsutils python-lxml python-mmc-report mmc-web-report python-mmc-update mmc-web-update pulse2-dlp-server pulse-update-manager pulse-licensed pulse-report python-mmc-support mmc-web-support pulse-first-run ttf-arphic-bkai00mp ttf-arphic-bsmi00lp ttf-arphic-gbsn00lp ttf-arphic-gbsn00lp fonts-ipaexfont python-importlib python-pycparser'
APACHE2='apache2-mpm-prefork libapache2-mod-php5'
PHP5='php5 php5-cgi php5-cli php5-common php5-ldap'
MYSQL='mysql-server mysql-client expect'
BACKUPPC='backuppc libfile-rsyncp-perl libio-dirent-perl samba-common-bin python-mmc-backuppc mmc-web-backuppc pulse2-uuid-resolver'
GLPI='glpi fusioninventory-for-glpi glpi-webservices glpi-manufacturersimports'
PULSE2_GLPI='python-mmc-glpi mmc-web-glpi'
PULSE2_INVENTORY='python-mmc-inventory mmc-web-inventory'
MONITORING='python-pulse2-common-database-monitoring python-mmc-monitoring mmc-web-monitoring'
ZABBIX='zabbix-agent zabbix-frontend-php zabbix-server-mysql'

# Add needed repos
cat << EOF >> /etc/apt/sources.list
# Pulse2
deb http://c1db8761-4d72-472e-b889-73de055bbeee:pass@pulse.mandriva.org/pub/pulse2/server/debian wheezy 3.0.0
deb http://ftp.fr.debian.org/debian/ wheezy main
EOF

DEBIAN_FRONTEND=noninteractive univention-install ${MMC} ${PULSE_DEPS} ${PULSE2} ${APACHE2} ${MYSQL} ${BACKUPPC} ${GLPI} ${PULSE2_GLPI} ${ZABBIX} ${MONITORING} php5-ldap sudo patch pwgen autossh python-requests rpm -y --force-yes
#univention-install ${MMC} ${PULSE2} ${APACHE2} ${PHP5} ${MYSQL} ${BACKUPPC} ${GLPI} ${PULSE2_GLPI} -y --force-yes

#------------------------------------------#

#run-parts ${SCRIPT_DIR}/config/MMC --arg=${SCRIPT_DIR}
#run-parts ${SCRIPT_DIR}/config/PULSE2 --arg=${SCRIPT_DIR}
#run-parts ${SCRIPT_DIR}/config/BACKUPPC
#run-parts ${SCRIPT_DIR}/config/linbox-config/glpi
#run-parts ${SCRIPT_DIR}/config/linbox-config/pulse2 --arg=${SCRIPT_DIR}
