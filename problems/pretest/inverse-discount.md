# BEGIN PROB

At a furniture store, suppose every item has a "true value" that represents its worth. Every item in the store has a ticketed price, which is the amount that is printed on the item's price tag that customers will pay, that is 25% higher its true value. The store wants its employees to be able to buy items at their true value. What percent discount does it need to give its employees off the ticketed price to accomplish this?

In general, if a store marks up prices by $p$%, what percent discount does it need to give to employees off the ticketed price so that they can buy things at the true value?

Solve this problem without a calculator.

# BEGIN SOLUTION

**Answer**: 20%, or more generally, $\frac{100p}{100+p}\%$

Let $v$ represent the true value of an item in the furniture store. The store sells the item for $v$ + 25% of $v$, which can be expressed as $1.25v$. We'll call this the ticketed price, which is the amount that would be printed on the item's price tag.

Now, just to demonstrate the kind of calculation involved, let's say the store provides employees with a 25% discount. This would mean that employees pay $100\% - 25\% = 75\%$ of the ticketed price, which is $0.75 \cdot 1.25v$. This simplifies to $0.9375v$, which is less than the true value $v$. This means a 25% employee discount is too much of a discount, since it allows employees to buy items at less than the true value. Since the ticketed price is 25% more than the true value, 25% of the ticketed price is larger than 25% of the true value; since the employee discount is taken off of the ticketed price, it needs to be less than 25%.

The question, then, is what percentage discount should the store provide to employees so that the post-discount price is equal to $v$? Suppose they provide employees with a discount of $d$, where $d$ is a decimal between 0 and 1 (in the previous example, for instance, it would have been 0.25, which corresponds to 25%). Then, employees pay $(1 - d) \cdot 1.25v$. Now, we need to pick the value of $d$ that makes $(1 - d) \cdot 1.25v$ equal to $v$. Let's set up an equation:

$$(1 - d) \cdot 1.25v = v$$

We need to solve this for $d$, and fortunately, if we divide both sides by $v$, this becomes an equation with just one variable, which we can solve with algebra:

$$\begin{align*}(1 - d) \cdot 1.25 &= 1 \\ 1 - d &= \frac{1}{1.25} \\ d &= 1 - \frac{1}{1.25} \end{align*}$$

Since $1.25 = \frac{5}{4}$, we have:

$$d = 1 - \frac{1}{1.25} = 1 - \frac{1}{\frac{5}{4}} = 1 - \frac{4}{5} = \frac{1}{5}$$

This means that the store needs to give employees a discount of $d = \frac{1}{5} = 0.2$, or 20%, in order for their post-discount price to be equal to the true value of the item they're buying.

More generally, if a store sells an item for $p$% more than its true value, $v$, then the ticketed price is $\left(1 + \frac{p}{100} \right)v$, or $\left(\frac{100 + p}{100}\right)v$. For instance, if $p = 25$, then the ticketed price is $\frac{100 + 25}{100}v = 1.25v$, which we saw before. Then, the store would need to offer employees a discount of $d$ (where $d$ is a decimal between 0 and 1) such that $(1 - d) \cdot \frac{100 + p}{100} = 1$. Solving for $d$ gives:

$$\begin{align*} (1 - d) \cdot \frac{100 + p}{100} &= 1 \\ 1 - d &= \frac{100}{100 + p} \\ d &= 1 - \frac{100}{100 + p} \\ d &= \frac{100 + p}{100 + p} - \frac{100}{100 + p} \\ d &= \frac{p}{100 + p} \end{align*}$$

$\frac{p}{100 + p}$ is a decimal between 0 and 1, so to convert it to a percentage we can multiply it by $100\%$. To conclude, if a store sells an item for $p$% more than its true value, $v$, then they must offer employees a discount of $\frac{p}{100 + p} \cdot 100\%$ in order for their post-discount price to be equal to $v$.

This is a scary-looking formula, but let's try it in action: if we let $p$ be 25, as it was in the first part of this question, we then have a discount of $\frac{25}{100 + 25} \cdot 100\%$, or $0.2 \cdot 100\%$, or $20\%$.

# END SOLUTION

# END PROB
