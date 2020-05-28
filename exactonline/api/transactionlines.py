from .manager import Manager


class TransactionLines(Manager):
    resource = 'bulk/Financial/TransactionLines'

    def filter(self, transaction_id=None, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = 'AccountName,ItemCode,ItemDescription,SerialNumber,Type,Quantity,OrderNumber,LineNumber,LineType,Date'

        if transaction_id is not None:
            # Filter by our EntryID
            self._filter_append(kwargs, u'ID eq  %s' % (transaction_id,))

        return super(TransactionLines, self).filter(**kwargs)