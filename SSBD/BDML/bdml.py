# ./bdml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e01766ecb53ded9d555cf79aee1c1c2bc2d89e22
# Generated 2013-07-05 17:11:18.744517 by PyXB version 1.2.2
# Namespace http://ssbd.qbic.riken.jp/bdml/level1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:787c11c2-e54a-11e2-9bb5-0800270a691a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://ssbd.qbic.riken.jp/bdml/level1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://ssbd.qbic.riken.jp/bdml/level1}UnitKind
class UnitKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UnitKind')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 9, 1)
    _Documentation = None
UnitKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=UnitKind, enum_prefix=None)
UnitKind.ampere = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'ampere', tag=u'ampere')
UnitKind.candela = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'candela', tag=u'candela')
UnitKind.celsius = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'celsius', tag=u'celsius')
UnitKind.coulomb = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'coulomb', tag=u'coulomb')
UnitKind.dimensionless = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'dimensionless', tag=u'dimensionless')
UnitKind.farad = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'farad', tag=u'farad')
UnitKind.gram = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'gram', tag=u'gram')
UnitKind.gray = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'gray', tag=u'gray')
UnitKind.henry = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'henry', tag=u'henry')
UnitKind.hertz = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'hertz', tag=u'hertz')
UnitKind.hour = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'hour', tag=u'hour')
UnitKind.intensity = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'intensity', tag=u'intensity')
UnitKind.item = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'item', tag=u'item')
UnitKind.joule = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'joule', tag=u'joule')
UnitKind.katal = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'katal', tag=u'katal')
UnitKind.kelvin = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'kelvin', tag=u'kelvin')
UnitKind.kilogram = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'kilogram', tag=u'kilogram')
UnitKind.liter = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'liter', tag=u'liter')
UnitKind.litre = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'litre', tag=u'litre')
UnitKind.lumen = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'lumen', tag=u'lumen')
UnitKind.lux = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'lux', tag=u'lux')
UnitKind.meter = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'meter', tag=u'meter')
UnitKind.metre = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'metre', tag=u'metre')
UnitKind.micrometer = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'micrometer', tag=u'micrometer')
UnitKind.micrometre = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'micrometre', tag=u'micrometre')
UnitKind.minute = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'minute', tag=u'minute')
UnitKind.mole = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'mole', tag=u'mole')
UnitKind.newton = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'newton', tag=u'newton')
UnitKind.ohm = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'ohm', tag=u'ohm')
UnitKind.pascal = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'pascal', tag=u'pascal')
UnitKind.pixel = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'pixel', tag=u'pixel')
UnitKind.radian = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'radian', tag=u'radian')
UnitKind.relative = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'relative', tag=u'relative')
UnitKind.second = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'second', tag=u'second')
UnitKind.siemens = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'siemens', tag=u'siemens')
UnitKind.sievert = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'sievert', tag=u'sievert')
UnitKind.steradian = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'steradian', tag=u'steradian')
UnitKind.tesla = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'tesla', tag=u'tesla')
UnitKind.volt = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'volt', tag=u'volt')
UnitKind.watt = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'watt', tag=u'watt')
UnitKind.weber = UnitKind._CF_enumeration.addEnumeration(unicode_value=u'weber', tag=u'weber')
UnitKind._InitializeFacetMap(UnitKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'UnitKind', UnitKind)

# Atomic simple type: {http://ssbd.qbic.riken.jp/bdml/level1}BasedOn
class BasedOn (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BasedOn')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 55, 1)
    _Documentation = None
BasedOn._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=BasedOn, enum_prefix=None)
BasedOn.Measurement = BasedOn._CF_enumeration.addEnumeration(unicode_value=u'Measurement', tag=u'Measurement')
BasedOn.Simulation = BasedOn._CF_enumeration.addEnumeration(unicode_value=u'Simulation', tag=u'Simulation')
BasedOn._InitializeFacetMap(BasedOn._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'BasedOn', BasedOn)

# Atomic simple type: {http://ssbd.qbic.riken.jp/bdml/level1}UUIDType
class UUIDType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'UUIDType')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 62, 1)
    _Documentation = None
