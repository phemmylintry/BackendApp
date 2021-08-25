from django.contrib import admin
from .models import (User, CustomToken, PasswordResetToken, UserService, 
                    CustomerProfile, CustomerQualifications, QualificationLabel, WorkExperienceLabel,
                    CustomerWorkExperience, CustomerProfileLabel, RelativeInCanada, RelativeInCanadaLabel,
                    EducationalCreationalAssessment, EducationalCreationalAssessmentLabel, AgentProfile)
from keel.Core.models import Country, State, City

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']


class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'age',)
    readonly_fields = ('deleted_at', )

class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'license', 'country')
    readonly_fields = ('deleted_at', )

class CustomerProfileLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class CustomerQualificationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'institute', 'country', 'start_date', 'end_date')
    readonly_fields = ('deleted_at', )

    class Media:
        js = ("selectajax.js", )

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            form = super(CustomerQualificationsAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['state'].queryset = State.objects.filter(country=obj.country)
            form.base_fields['city'].queryset = City.objects.filter(state=obj.state)
            return form
        return super().get_form(request, obj=obj, **kwargs)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     print(kwargs)
    #     if db_field.name == "state":
    #         kwargs['queryset'] = State.objects.filter()
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
class QualificationLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class CustomerWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'designation', 'start_date', 'end_date')
    readonly_fields = ('deleted_at', )

    class Media:
        js = ("selectajax.js", )

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            form = super(CustomerWorkExperienceAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['state'].queryset = State.objects.filter(country=obj.country)
            form.base_fields['city'].queryset = City.objects.filter(state=obj.state)
            return form
        return super().get_form(request, obj=obj, **kwargs)

class WorkExperienceLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class RelativeInCanadaAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email_address', 'relationship', 'immigration_status')
    readonly_fields = ('deleted_at', )

class RelativeInCanadaLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class EducationalCreationalAssessmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'eca_authority_name', 'eca_authority_number', 'canadian_equivalency_summary')
    readonly_fields = ('deleted_at', )

class EducationalCreationalAssessmentLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

admin.site.register(User, UserAdmin)
admin.site.register(UserService)
admin.site.register(PasswordResetToken)
admin.site.register(CustomToken)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(AgentProfile, AgentProfileAdmin)
admin.site.register(CustomerProfileLabel, CustomerProfileLabelAdmin)
admin.site.register(CustomerQualifications, CustomerQualificationsAdmin)
admin.site.register(QualificationLabel, QualificationLabelAdmin)
admin.site.register(CustomerWorkExperience, CustomerWorkExperienceAdmin)
admin.site.register(WorkExperienceLabel, WorkExperienceLabelAdmin)
admin.site.register(RelativeInCanada, RelativeInCanadaAdmin)
admin.site.register(RelativeInCanadaLabel, RelativeInCanadaLabelAdmin)
admin.site.register(EducationalCreationalAssessment, EducationalCreationalAssessmentAdmin)
admin.site.register(EducationalCreationalAssessmentLabel, EducationalCreationalAssessmentLabelAdmin)