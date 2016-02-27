[Soft Updates: A Solution to the Metadata Update Problem in File Systems](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjOxNfwwJfLAhVX0GMKHaZMBaAQFggdMAA&url=http%3A%2F%2Fwww.read.seas.harvard.edu%2F~kohler%2Fclass%2F04f-aos%2Fref%2Fganger00soft.pdf&usg=AFQjCNHDQGUSJFch6pltCes-Ftmpuq4XsA&sig2=0yk58PLB1pUsq2KupG6M-Q)

**Soft update**是一种保持文件系统meta-data consistency的方法. 当要更新磁盘meta-data的时候, 文件系统会根据dependency的信息, 有次序去更新. 另外一种保持一致性的方法是**Journaling**.

**Soft Update** 允许那些不会导致文件系统信息不一致的异步写入，也可以允许那些仅仅导致资源浪费的写.(比如我删文件夹D下的文件A, 我先擦除D中的entry, 然后没电了, 这个inode就被浪费了).

**Soft Update**的特点就是 **fsck** 快, 因为 **meta-data** 是**consistent**的. 只需要在 **后台** 做一下资源的回收. 比如上面提到的inode浪费了, 是可以被fsck检查出来的. 因为这个inode没有被任何目录reference. 这些只需要在后台运行, 所以 **mount filesystem** 很快.
