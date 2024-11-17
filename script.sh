#!/bin/bash

# Function to read and print export commands from the JSON config file
load_config() {
    local json_file="$1"
    if [[ -f "$json_file" ]]; then
        while IFS="=" read -r key value; do
            value=$(echo "$value" | sed 's/^"//;s/"$//')  # Trim quotes if present
            echo "export $key='$value'"
        done < <(jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' "$json_file")
    else
        echo "Error: File $json_file not found"
        exit 1
    fi
}

# Path to your JSON config file
CONFIG_FILE="/home/pinaka/pinak/$IP_ADDRESS/config.json"

# Load and execute the configuration as exports
eval $(load_config "$CONFIG_FILE")
