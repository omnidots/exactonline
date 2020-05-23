from .manager import Manager


class StockSerialNumbers(Manager):
    resource = 'inventory/StockSerialNumbers'

    def filter(self, serial_number=None, **kwargs):
        if 'select' not in kwargs:
                kwargs['select'] = 'ItemCode,SerialNumber,StockTransactionType'

        if serial_number is not None:
            # Filter by our serial number.
            self._filter_append(kwargs, u'trim(SerialNumber) eq  %s' % (serial_number,))

        return super(StockSerialNumbers, self).filter(**kwargs)
