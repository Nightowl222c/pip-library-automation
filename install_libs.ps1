# Define the list of packages to install
$packages_to_install = "python-gitlab", "python-dotenv", "gitpython", "jsonpath-ng", "jsonpath-rw-ext"

# Define a function to update pip
function Update-Pip {
    try {
        pip install --upgrade pip
        Write-Host "The pip installer has been successfully updated."
    }
    catch {
        Write-Host "An error occurred while updating pip: $_"
    }
}

# Define a function to install packages
function Install-Packages {
    param($packages)
    try {
        Update-Pip
        foreach ($package in $packages) {
            pip install $package
            Write-Host "The package '$package' has been installed."
        }
    }
    catch {
        Write-Host "An error occurred while installing the package '$package': $_"
    }
}

# Define a function to get installed packages
function Get-InstalledPackages {
    try {
        pip list
    }
    catch {
        Write-Host "An error occurred while getting installed packages: $_"
    }
}

# Main script
try {
    Write-Host "Starting the installation of the packages..."
    Install-Packages $packages_to_install
    Get-InstalledPackages
    Write-Host "The installation of the packages has been completed."
}
catch {
    Write-Host "An error occurred: $_"
}
finally {
    Read-Host "Press Enter to exit the script..."
}