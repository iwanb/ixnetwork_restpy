# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class PceUpdateXroSubObjectList(Base):
    """
    The PceUpdateXroSubObjectList class encapsulates a list of pceUpdateXroSubObjectList resources that is managed by the system.
    A list of resources can be retrieved from the server using the PceUpdateXroSubObjectList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pceUpdateXroSubObjectList'

    def __init__(self, parent):
        super(PceUpdateXroSubObjectList, self).__init__(parent)

    @property
    def ActiveXRO(self):
        """Controls whether the XRO sub-object will be sent in the PCRequest message.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('activeXRO')

    @property
    def AsNumber(self):
        """AS Number

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('asNumber')

    @property
    def Attribute(self):
        """Indicates how the exclusion subobject is to be indicated

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('attribute')

    @property
    def InterfaceId(self):
        """Interface ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('interfaceId')

    @property
    def Ipv4Address(self):
        """IPv4 Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv4Address')

    @property
    def Ipv6Address(self):
        """IPv6 Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ipv6Address')

    @property
    def PFlagXro(self):
        """XRO P Flag

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('pFlagXro')

    @property
    def PceId128(self):
        """128 bit PKS ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('pceId128')

    @property
    def PceId32(self):
        """32 bit PKS ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('pceId32')

    @property
    def PrefixLength(self):
        """Prefix Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('prefixLength')

    @property
    def RouterId(self):
        """Router ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('routerId')

    @property
    def SrlgId(self):
        """SRLG ID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('srlgId')

    @property
    def SubObjectType(self):
        """Using the Sub Object Type control user can configure which sub object needs to be included from the following options: IPv4 Prefix IPv6 Prefix Unnumbered Interface ID AS Number. SRLG

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('subObjectType')

    @property
    def XBit(self):
        """Indicates whether the exclusion is mandatory or desired.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('xBit')

    def find(self):
        """Finds and retrieves pceUpdateXroSubObjectList data from the server.

        All named parameters support regex and can be used to selectively retrieve pceUpdateXroSubObjectList data from the server.
        By default the find method takes no parameters and will retrieve all pceUpdateXroSubObjectList data from the server.

        Returns:
            self: This instance with matching pceUpdateXroSubObjectList data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of pceUpdateXroSubObjectList data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the pceUpdateXroSubObjectList data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActiveXRO=None, AsNumber=None, Attribute=None, InterfaceId=None, Ipv4Address=None, Ipv6Address=None, PFlagXro=None, PceId128=None, PceId32=None, PrefixLength=None, RouterId=None, SrlgId=None, SubObjectType=None, XBit=None):
        """Base class infrastructure that gets a list of pceUpdateXroSubObjectList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            ActiveXRO (str): optional regex of activeXRO
            AsNumber (str): optional regex of asNumber
            Attribute (str): optional regex of attribute
            InterfaceId (str): optional regex of interfaceId
            Ipv4Address (str): optional regex of ipv4Address
            Ipv6Address (str): optional regex of ipv6Address
            PFlagXro (str): optional regex of pFlagXro
            PceId128 (str): optional regex of pceId128
            PceId32 (str): optional regex of pceId32
            PrefixLength (str): optional regex of prefixLength
            RouterId (str): optional regex of routerId
            SrlgId (str): optional regex of srlgId
            SubObjectType (str): optional regex of subObjectType
            XBit (str): optional regex of xBit

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
