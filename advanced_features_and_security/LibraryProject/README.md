# Permissions and Groups Setup

This application uses Django's groups and permissions to control access to the Book model.

## Permissions

-   `can_view`: Allows users to view books.
-   `can_create`: Allows users to create new books.
-   `can_edit`: Allows users to edit existing books.
-   `can_delete`: Allows users to delete books.

## Groups

-   **Viewers:** Have only `can_view` permission.
-   **Editors:** Have `can_create` and `can_edit` permissions.
-   **Admins:** Have all permissions.

## Usage

Permissions are enforced in views using the `@permission_required` decorator.
