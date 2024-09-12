#!/bin/bash
# Detailed Explanation of the Script:
#    Shebang (#!/bin/bash):
#        This tells the system to use the bash shell to run the script.
#
#    VERSION File Check:
#        We define the path to the VERSION file (versionFilePath="VERSION").
#        The script checks if the VERSION file exists using [ ! -f "$versionFilePath" ].
#        If it doesn't exist, the script prints an error and defaults to version v0.0.0.
#
#    Version Format Validation:
#        The script checks if the version string follows the vx.y.z format using a regular expression
#        ([[ ! "$currentVersion" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]).
#        If the format is not valid, it prints an error and exits with a non-zero status (exit 1).
#
#    Version Increment:
#        The version is split into its major, minor, and patch parts using
#        IFS='.' read -r major minor patch <<< "${currentVersion:1}", where the IFS (Internal Field Separator) is
#        set to . to split the version string.
#        The patch is incremented by 1 (patch=$((patch + 1))).
#        A new version string is constructed using newVersion="v${major}.${minor}.${patch}".
#
#    Write the New Version:
#        The new version is written back to the VERSION file using echo "$newVersion" > "$versionFilePath".
#
#    Git Commit:
#        The script stages all changes (git add --all) and commits them with a message containing the new version (
#        git commit -m "VERSION is updated to $newVersion").
#        If the commit fails, it prints an error and exits.
#
#    Git Remotes:
#        The script defines Git remotes in an associative array (declare -A remotes).
#        It iterates over the defined remotes and checks if they exist using git remote | grep -q "^$remote$".
#        If a remote doesn't exist, it adds the remote using git remote add $remote ${remotes[$remote]}.
#
#    Tag Creation:
#        The script creates a new Git tag using git tag "$newVersion".
#        If tag creation fails, it prints an error and exits.
#
#    Push to Remote:
#        The script pushes the new tag and the master branch to each remote using git push --tags "$remote" master.
#        If the push fails, it prints an error and exits.
#
#    Completion:
#        Finally, the script prints a success message indicating that the version update process is complete.
#
# Running the Script:
#    Make the script executable:
#        chmod +x automatic_patch_versioning.sh
#
#    Run the script:
#        ./automatic_patch_versioning.sh

# Path to the VERSION file
versionFilePath="VERSION"

echo "=============================== Check if VERSION exists"

# Check if the VERSION file exists
if [ ! -f "$versionFilePath" ]; then
    # If the VERSION file doesn't exist, print an error message and set the version to v0.0.0
    echo "Error: VERSION file not found."
    currentVersion="v0.0.0"  # Default version if no file exists
    echo "Current version is: $currentVersion"
else
    # If the VERSION file exists, read the content of the file (the current version)
    currentVersion=$(cat "$versionFilePath")
    echo "Current version is: $currentVersion"
fi

# Ensure the version follows the vx.y.z format (e.g., v1.2.3)
if [[ ! "$currentVersion" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    # If the version doesn't match the format, print an error and exit
    echo "Error: VERSION does not contain a valid version (vx.y.z format)."
    exit 1
fi

echo "=============================== Increment patch"

# Split the version string (removing the 'v' at the beginning)
# 'IFS' is the Internal Field Separator used to break the version string by '.'
IFS='.' read -r major minor patch <<< "${currentVersion:1}"

# Increment the patch version (the last part of the version)
patch=$((patch + 1))

# Form the new version string by combining major, minor, and incremented patch
newVersion="v${major}.${minor}.${patch}"
echo "New version is: $newVersion"

# Write the new version back into the VERSION file, overwriting the old version
echo "$newVersion" > "$versionFilePath"

echo "=============================== Commit the change"

# Stage all changes (including the updated VERSION file) and commit with a message
git add --all
if ! git commit -m "VERSION is updated to $newVersion"; then
    # If the commit fails, print an error and exit
    echo "Error: Failed to commit changes."
    exit 1
fi

# Define remotes and their URLs in an associative array
declare -A remotes=(
    ["github"]="git@github.com:hacknitive/utilsweb.git"
    ["gitlab"]="git@gitlab.com:hacknitive/utilsweb.git"
)

# Ensure the remotes are added
for remote in "${!remotes[@]}"; do
    echo "=============================== Check if $remote remote exists"

    # Check if the remote exists by searching for the remote name
    if ! git remote | grep -q "^$remote$"; then
        # If the remote doesn't exist, add it using the URL from the array
        echo "$remote remote not found. Adding $remote..."
        git remote add "$remote" "${remotes[$remote]}"
        if [ $? -ne 0 ]; then
            # If adding the remote fails, print an error and exit
            echo "Error: Failed to add $remote remote."
            exit 1
        fi
    else
        # If the remote already exists, just print a message
        echo "$remote remote already exists."
    fi
done

echo "=============================== Create the new tag"

# Create a new Git tag with the new version
if ! git tag "$newVersion"; then
    # If creating the tag fails, print an error and exit
    echo "Error: Failed to create or list tags."
    exit 1
fi

# List all tags to confirm the new one has been created
git --no-pager tag

# Push the changes and the new tag to the remotes
for remote in "${!remotes[@]}"; do
    echo "=============================== Push to $remote"
    # Push the new tag and master branch to the remote repository
    if ! git push --tags "$remote" master; then
        # If the push fails, print an error and exit
        echo "Error: Failed to push to $remote."
        exit 1
    fi
done

# Print a success message with the new version
echo "=============================== Version updated to $newVersion."