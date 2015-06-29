#!/bin/bash

for i in ./test*.py ; do
    if [ "$1" == "-v" ] ; then
        echo -e "\n\n\e[31mTest: $i\e[0m"
        echo -e "\e[31m=============================================\e[0m"
        python $i -v
    else
        python $i >/dev/null 2>&1
        if [ "$?" == "0" ] ; then
            echo "[Success] $i"
        else
            echo "[Failed]  $i"
        fi
    fi
done
