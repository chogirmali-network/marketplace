from django.contrib import admin
from .models import User as CustomUser, SubscriptionPlan, Project, Client, Team, Member, TeamBadge, UserBadge, SavedProject, RankingProject, SoldProject

admin.site.register(CustomUser)
admin.site.register(SubscriptionPlan)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(TeamBadge)
admin.site.register(UserBadge)
admin.site.register(SavedProject)
admin.site.register(RankingProject)
admin.site.register(SoldProject)
