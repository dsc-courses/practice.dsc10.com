In the video game *Minecraft*, players mine raw materials, craft various tools, and build structures such as houses.  
A player named Steve has several storage chests in which he keeps items he owns. Each chest has a **different** descriptive name and contains items of various types. For example, one of Steve’s chests is called `"Food"` and it contains 12 `"Golden Carrot"` and 8 `"Rabbit Stew"` items.

The `items` DataFrame contains all the items Steve has in his chests. It is indexed by `"Item"` (name of the item). The columns are `"Quantity"` (number of such items) and `"Chest"` (name of the chest where **all** such items are stored). The first few rows are shown below, though `items` has more rows than pictured.

| Item          | Quantity | Chest     |
|---------------|----------|-----------|
| Golden Carrot | 12       | Food      |
| Cobblestone   | 429      | Materials |
| Rabbit Stew   | 8        | Food      |
| Wood          | 38       | Materials |
| Emerald       | 2        | Gems      |
