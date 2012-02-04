#!/bin/bash
git archive --format=tar --prefix=fcmp_1.2.2/ HEAD | gzip > ../fcmp_1.2.2.orig.tar.gz
