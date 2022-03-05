#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 2.7
# des fonction utiles
# Equipe ML (Aries & Benatchba), 2020
#
import numpy as np

def normaliser(X, mean=None, std=None): 
    if (mean is None) or (std is None): 
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
    X_norm = np.where(std==0, X, (X - mean)/std)
    return X_norm, mean, std

def preparer(X, norm=True, const=True, mean=None, std=None): 
    X_pre = X.copy()
    if norm: 
        X_pre, mean, std = normaliser(X_pre,mean=mean, std=std)
    if const:
        X_pre = np.append(np.ones((X_pre.shape[0],1)), X_pre ,axis=1)
    return X_pre, mean, std

def generer_zeros_1(nbr):
    return np.zeros(nbr)

def generer_uns_1(nbr):
    return np.ones(nbr)

def generer_aleatoire_1(nbr):
    return np.random.rand(nbr)

def ligne_decision(X, Theta, mean=[0, 0], std=[1, 1]):
    X1 = [np.min(X[:,0]), np.max(X[:,0])]
    X2_min = mean[1] - std[1] * (Theta[0] + Theta[1] * (X1[0] - mean[0])/std[0]) / Theta[2]
    X2_max = mean[1] - std[1] * (Theta[0] + Theta[1] * (X1[1] - mean[0])/std[0]) / Theta[2]
    return X1, [X2_min, X2_max]

def courbe_decision(X1_min, X1_max, pas, Theta, mean=[0, 0], std=[1, 1]):
    X1 = np.arange(X1_min, X1_max, pas)
    X2 = mean[1] - std[1] * (Theta[0] + Theta[1] * (X1 - mean[0])/std[0]) / Theta[2]
    return X1, X2

def afficher_droite(X, Y, theta, mean=[0, 0], std=[1, 1]):
    plt.scatter(X[:,1], Y, color="blue")
    Xg, Yg = ligne_decision(X, Theta, mean=mean, std=std)
    plt.plot(Xg, Yg, color="red")
    plt.show()
