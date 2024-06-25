# WAE vs IntroVAE

In this repository I compare WAE (Wasserstein Auto-Encoder) and IntroVAE (Information-theoretic Variational Autoencoder), both generative models that use Variational Autoencoders (VAEs) as their foundation. The main difference lies in the objective function they use to optimize the learning process.

![Latent manifold](latent_manifold.gif)

In my experiment I train WAE and IntroVAE models on CelebA dataset, which cointains 202599 pictures of celebrities.

We conclude that WAE-MMD leads to a better train and test sets recostruction and an improvement on the latent manifold.
