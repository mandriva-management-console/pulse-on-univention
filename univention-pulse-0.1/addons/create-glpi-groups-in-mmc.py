#!/usr/bin/python

from mmc.plugins.base import createGroup, changeGroupDescription
from mmc.plugins.base.config import BasePluginConfig
from mmc.plugins.glpi.config import GlpiConfig
import ldap
import MySQLdb
import sys

# GLPI MySQL parameters
configglpi = GlpiConfig("glpi")
dbhost = configglpi.dbhost
dbname = configglpi.dbname
dbuser = configglpi.dbuser
dbpasswd = configglpi.dbpasswd

# MySQL connexion
mysqlcon = None

# Get GLPI profile list from MySQL
try:
    mysqlcon = MySQLdb.connect(dbhost,dbuser,dbpasswd,dbname)
    mysqlcur = mysqlcon.cursor()
    mysqlcur.execute("SELECT %s FROM %s" % ("name","glpi_profiles"))
    glpi_profiles = mysqlcur.fetchall()
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

# Create GLPI-<group> in MMC
# Also create it in GLPI
# GLPI will query the LDAP for its content but it requires the initial import
# to be done through the interface

configbase = BasePluginConfig("base")
groupsbasedn = configbase.getdn("ldap", "baseGroupsDN")

for group in glpi_profiles:
  group = group[0]
  # LDAP stuff
  try:
    createGroup("GLPI-"+group)
  except ldap.ALREADY_EXISTS:
    pass
  changeGroupDescription("GLPI-"+group, "Users with GLPI "+group+" profile")
  
  # MySQL GLPI stuff

  # BEFORE dropping groups and rules, clean link tables;
  # May not exists yet:
  try:
    # Get group id
    mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_groups","GLPI-"+group))
    groupid = mysqlcur.fetchone()[0]
    # Get its rules id
    mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_rules","Pulse-"+group))
    rulesid = mysqlcur.fetchone()[0]
    # Get GLPI's internal profile
    mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_profiles",group))
    profilesid = mysqlcur.fetchone()[0]
    # Drop entry from glpi_rulecriterias link table
    mysqlcur.execute("DELETE FROM %s WHERE pattern = %s AND rules_id = %s" % ("glpi_rulecriterias",groupid,rulesid))
    # Drop entry from glpi_ruleactions link table
    mysqlcur.execute("DELETE FROM %s WHERE rules_id = %s AND field = \"profiles_id\" AND value = %s" % ("glpi_ruleactions",rulesid,profilesid))
  except:
    pass

  # Create groups
  mysqlcur.execute("DELETE FROM %s WHERE name = \"%s\"" % ("glpi_groups","GLPI-"+group))
  mysqlcur.execute("INSERT INTO %s (name,comment,ldap_group_dn,date_mod,completename,level) VALUES (\"%s\",\"%s\",\"%s\",%s,\"%s\",%s)" % ("glpi_groups","GLPI-"+group,"Members of group GLPI-"+group+" in Pulse","cn=GLPI-"+group+","+groupsbasedn,"NOW()","GLPI-"+group,"1"))
  
  # Corresponding rules
  mysqlcur.execute("DELETE FROM %s WHERE name = \"%s\"" % ("glpi_rules","Pulse-"+group))
  mysqlcur.execute("INSERT INTO %s (sub_type,ranking,name,description,`match`,is_active,date_mod) VALUES (\"%s\",%s,\"%s\",\"%s\",\"%s\",%s,%s)" % ("glpi_rules","RuleRight","2","Pulse-"+group,"Members of group GLPI-"+group+" in Pulse","AND","1","NOW()"))
  
  # Get group id
  mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_groups","GLPI-"+group))
  groupid = mysqlcur.fetchone()[0]
  # Get its rules id
  mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_rules","Pulse-"+group))
  rulesid = mysqlcur.fetchone()[0]
  # Get GLPI's internal profile
  mysqlcur.execute("SELECT id from %s WHERE name = \"%s\"" % ("glpi_profiles",group))
  profilesid = mysqlcur.fetchone()[0]

  # Link the rules with the group membership criteria
  mysqlcur.execute("INSERT INTO %s (rules_id,criteria,pattern) VALUES (%s,\"%s\",%s)" % ("glpi_rulecriterias",rulesid,"GROUPS",groupid))

  # Link the rules with profiles selection table
  mysqlcur.execute("INSERT INTO %s (rules_id,action_type,field,value) VALUES (%s,\"%s\",\"%s\",%s)" % ("glpi_ruleactions",rulesid,"assign","profiles_id",profilesid))
  # Assign to root entity
  mysqlcur.execute("INSERT INTO %s (rules_id,action_type,field,value) VALUES (%s,\"%s\",\"%s\",%s)" % ("glpi_ruleactions",rulesid,"assign","entities_id","0"))
  # And make it recursive
  mysqlcur.execute("INSERT INTO %s (rules_id,action_type,field,value) VALUES (%s,\"%s\",\"%s\",%s)" % ("glpi_ruleactions",rulesid,"assign","is_recursive","1"))

# MySQL connexion
mysqlcon.close()
