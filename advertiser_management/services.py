from django.contrib.admin import SimpleListFilter


class ApproveStatusFilter(SimpleListFilter):
    title = 'approve status'
    parameter_name = 'ads'

    def lookups(self, request, model_admin):
        return [
            ('accepted', 'accepted'),
            ('denied', 'denied')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'accepted':
            return queryset.filter(approve='accepted')
        elif self.value() == 'denied':
            return queryset.filter(approve='denied')
        else:
            return queryset
