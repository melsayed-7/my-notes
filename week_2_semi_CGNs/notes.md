## Those are my notes around semi-supervised classification using GCNs.

### some termonolgy

- localized first-order approximation
- delta = D - A denotes the unnormalized graph laplacian of an undirceted graph. check [this](https://en.wikipedia.org/wiki/Laplacian_matrix)
- This

## Graph convolutional networks in general.

- inputs: X (NxF (F is the number of features) ), A (Adjacency matrix)
- A hidden layer takes H_i-1 and A gives back H_i (H is the representation like in RNNs)
- The weight matrix of the current layer is $F_prime x F$
- Graph networks aggregate featrues to the neighbouring nodes
- to make sure we aggregate our current node we add a self-loop (dummy one)
- a problem that is worth solving is that nodes with high degrees can lead to exploding gradients. This can be solved using **normalization**
- **normalization** can be done using the inverse of the degree matrix.
- The new normalization technique unlike A/D it uses D_ii x A x D_jj so it also takes into account the node i am propagating it to.
