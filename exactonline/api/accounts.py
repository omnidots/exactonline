from .manager import Manager


class Accounts(Manager):
    resource = 'crm/Accounts'

    def filter(self, account_id=None, **kwargs):
        self.resource = 'bulk/CRM/Accounts'

        if account_id is not None:
            remote_id = self._remote_guid(account_id)
            # Filter by our account number.
            self._filter_append(kwargs, u'Account eq %s' % (remote_id,))

        return super(Accounts, self).filter(**kwargs)
