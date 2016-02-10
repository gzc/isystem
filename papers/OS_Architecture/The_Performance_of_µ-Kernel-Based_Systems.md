[The Performance of Micro-Kernel- Based Systems](http://cseweb.ucsd.edu/classes/fa01/cse221/papers/haertig-ukernel-perf-sosp97.pdf)

`What is a microkernel`

1. kernels that only provide address spaces, threads, and IPC
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
