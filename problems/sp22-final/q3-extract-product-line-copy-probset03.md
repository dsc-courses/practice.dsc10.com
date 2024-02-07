# BEGIN PROB

In the `ikea` DataFrame, the first word of each string in the `'product'` column represents the product line. For example the HEMNES line of products includes several different products, such as beds, dressers, and bedside tables.

The code below assigns a new column to the `ikea` DataFrame containing the product line associated with each product. 

```py
(ikea.assign(product_line = ikea.get('product')
                                .apply(extract_product_line)))
```

# BEGIN SUBPROB

What are the input and output types of the `extract_product_line` function?

( ) takes a string as input, returns a string
( ) takes a string as input, returns a Series
( ) takes a Series as input, returns a string
( ) takes a Series as input, returns a Series

# BEGIN SOLUTION

**Answer: ** takes a string as input, returns a string

To use the Series method `.apply`, we first need a Series, containing values of any type. We pass in the name of a function to `.apply` and essentially, `.apply` calls the given function on each value of the Series, producing a Series with the resulting outputs of those function calls. In this case, `.apply(extract_product_line)` is called on the Series `ikea.get('product')`, which contains string values. This means the function `extract_product_line` must take strings as inputs. We're told that the code assigns a new column to the `ikea` DataFrame containing the product line associated with each product, and we know that the product line is a string, as it's the first word of the product name. This means the function `extract_product_line` must output a string. 

<average>72</average>
# END SOLUTION

# END SUBPROB

# BEGIN SUBPROB

Complete the return statement in the `extract_product_line` function below.

For example, `extract_product_line('HEMNES Daybed frame with 3 drawers, white, Twin')` should return `'HEMNES'`.

```py
def extract_product_line(x):
    return _________
```

What goes in the blank?

# BEGIN SOLUTION

**Answer: ** `x.split(' ')[0]`

This function should take as input a string `x`, representing a product name, and return the first word of that string, representing the product line. Since words are separated by spaces, we want to split the string on the space character `' '`. 

It's also correct to answer `x.split()[0]` without specifying to split on spaces, because the default behavior of the string `.split` method is to split on any whitespace, which includes any number of spaces, tabs, newlines, etc. Since we're only extracting the first word, which will be separated from the rest of the product name by a single space, it's equivalent to split using single spaces and using the default of any whitespace.
<average>84</average>
# END SOLUTION

# END SUBPROB

# END PROB

