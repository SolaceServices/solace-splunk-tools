# Syslog severity mapping in Splunk

When Solace sylogs are forwared to Splunk, sometimes they may appear as numbers such as <142>, <166>, etc. instead of familiar "INFO", "WARNING". This is beacause Splunk displays the codes as is without expanding them. These mappings are defined in [RFC 5424](https://tools.ietf.org/html/rfc5424.html#page-36) if you are really curious.

Splunk supports [lookup tables](https://docs.splunk.com/Documentation/Splunk/8.2.0/Knowledge/Aboutdatasets?ref=hk) that can be used to remap these fields. This is a 3 step process.

1. Extract existing numeric code to a field using [field extraction](https://docs.splunk.com/Documentation/Splunk/8.2.0/Knowledge/ExtractfieldsinteractivelywithIFX). eg: priority
2. Upload mapping csv file as Lookup table.
    1. Verify its working with the following search.
    > | inputlookup solace-priority.csv
3. Remap and create new field with string values eg: severity.
    1. Verify this extracts new field with
    > source="solace-event" index="solace" sourcetype="syslog" | lookup solace-priority.csv priority OUTPUT severity

You can use the script [mk-syslog-priority-map.py](bin/mk-syslog-priority-map.py) to generate the datafile afresh or grab it from [solace_priority.csv](data/solace_priority.csv)

Pl see [docs](docs/) folder for additional help.

## AUTHORS

Ramesh Natarajan (nram), Solace PSG