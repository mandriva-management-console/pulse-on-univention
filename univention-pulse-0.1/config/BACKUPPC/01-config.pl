#!/bin/bash

sed -i 's!^\(\$Conf{BackupPCUserVerify}[[:space:]]*=\).*!\1 0;!' /etc/backuppc/config.pl

sed -i 's!^\(\$Conf{FullKeepCnt}[[:space:]]*=\).*!\1 4;!' /etc/backuppc/config.pl
sed -i 's!^\(\$Conf{FullKeepCntMin}[[:space:]]*=\).*!\1 2;!' /etc/backuppc/config.pl
sed -i 's!^\(\$Conf{IncrKeepCnt}[[:space:]]*=\).*!\1 12;!' /etc/backuppc/config.pl
sed -i 's!^\(\$Conf{IncrKeepCntMin}[[:space:]]*=\).*!\1 4;!' /etc/backuppc/config.pl

sed -i 's!^\([[:space:]]\+.\)\-\-devices\(.,.*\)!\1-D\2!' /etc/backuppc/config.pl

sed -i 's!\-U \$userName \-E \-N \-d 1!-U $userName -E -d 1!' /etc/backuppc/config.pl

sed -i 's!^\(\$Conf{RsyncClient\(Restore\)\?Cmd}[[:space:]]*=\).*$!\1 MDVFIXME/usr/bin/env LANG=en $sshPath -q -x -l root -o StrictHostKeyChecking=no $host $rsyncPath $argList+MDVFIXME;!' /etc/backuppc/config.pl
sed -i "s!MDVFIXME!'!g" /etc/backuppc/config.pl