UUIDType._CF_pattern = pyxb.binding.facets.CF_pattern()
UUIDType._CF_pattern.addPattern(pattern=u'[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
UUIDType._InitializeFacetMap(UUIDType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'UUIDType', UUIDType)

# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Info with content type ELEMENT_ONLY
class Info (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Info with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Info')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 68, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}bdmlID uses Python identifier bdmlID
    __bdmlID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'bdmlID'), 'bdmlID', '__httpssbd_qbic_riken_jpbdmllevel1_Info_httpssbd_qbic_riken_jpbdmllevel1bdmlID', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 70, 3), )

    
    bdmlID = property(__bdmlID.value, __bdmlID.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpssbd_qbic_riken_jpbdmllevel1_Info_httpssbd_qbic_riken_jpbdmllevel1title', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 71, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'version'), 'version', '__httpssbd_qbic_riken_jpbdmllevel1_Info_httpssbd_qbic_riken_jpbdmllevel1version', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 72, 3), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}release uses Python identifier release
    __release = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'release'), 'release', '__httpssbd_qbic_riken_jpbdmllevel1_Info_httpssbd_qbic_riken_jpbdmllevel1release', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 73, 3), )

    
    release = property(__release.value, __release.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}license uses Python identifier license
    __license = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'license'), 'license', '__httpssbd_qbic_riken_jpbdmllevel1_Info_httpssbd_qbic_riken_jpbdmllevel1license', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 74, 3), )

    
    license = property(__license.value, __license.set, None, None)

    _ElementMap.update({
        __bdmlID.name() : __bdmlID,
        __title.name() : __title,
        __version.name() : __version,
        __release.name() : __release,
        __license.name() : __license
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Info', Info)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Summary with content type ELEMENT_ONLY
class Summary (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Summary with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Summary')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 78, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'description'), 'description', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1description', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 80, 3), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}organism uses Python identifier organism
    __organism = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organism'), 'organism', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1organism', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 81, 3), )

    
    organism = property(__organism.value, __organism.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}datatype uses Python identifier datatype
    __datatype = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'datatype'), 'datatype', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1datatype', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 82, 3), )

    
    datatype = property(__datatype.value, __datatype.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'identifier'), 'identifier', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1identifier', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 83, 3), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}basedon uses Python identifier basedon
    __basedon = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'basedon'), 'basedon', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1basedon', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 84, 3), )

    
    basedon = property(__basedon.value, __basedon.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}contributors uses Python identifier contributors
    __contributors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'contributors'), 'contributors', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1contributors', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 85, 3), )

    
    contributors = property(__contributors.value, __contributors.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}citation uses Python identifier citation
    __citation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'citation'), 'citation', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1citation', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 86, 3), )

    
    citation = property(__citation.value, __citation.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}PMID uses Python identifier PMID
    __PMID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PMID'), 'PMID', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1PMID', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 87, 3), )

    
    PMID = property(__PMID.value, __PMID.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}dblink uses Python identifier dblink
    __dblink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dblink'), 'dblink', '__httpssbd_qbic_riken_jpbdmllevel1_Summary_httpssbd_qbic_riken_jpbdmllevel1dblink', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 88, 3), )

    
    dblink = property(__dblink.value, __dblink.set, None, None)

    _ElementMap.update({
        __description.name() : __description,
        __organism.name() : __organism,
        __datatype.name() : __datatype,
        __identifier.name() : __identifier,
        __basedon.name() : __basedon,
        __contributors.name() : __contributors,
        __citation.name() : __citation,
        __PMID.name() : __PMID,
        __dblink.name() : __dblink
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Summary', Summary)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Contact with content type ELEMENT_ONLY
class Contact (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Contact with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Contact')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 92, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}contactname uses Python identifier contactname
    __contactname = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'contactname'), 'contactname', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1contactname', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 94, 3), )

    
    contactname = property(__contactname.value, __contactname.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}E-mail uses Python identifier E_mail
    __E_mail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'E-mail'), 'E_mail', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1E_mail', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 95, 3), )

    
    E_mail = property(__E_mail.value, __E_mail.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}phone uses Python identifier phone
    __phone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phone'), 'phone', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1phone', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 96, 3), )

    
    phone = property(__phone.value, __phone.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}URL uses Python identifier URL
    __URL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'URL'), 'URL', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1URL', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 97, 3), )

    
    URL = property(__URL.value, __URL.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}organization uses Python identifier organization
    __organization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organization'), 'organization', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1organization', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 98, 3), )

    
    organization = property(__organization.value, __organization.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}department uses Python identifier department
    __department = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'department'), 'department', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1department', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 99, 3), )

    
    department = property(__department.value, __department.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}laboratory uses Python identifier laboratory
    __laboratory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'laboratory'), 'laboratory', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1laboratory', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 100, 3), )

    
    laboratory = property(__laboratory.value, __laboratory.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'street'), 'street', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1street', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 101, 3), )

    
    street = property(__street.value, __street.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'city'), 'city', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1city', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 102, 3), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'code'), 'code', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1code', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 103, 3), )

    
    code = property(__code.value, __code.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpssbd_qbic_riken_jpbdmllevel1_Contact_httpssbd_qbic_riken_jpbdmllevel1country', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 104, 3), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __contactname.name() : __contactname,
        __E_mail.name() : __E_mail,
        __phone.name() : __phone,
        __URL.name() : __URL,
        __organization.name() : __organization,
        __department.name() : __department,
        __laboratory.name() : __laboratory,
        __street.name() : __street,
        __city.name() : __city,
        __code.name() : __code,
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Contact', Contact)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Methods with content type ELEMENT_ONLY
class Methods (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Methods with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Methods')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 108, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}methodssummary uses Python identifier methodssummary
    __methodssummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'methodssummary'), 'methodssummary', '__httpssbd_qbic_riken_jpbdmllevel1_Methods_httpssbd_qbic_riken_jpbdmllevel1methodssummary', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 110, 3), )

    
    methodssummary = property(__methodssummary.value, __methodssummary.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}environment uses Python identifier environment
    __environment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'environment'), 'environment', '__httpssbd_qbic_riken_jpbdmllevel1_Methods_httpssbd_qbic_riken_jpbdmllevel1environment', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 111, 3), )

    
    environment = property(__environment.value, __environment.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'input'), 'input', '__httpssbd_qbic_riken_jpbdmllevel1_Methods_httpssbd_qbic_riken_jpbdmllevel1input', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 112, 3), )

    
    input = property(__input.value, __input.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}pdpml uses Python identifier pdpml
    __pdpml = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pdpml'), 'pdpml', '__httpssbd_qbic_riken_jpbdmllevel1_Methods_httpssbd_qbic_riken_jpbdmllevel1pdpml', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 113, 3), )

    
    pdpml = property(__pdpml.value, __pdpml.set, None, None)

    _ElementMap.update({
        __methodssummary.name() : __methodssummary,
        __environment.name() : __environment,
        __input.name() : __input,
        __pdpml.name() : __pdpml
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Methods', Methods)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}ScaleUnit with content type ELEMENT_ONLY
class ScaleUnit (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}ScaleUnit with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ScaleUnit')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 117, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}xScale uses Python identifier xScale
    __xScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xScale'), 'xScale', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1xScale', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 119, 3), )

    
    xScale = property(__xScale.value, __xScale.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}yScale uses Python identifier yScale
    __yScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'yScale'), 'yScale', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1yScale', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 120, 3), )

    
    yScale = property(__yScale.value, __yScale.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}zScale uses Python identifier zScale
    __zScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'zScale'), 'zScale', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1zScale', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 121, 3), )

    
    zScale = property(__zScale.value, __zScale.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}xyzUnit uses Python identifier xyzUnit
    __xyzUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'xyzUnit'), 'xyzUnit', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1xyzUnit', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 122, 3), )

    
    xyzUnit = property(__xyzUnit.value, __xyzUnit.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}tScale uses Python identifier tScale
    __tScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tScale'), 'tScale', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1tScale', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 123, 3), )

    
    tScale = property(__tScale.value, __tScale.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}tUnit uses Python identifier tUnit
    __tUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'tUnit'), 'tUnit', '__httpssbd_qbic_riken_jpbdmllevel1_ScaleUnit_httpssbd_qbic_riken_jpbdmllevel1tUnit', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 124, 3), )

    
    tUnit = property(__tUnit.value, __tUnit.set, None, None)

    _ElementMap.update({
        __xScale.name() : __xScale,
        __yScale.name() : __yScale,
        __zScale.name() : __zScale,
        __xyzUnit.name() : __xyzUnit,
        __tScale.name() : __tScale,
        __tUnit.name() : __tUnit
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ScaleUnit', ScaleUnit)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Target with content type ELEMENT_ONLY
class Target (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Target with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Target')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 128, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpssbd_qbic_riken_jpbdmllevel1_Target_httpssbd_qbic_riken_jpbdmllevel1name', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 130, 3), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'scale'), 'scale', '__httpssbd_qbic_riken_jpbdmllevel1_Target_httpssbd_qbic_riken_jpbdmllevel1scale', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 131, 3), )

    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}unit uses Python identifier unit
    __unit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'unit'), 'unit', '__httpssbd_qbic_riken_jpbdmllevel1_Target_httpssbd_qbic_riken_jpbdmllevel1unit', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 132, 3), )

    
    unit = property(__unit.value, __unit.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __scale.name() : __scale,
        __unit.name() : __unit
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Target', Target)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Point with content type ELEMENT_ONLY
class Point (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Point with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Point')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 136, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}pointCoord uses Python identifier pointCoord
    __pointCoord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pointCoord'), 'pointCoord', '__httpssbd_qbic_riken_jpbdmllevel1_Point_httpssbd_qbic_riken_jpbdmllevel1pointCoord', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 138, 3), )

    
    pointCoord = property(__pointCoord.value, __pointCoord.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}pointVal uses Python identifier pointVal
    __pointVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'pointVal'), 'pointVal', '__httpssbd_qbic_riken_jpbdmllevel1_Point_httpssbd_qbic_riken_jpbdmllevel1pointVal', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 139, 3), )

    
    pointVal = property(__pointVal.value, __pointVal.set, None, None)

    _ElementMap.update({
        __pointCoord.name() : __pointCoord,
        __pointVal.name() : __pointVal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Point', Point)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Lines with content type ELEMENT_ONLY
class Lines (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Lines with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Lines')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 143, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}linesCoord uses Python identifier linesCoord
    __linesCoord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'linesCoord'), 'linesCoord', '__httpssbd_qbic_riken_jpbdmllevel1_Lines_httpssbd_qbic_riken_jpbdmllevel1linesCoord', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 145, 3), )

    
    linesCoord = property(__linesCoord.value, __linesCoord.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}linesVal uses Python identifier linesVal
    __linesVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'linesVal'), 'linesVal', '__httpssbd_qbic_riken_jpbdmllevel1_Lines_httpssbd_qbic_riken_jpbdmllevel1linesVal', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 146, 3), )

    
    linesVal = property(__linesVal.value, __linesVal.set, None, None)

    _ElementMap.update({
        __linesCoord.name() : __linesCoord,
        __linesVal.name() : __linesVal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Lines', Lines)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Face with content type ELEMENT_ONLY
class Face (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Face with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Face')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 150, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}faceCoord uses Python identifier faceCoord
    __faceCoord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'faceCoord'), 'faceCoord', '__httpssbd_qbic_riken_jpbdmllevel1_Face_httpssbd_qbic_riken_jpbdmllevel1faceCoord', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 152, 3), )

    
    faceCoord = property(__faceCoord.value, __faceCoord.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}faceVal uses Python identifier faceVal
    __faceVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'faceVal'), 'faceVal', '__httpssbd_qbic_riken_jpbdmllevel1_Face_httpssbd_qbic_riken_jpbdmllevel1faceVal', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 153, 3), )

    
    faceVal = property(__faceVal.value, __faceVal.set, None, None)

    _ElementMap.update({
        __faceCoord.name() : __faceCoord,
        __faceVal.name() : __faceVal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Face', Face)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Circle with content type ELEMENT_ONLY
class Circle (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Circle with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Circle')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 157, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}circleCoord uses Python identifier circleCoord
    __circleCoord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'circleCoord'), 'circleCoord', '__httpssbd_qbic_riken_jpbdmllevel1_Circle_httpssbd_qbic_riken_jpbdmllevel1circleCoord', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 159, 3), )

    
    circleCoord = property(__circleCoord.value, __circleCoord.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}circleRadius uses Python identifier circleRadius
    __circleRadius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'circleRadius'), 'circleRadius', '__httpssbd_qbic_riken_jpbdmllevel1_Circle_httpssbd_qbic_riken_jpbdmllevel1circleRadius', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 160, 3), )

    
    circleRadius = property(__circleRadius.value, __circleRadius.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}circleVal uses Python identifier circleVal
    __circleVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'circleVal'), 'circleVal', '__httpssbd_qbic_riken_jpbdmllevel1_Circle_httpssbd_qbic_riken_jpbdmllevel1circleVal', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 161, 3), )

    
    circleVal = property(__circleVal.value, __circleVal.set, None, None)

    _ElementMap.update({
        __circleCoord.name() : __circleCoord,
        __circleRadius.name() : __circleRadius,
        __circleVal.name() : __circleVal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Circle', Circle)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Sphere with content type ELEMENT_ONLY
class Sphere (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Sphere with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Sphere')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 165, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}sphereCoord uses Python identifier sphereCoord
    __sphereCoord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sphereCoord'), 'sphereCoord', '__httpssbd_qbic_riken_jpbdmllevel1_Sphere_httpssbd_qbic_riken_jpbdmllevel1sphereCoord', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 167, 3), )

    
    sphereCoord = property(__sphereCoord.value, __sphereCoord.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}sphereRadius uses Python identifier sphereRadius
    __sphereRadius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sphereRadius'), 'sphereRadius', '__httpssbd_qbic_riken_jpbdmllevel1_Sphere_httpssbd_qbic_riken_jpbdmllevel1sphereRadius', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 168, 3), )

    
    sphereRadius = property(__sphereRadius.value, __sphereRadius.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}sphereVal uses Python identifier sphereVal
    __sphereVal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sphereVal'), 'sphereVal', '__httpssbd_qbic_riken_jpbdmllevel1_Sphere_httpssbd_qbic_riken_jpbdmllevel1sphereVal', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 169, 3), )

    
    sphereVal = property(__sphereVal.value, __sphereVal.set, None, None)

    _ElementMap.update({
        __sphereCoord.name() : __sphereCoord,
        __sphereRadius.name() : __sphereRadius,
        __sphereVal.name() : __sphereVal
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Sphere', Sphere)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Measurement with content type ELEMENT_ONLY
class Measurement (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Measurement with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Measurement')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 173, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}targetRef uses Python identifier targetRef
    __targetRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'targetRef'), 'targetRef', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1targetRef', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 175, 3), )

    
    targetRef = property(__targetRef.value, __targetRef.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'point'), 'point', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1point', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 176, 3), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}lines uses Python identifier lines
    __lines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lines'), 'lines', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1lines', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 177, 3), )

    
    lines = property(__lines.value, __lines.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}face uses Python identifier face
    __face = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'face'), 'face', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1face', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 178, 3), )

    
    face = property(__face.value, __face.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}circle uses Python identifier circle
    __circle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'circle'), 'circle', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1circle', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 179, 3), )

    
    circle = property(__circle.value, __circle.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}sphere uses Python identifier sphere
    __sphere = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sphere'), 'sphere', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1sphere', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 180, 3), )

    
    sphere = property(__sphere.value, __sphere.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'value'), 'value_', '__httpssbd_qbic_riken_jpbdmllevel1_Measurement_httpssbd_qbic_riken_jpbdmllevel1value', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 181, 3), )

    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        __targetRef.name() : __targetRef,
        __point.name() : __point,
        __lines.name() : __lines,
        __face.name() : __face,
        __circle.name() : __circle,
        __sphere.name() : __sphere,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Measurement', Measurement)


# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Component with content type ELEMENT_ONLY
class Component (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Component with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Component')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 185, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}ID uses Python identifier ID
    __ID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ID'), 'ID', '__httpssbd_qbic_riken_jpbdmllevel1_Component_httpssbd_qbic_riken_jpbdmllevel1ID', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 187, 3), )

    
    ID = property(__ID.value, __ID.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}listOfPrevIDs uses Python identifier listOfPrevIDs
    __listOfPrevIDs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listOfPrevIDs'), 'listOfPrevIDs', '__httpssbd_qbic_riken_jpbdmllevel1_Component_httpssbd_qbic_riken_jpbdmllevel1listOfPrevIDs', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 188, 3), )

    
    listOfPrevIDs = property(__listOfPrevIDs.value, __listOfPrevIDs.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'time'), 'time', '__httpssbd_qbic_riken_jpbdmllevel1_Component_httpssbd_qbic_riken_jpbdmllevel1time', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 195, 3), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}listOfMeasurements uses Python identifier listOfMeasurements
    __listOfMeasurements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listOfMeasurements'), 'listOfMeasurements', '__httpssbd_qbic_riken_jpbdmllevel1_Component_httpssbd_qbic_riken_jpbdmllevel1listOfMeasurements', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 196, 3), )

    
    listOfMeasurements = property(__listOfMeasurements.value, __listOfMeasurements.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpssbd_qbic_riken_jpbdmllevel1_Component_httpssbd_qbic_riken_jpbdmllevel1name', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 203, 3), )

    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __ID.name() : __ID,
        __listOfPrevIDs.name() : __listOfPrevIDs,
        __time.name() : __time,
        __listOfMeasurements.name() : __listOfMeasurements,
        __name.name() : __name
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Component', Component)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 189, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}prevID uses Python identifier prevID
    __prevID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'prevID'), 'prevID', '__httpssbd_qbic_riken_jpbdmllevel1_CTD_ANON_httpssbd_qbic_riken_jpbdmllevel1prevID', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 191, 6), )

    
    prevID = property(__prevID.value, __prevID.set, None, None)

    _ElementMap.update({
        __prevID.name() : __prevID
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 197, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}measurement uses Python identifier measurement
    __measurement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'measurement'), 'measurement', '__httpssbd_qbic_riken_jpbdmllevel1_CTD_ANON__httpssbd_qbic_riken_jpbdmllevel1measurement', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 199, 6), )

    
    measurement = property(__measurement.value, __measurement.set, None, None)

    _ElementMap.update({
        __measurement.name() : __measurement
    })
    _AttributeMap.update({
        
    })



# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Data with content type ELEMENT_ONLY
class Data (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}Data with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Data')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 207, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}scaleUnit uses Python identifier scaleUnit
    __scaleUnit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'scaleUnit'), 'scaleUnit', '__httpssbd_qbic_riken_jpbdmllevel1_Data_httpssbd_qbic_riken_jpbdmllevel1scaleUnit', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 209, 3), )

    
    scaleUnit = property(__scaleUnit.value, __scaleUnit.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}listOfTargets uses Python identifier listOfTargets
    __listOfTargets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listOfTargets'), 'listOfTargets', '__httpssbd_qbic_riken_jpbdmllevel1_Data_httpssbd_qbic_riken_jpbdmllevel1listOfTargets', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 210, 3), )

    
    listOfTargets = property(__listOfTargets.value, __listOfTargets.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}listOfComponents uses Python identifier listOfComponents
    __listOfComponents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'listOfComponents'), 'listOfComponents', '__httpssbd_qbic_riken_jpbdmllevel1_Data_httpssbd_qbic_riken_jpbdmllevel1listOfComponents', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 217, 3), )

    
    listOfComponents = property(__listOfComponents.value, __listOfComponents.set, None, None)

    _ElementMap.update({
        __scaleUnit.name() : __scaleUnit,
        __listOfTargets.name() : __listOfTargets,
        __listOfComponents.name() : __listOfComponents
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Data', Data)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 211, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'target'), 'target', '__httpssbd_qbic_riken_jpbdmllevel1_CTD_ANON_2_httpssbd_qbic_riken_jpbdmllevel1target', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 213, 6), )

    
    target = property(__target.value, __target.set, None, None)

    _ElementMap.update({
        __target.name() : __target
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 218, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}component uses Python identifier component
    __component = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'component'), 'component', '__httpssbd_qbic_riken_jpbdmllevel1_CTD_ANON_3_httpssbd_qbic_riken_jpbdmllevel1component', True, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 220, 6), )

    
    component = property(__component.value, __component.set, None, None)

    _ElementMap.update({
        __component.name() : __component
    })
    _AttributeMap.update({
        
    })



