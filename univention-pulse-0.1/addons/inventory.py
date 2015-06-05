#
# (c) 2004-2007 Linbox / Free&ALter Soft, http://linbox.com
#
# $Id$
#
# This file is part of MMC.
#
# MMC is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# MMC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MMC; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
Pulse2 mmc-agent plugin
give a central access to the Managers that can be needed by pulse2 modules
"""

import subprocess
from mmc.plugins.base.computers import ComputerManager
from mmc.support.mmctools import SecurityContext
from json import loads

def runInShell(cmd):
    process = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    return out.strip(), err.strip(), process.returncode

def getSubscriptionInfo():
    
    # Creating root context
    ctx = SecurityContext()
    ctx.userid = 'root'
    
    # Get all machine count
    count = ComputerManager().getComputerCount(ctx)
    
    # Get license max_machines
    out, err, ec = runInShell('/usr/sbin/pulse-licensed -G /etc/pulse-licensing/installation_id -l /etc/pulse-licensing/license.dat -p /etc/pulse-licensing/license -i')
    
    if ec == 0:
        data = loads(out)
        for license in data:
            if license['alias'] == 'pulse':
                max_machines = int(license['custon_number'])
                ts_expiration = int(license['licencingtime'])
                break
        else:
            max_machines = 5
    else:
        max_machines = 5
    
    if max_machines == 5:
        ts_expiration = 0

    return [count, max_machines, ts_expiration]

def canDoInventory():
    count, max_machines, lt = getSubscriptionInfo()
    return count < max_machines
