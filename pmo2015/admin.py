from django.contrib import admin
from pmo2015.models import PmoAdmin, Player, MainComment, BackComment, Vote
# Register your models here.
admin.site.register(PmoAdmin)
admin.site.register(Player)
admin.site.register(MainComment)
admin.site.register(BackComment)
admin.site.register(Vote)
