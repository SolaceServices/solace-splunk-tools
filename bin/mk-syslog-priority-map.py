#!/usr/bin/python
# Create CSV file to map Syslog Priority codes to Severity text
# as defined in RFC 5424
# Ref : https://tools.ietf.org/html/rfc5424.html#page-36
#
# Ramesh Natarajan (nram), Solace PSG

from __future__ import print_function

#------------------------------------------------------------
# globals
#
fn_csv = 'solace_priority.csv'  # output csv file 
d_facility = { 'local0' : 16,   # facility numbers
               'local1' : 17,
               'local2' : 18,
               'local3' : 19,
               'local4' : 20 }
d_severity = {'emergency' : 0, # priority numbers
              'alert'     : 1,
              'critical'  : 2,
              'error'     : 3,
              'warning'   : 4,
              'notice'    : 5,
              'info'      : 6,
              'debug'     : 7 }
#d_priority = {}
d_priority_severity = {}
d_priority_facility = {}

#------------------------------------------------------------
# get_priority
# Calculate priority from facility and severity as defined in 
# rfc5424 PRI section
#
def get_priority(f, s):
       p =  f*8+s
       #print ('   Facility {} Severity {} => Priority {}'.format(f,s,p))
       return p

#------------------------------------------------------------
# print_map
# print dictionary for debug
#
def print_map(t, d):
   print ('\n--- {} ---'.format(t))
   for t, v in d.items():
       print ('\t{} : {}'. format(t, v))

#------------------------------------------------------------
# print_maps
# print dictionaries for debug
#
def print_maps():
   print_map ('Facilities', d_facility)
   print_map ('Severity', d_severity)
   #print_map ('Priority', d_priority)
   print_map ('Priority to Severity Map', d_priority_severity)
   print_map ('Priority to Facility Map', d_priority_facility)

#------------------------------------------------------------
# main
#------------------------------------------------------------

print ('Generating severity and facility maps')
for f, fv in d_facility.items():
   for s, sv in d_severity.items():
       p = get_priority(fv, sv)
       #d_priority['{}.{}'.format(f,s)] = p
       d_priority_severity[p] = s.upper()
       d_priority_facility[p] = f.lower()

#print_maps()
n = 0
print ('Creating CSV file {}'.format(fn_csv))
with open(fn_csv, 'w') as fd_csv: 
   print ('priority,severity,facility', end='\n', file=fd_csv)
   for p in d_priority_severity.keys():
       print (('{},{},{}'. format(p, d_priority_severity[p], 
           d_priority_facility[p])), file=fd_csv)
       n = n+1
fd_csv.close()
print ('\t{} entries written to {}'.format(n, fn_csv))
