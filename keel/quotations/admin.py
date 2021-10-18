from django.contrib import admin
from keel.Core.admin import CustomBaseModelAdmin
from .models import Quotation, QuotationMilestone
class QuotationMilestoneLine(admin.TabularInline):
    model = QuotationMilestone
    max_num = 0
    readonly_fields = ('qm_id', )

class QuotationAdmin(admin.ModelAdmin):

    list_display = ('q_id', 'user', 'plan', 'total_amount', 'status')
    autocomplete_fields = ('user', 'plan')
    search_fields = ('q_id', )
    readonly_fields = ('deleted_at', 'q_id')
    inlines = [QuotationMilestoneLine]


class QuotationMilestioneAdmin(CustomBaseModelAdmin):
    list_display = ('qm_id', 'amount', 'status', 'due_date')
    readonly_fields = ('qm_id', 'deleted_at')

admin.site.register(Quotation, QuotationAdmin)
admin.site.register(QuotationMilestone, QuotationMilestioneAdmin)
