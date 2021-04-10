# SystemsBible
my systems bible

## Cracking System Design Interviews
[Consistent Hashing](https://youtu.be/aj1mXvHNcbQ)

[Consistent Hashing 一致性哈希中文版](https://youtu.be/mdR5VIeStcQ)

[Design a Web Crawler](https://youtu.be/vxqjjB3b-Zg)

[Design a Web Crawler 设计网络爬虫中文版](https://youtu.be/P8LFhmC2efc)

[Message Queue & RabbitMQ & Kafka](https://youtu.be/jeMbHH6PJIA)

[消息队列 & RabbitMQ & Kafka 中文版](https://youtu.be/5BdGCANeV2o)

## Background Enhancement

[文件系统](./basic/fs.md)

## Distributed Systems & Big Data
[Hadoop Intro](./bigdata/hadoop/intro.md) | [Hadoop YARN](http://www.zhihu.com/question/23167837) 介绍yarn的工作流 | [HDFS Performance](./bigdata/hadoop/hdfs_optimization.md) Improve the performance of HDFS

[Spark example](./bigdata/spark/sparktest)

[zookeeper](./bigdata/zookeeper/intro.md) 理解zookeeper

[Field Guide To Hadoop](http://www.allitebooks.com/field-guide-to-hadoop/) 介绍Hadoop生态系统

[数据序列化:Java序列化、Kryo、ProtoBuf序列化](./bigdata/serialization.md)

[分布式监控工具Ganglia](./bigdata/cluster_monitor.md)

[two-phase commit](./bigdata/algorithm/2pc.md) | [three-phase commit](./bigdata/algorithm/3pc.md)


## Theory

[paxos解读](http://drmingdrmer.github.io/tech/distributed/2015/11/11/paxos-slide.html)

## 课程资源
[UCSD Network Service](http://cseweb.ucsd.edu/~gmporter/classes/wi15/cse124/index.html) 学习分布式前可以温习下,网络基础,数据中心,可靠性与容错. Lab是写一个http server, Hadoop map reduce和twitter RPC的一个服务.

[UCSD OS](http://cseweb.ucsd.edu/classes/fa15/cse120-a/) Lab是Nachos Operating System,一个Java实现的toy OS.

[UCSD advanced OS](https://cseweb.ucsd.edu/classes/wi16/cse221-b/syllabus.html) 每节课读两篇论文,lab是systems performance measurement,测量包括CPU,Memory,Network和File Systems的一些性能.

[MIT6.824 yfs lab](https://pdos.csail.mit.edu/archive/6.824-2012/labs/) 这个lab做完收获会很大很多,现在的6.824是Go lang的lab. 你会实现一个基本的本地文件系统,然后实现RPC扩展到网络文件系统,然后还会实现paxos.  [网友的实现](https://github.com/ldaochen/yfs2012) [我一个学弟的代码](https://github.com/gaocegege/CSE-Labs) 我们SJTU软件学院是大二写的这个lab,我的代码已经找不到了.


## ARCHITECTURE
[WEB SEARCH FOR A PLANET :THE GOOGLE CLUSTER ARCHITECTURE](./papers/Google/Google_Cluster_Architecture.md)

[MapReduce](./papers/Google/mr.md) **OSDI' 04**

[The Google File System](./papers/Google/gfs.md) **SOSP' 03**

[RPC in Golang](./basic/go_rpc.md)

[f4: Facebook's Warm BLOB Storage System](./papers/facebook/f4.md) **OSDI' 14**

## Paper Reading

### Communication

[Implementing Remote Procedure Calls](./papers/communication/rpc.md) **TOCS' 84**

[IX: A Protected Dataplane Operating System for High Throughput and Low Latency](./papers/communication/IX.md) **OSDI' 14 Best Paper**

### OS/Architecture Interaction

[The Performance of µ-Kernel-Based Systems](./papers/OS_Architecture/The_Performance_of_µ-Kernel-Based_Systems.md)  **SOSP' 97**

[Exokernel: An Operating System Architecture for Application-Level Resource Management](./papers/OS_Architecture/Exokernel.md) **SOSP' 95**

[The Multikernel: A new OS architecture for scalable multicore systems](./papers/OS_Architecture/Multikernel.md) **SOSP' 09**

[An Analysis of Linux Scalability to Many Cores](./papers/OS_Architecture/Corey2.md) **OSDI' 10**

### Virtualization

[Xen and the Art of Virtualization](./papers/virtualization/xen.md) **SOSP' 03**

[Cells: A Virtual Mobile Smartphone Architecture](./papers/virtualization/Cells.md)  **SOSP' 11**

### Scheduler

[Scheduler Activations: Effective Kernel Support for the User-Level Management of Parallelism](./papers/scheduling/Scheduler_Activations.md) **SOSP' 91**

[Lottery Scheduling: Flexible Proportional-Share Resource Management](./papers/scheduling/lottery.md) **OSDI' 94**

### I/O and File Systems

[A Fast File System for Unix](./papers/fs/ffs.md) **TOCS' 84**

[The Design and Implementation of a Log-Structured File System](./papers/fs/lfs.md) **TOCS' 92**

[The Rio file cache: surviving operating system crashes](./papers/fs/rio.md) **ASPLOS' 96**

[Soft Updates: A Solution to the Metadata Update Problem in File Systems](./papers/fs/softupdate.md) **TOCS' 00**
