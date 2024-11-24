# Permissions and Groups Setup

In this application, we have defined custom permissions for the `Post` model to control access to different actions:
- `can_view`: View the post
- `can_create`: Create a new post
- `can_edit`: Edit an existing post
- `can_delete`: Delete a post

### Groups and Permissions
- **Admins**: All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)
- **Editors**: Can create, edit, and delete posts (`can_create`, `can_edit`, `can_delete`)
- **Viewers**: Can only view posts (`can_view`)

### Enforcing Permissions
We use Django's `@permission_required` decorator to enforce permissions on views like `edit_post`.

