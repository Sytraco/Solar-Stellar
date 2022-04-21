# Stellar modelisation

In the context of the final project of our Master's degree in Marine Physics, we are expected to produce an experimental research applied on Fluid Mechanics, using our acquired knowlegde until now. For this reason, the chosen subject is centered around numerical modelisation and fluid variations of the solar magma. The aim of this study is to reach an efficient model of our Sun by simulation and comparison using astronomical knowledge in addition.

---

## Connaissances

L'accélération gravitationnelle (pesanteur) déduite du potentiel gravitationnel $\phi$ s'écrit :
$$\vec{g} = -\overrightarrow{\nabla}\phi.$$

Où l'équation de Poisson affirme que :
$$\Delta \phi = -4\pi\rho G,$$

et donc 
$$\text{div}(\vec{g}) = \Delta \phi.$$


## Équation de Lane-Emden

L'équation de l'équilibre hydrostatique est donnée par :
$$\overrightarrow{\nabla}P = \rho \vec{g}.$$

La pression étant une fonction de la masse volumique, le gradient de pression peut s'écrire :
$$\overrightarrow{\nabla}P = \frac{dP}{d\rho} \overrightarrow{\nabla} \rho.$$

À l'aide de l'équilibre hydrostatique il est ainsi possible d'exprimer la pesanteur en fonction de la densité :
$$\vec{g} = \frac{1}{\rho}\frac{dP}{d\rho} \overrightarrow{\nabla} \rho.$$

L'objectif de cette démarche est de conduire à une équation permettant d'exprimer la densité de la sphère autogravitante. D'après l'équation de Poisson définie précédemment, cela donne:
$$\text{div}(\vec{g}) = \overrightarrow{\nabla}\cdot\left(\frac{1}{\rho}\frac{dP}{d\rho} \overrightarrow{\nabla} \rho\right) = \frac{1}{\rho}\frac{dP}{d\rho}\Delta\rho + \overrightarrow{\nabla}\rho\cdot\overrightarrow{\nabla}\left(\frac{1}{\rho}\frac{dP}{d\rho}\right) = -4\pi\rho G$$

Conduisant alors à
$$\Delta\rho + \overrightarrow{\nabla}\rho\cdot\overrightarrow{\nabla}\left(\frac{1}{\rho}\frac{dP}{d\rho}\right)\frac{1}{\frac{1}{\rho}\frac{dP}{d\rho}} = \frac{-4\pi G\rho}{\frac{1}{\rho}\frac{dP}{d\rho}}.$$

Or d'après l'équation d'état polytropique :
$$\frac{1}{\rho}\frac{dP}{d\rho} \propto \rho^{\gamma - 2}.$$

Cela conduit alors à l'équation de Lane-Emden généralisée :
$$\frac{\Delta\rho}{\rho} + (\gamma -2)\left(\frac{\overrightarrow{\nabla}\rho}{\rho}\right)^2 + \frac{4\pi G\rho}{\frac{1}{\rho}\frac{dP}{d\rho}} = 0.$$

En admettant que la masse volumique peut s'écrire en fonction du rayon : $\rho(r)$
$$\rho = \rho_c\theta^n \qquad \Longrightarrow \qquad \theta^n = \frac{\rho}{\rho_c},$$

un changement de variable pour obtenir la longueur d'échelle est obtenu par :
$$\xi = r\sqrt{\frac{4\pi G {\rho_c}^2}{(n+1)P_c}}.$$

Permettant de transformer l'équation différentielle en une forme plus élégante :
$$\frac{1}{\xi^2}\frac{d}{d\xi}\left(\xi^2\frac{d\theta}{d\xi}\right) + \theta^n = \frac{d^2\theta}{d\xi^2} + \frac{2}{\xi}\frac{d\theta}{d\xi} + \theta^n = 0$$