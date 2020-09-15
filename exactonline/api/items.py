from .manager import Manager


class Items(Manager):
    resource = 'logistics/Items'

    def filter(self, code=None, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = 'ID,Stock,Description,Code'

        if code is not None:
            # Filter by our Code.
            self._filter_append(kwargs, u'Code eq  %s' % (code,))

        return super(Items, self).filter(**kwargs)
