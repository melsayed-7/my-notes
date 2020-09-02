# My notes for course 1 of the bioinformatics specialization.

- DnaA portein binds to part of the origion of replication called **DnaA box**
- a good problem is to find the most frequent k-mer
- Different Genomes have different DnaA boxes
- previously, we were give oriC (origion of replication) and had to find the hidden messages (find most frequent k-mers), but what if you are not give oriC
- A way to lacate a 500 long oriC is to go through all possible window and count number of the most frequent k-mer at each window and the window with the most count (or above a certain threshold is a window of interest)
- in a DnaA oriC you can find the most frequent k-mer and its complement
