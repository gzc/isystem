# Four ways building a VMM

1. Emulation(BOCHS)
2. Trap and Emulate
3. Binary Translation(QEMU)
4. Paravirtualization(XEN)

## Emulation

![](./imgs/emulation.png)

Do whatever CPU does but ourselves, in software
* Fetch the next instruction
* Decode (is it an ADD, a XOR, a MOV?)
* Execute (using the SW emulated registers and memory)

For example:

    addl %ebx, %eax /* eax += ebx */

Is emulated as:

    enum {EAX=0, EBX=1, ECX=2, EDX=3, ...};
    unsigned long regs[8];
    regs[EAX] += regs[EBX];

Pro: Simple!

Con: Sloooooow...

Example: **BOCHS**

## Trap and Emulate
Actually, most VM code can execute directly on CPU just fine
* E.g., addl %ebx, %eax

So instead of emulating this code
* Let it run directly on the CPU

But some operations are sensitive and require the hypervisor to lie, e.g.,
* **int $0x80** (generates system call interrupt; hypervisor knows that from now on the guest thinks it’s in privileged mode; guest can’t really run in privileged mode, of course, because otherwise it’d be able to mess stuff up for the host / other guests)
* **movel <something>**, %cr3 (switch virtual memory address spaces; once again, hypervisor can’t allow the guest to actually manipulate address spaces on its own, but it can do it for the guest)
* **I/O ops** (I/O channels are multiplexed by the host so as to allow all the guests to use them, which once again means the hypervisor can’t allow direct access; also, I/O devices handling will not be able to tolerate multiple OSes performing uncoordinated ops)

#### Idea
* Trap-and-emulate all these **“sensitive”** instructions
* E.g., if guest runs INT $0x80, trap it and execute guest’s handler of interrupt 0x80
* We are leveraging the fact that many sensitive operations trigger an interrupt when performed by unprivileged user-mode SW

#### Problem
* Not all sensitive ops trigger a trap when executed in user-mode
* Example for x86/32bit
 * 1POPF, which may be used to set/clear interrupt flag (IF)
 * Will silently fail!
 * Namely, it will (1) not trap, and it will (2) not change the IF value

#### Solution #1
* HW support for virtualization (modern chips rectify the problem)
* Hypervisors can, e.g., configure which ops would generate traps
* Intel calls such support “VMX” AMD calls such support “SVM”

#### Example hypervisor
* As opposed to some other, earlier hypervisors, KVM was originally
implemented by making use of HW support for virtualization

#### Problem: hypervisors that predated HW support
* Had to solve the problem in some other way... (see next slides)

## Dynamic Binary Translation

#### Solution #2: binary translation – idea
* Block of (VM) ops encountered for 1st time?
* Translate it, on-the-fly, to “safe” code
 * Similarly to JIT-ing
 * Put it in the “code cache” (indexed by address)
* From now on
 * Safe code would be executed directly on CPU

#### Translation rules
* Most code translates identically
 * E.g., movl %eax, %ebx

* Sensitive ops are translated into “hypercalls”
 * Calls into hypervisor
   * (to ask for service)
 * Implemented as trapping ops
   * (unlike, e.g., POPF)
 * Similar to syscall
   * (call into hypervisor to request service)

Example hypervisors
* **Vmware (x86 32bit)**, **QEMU**

## Paravirtualization

* So far
 * Guest OS was unmodified


* Conversely, paravirtualization
 * Requires guest OS to “know” it is being virtualized
 * And to explicitly use hypervisor services through a hypercall
 * E.g., instead of doing “cli” to turn off interrupts,
   * guest OS should do: hypercall( DISABLE_INTERRUPTS )

#### Pros
 1. No hardware support required
 2. Performance can approach that of native HW support

#### Cons
1. Requires specifically modified guest
2. Same guest cannot run in the VM and on bare-metal

Example hypervisor

* ** Xen **
