dnl Process this file with autoconf to produce a configure script.
AC_INIT([fcmp],[1.2.2])
AC_CONFIG_SRCDIR([fcmp.c])
AM_INIT_AUTOMAKE
AC_CONFIG_HEADERS([config.h])

dnl Checks for programs.
AC_PROG_CC
AM_CONDITIONAL(USING_GCC, test x$GCC = xyes)

AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MAKE_SET
AM_PROG_LIBTOOL

dnl Checks for libraries. (Add them to LIBS if present.)
AC_CHECK_LIB(m, main)

dnl Checks for header files.

dnl Checks for typedefs, structures, and compiler characteristics.

dnl Checks for library functions.

AC_OUTPUT(Makefile)
AC_OUTPUT(fcmp.pc)
