# Knapping
Clay, Fire Clay and Leather Knapping recipe managers all works the same. Each one has three methods for manipulating recipes:
```zenscript
// Import the [Knapping] methods into your script
import mods.terrafirmacraft.[Knapping];
// Adds a recipe with the given parameters
[Knapping].addRecipe(String registryName, IItemStack output, String... pattern)
// Removes all recipes that have a given output
[Knapping].removeRecipe(IItemStack output)
// Removes a single recipe by registry name
[Knapping].removeRecipe(String registryName)

Where [Knapping] = ClayKnapping, FireClayKnapping or LeatherKnapping
```

Pattern must be a closed interval [1, 5]. Each input string is a line of the matrix. Empty spaces indicates where user must click, examples:
```
Small Ceramic Vessel:
" XXX ",
"XXXXX",
"XXXXX",
"XXXXX",
" XXX "
```
```
Ingot mold:
"XXXX",
"X  X",
"X  X",
"XXXX"
```

```zenscript
ClayKnapping.addRecipe("small_ceramic_vessel", <tfc:ceramics/unfired/vessel>, " XXX ", 
                                                                              "XXXXX", 
                                                                              "XXXXX", 
                                                                              "XXXXX", 
                                                                              " XXX ");
```