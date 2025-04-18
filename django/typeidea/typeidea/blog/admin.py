from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.custom_site import custom_site

from django.contrib.admin.models import LogEntry


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'owner')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']


class PostInLine(admin.TabularInline):
    fields = ('title', 'desc', 'owner')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInLine]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav', 'owner')
    search_fields = ['name']

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # form = PostAdminForm

    list_display = ('title', 'owner', 'category', 'status', 'created_time', 'operator')
    list_display_links = []

    date_hierarchy = 'created_time'
    list_filter = [CategoryOwnerFilter]
    # list_filter = ['owner',  'category', 'status']
    search_fields = ['title', 'category__name']
    search_help_text = '帮助'
    # list_editable = ['status']
    autocomplete_fields = ['category']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    exclude = ('owner',)
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),

        }),
        ('额外信息', {
            'fields': ['tag'],
        }),
    )

    @admin.display(description='操作')
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>', reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
        # return f'<a href="{reverse("cus_admin:blog_post_change", args=(obj.id,))}">编辑</a>'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css',),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
