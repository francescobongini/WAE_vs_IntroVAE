# WAE vs IntroVAE
![Latent manifold](latent_manifold.gif)

WAE (Wasserstein Auto-Encoder) and IntroVAE (Information-theoretic Variational Autoencoder) are both generative models that use Variational Autoencoders (VAEs) as their foundation. The main difference lies in the objective function they use to optimize the learning process.

WAE (Wasserstein Auto-Encoder)

WAE was introduced in a paper by Tolstikhin et al. in 2017. The main idea is to use the Wasserstein distance, a measure of the distance between two probability distributions, to optimize the VAE's parameters. Specifically, WAE aims to minimize the Earth Mover's distance (also known as the Wasserstein distance) between the learned latent space and a target distribution.

The WAE objective function is:

E[KL(q(z|x) || p(z))] + λ * E[D(P_g(z), P_r(z))

where:

q(z|x) is the encoder's output distribution
p(z) is a fixed target distribution
P_g(z) is the learned distribution in the latent space
P_r(z) is a reference distribution (e.g., a standard normal distribution)
λ is a hyperparameter controlling the importance of the regularization term
By minimizing this objective function, WAE aims to learn a more disentangled and interpretable representation of the data.

IntroVAE

IntroVAE was introduced in a paper by Chen et al. in 2016. The main idea is to use information-theoretic quantities, such as mutual information and Kullback-Leibler divergence, to optimize the VAE's parameters. IntroVAE aims to maximize the mutual information between the input data and the learned latent representation.

The IntroVAE objective function is:

E[KL(q(z|x) || p(z))] - β * I(x; z)

where:

I(x; z) is the mutual information between x and z
β is a hyperparameter controlling the importance of the mutual information term
By maximizing this objective function, IntroVAE aims to learn a more informative and interpretable representation of the data.
