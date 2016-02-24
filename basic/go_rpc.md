 https://golang.org/doc/effective_go.html

# Remote Procedure Call (RPC)
  * a key piece of distributed system machinery
  * goal: easy-to-program network communication
    * hides most details of client/server communication
    * client call is much like ordinary procedure call
    * server handlers are much like ordinary procedures
  * RPC is widely used!

<pre>
RPC ideally makes net communication look just like fn call:
  Client:
    z = fn(x, y)
  Server:
    fn(x, y) {
      compute
      return z
    }
  RPC aims for this level of transparency
</pre>

Go example:
  https://golang.org/pkg/net/rpc/

    RPC message diagram:
      Client             Server
          request--->
                 <---response

<pre>
Software structure
  client app         handlers
    stubs           dispatcher
   RPC lib           RPC lib
     net  ------------ net
</pre>

# A few details:
  * Which server function (handler) to call?
  * Marshalling: format data into packets
    * Tricky for arrays, pointers, objects, &c
    * Go's RPC library is pretty powerful!
    * some things you cannot pass: e.g., channels, functions
  * Binding: how does client know who to talk to?
    * Maybe client supplies server host name
    * Maybe a name service maps service names to best server host
  * Threads:
    * Clients may have many threads, so > 1 call outstanding, match up replies
    * Handlers may be slow, so server often runs each in a thread

# RPC problem: what to do about failures?
  e.g. lost packet, broken network, slow server, crashed server

# What does a failure look like to the client RPC library?
  * Client never sees a response from the server
  * Client does *not* know if the server saw the request!
  * Maybe server/net failed just before sending reply

# Simplest scheme: "at least once" behavior
  * RPC library waits for response for a while
  * If none arrives, re-send the request
  * Do this a few times
  * Still no response -- return an error to the application


# Better RPC behavior: "at most once"
  * idea: server RPC code detects duplicate requests
    returns previous reply instead of re-running handler
  * Q: how to detect a duplicate request?
  * client includes unique ID (XID) with each request
    * uses same XID for re-send

<pre>
  server:
    if seen[xid]:
      r = old[xid]
    else
      r = handler()
      old[xid] = r
      seen[xid] = true
</pre>

# some at-most-once complexities
  * how to ensure XID is unique?
    * big random number?
    * combine unique client ID (ip address?) with sequence #?
  * server must eventually discard info about old RPCs
    * when is discard safe?
    * idea:
      * unique client IDs
      * per-client RPC sequence numbers
      * client includes "seen all replies <= X" with every RPC
      * much like TCP sequence #s and acks
    * or only allow client one outstanding RPC at a time
      * arrival of seq+1 allows server to discard all <= seq
    * or client agrees to keep retrying for < 5 minutes
      * server discards after 5+ minutes
  * how to handle dup req while original is still executing?
    * server doesn't know reply yet; don't want to run twice
    * idea: "pending" flag per executing RPC; wait or ignore

# What if an at-most-once server crashes and re-starts?
  * if at-most-once duplicate info in memory, server will forget
    * and accept duplicate requests after re-start
  * maybe it should write the duplicate info to disk?
  * maybe replica server should also replicate duplicate info?

# What about "exactly once"?
  * at-most-once plus unbounded retries plus fault-tolerant service

# Go RPC is "at-most-once"
  * open TCP connection
  * write request to TCP connection
  * TCP may retransmit, but server's TCP will filter out duplicates
  * no retry in Go code (i.e. will NOT create 2nd TCP connection)
  * Go RPC code returns an error if it doesn't get a reply
    * perhaps after a timeout (from TCP)
    * perhaps server didn't see request
    * perhaps server processed request but server/net failed before reply came back



# structure (next all talk about [rpc](./labrpc.go) in go)
<pre>
struct Network
  description of network
    servers
    client endpoints
  mutex per network
</pre>


# RPC overview
<pre>
   many examples in test_test.go
    e.g., TestBasic()
    application calls Call()
      reply := end.Call("Raft.AppendEntries", args, &reply) --   * send an RPC, wait for reply
    servers side:
      srv := MakeServer()
      srv.AddService(svc) -- a server can have multiple services, e.g. Raft and k/v
        pass srv to net.AddServer()
      svc := MakeService(receiverObject) -- obj's methods will handle RPCs
        much like Go's rpcs.Register()
        pass svc to srv.AddService()
</pre>

# struct Server
  * a server support many services

# AddService
  * add a service name
  * Q: why a lock?
  * Q: what is defer()?

# Dispatch
  * dispatch a request to the right service
  * Q: why hold a lock?
  * Q: why not hold lock to end of function?

# Call():
  * Use reflect to find type of argument
  * Use gob marshall argument
  * e.ch is the channel to the network to send request
  * Make a channel to receive reply from network ( <- req.replyCh)

* MakeEnd():
  * has a thread/goroutine that simulates the network
    * reads from e.ch and process requests
    * each requests is processed in a separate goroutine
      * Q: can an end point have many outstanding requests?
    * Q: why rn.mu.Lock()?
    * Q: what does lock protect?

* ProcessReq():
  * finds server endpoint
  * if network unreliable, may delay and drop requests,
  * dispatch request to server in a new thread
  * waits on reply by reading ech or until 100 msec has passed
    * 100 msec just to see if server is dead
  * then return reply
    * Q: who will read the reply?
  * Q: is ok that ProcessReq doesn't hold rn lock?

* Service.dispatch():
 * find method for a request
 * unmarshall arguments
 * call method
 * marshall reply
 * return reply

<pre>
Go's "memory model" requires explicit synchronization to communicate!
  This code is not correct:
    var x int
    done := false
    go func() { x = f(...); done = true }
    while done == false { }
  it's very tempting to write, but the Go spec says it's undefined
  use a channel or sync.WaitGroup or instead
</pre>


# Study the Go tutorials on goroutines and channels
  * Use Go's race detector:
    https://golang.org/doc/articles/race_detector.html

        go test --race mypkg
