# Path to the VERSION file
$versionFilePath = "VERSION"

Write-Host "=============================== Check if VERSION exists"
# Check if the VERSION file exists
if (-not (Test-Path $versionFilePath)) {
    Write-Host "Error: VERSION file not found."
    # If the VERSION file doesn't exist, set the current version to v0.0.0
    $currentVersion = "v0.0.0"
    Write-Host "Current version is: $currentVersion"
} else {
    # Read the current version from the VERSION file
    $currentVersion = Get-Content -Path $versionFilePath
    Write-Host "Current version is: $currentVersion"
}

# Ensure the version follows the vx.y.z format
if ($currentVersion -notmatch "^v[0-9]+\.[0-9]+\.[0-9]+$") {
    Write-Host "Error: VERSION does not contain a valid version (vx.y.z format)."
    exit 1
}

Write-Host "=============================== Increment patch"
# Increment the last part (patch) of the version
$parts = $currentVersion.Substring(1).Split('.')
$major = [int]$parts[0]
$minor = [int]$parts[1]
$patch = [int]$parts[2]

# Increment the patch version
$patch += 1

# Form the new version string
$newVersion = "v{0}.{1}.{2}" -f $major, $minor, $patch
Write-Host "New version is: $newVersion"

# Write the new version to the VERSION file
Set-Content -Path $versionFilePath -Value $newVersion

Write-Host "=============================== Commit the change"
try {
    # Stage all changes and commit with a message
    git add --all
    git commit -m "VERSION is updated to $newVersion"
} catch {
    Write-Host "Error: Failed to commit changes."
    exit 1
}

# Define remotes and their URLs
$remotes = @{
    "github" = "git@github.com:hacknitive/utilsweb.git"
    "gitlab" = "git@gitlab.com:hacknitive/utilsweb.git"
}

# Ensure the remotes are added
foreach ($remote in $remotes.Keys) {
    Write-Host "=============================== Check if $remote remote exists"
    # Check if the remote exists
    $remoteExists = git remote | Select-String -Pattern "^$remote$"
    if (-not $remoteExists) {
        # Add the remote if it does not exist
        Write-Host "$remote remote not found. Adding $remote..."
        git remote add $remote $remotes[$remote]
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Error: Failed to add $remote remote."
            exit 1
        }
    } else {
        Write-Host "$remote remote already exists."
    }
}

Write-Host "=============================== Create the new tag"
try {
    # Create a new Git tag with the new version
    git tag $newVersion
    # List all tags to confirm
    git tag
} catch {
    Write-Host "Error: Failed to create or list tags."
    exit 1
}

# Push the changes and the new tag to the remotes
foreach ($remote in $remotes.Keys) {
    Write-Host "=============================== Push to $remote"
    try {
        # Push the tags and master branch to the remote repository
        git push --tags $remote master
    } catch {
        Write-Host "Error: Failed to push to $remote."
        exit 1
    }
}

Write-Host "=============================== Version updated to $newVersion."