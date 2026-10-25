#!/bin/bash

set -e
cd "$(dirname "$0")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ "$#" -eq 0 ]; then
    echo -e "${RED}❌ No index names provided."
    echo -e "${YELLOW}Usage: $0 index_0001 index_0002 ...${NC}"
    exit 1
fi

INDEXES=("$@")

echo -e "${GREEN}=== Starting batch run of indexes: ${INDEXES[*]} ===${NC}"

for index in "${INDEXES[@]}"; do
    echo ""
    echo -e " ${GREEN} ℹ️   Running $index${NC}"

    SRC_FILE="datasets/$index/processing.py"
    TARGET_FILE="main.py"

    if [[ -f "$SRC_FILE" ]]; then
        cp "$SRC_FILE" "$TARGET_FILE"

        echo -e "${GREEN} ℹ️   Copied $SRC_FILE to $TARGET_FILE${NC}"
        
        # Run the script, log success/failure
        if python3 "$TARGET_FILE"; then
            echo -e "${GREEN}✅ $index completed successfully${NC}"
        else
            echo -e "${RED}❌ $index failed to execute${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️ $SRC_FILE not found. Skipping.${NC}"
    fi
done

echo ""
echo -e "${GREEN}=== Batch run complete ===${NC}"
