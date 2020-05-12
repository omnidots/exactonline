# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for relation/contact resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2017 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class Contacts(Manager):
    resource = 'crm/Contacts'

    def filter(self, ID=None, **kwargs):
        if ID is not None:
            remote_id = self._remote_guid(ID)
            # Filter by our account number.
            self._filter_append(kwargs, u'ID eq %s' % (remote_id,))

        return super(Contacts, self).filter(**kwargs)

    def _remote_contact_code(self, code):
        return u"'%18s'" % (code.replace("'", "''"),)
