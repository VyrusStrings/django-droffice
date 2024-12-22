import os
from pathlib import Path

# Assuming you're currently in the main 'doctor_office' directory
base_dir = Path.cwd()

# Define the directories structure
apps = ['users', 'patients', 'appointments', 'medicines']
base_subdirs = [
    'templates', 'static', 'media'
]

# For each app, we need certain subdirectories
app_structure = {
    'users': ['templates/users'],
    'patients': ['templates/patients'],
    'appointments': ['templates/appointments'],
    'medicines': ['templates/medicines']
}

# Create base directories
for d in base_subdirs:
    (base_dir / d).mkdir(exist_ok=True)

# Create apps and their subdirectories
for app in apps:
    app_dir = base_dir / app
    app_dir.mkdir(exist_ok=True)
    # Create common Django files if not exist
    for fname in ['__init__.py', 'admin.py', 'apps.py', 'models.py', 'views.py', 'forms.py', 'urls.py']:
        fpath = app_dir / fname
        if not fpath.exists():
            fpath.touch()

    # Create templates subdirectories
    if app in app_structure:
        for t_dir in app_structure[app]:
            full_t_dir = base_dir / t_dir
            full_t_dir.mkdir(parents=True, exist_ok=True)

# Create project-level template files if needed
base_templates = ['base.html']
for tpl in base_templates:
    fpath = base_dir / 'templates' / tpl
    if not fpath.exists():
        fpath.touch()

# Add a __init__.py to the main project directory if needed
main_project_dir = base_dir / 'doctor_office'
if not (main_project_dir / '__init__.py').exists():
    (main_project_dir / '__init__.py').touch()

# Provide a summary
print("Project structure created/updated successfully.")