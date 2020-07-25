#!/bin/bash

function usage()
{
	echo "fillfs.sh fill | clean | help"
	echo ""
	echo "fill"
	echo "   fills all PMEM file systems with filler data to 80% of capacity"
	echo "clean"
	echo "   cleans up filler files on all PMEM filesystems from previous runs"
	echo "help"
	echo "   This usage message"
}


pct=80
f_name="fill.bin"

case $* in
	fill)
		op=fill
		;;
	clean)
		op=clean
		;;
	help)
		usage
		exit
		;;
	*)
		exit
		;;
esac

# get pmem devices on system.
# /dev/pmem0            1362136    4152   1270740   1% /mnt/pmem0
mnt_list=`df | grep /dev/pmem | awk '{print $6}'`

before=`df -k | grep '/dev/pmem'`

# create template file
# dd if=/dev/zero of=/tmp/fill.bin bs=1G count=1
dd if=/dev/zero of=/tmp/fill.bin bs=1M count=1

for mnt in $mnt_list
do
	# get fs_size fs_used fs_free
	# calc fill required to bring to limit

	size=`df | grep /dev/pmem | awk '{print $2}'`
	used=`df | grep /dev/pmem | awk '{print $3}'`

	# Calc required fill size in GB
	# gig fs_fill=`echo $(( $fs_size - fs_used / 1024 / 1024 ))`

	# fs_fill is the number of files needed to fill the fs to 80%
	f=`echo $(( $size - $used ))`

	fill=`echo $(( $f / 1024 * $pct / 100 ))`

	echo "-------------------- Details --------------------"
	echo "Mount: $mnt"
	echo "Size: $size"
	echo "Used: $used"
	echo "Fill: $fill"

	# this is a fill operation
	if [ "fill" = "$op" ] ; then
		remaining=$fill

		echo "Beginning to fill $mnt with $fill space files"

		while [ $remaining -gt 0 ] 
		do
			/bin/echo -n "... Filling $mnt/fill.bin_$remaining ... "
			cp /tmp/fill.bin $mnt/fill.bin_$remaining
			/bin/echo "  - done"

			remaining=$(( $remaining - 1 ))
		done
	fi

	# clean up operation
	if [ "clean" = "$op" ] ; then
			/bin/echo -n "... Cleaning $mnt/fill.bin* ... "
			/bin/rm -f /tmp/fill.bin $mnt/fill.bin*
			/bin/echo "  - done"
	fi

	echo "-------------------- Finished with $mnt --------------------"

done

after=`df -k | grep '/dev/pmem'`

echo "Before Filling with junk"
echo $before
echo "------------------------------"
echo $after