# Complex type {http://ssbd.qbic.riken.jp/bdml/level1}bdmlDocument with content type ELEMENT_ONLY
class bdmlDocument (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://ssbd.qbic.riken.jp/bdml/level1}bdmlDocument with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'bdmlDocument')
    _XSDLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 227, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}info uses Python identifier info
    __info = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'info'), 'info', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_httpssbd_qbic_riken_jpbdmllevel1info', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 229, 3), )

    
    info = property(__info.value, __info.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}summary uses Python identifier summary
    __summary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'summary'), 'summary', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_httpssbd_qbic_riken_jpbdmllevel1summary', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 230, 3), )

    
    summary = property(__summary.value, __summary.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}contact uses Python identifier contact
    __contact = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'contact'), 'contact', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_httpssbd_qbic_riken_jpbdmllevel1contact', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 231, 3), )

    
    contact = property(__contact.value, __contact.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}methods uses Python identifier methods
    __methods = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'methods'), 'methods', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_httpssbd_qbic_riken_jpbdmllevel1methods', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 232, 3), )

    
    methods = property(__methods.value, __methods.set, None, None)

    
    # Element {http://ssbd.qbic.riken.jp/bdml/level1}data uses Python identifier data
    __data = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'data'), 'data', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_httpssbd_qbic_riken_jpbdmllevel1data', False, pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 233, 3), )

    
    data = property(__data.value, __data.set, None, None)

    
    # Attribute level uses Python identifier level
    __level = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'level'), 'level', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_level', pyxb.binding.datatypes.positiveInteger, fixed=True, unicode_default=u'1', required=True)
    __level._DeclarationLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 235, 2)
    __level._UseLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 235, 2)
    
    level = property(__level.value, __level.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpssbd_qbic_riken_jpbdmllevel1_bdmlDocument_version', pyxb.binding.datatypes.positiveInteger, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 236, 2)
    __version._UseLocation = pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 236, 2)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __info.name() : __info,
        __summary.name() : __summary,
        __contact.name() : __contact,
        __methods.name() : __methods,
        __data.name() : __data
    })
    _AttributeMap.update({
        __level.name() : __level,
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', u'bdmlDocument', bdmlDocument)


bdml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bdml'), bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 238, 1))
Namespace.addCategoryObject('elementBinding', bdml.name().localName(), bdml)



Info._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bdmlID'), UUIDType, scope=Info, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 70, 3)))

Info._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), pyxb.binding.datatypes.string, scope=Info, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 71, 3)))

