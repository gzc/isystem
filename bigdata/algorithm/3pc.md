# Three-phase commit protocol

[wiki](https://en.wikipedia.org/wiki/Three-phase_commit_protocol)

[中文wiki](https://zh.wikipedia.org/wiki/%E4%B8%89%E9%98%B6%E6%AE%B5%E6%8F%90%E4%BA%A4)

[2pc vs. 3pc](http://www.hollischuang.com/archives/681)

![](./imgs/Three-phase_commit_diagram.png)

三阶段提交是为解决两阶段提交协议的缺点而设计的.

与两阶段提交不同的是，三阶段提交是“非阻塞”协议。三阶段提交在两阶段提交的第一阶段与第二阶段之间插入了一个准备阶段，使得原先在两阶段提交中，参与者在投票之后，由于协调者发生崩溃或错误，而导致参与者处于无法知晓是否提交或者中止的“不确定状态”所产生的可能相当长的延时的问题得以解决。 举例來说，假设有一个决策小組由一個主持人负责与多位组员以电话联络方式协调是否通过一個提案.

以两阶段提交來說，主持人收到一個提案请求，打电话跟每个组员询问是否通过并统计回复，然后將最后決定打电话通知各组员。要是主持人在跟第一位组员通完电话后失忆，而第一位組員在得知结果并执行后老人痴呆，那么即使重新选出主持人，也沒人知道最后的提案決定是什么，也许是通过，也许是驳回，不管大家选择哪一种決定，都有可能与第一位组员已执行过的真是決定不一致，老板就会不开心认为決策小組沟通有问題而解雇。

三阶段提交即是引入了另一個步骤，主持人打电话跟组员通知请准备通过提案，以避免沒人知道真实決定而造成決定不一致的失业危机。为什么能够解決二阶段提交的问题呢？回到刚刚提到的狀況，在主持人通知完第一位组员请准备通过过俩人意外失忆，即使沒人知道全体在第一阶段的決定为何，全体決策组员仍可以重新协调过程或直接否決，不會有不一致決定而失业。那么当主持人通知全部組員请准备通过并得到大家的再次確定后进入第三阶段，当主持人通知第一位组员请通过提案后俩人意外失忆，这时候其他組員再重新选出主持人后，仍可以知道目前至少是处于准备通过提案阶段，表示第一阶段大家都已经決定要通过了，此时便可以直接通过。

***

In computer networking and databases, the **three-phase commit** protocol (3PC) is a distributed algorithm which lets all nodes in a distributed system agree to commit a transaction. Unlike the two-phase commit protocol (2PC) however, 3PC is **non-blocking**. Specifically, 3PC places an **upper bound** on the amount of time required before a transaction either commits or aborts. This property ensures that if a given transaction is attempting to commit via 3PC and holds some resource locks, it will release the locks after the timeout.


# Coordinator

1. The coordinator receives a transaction request. If there is a failure at this point, the coordinator aborts the transaction (i.e. upon recovery, it will consider the transaction aborted). Otherwise, the coordinator sends a canCommit? message to the cohorts and moves to the waiting state.
2. If there is a failure, timeout, or if the coordinator receives a No message in the waiting state, the coordinator aborts the transaction and sends an abort message to all cohorts. Otherwise the coordinator will receive Yes messages from all cohorts within the time window, so it sends preCommit messages to all cohorts and moves to the prepared state.
3. If the coordinator succeeds in the prepared state, it will move to the commit state. However if the coordinator times out while waiting for an acknowledgement from a cohort, it will abort the transaction. In the case where all acknowledgements are received, the coordinator moves to the commit state as well.

# Cohort

1. The cohort receives a canCommit? message from the coordinator. If the cohort agrees it sends a Yes message to the coordinator and moves to the prepared state. Otherwise it sends a No message and aborts. If there is a failure, it moves to the abort state.
2. In the prepared state, if the cohort receives an abort message from the coordinator, fails, or times out waiting for a commit, it aborts. If the cohort receives a preCommit message, it sends an ACK message back and awaits a final commit or abort.
3. If, after a cohort member receives a preCommit message, the coordinator fails or times out, the cohort member goes forward with the commit.


# Disadvantage
The main disadvantage to this algorithm is that it cannot recover in the event the network is segmented in any manner. The original 3PC algorithm assumes a fail-stop model, where processes fail by crashing and crashes can be accurately detected, and does not work with network partitions or asynchronous communication.

Keidar and Dolev's **E3PC** algorithm eliminates this disadvantage.

The protocol requires at least 3 round trips to complete, needing a minimum of 3 round trip times (RTTs). This is potentially a long latency to complete each transaction.


***

了解了2PC和3PC之后，我们可以发现，无论是二阶段提交还是三阶段提交都无法彻底解决分布式的一致性问题。Google Chubby的作者Mike Burrows说过， there is only one consensus protocol, and that’s Paxos” – all other approaches are just broken versions of Paxos. 意即世上只有一种一致性算法，那就是**Paxos**，所有其他一致性算法都是Paxos算法的不完整版.
