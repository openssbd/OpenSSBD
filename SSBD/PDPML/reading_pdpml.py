# Reading in PDPML files - just checking on usage

import pyxb
#import pdpml       # pyxb generated python class file
import sys

from SSBD.PDPML import pdpml_api

if __name__ == '__main__':
 reading in sample-pdpml.xml file using pyxb
    xml = file('sample-pdpml.xml').read()
    m = pdpml.CreateFromDocument(xml)

# reading in sample-pdpml.xml file using generateDS
#    m = pdpml_api.parse('sample-pdpml.xml')

    print 'contactname: %s organization:%s' % (m.contact.contactname, m.contact.organization)
    pretty_print=False
    m.export(sys.stdout, 0)
