from django.contrib import admin
from skycode.models import *


class QuestionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(QuestionAdmin, self).get_queryset(request)
        return qs.filter(answered=False)


class RequestAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        rs = super(RequestAdmin, self).get_queryset(request)
        return rs.filter(accepted=False)


admin.site.register(Teacher)
admin.site.register(Partner)
admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(News)