Info._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'version'), pyxb.binding.datatypes.positiveInteger, scope=Info, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 72, 3)))

Info._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'release'), pyxb.binding.datatypes.date, scope=Info, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 73, 3)))

Info._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'license'), pyxb.binding.datatypes.string, scope=Info, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 74, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Info._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bdmlID')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 70, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Info._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 71, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Info._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'version')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 72, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Info._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'release')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 73, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Info._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'license')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 74, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Info._Automaton = _BuildAutomaton()




Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'description'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 80, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organism'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 81, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'datatype'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 82, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'identifier'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 83, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'basedon'), BasedOn, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 84, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contributors'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 85, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'citation'), pyxb.binding.datatypes.string, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 86, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PMID'), pyxb.binding.datatypes.positiveInteger, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 87, 3)))

Summary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dblink'), pyxb.binding.datatypes.anyURI, scope=Summary, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 88, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 86, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 87, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 88, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'description')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 80, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organism')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 81, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'datatype')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 82, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'identifier')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 83, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'basedon')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 84, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contributors')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 85, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'citation')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 86, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PMID')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 87, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Summary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dblink')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 88, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Summary._Automaton = _BuildAutomaton_()




Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contactname'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 94, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'E-mail'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 95, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phone'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 96, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'URL'), pyxb.binding.datatypes.anyURI, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 97, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organization'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 98, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'department'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 99, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'laboratory'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 100, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'street'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 101, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'city'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 102, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'code'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 103, 3)))

