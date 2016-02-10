# SystemsBible
my systems bible


## Theory

[paxos解读](http://drmingdrmer.github.io/tech/distributed/2015/11/11/paxos-slide.html)

## Resource

[OS history](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiBgJzJ0pTKAhVD1mMKHYDvAAkQFggiMAE&url=http%3A%2F%2Fweb.mst.edu%2F~ercal%2F284%2Fslides-1%2FCHAP2.ppt&usg=AFQjCNEkcTtlkmFs2YE9-7Jp9pLfvrZU_A&bvm=bv.110151844,d.cGc) 从batch system -> multiprogramming system -> time-sharing -> micro kernel......

[Hadoop YARN](http://www.zhihu.com/question/23167837) 介绍yarn的工作流

[zookeeper](https://www.zhihu.com/question/35139415#answer-20040689) 理解zookeeper

[Field Guide To Hadoop](http://www.allitebooks.com/field-guide-to-hadoop/) 介绍Hadoop生态系统

[micro kernels introduction](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0ahUKEwiBgJzJ0pTKAhVD1mMKHYDvAAkQFggyMAM&url=http%3A%2F%2Ffaculty.cs.nku.edu%2F~waldenj%2Fclasses%2F2007%2Fspring%2Fcsc660%2Flectures%2FMicrokernels.ppt&usg=AFQjCNGFhhR9HvFMab6Hoeh03xcn--fGeg&bvm=bv.110151844,d.cGc)

## 课程资源
[UCSD Network Service](http://cseweb.ucsd.edu/~gmporter/classes/wi15/cse124/index.html) 学习分布式前可以温习下,网络基础,数据中心,可靠性与容错. Lab是写一个http server, Hadoop map reduce和twitter RPC的一个服务.

[UCSD OS](http://cseweb.ucsd.edu/classes/fa15/cse120-a/) Lab是Nachos Operating System,一个Java实现的toy OS.

[UCSD advanced OS](https://cseweb.ucsd.edu/classes/wi16/cse221-b/syllabus.html) 每节课读两篇论文,lab是systems performance measurement,测量包括CPU,Memory,Network和File Systems的一些性能.

[MIT6.824 yfs lab](https://pdos.csail.mit.edu/archive/6.824-2012/labs/) 这个lab做完收获会很大很多,现在的6.824是Go lang的lab. 你会实现一个基本的本地文件系统,然后实现RPC扩展到网络文件系统,然后还会实现paxos.  [网友的实现](https://github.com/ldaochen/yfs2012) [我一个学弟的代码](https://github.com/gaocegege/CSE-Labs) 我们SJTU软件学院是大二写的这个lab,我的代码已经找不到了.


## ARCHITECTURE
[WEB SEARCH FOR A PLANET :THE GOOGLE CLUSTER ARCHITECTURE](./papers/Google/Google_Cluster_Architecture.md)



## Paper Reading

### OS/Architecture Interaction

[The Performance of µ-Kernel-Based Systems](./papers/OS_Architecture/The_Performance_of_µ-Kernel-Based_Systems.md)  **SOSP 97'**
