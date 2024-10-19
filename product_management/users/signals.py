from django.db.models.signals import post_migrate
from django.core.management import call_command
from django.dispatch import receiver


@receiver(post_migrate)  # This will run after the migrate command is executed
def create_user_groups(sender, **kwargs):
    """
    Create user groups and assign permissions
    """
    # Call the management command to create groups and permissions
    call_command('create_groups')
