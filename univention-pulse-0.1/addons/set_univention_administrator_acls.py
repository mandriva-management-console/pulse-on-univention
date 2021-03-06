#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# (c) 2004-2007 Linbox / Free&ALter Soft, http://linbox.com
# (c) 2007-2012 Mandriva, http://www.mandriva.com/
#
# This file is part of Mandriva Management Console (MMC).
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
A script for massively setting users acls
"""

from sys import exit
from mmc.plugins.base import getUsersLdap, getUserAcl, setUserAcl

uid = 'Administrator'

passwordAcl = ":backuppc#backuppc#index:backuppc#backuppc#hostStatus:backuppc#backuppc#EditBackupProfile:backuppc#backuppc#EditPeriodProfile:backuppc#backuppc#pending:backuppc#backuppc#BrowseBackups:backuppc#backuppc#BrowseShareNames:backuppc#backuppc#BrowseFiles:backuppc#backuppc#ViewProfiles:backuppc#backuppc#deleteProfile:backuppc#backuppc#download:base#main#default:base#logview#index:base#status#index:base#users#index:base#users#editacl:base#computers#index:base#computers#add:base#computers#edit:base#computers#delete:base#computers#computersgroupcreator:base#computers#computersgroupcreatesubedit:base#computers#computersgroupcreatesubdel:base#computers#computersgroupedit:base#computers#computersgroupsubedit:base#computers#computersgroupsubdel:base#computers#tmpdisplay:base#computers#display:base#computers#edit_share:base#computers#creator_step2:base#computers#save:base#computers#save_detail:base#computers#list:base#computers#delete_group:base#computers#remove_machine:base#computers#csv:base#computers#updateMachineCache:base#computers#createStaticGroup:base#computers#createAntivirusStaticGroup:base#computers#createOSStaticGroup:base#computers#groupglpitabs:base#computers#glpitabs:base#computers#register_target:base#computers#createCustomMenuStaticGroup:base#computers#imgtabs:base#computers#bootmenu_remove:base#computers#showtarget:base#computers#showsyncstatus:base#computers#addservice:base#computers#editservice:base#computers#delservice:base#computers#addimage:base#computers#editimage:base#computers#images_delete:base#computers#images_iso:base#computers#remove_from_pull:base#computers#groupmsctabs:base#computers#msctabs:base#computers#download_file:base#computers#download_file_remove:base#computers#download_file_get:base#computers#vnc_client:base#computers#msctabsplay:base#computers#msctabspause:base#computers#msctabsstop:base#computers#msctabsstatus:base#computers#reschedule:base#computers#msctabssinglestatus:base#computers#package_detail:base#computers#start_command:base#computers#start_adv_command:base#computers#convergence:base#computers#start_quick_action:base#computers#packages:base#computers#statuscsv:base#computers#computers_list:base#computers#select_location:dashboard#main#default:glpi#glpi#glpi_dashboard:imaging#manage#index:imaging#manage#master:imaging#manage#master_remove:imaging#manage#master_delete:imaging#manage#master_edit:imaging#manage#master_add:imaging#manage#master_iso:imaging#manage#service:imaging#manage#service_edit:imaging#manage#service_del:imaging#manage#service_add:imaging#manage#service_remove:imaging#manage#service_show_used:imaging#manage#bootmenu:imaging#manage#bootmenu_up:imaging#manage#bootmenu_down:imaging#manage#bootmenu_edit:imaging#manage#postinstall:imaging#manage#postinstall_edit:imaging#manage#postinstall_duplicate:imaging#manage#postinstall_create_boot_service:imaging#manage#postinstall_redirect_to_boot_service:imaging#manage#postinstall_delete:imaging#manage#configuration:imaging#manage#save_configuration:imaging#manage#computersprofilecreator:imaging#manage#computersprofilecreatesubedit:imaging#manage#computersprofilecreatesubdel:imaging#manage#computersprofileedit:imaging#manage#computersprofilesubedit:imaging#manage#computersprofilesubdel:imaging#manage#list_profiles:imaging#manage#groupregister_target:imaging#manage#groupimgtabs:imaging#manage#groupbootmenu_remove:imaging#manage#display:imaging#manage#delete_group:imaging#manage#computersgroupedit:imaging#manage#edit_share:imaging#manage#groupmsctabs:msc#logs#consult:msc#logs#consultAll:msc#logs#viewLogs:msc#logs#all:msc#logs#pending:msc#logs#running:msc#logs#finished:msc#logs#custom:pkgs#pkgs#index:pkgs#pkgs#add:pkgs#pkgs#edit:pkgs#pkgs#pending:pkgs#pkgs#rsync:pkgs#pkgs#delete:report#report#index:report#report#get_file:support#support#connect:support#support#disconnect:update#update#index:update#update#viewUpdates:update#update#ajaxUpdates:update#update#enableUpdate:update#update#disableUpdate:update#update#settings:update#update#installProductUpdates:update#update#viewProductUpdates:update#update#ajaxInstallProductUpdates:backuppc#backuppc#hostStatus#tab1:backuppc#backuppc#hostStatus#tab2:backuppc#backuppc#hostStatus#tab3:base#computers#computersgroupcreator#tabdyn:base#computers#computersgroupcreator#tabsta:base#computers#computersgroupcreator#tabfromfile:base#computers#computersgroupcreatesubedit#tabdyn:base#computers#computersgroupcreatesubedit#tabsta:base#computers#computersgroupcreatesubedit#tabfromfile:base#computers#computersgroupcreatesubdel#tabdyn:base#computers#computersgroupcreatesubdel#tabsta:base#computers#computersgroupcreatesubdel#tabfromfile:base#computers#groupglpitabs#tab0:base#computers#groupglpitabs#tab1:base#computers#groupglpitabs#tab2:base#computers#groupglpitabs#tab3:base#computers#groupglpitabs#tab4:base#computers#groupglpitabs#tab5:base#computers#groupglpitabs#tab6:base#computers#groupglpitabs#tab7:base#computers#glpitabs#tab0:base#computers#glpitabs#tab1:base#computers#glpitabs#tab2:base#computers#glpitabs#tab3:base#computers#glpitabs#tab4:base#computers#glpitabs#tab5:base#computers#glpitabs#tab6:base#computers#glpitabs#tab7:base#computers#imgtabs#tabbootmenu:base#computers#imgtabs#tabimages:base#computers#imgtabs#tabservices:base#computers#imgtabs#tabimlogs:base#computers#imgtabs#tabconfigure:base#computers#groupmsctabs#grouptablaunch:base#computers#groupmsctabs#grouptabbundle:base#computers#groupmsctabs#grouptablogs:base#computers#msctabs#tablaunch:base#computers#msctabs#tabbundle:base#computers#msctabs#tablogs:imaging#manage#computersprofilecreator#tabdyn:imaging#manage#computersprofilecreator#tabsta:imaging#manage#computersprofilecreator#tabfromfile:imaging#manage#computersprofilecreatesubedit#tabdyn:imaging#manage#computersprofilecreatesubedit#tabsta:imaging#manage#computersprofilecreatesubedit#tabfromfile:imaging#manage#computersprofilecreatesubdel#tabdyn:imaging#manage#computersprofilecreatesubdel#tabsta:imaging#manage#computersprofilecreatesubdel#tabfromfile:imaging#manage#groupimgtabs#grouptabbootmenu:imaging#manage#groupimgtabs#grouptabimages:imaging#manage#groupimgtabs#grouptabservices:imaging#manage#groupimgtabs#grouptabimlogs:imaging#manage#groupimgtabs#grouptabconfigure:imaging#manage#groupmsctabs#grouptablaunch:imaging#manage#groupmsctabs#grouptabbundle:imaging#manage#groupmsctabs#grouptablogs:imaging#manage#groupmsctabs#grouptabhistory/:jpegPhoto=rw:uid=rw:sn=rw:givenName=rw:homeDir=rw:loginShell=rw:title=rw:mail=rw:telephoneNumber=rw:mobile=rw:facsimileTelephoneNumber=rw:homePhone=rw:primary=rw:secondary=rw:cn=rw:displayName=rw:pass=rw:confpass=rw:isBaseDesactive=rw"


try:
    getUserAcl(uid)
except Exception, e:
    print e
    exit(1)

setUserAcl(uid, passwordAcl)
