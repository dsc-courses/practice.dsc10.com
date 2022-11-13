# BEGIN PROB
Suppose that when someone downloads the app, the app requires them to choose a username, which must be different from all other registered usernames. 

**True or False**: If `app_data` had included a column with the username of the person who reported each product build, it would make sense to index `app_data` by username.

( ) True
( ) False

# BEGIN SOLUTION

**Answer: ** False

Even though people must have distinct usernames, one person can build multiple different IKEA products and log their time for each build. So we don't expect every row of `app_data` to have a distinct username associated with it, and therefore username would not be suitable as an index, since the index should have distinct values.

<average>52</average>
# END SOLUTION



# END PROB
