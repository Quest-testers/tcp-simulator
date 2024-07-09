#!/bin/bash

# AWS CodeArtifact configuration
AWS_REGION="ap-south-1"
REPOSITORY_ENDPOINT="https://questpoc-851725253190.d.codeartifact.${AWS_REGION}.amazonaws.com/npm/poc/"
PACKAGE_NAME="my-angular-app"

# Directory where the Angular app is deployed
APP_DIR="/home/ec2-user/angular/my-angular-app"

# Function to compare versions
version_compare() {
    printf '%s\n' "$@" | sort -V | head -n 1
}

# Authenticate with AWS CodeArtifact
auth_token=$(aws codeartifact get-authorization-token --domain questpoc --domain-owner 851725253190 --query authorizationToken --output text)
npm config set //questpoc-851725253190.d.codeartifact.${AWS_REGION}.amazonaws.com/npm/poc/:_authToken $auth_token

# Get current installed version of the Angular app
current_version=$(npm list --depth=0 $PACKAGE_NAME 2>/dev/null | grep $PACKAGE_NAME | awk '{print $NF}')
current_version=${current_version#*@}

# Get latest version available in CodeArtifact
latest_version=$(npm view $PACKAGE_NAME version)

# Check if the package is installed or not
if [ -z "$current_version" ]; then
    echo "No version of $PACKAGE_NAME is currently installed. Installing the latest version $latest_version..."

    # Install the latest version from CodeArtifact
    npm install ${PACKAGE_NAME}@${latest_version}

    # Extract the downloaded package
    tarball_path=$(npm pack ${PACKAGE_NAME}@${latest_version} | tail -n 1)
    mkdir -p $APP_DIR
    tar -xzf $tarball_path -C $APP_DIR --strip-components=1

    # Cleanup - remove the downloaded .tgz file
    rm $tarball_path
