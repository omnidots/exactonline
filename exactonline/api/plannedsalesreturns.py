from .manager import Manager


class PlannedSalesReturns(Manager):
    resource = 'salesorder/PlannedSalesReturns'

    def filter(self, plannedsalesreturn_id=None, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = (
                'DeliveredTo,ReturnDate,PlannedSalesReturnLines/ItemCode,'
                'PlannedSalesReturnLines/SerialNumbers/SerialNumber'
            )

        if plannedsalesreturn_id is not None:
            # Filter by our PlannedSalesReturnID.
            self._filter_append(kwargs, u'PlannedSalesReturnID eq  %s' % (plannedsalesreturn_id,))

        return super(PlannedSalesReturns, self).filter(**kwargs)
