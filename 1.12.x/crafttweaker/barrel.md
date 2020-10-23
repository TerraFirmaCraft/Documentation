# Barrel Recipes

Barrel recipe manager has three methods for manipulating recipes:

```java
// Import barrel methods into your script
import mods.terrafirmacraft.Barrel;
// Adds a recipe with the given parameters
Barrel.addRecipe(String registryName, @Optional IIngredient itemInput, ILiquidStack fluidInput, @Optional IItemStack itemOutput, @Optional ILiquidStack fluidOutput, int hours)
// Removes all recipes that have a given output
Barrel.removeRecipe(@Optional IItemStack outputItem, @Optional ILiquidStack outputLiquid)
// Removes a single recipe by registry name
Barrel.removeRecipe(String registryName)
```

At least one output(liquid or item) must be supplied, for both removing and adding recipes.
