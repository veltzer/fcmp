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
# File: fcmp.spec
#
# Description: RPM spec file

Summary: Safer floating-point comparison
Name: fcmp
Version: 1.2.2
Release: 1
Copyright: LGPL
Group: Development/Libraries
Source: http://download.sourceforge.net/fcmp/fcmp-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-root
URL: http://fcmp.sourceforge.net/
Packager: Theodore C. Belding <Ted.Belding@umich.edu>

%description
It is generally not wise to compare two floating-point values for
exact equality, for example using the C == operator.  The fcmp package
implements Knuth's suggestions for safer floating-point comparison
operators as a C function.

%prep
%setup -q

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=${RPM_BUILD_ROOT}%{_prefix} \
    exec_prefix=${RPM_BUILD_ROOT}%{_exec_prefix} \
    bindir=${RPM_BUILD_ROOT}%{_bindir} \
    sbindir=${RPM_BUILD_ROOT}%{_sbindir} \
    libexecdir=${RPM_BUILD_ROOT}%{_libexecdir} \
    datadir=${RPM_BUILD_ROOT}%{_datadir} \
    sysconfdir=${RPM_BUILD_ROOT}%{_sysconfdir} \
    sharedstatedir=${RPM_BUILD_ROOT}%{_sharedstatedir} \
    localstatedir=${RPM_BUILD_ROOT}%{_localstatedir} \
    libdir=${RPM_BUILD_ROOT}%{_libdir} \
    infodir=${RPM_BUILD_ROOT}%{_infodir} \
    mandir=${RPM_BUILD_ROOT}%{_mandir} \
    includedir=${RPM_BUILD_ROOT}%{_includedir} \
    oldincludedir=${RPM_BUILD_ROOT}%{_oldincludedir} \
	install

%post
ldconfig

%preun

%postun
ldconfig 

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)

%doc AUTHORS COPYING INSTALL NEWS README THANKS 

%{_includedir}/*
%{_libdir}/*
%{_mandir}/man*/*

%changelog
* Thu Nov 4 2000 Theodore C. Belding <Ted.Belding@umich.edu>
- Use fcmp 1.2.2

* Thu Nov 2 2000 Theodore C. Belding <Ted.Belding@umich.edu>
- Use fcmp 1.2.1

* Sun Oct 1 2000 Theodore C. Belding <Ted.Belding@umich.edu>
- Initial version
