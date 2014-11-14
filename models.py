__author__ = 'agustin'

import json
import urllib2

"""
    Check draft on RDAP JSON-Response
    https://tools.ietf.org/html/draft-ietf-weirds-json-response-11
"""

r = urllib2.urlopen("http://127.0.0.1:8080/rdap/ip/200.7.84/24?apikey=bf30f017-c6f1-403c-85d1-7f2f5ed12b8f")
text = r.read()
entity = json.loads(text)

# commons.events = ""
structures = dict(rdapConformance="rdapConformance", links="links", notices="notices", remarks="remarks",
                  events="events", status="status", port43="port43", publicIds="publicIds",
                  objectClassName="objectClassName")

structures_events = ['eventAction', 'eventActor', 'eventDate', 'links']
structures_publicIds = ['type', 'identifier']

for s in structures:
    try:
        print "%s: %s" % (s, entity[s])
    except KeyError:
        print "Problem with Key %s" % s




class Links():
    def __init__(self, value, rel, href, type):
        self.value = value
        self.rel = rel
        self.href = href
        self.type = type

class Notices():
    def __init__(self, title, type, description, links):
        self.title = title
        self.type = type
        self.description = description
        self.links = links

class Events():
    def __init__(self, eventAction, eventActor, eventDate, links):
        self.eventAction = eventAction
        self.eventActor = eventActor
        self.eventDate = eventDate
        self.links = links

class Entity():
    def __init__(self, links):
        self.links = links

class RdapObject():
    def __init__(self, links):
        self.links = links