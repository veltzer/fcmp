## Process this file with automake to produce Makefile.in

# fcmp
# Copyright (c) 1999-2000 Theodore C. Belding
# University of Michigan Center for the Study of Complex Systems
# <mailto:Ted.Belding@umich.edu>
# <http://www-personal.umich.edu/~streak/>                
#
# This file is part of the fcmp distribution. fcmp is free 
# software; you can redistribute and modify it under the terms of the 
# GNU Library General Public License (LGPL), version 2 or later.  This 
# software comes with absolutely no warranty. See the file COPYING for 
# details and terms of copying.
#
# File: Makefile
#
# Description: fcmp makefile

## libtool versioning info, from libtool.info

##   Here are a set of rules to help you update your library version
## information:
##
##  1. Start with version information of `0:0:0' for each libtool library.
##
##  2. Update the version information only immediately before a public
##     release of your software.  More frequent updates are unnecessary,
##     and only guarantee that the current interface number gets larger
##     faster.
##
##  3. If the library source code has changed at all since the last
##     update, then increment REVISION (`C:R:A' becomes `C:r+1:A').
##
##  4. If any interfaces have been added, removed, or changed since the
##     last update, increment CURRENT, and set REVISION to 0.
##
##  5. If any interfaces have been added since the last public release,
##     then increment AGE.
##
##  6. If any interfaces have been removed since the last public release,
##     then set AGE to 0.
##
##   *_Never_* try to set the interface numbers so that they correspond
## to the release number of your package.  This is an abuse that only
## fosters misunderstanding of the purpose of library versions.  Instead,
## use the `-release' flag (*note Release numbers::), but be warned that
## every release of your package will not be binary compatible with any
## other release.

if USING_GCC
AM_CFLAGS= -Wall -Werror
endif

## Build a libtool library libDroneUtil.la for installation in libdir.
CURRENT = 2
REVISION = 3
AGE = 0

lib_LTLIBRARIES = libfcmp.la
libfcmp_la_SOURCES = fcmp.c
libfcmp_la_LDFLAGS = -version-info $(CURRENT):$(REVISION):$(AGE)
include_HEADERS = fcmp.h
man_MANS = fcmp.3
EXTRA_DIST = $(include_HEADERS) $(man_MANS) fcmp.spec bootstrap
MOSTLYCLEANFILES = *~ *.bak

pkgconfigdir = /usr/share/pkgconfig
pkgconfig_DATA = fcmp.pc
