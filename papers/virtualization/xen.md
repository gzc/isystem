[ Xen and the Art of Virtualization](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwjl4dyQ5vPKAhWDKWMKHShaDJsQFggmMAE&url=http%3A%2F%2Flass.cs.umass.edu%2F~shenoy%2Fcourses%2Ffall07%2Fpapers%2Fxen.pdf&usg=AFQjCNFpaEETsZwSNjP507dnLw1UjkCAJg&sig2=HCV8m1LePZOCZNlUpbgQrg&bvm=bv.114195076,d.cGc)

## Requirement

* ISOLATION
* resource accounting
* APPs unmodified(OS)
* software heterogeneity
* perfomance/overhead
* scale

## 核心idea

paravirtualization : modify the OS

当时没有HW support, 也不想使用binary dynamic translation. 就修改OS, 改变跑特权指令的那部分.

## CPU scheduling

Borrowed Vir- tual Time (BVT) scheduling algorithm


## Virtual address translation


Xen need only be involved in page table updates, to prevent guest OSes from making unacceptable changes

the approach in Xen is to register guest OS page tables directly with the MMU, and restrict guest OSes to read-only access. Page table updates are passed to Xen via a hypercall; to ensure safety, requests are validated before being applied


## Deawback
不过Xen要使用Domain0的real driver和其他domain的虚拟driver通信，速度慢. Vmware ESX解决了这个问题.
