__author__ = 'agustin'

import json
import urllib2

"""
    Check draft on RDAP JSON-Response
    https://tools.ietf.org/html/draft-ietf-weirds-json-response-11
"""

# web
# r = urllib2.urlopen("http://127.0.0.1:8080/rdap/ip/200.7.84/24?apikey=bf30f017-c6f1-403c-85d1-7f2f5ed12b8f")
# text = r.read()

# local file
text = open('example.rdap', 'r').read()
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

class Notices(): # and Remarks
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

class publicId():
    def __init__(self, type, identifier):
        self.type = type
        self.identifier = identifier





class RdapObject():
    def __init__(self, objectClassName, handle, roles, entities, remarks, links, events, status, port43):
        self.objectClassName = objectClassName
        self.handle = handle
        self.roles = roles
        self.entities = entities
        self.remarks = remarks
        self.links = links
        self.events = events
        self.status = status
        self.port43 = port43

class Entity(RdapObject):
    def __init__(self, roles, publicIds, entities, networks, autnums, asEventActor):
        self.roles = roles
        self.publicIds = publicIds
        self.entities = entities
        self.networks = networks
        self.autnums = autnums
        self.asEventActor = asEventActor

class Autnum():
    def __init__(self):
        self.startAutnum
        self.endAutnum
        self.name