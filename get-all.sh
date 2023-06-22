#!/bin/sh

REPO_URL="https://github.com/roomsensr/install.git"
DESTINATION_FOLDER="packages"
DESTINATION_FOLDER2="pyscript"
DESTINATION_FOLDER3="www/cards"
DESTINATION_FOLDER4="custom_components/pyscript"
PYSCRIPT_RELEASE_URL="https://github.com/custom-components/pyscript/releases/download/1.4.0/hass-custom-pyscript.zip"
# Clone the repository
git clone $REPO_URL temp_dir

# Move to the first destination folder if it exists or create it
if [ -d "$DESTINATION_FOLDER" ]; then
    mv temp_dir/packages/* $DESTINATION_FOLDER
else
    mkdir $DESTINATION_FOLDER
    mv temp_dir/packages/* $DESTINATION_FOLDER
fi

# Move to the second destination folder if it exists or create it
if [ -d "$DESTINATION_FOLDER2" ]; then
    mv temp_dir/pyscript/* $DESTINATION_FOLDER2
else
    mkdir $DESTINATION_FOLDER2
    mv temp_dir/pyscript/* $DESTINATION_FOLDER2
fi

# Move card destination folder if it exists or create it
if [ -d "$DESTINATION_FOLDER3" ]; then
    mv temp_dir/cards/* $DESTINATION_FOLDER3
else
    if [ ! -d "www" ]; then
        mkdir www
    fi
    mkdir $DESTINATION_FOLDER3
    mv temp_dir/cards/* $DESTINATION_FOLDER3
fi


if [ -d "$DESTINATION_FOLDER4" ]; then
    :
else
    mkdir -p "$DESTINATION_FOLDER4"
    wget "$PYSCRIPT_RELEASE_URL" -O pyscript-release.zip
    unzip pyscript-release.zip -d "$DESTINATION_FOLDER4"
    rm pyscript-release.zip
fi

mv temp_dir/dash-design.yaml .
mv temp_dir/dashboards.yaml .
mv temp_dir/logo_transparent_background.png www

# Cleanup - remove the temporary directory
rm -rf temp_dir
