# Some tips to improve HDFS performance

1. set **noatime** and **nodiratime** attributes when mount disk.
 * noatime : do not update inode access time in this file system.
 * nodiratime : do not update directory access time in this file system.

2. set the prefetched data-buffer size can significantly improve the performance of sequential data accessing. The default parameter is 256 sectors，we can increase it to 1024/2408 sectors. We have to write this setting to /etc/rc.local，otherwise will be invalid when rebooting.
                              
                /sbin/blockdev --setra 2048 /dev/sda

3. Decrease the preserved blocks in **ext4 file system**. By doing this we can give HDFS more storing space. generally，The default setting is 5%. It can be decreased to 1%.
           
                 sudo tune2fs -m 1 /dev/sdb1 
