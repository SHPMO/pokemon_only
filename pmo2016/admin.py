from django.contrib import admin

from pmo2016.models import (
    Player, MainComment,
    BackComment2016
)

admin.site.register(Player)
admin.site.register(MainComment)
admin.site.register(BackComment2016)
