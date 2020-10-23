# Heating Recipes

This is the central place to add any heat transformation recipes. This includes

- food turning into cooked variants at some temperature
- food "burning" and disappearing when heated to high
- firing pottery in a pit kiln
- any other heat related transformation. It will be applied by any device that supports it.

```zenscript
// Imports Heating methods into your script
import mods.terrafirmacraft.Heating;
// Adds a recipe with the given parameters
Heating.addRecipe(String registryName, IItemStack input, IItemStack output, float transformTemp, float maxTemp)
// Removes all recipes that have a given output
Heating.removeRecipe(IItemStack output)
// Removes a single recipe by registry name
Heating.removeRecipe(String registryName)
```

Important things to note:

- `transformTemp` is at which temperature the recipe completely transform the input into the output stack.
- `maxTemp` is at which temperature the input is destroyed.

For temperature specifics, check the appropriate [reference](../temperatures/).
