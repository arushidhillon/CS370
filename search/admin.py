from django.contrib import admin
from .models import SearchQuery

class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'timestamp')
    search_fields = ('user__username', 'query')
    list_filter = ('timestamp',)
    date_hierarchy = 'timestamp'

admin.site.register(SearchQuery, SearchQueryAdmin)