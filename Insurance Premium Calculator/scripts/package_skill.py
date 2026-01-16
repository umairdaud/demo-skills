#!/usr/bin/env python3
"""
Script to package the Insurance Premium Calculator skill into a distributable .skill file
"""
import os
import zipfile
import sys
from pathlib import Path

def package_skill(skill_dir, output_dir=None):
    """
    Package a skill directory into a .skill file

    Args:
        skill_dir (str): Path to the skill directory
        output_dir (str): Optional output directory, defaults to current directory
    """
    skill_path = Path(skill_dir)

    if not skill_path.exists():
        print(f"Error: Skill directory '{skill_dir}' does not exist")
        return False

    if not (skill_path / "SKILL.md").exists():
        print(f"Error: SKILL.md not found in '{skill_dir}'")
        return False

    # Get skill name from directory name
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir)
    else:
        output_path = Path.cwd()

    output_path.mkdir(parents=True, exist_ok=True)
    skill_file = output_path / f"{skill_name}.skill"

    # Create the skill package as a zip file
    with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skill_dir):
            for file in files:
                file_path = Path(root) / file
                # Adjust the arc_path to be relative to the skill directory itself, not its parent
                arc_path = file_path.relative_to(skill_path)
                zipf.write(file_path, arc_path)

    print(f"Skill packaged successfully: {skill_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <skill_directory> [output_directory]")
        sys.exit(1)

    skill_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    success = package_skill(skill_dir, output_dir)
    if not success:
        sys.exit(1)