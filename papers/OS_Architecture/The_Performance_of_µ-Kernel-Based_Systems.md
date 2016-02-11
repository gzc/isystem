[The Performance of Micro-Kernel- Based Systems](http://cseweb.ucsd.edu/classes/fa01/cse221/papers/haertig-ukernel-perf-sosp97.pdf)

# Goals


* Native OS(Linux) performance on Micro-Kernel(5-10% lower)
* CO-LOCATED OS
* specialization(PIPES), extensibility(CACHE-AWARE, VM, REAL-TIME)
* 100% binary compatibility

# Basic

`What is a microkernel`

1. kernels that only provide **process + address spaces**(memory), **threads**(CPU), and **IPC**(communication)
2. kernel does not handle e.g. the file system or interrupts

`what is L4`

1. so called 2nd generation microkernel
2. built from scratch as opposed to a developed from earlier monolithic kernel approaches (e.g. Mach)

`L4 essentials`

1. threads, address spaces and cross-address-space communication (IPC)
2. other kernel operations e.g. RPC and address-space crossing thread migration are built up from IPC primitives

`Address spaces`

1. recursive construction
2. granting, mapping, unmapping
3. a page owner can grant or map any of its pages to another address space with the receiver permission.  That page is then accessible to both address spaces
4. only the grant, map, and unmap are implemented in the kernel
5. user-level “pagers” handle page faults

`Interrupts, exceptions, and traps`

1. all handled at user level
2. interrupts are transformed, by kernel, into IPC messages and sent to appropriate user level thread
3. exceptions and traps are synchronous to associated thread and kernel mirrors them to that thread


***

Slower than native linux

GNU/HURD就是微内核的，你如果感兴趣，可以使用kexec命令自动切换内核去尝试一下.

微内核的坏处，光性能损耗一条就够了。那么多驱动运行在非0态，每次进程调度导致 TLB 刷新，调度后运行稍微多些代码，又导致L1、L2 失效。

**Tagged TLB** <br />
  不需要flush, speed up. But reduce the size of effective TLB.
