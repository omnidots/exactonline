from .manager import Manager


class GoodsDeliveries(Manager):
    resource = 'bulk/Salesorder/GoodsDeliveries'

    def filter(self, entry_id=None, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = (
                'DeliveryAccount,DeliveryDate,DeliveryNumber,'
                'GoodsDeliveryLines/ItemCode,GoodsDeliveryLines/SerialNumbers/SerialNumber'
            )

        if entry_id is not None:
            # Filter by our EntryID
            self._filter_append(kwargs, u'EntryID eq  %s' % (entry_id,))

        return super(GoodsDeliveries, self).filter(**kwargs)
