## Scott Schumacher
Due: Oct 18th by classtime.

For up to 15 points to be added to your exam, complete the following.

### Multi\*
Define the following and give examples of each.

1. Multi-tasking- 		Our text (p. 57) actually equates multiprogramming and multitasking: "The approach is known as 
						multiprogramming or multitasking." However, we have defined multitasking as a single processer
						switching contexts so rapidly that it appears the processes were running concurrently. Really,
						it's extremely rapid serial execution of slices of each process.
					
2. Multi-programming-	As noted above; Multiprogrammed batch systems have the advantage of increased processor utilization
						compared to uniprogrammed systems. Since any given process spends much of its time waiting for I/O,
						the processor can switch between processes without any penalty in speed. Multiprogramming relies on
						hardware that supports interrupts and DMA (p. 58).
						
3. Multi-processing-	Multiprocessing requires multiple processors or multiple cores. This is actual concurrent processing;
						multiple processes can be running simultaneously, each on a separate processor / core. 

4. Multi-threaded-		"Multithreading is a technique in which a process, executing an application, is divided into threads 
						that can run concurrently..." where  a thread is "... a dispatchable unit of work. It includes a 
						processor context... and its own data area... A thread executes sequentially and is interruptible so 
						that the processor can turn to another thread." (p. 70-71). Does not require multiple processors/cores.

### Review Questions From Chapters 3
1. What is an instruction trace?	An instruction trace is a sequential listing of the instructions that execute in a process. (p.109)

2. What common events lead to the creation of a process?	A process may be created in one of four ways: as a new batch job;  in
															response to an interactive log-on; created by the OS to provide a service
															(such as to control printing); or may be spawned by an existing process. (p.113)
															
3. What does it mean to preempt a process?	Since the OS assigns varying priorities to different processes, the OS may interrupt
											a lower priority process if the event that a higher priority process has been waiting for
											occurs. (p.117)
											
4. What is swapping and what is its purpose?	Swapping is when the OS moves a process from main memory to virtual memory; it is done
												to allow more processes to run than would be possible without virtual memory. Without 
												virtual memory, any running process would have to be resident in main memory; main 
												memory is limited, therefore the number of possible processes is restricted. Swapping
												increases the number of processes that can run by allowing the OS to move a process out
												of main memory to virtual memory in order to move another process into main to run.(p.119)
												
5. Why does Figure 3.9b have two blocked states?	A process that's blocked while awaiting an event still takes up space in main memory;
													it makes sense to have an additional blocked/suspended state so that processes that
													are waiting can be moved to virtual memory. Then main memory is available to processes
													that are running or ready.
													
6. List four characteristics of a suspended process.	"1. The process is not immediately available for execution; 2. The process may or may
														not be awaiting an event. If it is, this blocked condition is independent of the suspend 
														condition,  and occurrence of the blocking event does not enable the process to be
														executed immediately; 3. The process was placed in a suspended state by and agent; either
														itself, or the OS, for the purpose of preventing its execution; 4. The process may not be
														removed from this state until the agen explicitly orders the removal." (p.123)
														
7. List three general categories of information in a process control block.	Process identification, Processor state information, and 
																			Process control information. (p. 128)
																			
8. Why are two modes (user and kernel) needed?	To establish distinct levels of access to memory; the OS, operating is kernel or system mode
												has a higher level of access than a user program. This is necessary to protect the OS and key
												operating system tables, such as process control blocks, from being modified by user programs. (p. 134)
												
1. What is the difference between an interrupt and a trap?	An interrupt is externally generated, while a trap interrupts the process because 
															of or in response to an internal event or condition. (p. 136)
															
1. Give three examples of an interrupt.	A clock interrupt- the process's time slice has expired; an I/O interrupt- if the process is preempted
										when a higher priority process gets an awaited I/O event; a memory fault- if a required part of process 
										is not in main memory, the process will be interrupted until the OS retrieves the required word from
										virtual memory. (p. 136)
										
1. What is the difference between a mode switch and a process switch?	A mode switch involves changing from user mode to kernel mode, while a 
																		process switch is changing only between processes without switching to 
																		kernel mode. In most OS, the occurrence of an interrupt doesn't 
																		necessarily mean a process switch; after the OS has accomplished its
																		work in kernel mode, it may resume the same process as befor the 
																		interrupt. (p. 138)

### What to turn in:
- A markdown file that contains your answers in a structured format.
- Name your file: `Test_One_Addon.md`
- Thorough well thought out answers to the questions.
- Mardown reference: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
- This is to add a letter grade and a half to your exam, so I will be extremely picky.
