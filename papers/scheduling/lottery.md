# Lottery Scheduling

[lottery.c](./lottery.c)

Lottery Scheduling is a probabilistic scheduling algorithm for processes in an operating system. Processes are each assigned some number of lottery tickets, and the scheduler draws a random ticket to select the next process. The distribution of tickets need not be uniform; granting a process more tickets provides it a relative higher chance of selection. This technique can be used to approximate other scheduling algorithms, such as Shortest job next and Fair-share scheduling.

Lottery scheduling solves the problem of starvation. Giving each process at least one lottery ticket guarantees that it has non-zero probability of being selected at each scheduling operation.

Implementations of lottery scheduling should take into consideration that there could be billions of tickets distributed among a large pool of threads. To have an array where each index represents a ticket, and each location contains the thread corresponding to that ticket, may be highly inefficient. Lottery scheduling can be preemptive or non-preemptive.

Lottery scheduling is **starvation-free**
Every ticket holder will finally get  the resource

**ticket currency** : Currency allows a user with a set of tick- ets to allocate tickets among their own jobs in whatever currency they would like; the system then automatically converts said currency into the correct global value.

**ticket transfer** : With transfers, a process can temporarily hand off its tickets to another process

**ticket inflation** : a process can temporarily raise or lower the number of tickets it owns.
