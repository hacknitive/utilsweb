# Path to the VERSION file
$versionFilePath = "VERSION"

# Check if VERSION exists
if (-not (Test-Path $versionFilePath))
{
    Write-Host "Error: VERSION file not found."
    $currentVersion = "v0.0.0"
    Write-Host "Current version is: $currentVersion"
}
else
{
    # Read the current version from VERSION
    $currentVersion = Get-Content -Path $versionFilePath
    Write-Host "Current version is: $currentVersion"
}

# Ensure the version follows the vx.y.z format
if ($currentVersion -notmatch "^v[0-9]+\.[0-9]+\.[0-9]+$")
{
    Write-Host "Error: VERSION does not contain a valid version (vx.y.z format)."
    exit 1
}

# Increment the last part of the version
$parts = $currentVersion.Substring(1).Split('.')
$major = [int]$parts[0]
$minor = [int]$parts[1]
$patch = [int]$parts[2]

# Increment the patch version
$patch += 1

# Form the new version
$newVersion = "v{0}.{1}.{2}" -f $major, $minor, $patch
Write-Host "New version is: $newVersion"

# Write the new version to VERSION
Set-Content -Path $versionFilePath -Value $newVersion

# Commit the change
Write-Host "git add --all"
git add --all

Write-Host "git commit -m 'VERSION is updated to $newVersion'"
git commit -m "VERSION is updated to $newVersion"

# Create the new tag
Write-Host "git tag $newVersion'"
git tag $newVersion

# Push the changes and the new tag to the server
Write-Host "git push --tags github master"
git push --tags github master
Write-Host "git push --tags gitlab master"
git push --tags gitlab master

Write-Host "Version updated to $newVersion and pushed to the server."