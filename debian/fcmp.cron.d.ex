#
# Regular cron jobs for the fcmp package
#
0 4	* * *	root	[ -x /usr/bin/fcmp_maintenance ] && /usr/bin/fcmp_maintenance
