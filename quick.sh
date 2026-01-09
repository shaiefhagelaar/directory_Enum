#!/bin/bash

for dir in admin upload uploads files api images css js assets; do
    echo "Checking /$dir:"
    curl -s -o /dev/null -w "%{http_code}" http://{target_machine}/$dir/
    echo ""
done
