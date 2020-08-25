## [Semi-Supervised Classification With Graph convolutional network](https://arxiv.org/pdf/1609.02907.pdf)

## Those are my notes around semi-supervised classification using GCNs.

- L_reg to me, it seems that encoding of neighbouring nodes should be too similar that the difference would be almost zero.
- A_hat = A + I, we are adding the identity because A does not have 1 in the current node position i,i and though it will not be able to propagate the current node featrues to the neighbouring ones, so by adding the identity matrix we allow it to do so.

## some termonolgy

- localized first-order approximation
- delta = D - A denotes the unnormalized graph laplacian of an undirceted graph. check [this](https://en.wikipedia.org/wiki/Laplacian_matrix)
- This
- sigmoid here is just a non-linearity function.

## Graph convolutional networks in general.

- inputs: X (NxF (F is the number of features) ), A (Adjacency matrix)
- A hidden layer takes H_i-1 and A gives back H_i (H is the representation like in RNNs)
- The weight matrix of the current layer is $ F_prime x F $
- Graph networks aggregate featrues to the neighbouring nodes
- to make sure we aggregate our current node we add a self-loop (dummy one)
- a problem that is worth solving is that nodes with high degrees can lead to exploding gradients. This can be solved using **normalization**
- **normalization** can be done using the inverse of the degree matrix.
- The new normalization technique unlike A/D it uses D_ii x A x D_jj so it also takes into account the node i am propagating it to.

## Spectral graph convolutions

- unlike spactial convolutions, which depend on the neighbouring nodes, this basically does decomposition to the graph so that we can understand the underlying structure.
- we will decompose the input to a more simple, independent (orthogonal) representations.
- in GNNs, we imply eigen-decomposition of the graph laplacian.
- we can think of the graph Laplacian L as an adjacency matrix A normalized in a special way, whereas eigen-decomposition is a way to find those elementary orthogonal components that make up our graph.
- In a more intuitive way: the laplacian shows the directions and how smoothly the "energy" will propagate from a node (with a higher potential) to the rest of the nodes.

## Cool references

- https://en.wikipedia.org/wiki/Laplacian_matrix
- https://en.wikipedia.org/wiki/Spectral_graph_theory
- http://outobox.cs.umn.edu/PCA_on_a_Graph.pdf (**to be read**)
- http://blog.shriphani.com/2015/04/06/the-smallest-eigenvalues-of-a-graph-laplacian/ (really good blog showing the importance of Eigen decomposition)
- https://ai.stackexchange.com/questions/14003/what-is-the-difference-between-graph-convolution-in-the-spatial-vs-spectral-doma
- https://towardsdatascience.com/how-to-do-deep-learning-on-graphs-with-graph-convolutional-networks-7d2250723780
- https://towardsdatascience.com/how-to-do-deep-learning-on-graphs-with-graph-convolutional-networks-62acf5b143d0
- https://towardsdatascience.com/spectral-graph-convolution-explained-and-implemented-step-by-step-2e495b57f801
