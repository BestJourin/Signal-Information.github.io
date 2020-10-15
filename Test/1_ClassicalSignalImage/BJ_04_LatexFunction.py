
import matplotlib.pyplot as plt

ax=plt.subplot(111)

ax.text(0.1,0.8,r"$\int_a^b f(x)\mathrm{d}x$",fontsize=30,color="red")

ax.text(0.1,0.3,r"$\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}!$",fontsize=30)

# ax.text(0.1,0.3,r"$\begin{cases}{4 (t>{2})}\\{t+2(-2\leq t\leq2)}\\{0 (t<-2)}\end{cases}$")

plt.show()