"""This module contains the general information for SwZoneInitiatorMember ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class SwZoneInitiatorMemberConsts:
    LC_ALLOCATED = "allocated"
    LC_AVAILABLE = "available"
    LC_DEALLOCATED = "deallocated"
    LC_REPURPOSED = "repurposed"


class SwZoneInitiatorMember(ManagedObject):
    """This is SwZoneInitiatorMember class."""

    consts = SwZoneInitiatorMemberConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("SwZoneInitiatorMember", "swZoneInitiatorMember", "initiator-[name]", VersionMeta.Version211a, "InputOutput", 0x3f, [], ["read-only"], [u'swFcServerZoneGroup'], [u'swFcZone'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version211a, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "lc": MoPropertyMeta("lc", "lc", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["allocated", "available", "deallocated", "repurposed"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version211a, MoPropertyMeta.NAMING, 0x8, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "peer_dn": MoPropertyMeta("peer_dn", "peerDn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, 0, 256, r"""(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "lc": "lc", 
        "name": "name", 
        "peerDn": "peer_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "wwpn": "wwpn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ep_dn = None
        self.lc = None
        self.peer_dn = None
        self.sacl = None
        self.status = None
        self.wwpn = None

        ManagedObject.__init__(self, "SwZoneInitiatorMember", parent_mo_or_dn, **kwargs)
