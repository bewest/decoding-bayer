
Rendering data from successful run

## `complete-pump-nextlink.csv`

`complete-pump-nextlink.csv` is a TotalPhase csv export.  The
`totalphase_csv_hexdump.sh` renders it into a prettier hexdump that is easier
to audit.

It's a large file, `1359` transactions.

```
complete-pump-nextlink/
├── head-1k.markdown
└── tail-1k.markdown
```
Only the first and last thousand transactions are rendered to markdown.


```
 ./totalphase_csv_hexdump.sh complete-pump-nextlink.csv  | grep  'a7 66' | tr -s ' ' | cut -d' ' -f 5- | while read head line ; do echo  $(python -c "print '{0:#010b}'.format(0x${head:0:2})") ${head:0:2} $head $line ; done | sort | uniq -c  | sort -n | tee complete-pump-nextlink/byte-before-a7.txt 
```
