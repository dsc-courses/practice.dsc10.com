# BEGIN PROB

Assume you have a DataFrame named `ikea` that contains information about IKEA products, including columns called `'product'`(`str`): the name of the product, `'assembly_cost'`(`int`): the assembly cost of each product, and `'packages'`(`int`): the number of packages each product comes in. Complete the expression below so that it evaluates to the name of the product for which the average assembly cost per package is lowest.

```py
(ikea.assign(assembly_per_package = ___(a)___)
     .sort_values(by='assembly_per_package').___(b)___)
```

# BEGIN SUBPROB

What goes in blank (a)?

# BEGIN SOLUTION

**Answer: ** `ikea.get('assembly_cost')/ikea.get('packages')`

This column, as its name suggests, contains the average assembly cost per package, obtained by dividing the total cost of each product by the number of packages that product comes in. This code uses the fact that arithmetic operations between two Series happens element-wise.

<average>91</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

What goes in blank (b)?

# BEGIN SOLUTION

**Answer: ** `get('product').iloc[0]`

After adding the `'assembly_per_package'` column and sorting by that column in the default ascending order, the product with the lowest `'assembly_per_package'` will be in the very first row. To access the name of that product, we need to `get` the column containing product names and use `iloc` to access an element of that Series by integer position.

<average>66</average>
# END SOLUTION

# END SUBPROB

# END PROB