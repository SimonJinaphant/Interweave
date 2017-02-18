# Difference between process and thread?

A process is a runnable program with 2 important fields
 * Address space
 * Threads

Threads share the same address space, thus they can access anything other threads declare on their heap
Processes do not share address space with other processes