Contact._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), pyxb.binding.datatypes.string, scope=Contact, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 104, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 96, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 97, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 101, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contactname')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 94, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'E-mail')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 95, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phone')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 96, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'URL')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 97, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organization')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 98, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'department')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 99, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'laboratory')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 100, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'street')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 101, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'city')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 102, 3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'code')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 103, 3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Contact._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 104, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Contact._Automaton = _BuildAutomaton_2()




Methods._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'methodssummary'), pyxb.binding.datatypes.string, scope=Methods, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 110, 3)))

Methods._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'environment'), pyxb.binding.datatypes.anyURI, scope=Methods, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 111, 3)))

Methods._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'input'), pyxb.binding.datatypes.anyURI, scope=Methods, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 112, 3)))

Methods._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pdpml'), pyxb.binding.datatypes.anyURI, scope=Methods, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 113, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 111, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 112, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 113, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Methods._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'methodssummary')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 110, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Methods._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'environment')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 111, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Methods._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'input')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 112, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Methods._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pdpml')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 113, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Methods._Automaton = _BuildAutomaton_3()




ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xScale'), pyxb.binding.datatypes.double, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 119, 3)))

ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yScale'), pyxb.binding.datatypes.double, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 120, 3)))

ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'zScale'), pyxb.binding.datatypes.double, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 121, 3)))

ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xyzUnit'), UnitKind, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 122, 3)))

ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tScale'), pyxb.binding.datatypes.double, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 123, 3)))

ScaleUnit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tUnit'), UnitKind, scope=ScaleUnit, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 124, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xScale')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 119, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yScale')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 120, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'zScale')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 121, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xyzUnit')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 122, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tScale')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 123, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ScaleUnit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tUnit')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 124, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ScaleUnit._Automaton = _BuildAutomaton_4()




Target._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=Target, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 130, 3)))

Target._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scale'), pyxb.binding.datatypes.double, scope=Target, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 131, 3)))

Target._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'unit'), UnitKind, scope=Target, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 132, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 131, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Target._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 130, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Target._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scale')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 131, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Target._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'unit')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 132, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Target._Automaton = _BuildAutomaton_5()




Point._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pointCoord'), pyxb.binding.datatypes.string, scope=Point, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 138, 3)))

Point._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pointVal'), pyxb.binding.datatypes.double, scope=Point, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 139, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 139, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Point._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pointCoord')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 138, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Point._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pointVal')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 139, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Point._Automaton = _BuildAutomaton_6()




