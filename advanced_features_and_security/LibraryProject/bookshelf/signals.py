# blog/signals.py

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Post

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    # Define permissions for Post model
    content_type = ContentType.objects.get_for_model(Post)

    permissions = {
        'can_view': 'Can view post',
        'can_create': 'Can create post',
        'can_edit': 'Can edit post',
        'can_delete': 'Can delete post',
    }

    # Create groups
    admin_group, created = Group.objects.get_or_create(name='Admins')
    editor_group, created = Group.objects.get_or_create(name='Editors')
    viewer_group, created = Group.objects.get_or_create(name='Viewers')

    # Assign permissions to the groups
    for perm_name, perm_desc in permissions.items():
        permission = Permission.objects.get(codename=perm_name, content_type=content_type)
        admin_group.permissions.add(permission)
        if perm_name in ['can_create', 'can_edit', 'can_delete']:
            editor_group.permissions.add(permission)
        if perm_name == 'can_view':
            viewer_group.permissions.add(permission)

