from pathlib import Path
from git import Repo 

# Repository root (current working directory)
repo_root = Path("/workspaces/MSSP6070/")

# Root-level folders
root_folders = [
    "WeeklyModules,"
    "Assignments",
    "data"
]

# Create root folders
for folder in root_folders:
    (repo_root / folder).mkdir(parents=True, exist_ok=False)

# Create WeeklyModules subfolders Week01 - Week14
weekly_modules = repo_root / "WeeklyModules"

for week_num in range(1, 15):
    week_folder = weekly_modules / f"Week{week_num:02d}"
    week_folder.mkdir(parents=True, exist_ok=False)

print("Folder structure created successfully!")