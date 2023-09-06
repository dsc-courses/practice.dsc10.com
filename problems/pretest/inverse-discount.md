# BEGIN PROB

At a furniture store, suppose every item has a "true value" that represents its worth. Every item in the store is marked up by 25%, so it's sold at a price higher than its true value for the store to make a profit. But the store wants its employees to be able to buy items at their true value. What percent discount does it need to give its employees off the sale price to accomplish this?

In general, if a store marks up prices by $p$%, what percent discount does it need to give to employees so that they can buy things at the true value?

# BEGIN SOLUTION

**Answer**: 20%, or more generally, $\frac{p}{100+p} \cdot 100\%$

Let $t$ represent the true value of an item in the furniture store. The store sells the item for $t$ + 25% of $t$, which can be expressed as $1.25t$. 

Now, just to demonstrate the kind of calculation involved, let's say the store provides employees with a 25% discount. This would mean that employees pay $100\% - 25\% = 75\%$ of the sale price, which is $0.75 \cdot 1.25t$. This simplifies to $0.9375t$, which is less than $t$, which means that 25% is too much of a discount! Since the sale price is 25% more than the true value, 25% of the sale price is more than 25% of the true value; since the employee discount is taken off of the sale price, it needs to be less than 25%.

The question, then, is what percentage discount should the store provide employees with so that the post-discount sale price is equal to $t$? Suppose they provide employees with a discount of $e$, where $e$ is a decimal between 0 and 1 (in the previous example, for instance, it would have been 0.25, which corresponds to 25%). Then, employees pay $(1 - e) \cdot 1.25t$. Now, we need to pick the value of $e$ that makes $(1 - e) \cdot 1.25t$ equal to $t$. This is equivalent to picking the value of $e$ that makes $(1 - e) \cdot 1.25$ equal to 1. Let's solve:

$$\begin{align*}(1 - e) \cdot 1.25 &= 1 \\ 1 - e &= \frac{1}{1.25} \\ e &= 1 - \frac{1}{1.25} \end{align*}$$

Since $1.25 = \frac{5}{4}$, we have:

$$e = 1 - \frac{1}{1.25} = 1 - \frac{1}{\frac{5}{4}} = 1 - \frac{4}{5} = \frac{1}{5}$$

This means that the store needs to give employees a discount of $\frac{1}{5} = 0.2$, or 20%, in order for their post-discount price to be equal to the true value of the item they're buying.

More generally, if a store sells an item for $p$% more than its true value, $t$, then its sale price is $\left(1 + \frac{p}{100} \right)t$, or $\frac{100 + p}{100}t$ (for instance, if $p = 25$, then the sale price is $\frac{100 + 25}{100}t = 1.25t$, which we saw before). Then, the store would need to offer employees a discount of $e$ (where $e$ is a decimal between 0 and 1) such that $(1 - e) \cdot \frac{100 + p}{100} = 1$. Solving for $e$ gives:

$$\begin{align*} (1 - e) \cdot \frac{100 + p}{100} &= 1 \\ 1 - e &= \frac{100}{100 + p} \\ e &= 1 - \frac{100}{100 + p} \\ e &= \frac{100 + p}{100 + p} - \frac{100}{100 + p} \\ e &= \frac{p}{100 + p} \end{align*}$$

$\frac{p}{100 + p}$ is a decimal between 0 and 1, so to convert it to a percentage we can multiply it by $100\%$. To conclude, if a store sells an item for $p$% more than its true value, $t$, then they must offer employees a discount of $\frac{p}{100 + p} \cdot 100\%$ in order for their post-discount price to be equal to $t$.

This is a scary looking formula, but let's try it in action: if we let $p$ be 25, as it was in the first part of this question, we then have a discount of $\frac{25}{100 + 25} \cdot 100\%$, or $0.2 \cdot 100\%$, or $20\%$.

# END SOLUTION

# END PROB
