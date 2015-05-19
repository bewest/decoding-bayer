#!/bin/bash

INPUT=${1-'-'}

# cat bayer-contour-nextlink-interupt-stall.csv | while IFS=',' read level sp i offset dur len err dev ep record data summary ascii ; do    IFS=' ' read direction txn rest <<< "$record"; if [[ $direction == "OUT" || $direction ==  "IN" ]] ; then test $txn == "txn" && echo $offset $direction ; echo $data | xxd -r -p | xxd  ; fi ; done  | head -600 
cat $INPUT | while IFS=',' read level sp i offset dur len err dev ep record data summary ascii ; do
  IFS=' ' read direction txn rest <<< "$record"
  if [[ $direction == "OUT" || $direction ==  "IN" ]] ; then
    if [[ $txn == "txn" ]] ; then
    # test $txn == "txn" && echo -n '##' $offset $direction && echo ' '$(echo $data | wc -w) && (echo $data | xxd -r -p | xxd | sed 's,^,    ,g') && echo ''
    # test 
      echo -n '##' $offset $direction
      echo ' '$(echo $data | wc -w)
      (echo $data | xxd -r -p | xxd | sed 's,^,    ,g')
      echo ''
    fi
  fi
done

