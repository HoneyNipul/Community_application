import MySQLdb
from django.contrib import admin
from models import Address, Member, Relation,  eventRegistration, eventInvitee
from django.contrib.auth.models import UserManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class MembersInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MembersInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(Relation)
admin.site.register(eventInvitee)
admin.site.register(eventRegistration)
admin.site.register(Member)


# class MemberAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#       user_manager = UserManager()
#       admin_user = user_manager.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
#       obj.auth_id = admin_user.id
#       obj.save()

#
# admin.site.register(eventnotification)
# admin.site.register(group)
# admin.site.register(group_member)


