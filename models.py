__author__ = 'agustin'

import json
import urllib2

"""
    Check draft on RDAP JSON-Response
    https://tools.ietf.org/html/draft-ietf-weirds-json-response-11
"""

def run():

    # web
    # r = urllib2.urlopen("http://127.0.0.1:8080/rdap/ip/200.7.84/24?apikey=bf30f017-c6f1-403c-85d1-7f2f5ed12b8f")
    # text = r.read()

    # local file
    text = open('example.rdap', 'r').read()
    entity = json.loads(text)

    RdapObject.parse(entity)
#
#
# for s in structures:
#     try:
#         print "%s: %s" % (s, entity[s])
#     except KeyError:
#         print "Problem with Key %s" % s




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

class PublicId():
    def __init__(self, type, identifier):
        self.type = type
        self.identifier = identifier

class IpAddresses():
    def __init__(self, v4, v6):
        self.v4 = v4
        self.v6 = v6



class RdapObject():
    """

    """

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

    @staticmethod
    def parse(text):
        """
            Parse
        """

        members = dict(rdapConformance="rdapConformance", links="links", notices="notices", remarks="remarks", events="events", status="status", port43="port43", publicIds="publicIds", objectClassName="objectClassName")
        present = [] # those members present in text

        for m in members:
            try:
                print "%s: %s" % (m, text[m])
                present.append(text[m])
            except KeyError:
                print "Problem with Key %s" % m


class Entity(RdapObject):
    """
        https://tools.ietf.org/html/draft-ietf-weirds-json-response-12#section-5.1
    """
    def __init__(self, roles, publicIds, entities, networks, autnums, asEventActor):
        self.roles = roles
        self.publicIds = publicIds
        self.entities = entities
        self.networks = networks
        self.autnums = autnums
        self.asEventActor = asEventActor

class NameServer(RdapObject):
    """
        https://tools.ietf.org/html/draft-ietf-weirds-json-response-12#section-5.2
    """

    def __init__(self, ldhName, unicodeName, ipAddresses, entities):
        self.ldhName = ldhName
        self.unicodeName = unicodeName
        self.ipAddresses = ipAddresses
        self.entities = entities

class Ip():
    """
        https://tools.ietf.org/html/draft-ietf-weirds-json-response-12#section-5.4
    """

    def __init__(self, startAddress, endAddress, ipVersion, name, type, country, parentHandle):
        self.startAddress = startAddress
        self.endAddress = endAddress
        self.ipVersion = ipVersion
        self.name = name
        self.type = type
        self.country = country
        self.parentHandle = parentHandle
        self.entities = entities

class Autnum():
    """
        https://tools.ietf.org/html/draft-ietf-weirds-json-response-12#section-5.5
    """

    def __init__(self, startAutnum, endAutnum, name, type):
        self.startAutnum = startAutnum
        self.endAutnum = endAutnum
        self.name = name
        self.type = type
        self.country = country
        self.entities = entities

# class Domain(RdapObject):

run()