from django.contrib import admin
from .models import (User, CustomToken, PasswordResetToken, UserService, 
                    CustomerProfile, CustomerQualifications, QualificationLabel, WorkExperienceLabel,
                    CustomerWorkExperience, CustomerProfileLabel, RelativeInCanada, RelativeInCanadaLabel,
                    EducationalCreationalAssessment, EducationalCreationalAssessmentLabel)


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']


class CustomerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class CustomerProfileLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class CustomerQualificationsAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class QualificationLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class CustomerWorkExperienceAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class WorkExperienceLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class RelativeInCanadaAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class RelativeInCanadaLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class EducationalCreationalAssessmentAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

class EducationalCreationalAssessmentLabelAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', )

admin.site.register(User, UserAdmin)
admin.site.register(UserService)
admin.site.register(PasswordResetToken)
admin.site.register(CustomToken)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(CustomerProfileLabel, CustomerProfileLabelAdmin)
admin.site.register(CustomerQualifications, CustomerQualificationsAdmin)
admin.site.register(QualificationLabel, QualificationLabelAdmin)
admin.site.register(CustomerWorkExperience, CustomerWorkExperienceAdmin)
admin.site.register(WorkExperienceLabel, WorkExperienceLabelAdmin)
admin.site.register(RelativeInCanada, RelativeInCanadaAdmin)
admin.site.register(RelativeInCanadaLabel, RelativeInCanadaLabelAdmin)
admin.site.register(EducationalCreationalAssessment, EducationalCreationalAssessmentAdmin)
admin.site.register(EducationalCreationalAssessmentLabel, EducationalCreationalAssessmentLabelAdmin)