Lines._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'linesCoord'), pyxb.binding.datatypes.string, scope=Lines, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 145, 3)))

Lines._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'linesVal'), pyxb.binding.datatypes.double, scope=Lines, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 146, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 146, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Lines._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'linesCoord')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 145, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Lines._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'linesVal')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 146, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Lines._Automaton = _BuildAutomaton_7()




Face._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'faceCoord'), pyxb.binding.datatypes.string, scope=Face, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 152, 3)))

Face._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'faceVal'), pyxb.binding.datatypes.double, scope=Face, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 153, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 153, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Face._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'faceCoord')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 152, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Face._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'faceVal')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 153, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Face._Automaton = _BuildAutomaton_8()




Circle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'circleCoord'), pyxb.binding.datatypes.string, scope=Circle, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 159, 3)))

Circle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'circleRadius'), pyxb.binding.datatypes.double, scope=Circle, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 160, 3)))

Circle._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'circleVal'), pyxb.binding.datatypes.double, scope=Circle, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 161, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 161, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Circle._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'circleCoord')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 159, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Circle._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'circleRadius')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 160, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Circle._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'circleVal')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 161, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Circle._Automaton = _BuildAutomaton_9()




Sphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sphereCoord'), pyxb.binding.datatypes.string, scope=Sphere, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 167, 3)))

Sphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sphereRadius'), pyxb.binding.datatypes.double, scope=Sphere, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 168, 3)))

Sphere._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sphereVal'), pyxb.binding.datatypes.double, scope=Sphere, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 169, 3)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 169, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Sphere._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sphereCoord')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 167, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Sphere._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sphereRadius')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 168, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Sphere._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sphereVal')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 169, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Sphere._Automaton = _BuildAutomaton_10()




Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'targetRef'), pyxb.binding.datatypes.string, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 175, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'point'), Point, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 176, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lines'), Lines, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 177, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'face'), Face, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 178, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'circle'), Circle, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 179, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sphere'), Sphere, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 180, 3)))

Measurement._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'value'), pyxb.binding.datatypes.double, scope=Measurement, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 181, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 176, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 177, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 178, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 179, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 180, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 181, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'targetRef')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 175, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'point')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 176, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lines')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 177, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'face')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 178, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'circle')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 179, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sphere')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 180, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Measurement._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'value')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 181, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Measurement._Automaton = _BuildAutomaton_11()




Component._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ID'), pyxb.binding.datatypes.string, scope=Component, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 187, 3)))

Component._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listOfPrevIDs'), CTD_ANON, scope=Component, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 188, 3)))

Component._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'time'), pyxb.binding.datatypes.double, scope=Component, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 195, 3)))

Component._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listOfMeasurements'), CTD_ANON_, scope=Component, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 196, 3)))

Component._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=Component, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 203, 3)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 188, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Component._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ID')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 187, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Component._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listOfPrevIDs')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 188, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Component._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'time')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 195, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Component._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listOfMeasurements')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 196, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Component._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 203, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Component._Automaton = _BuildAutomaton_12()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'prevID'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 191, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'prevID')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_13()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'measurement'), Measurement, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 199, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'measurement')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 199, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_14()




Data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scaleUnit'), ScaleUnit, scope=Data, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 209, 3)))

Data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listOfTargets'), CTD_ANON_2, scope=Data, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 210, 3)))

Data._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'listOfComponents'), CTD_ANON_3, scope=Data, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 217, 3)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Data._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scaleUnit')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 209, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Data._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listOfTargets')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 210, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Data._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'listOfComponents')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 217, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Data._Automaton = _BuildAutomaton_15()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'target'), Target, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 213, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'target')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 213, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_16()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'component'), Component, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 220, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'component')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 220, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_17()




bdmlDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'info'), Info, scope=bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 229, 3)))

bdmlDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'summary'), Summary, scope=bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 230, 3)))

bdmlDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contact'), Contact, scope=bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 231, 3)))

bdmlDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'methods'), Methods, scope=bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 232, 3)))

bdmlDocument._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'data'), Data, scope=bdmlDocument, location=pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 233, 3)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bdmlDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'info')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 229, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bdmlDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'summary')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 230, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bdmlDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contact')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 231, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bdmlDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'methods')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 232, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(bdmlDocument._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'data')), pyxb.utils.utility.Location('/home/db2inst1/trail5/bdml-level1-version1-draft10.xsd', 233, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
bdmlDocument._Automaton = _BuildAutomaton_18()

