import subprocess
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s', handlers=[logging.FileHandler('install_lib.log'), logging.StreamHandler()])

def update_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        logging.info("The pip installer has been successfully updated.")
    except Exception as e:
        logging.error(f"An error occurred while updating pip: {e}")

def install_packages(packages):
    try:
        update_pip()
        for package in packages:
            result = subprocess.check_output([sys.executable, "-m", "pip", "install", package], stderr=subprocess.STDOUT)
            result = result.decode("utf-8")
            logging.info(f"The following installation messages were generated for '{package}':\n{result}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error: The package '{package}' could not be installed. Error details:\n{e.output.decode('utf-8')}")
    except Exception as e:
        logging.error(f"Error: An unexpected error occurred while installing '{package}': {e}")

def list_installed_packages():
    try:
        result = subprocess.check_output([sys.executable, "-m", "pip", "list", "--format=columns"], stderr=subprocess.STDOUT)
        installed_packages = result.decode("utf-8").splitlines()[2:]
        logging.info("\nList of installed packages:")
        for package in installed_packages:
            logging.info(package)
    except Exception as e:
        logging.error(f"An error occurred while listing installed packages: {e}")

if __name__ == "__main__":
    logging.info("Starting the installation of the packages...")
    packages_to_install = ["python-gitlab", "python-dotenv", "gitpython", "jsonpath-ng", "jsonpath-rw-ext"]
    install_packages(packages_to_install)
    list_installed_packages()
    logging.info("The installation of the packages has been completed.")
    input("Press the Enter key to exit the script...")
