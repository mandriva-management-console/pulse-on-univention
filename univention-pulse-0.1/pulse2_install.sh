#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# debconf
#run-parts ${SCRIPT_DIR}/debconf

# Define packages to install
PULSE_DEPS='curl nsis python-sqlalchemy'
MMC='mmc-agent mmc-web-base python-mmc-base mmc-web-dashboard python-mmc-dashboard'
PULSE2='atftpd openbsd-inetd pulse2 dnsutils python-lxml python-mmc-report mmc-web-report python-mmc-update mmc-web-update pulse2-dlp-server pulse-update-manager pulse-licensed pulse-report python-mmc-support mmc-web-support pulse-first-run ttf-arphic-bkai00mp ttf-arphic-bsmi00lp ttf-arphic-gbsn00lp ttf-arphic-gbsn00lp fonts-ipaexfont python-importlib python-pycparser'
APACHE2='apache2-mpm-prefork libapache2-mod-php5'
PHP5='php5 php5-cgi php5-cli php5-common php5-ldap'
MYSQL='mysql-server mysql-client expect'
BACKUPPC='backuppc libfile-rsyncp-perl libio-dirent-perl samba-common-bin python-mmc-backuppc mmc-web-backuppc pulse2-uuid-resolver'
GLPI='glpi fusioninventory-for-glpi glpi-webservices glpi-manufacturersimports'
PULSE2_GLPI='python-mmc-glpi mmc-web-glpi'
PULSE2_INVENTORY='python-mmc-inventory mmc-web-inventory'

# Add needed repos
# squeeze: curl nsis libcrypto++8 python-antlr python-argparse python-xlwt ttf-arphic-bkai00mp ttf-arphic-bsmi00lp ttf-arphic-gbsn00lp uuid-runtime libcrypt-openssl-random-perl perl libperl5.10 libuuid-perl libtext-iconv-perl libtext-charwidth-perl liblocale-gettext-perl perl-base perl-suid backuppc libfile-rsyncp-perl libio-dirent-perl rrdtool python-pyquery libdbi-perl libdbd-mysql-perl libhtml-template-perl libphp-phpmailer libjs-extjs x-ttcidfont-conf
# backports: python-sqlalchemy(-ext) (0.7) tinymce 
cat << EOF >> /etc/apt/sources.list
# Squeeze repos
deb http://cdn.debian.net/debian squeeze main
deb http://ftp.debian.org/debian/ squeeze-updates main
deb http://security.debian.org/ squeeze/updates main

# Squeeze backports
deb http://http.debian.net/debian-backports squeeze-backports main

# Pulse
deb http://2bc60578-6e20-41cc-a1aa-c89dfcad9b6b:a0@pulse.mandriva.org/pub/pulse2/server/debian squeeze 2.0
EOF

# For a correct backuppc installation, some packages must pinned
cat << EOF >> /etc/apt/preferences
Package: *
Pin: origin "cdn.debian.net"
Pin-Priority: 1

Package: *
Pin: origin "http.debian.net"
Pin-Priority: 1

Package: *
Pin: origin "security.debian.org"
Pin-Priority: 1

Package: *
Pin: origin "ftp.debian.org"
Pin-Priority: 1

Package: libcrypt-openssl-random-perl liblocale-gettext-perl libperl5.10 libsocket6-perl libtext-charwidth-perl libtext-iconv-perl libuuid-perl perl perl-base libdbi-perl libdbd-mysql-perl
Pin: origin "cdn.debian.net"
Pin-Priority: 900

Package: python-sqlalchemy python-sqlalchemy-ext
Pin: origin "http.debian.net"
Pin-Priority: 900
EOF

# Speed up Pulse install
univention-install eatmydata -y --force-yes
ln -s /usr/bin/eatmydata /usr/local/bin/aptitude
ln -s /usr/bin/eatmydata /usr/local/bin/apt-get
ln -s /usr/bin/eatmydata /usr/local/bin/univention-install
ln -s /usr/bin/eatmydata /usr/local/bin/univention-remove

DEBIAN_FRONTEND=noninteractive univention-install ${MMC} ${PULSE2} ${APACHE2} ${MYSQL} ${BACKUPPC} ${GLPI} ${PULSE2_GLPI} php5-ldap sudo patch pwgen autossh python-requests rpm -y --force-yes
#univention-install ${MMC} ${PULSE2} ${APACHE2} ${PHP5} ${MYSQL} ${BACKUPPC} ${GLPI} ${PULSE2_GLPI} -y --force-yes

#------------------------------------------#

#run-parts ${SCRIPT_DIR}/config/MMC --arg=${SCRIPT_DIR}
#run-parts ${SCRIPT_DIR}/config/PULSE2 --arg=${SCRIPT_DIR}
#run-parts ${SCRIPT_DIR}/config/BACKUPPC
#run-parts ${SCRIPT_DIR}/config/linbox-config/glpi
#run-parts ${SCRIPT_DIR}/config/linbox-config/pulse2 --arg=${SCRIPT_DIR}
