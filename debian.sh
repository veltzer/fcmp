#!/bin/bash
git archive --format=tar --prefix=fcmp_1.2.2/ HEAD | gzip > ../fcmp_1.2.2.orig.tar.gz
dh_make --packagename fcmp_1.2.2 --library --copyright gpl2 --email mark.veltzer@gmail.com
rm -f ../fcmp_1.2.2.orig.tar.gz
