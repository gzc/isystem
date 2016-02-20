# Feature

## 统一命名空间.
跟访问普通文件系统一样.

## namenode vs. datanode
namenode相当于master,协调全局;datanode是slave节点,负责储存实际数据,组织自己机器上的block.

## 多重备份, racks.
可以设置replication数量,分散到不同的rack.

## 负载均衡, rebalancing.
可以强制要求磁盘利用率不高于某一个threshold(当集群容量足够大)

## 流式读(locality)
streaming data access. 读的时候会从近的rack去读.

## Replication Pipelining
接力棒. Client create file(备份比如为3). 那么数据流就是Client -> machine A -> machine B -> machine C.

## Data Integrity
有checksum

## Metadata Disk Failure
有多个FsImage和Editlog

## Write once read many
一次写多次读,天然高吞吐量

## Heartbeat携带message,进行交流.
namenode不主动发起请求, datanode发送心跳信息到namenode, namenode再把要做的事情返回(无非就是一种特定的protocal)

## Snapshot(快照)
备份,也是放在HDFS.重要的文件就建个snapshot呗.

## safemode
namenode刚起来,会收集所有机器的信息.这时候是safenode,无法写;等信息收集完毕会exit samenode.

## Secondary namenode vs. HA(high avaliablity)
Secondary namenode是Hadoop Version1 的特性.并不是第二个server.而是一个辅助机器帮助namenode merge Editlog, FsImage. Hadoop Version2的HA才是第二个server.
