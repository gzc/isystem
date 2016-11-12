# ZOOKEEPER

---
***

## what is zookeeper
  * Developed at Yahoo! for internal use
  * Inspired by Chubby (Google's global lock service)
  * Use by Yahoo! YMB and Crawler
  * Open source, as part of Hadoop (MapReduce)
  * Widely-used by companies

## Motivation: many applications need a "master" service
  * Example: GFS
    * master has list of chunk servers for each chunk
    * master decides which chunk server is primary
  * Other examples: YMB, Crawler, etc.
    * YMB needs master to shard topics
    * Crawler needs master that commands page fetching 
    	(e.g., a bit like the master in mapreduce)
  * Master service typically used for "coordination"
  * Zookeeper: a generic "master" service


## Zookeeper API overview
  * replicated state machine
    * several servers implementing the service
    * operations are performed in global order
      * with some exceptions, if consistency isn't important
  * the replicated objects are: znodes
    * hierarchy of znodes
      * named by pathnames
    * znodes contain **metadata** of application
      * configuration information
        * machines that participate in the application
        * which machine is the primary
      * timestamps
      * version number
    * types of znodes:
      * regular
      * empheral
      * sequential: name + seqno
        * seqno(p) >= max(children)
  * sessions
    * clients sign into zookeeper
    * session allows a client to fail-over to another zookeeper service
      * client know the term and index of last completed operation
      * send it on each request
        * service performs operation only if caught up with what client has seen
    * sessions can timeout
      * client must refresh a session continuously
        * send a heartbeat to the server (like a lease)
      * zookeer considers client "dead" if doesn't hear from a client
      * client may keep doing its thing (e.g., network partition)
        * but cannot perform other zookeeper ops in that session

## Operations on znodes
  	create(path, data, flags)
  	delete(path, version)
      if znode.version = version, then delete
  	exists(path, watch)
  	getData(path, watch)
  	setData(path, data, version)
    	if znode.version = version, then update
  	getChildren(path, watch)
  	sync()
  	
1. above operations are asynchronous
2. all operations are FIFO-ordered per client
3. sync waits until all preceding operations have been "propagated"

## Ordering guarantees
  * all write operations are totally ordered, if a write is performed by zookeeper, later writes from other clients see it
  * all operations are FIFO-ordered per client
  * implications:
    * a read observes the result of an earlier write from the same client
    * a read observes some prefix of the writes, perhaps not including most recent write
      -> read can return stale data
    * if a read observes some prefix of writes, a later read observes that prefix too


## Example usage 1: slow lock
  
### acquire lock:
   	retry:
    	r = create("app/lock", "", empheral)
     	if r:
       		return
     	else:
       		getData("app/lock", watch=True)

    watch_event:
       goto retry
      
### release lock: (voluntarily or session timeout)
    delete("app/lock")


## Challenge: Read operations
  * Many operations are read operations
    * they don't modify replicated state
  * Must they go through ZAB/Raft or not?
  * Can any replica execute the read op?
  * Performance is slow if read ops go through Raft
    * Adds: 1 PRC to and 1 write at each replica --- ouch!

**Problem: read may return stale data if only master performs it**


**Zookeeper solution**: *don't promise non-stale data (by default)*
	
 * Reads are allowed to return stale data
 * Reads can be executed by any replica
 * Read throughput increases as number of servers increases
 * Read returns the last xid it has seen
 * Only sync-read() guarantees data is not stale, goes through **ZAB layer**


References: https://pdos.csail.mit.edu/6.824/notes/l-zookeeper.txt
  
  

