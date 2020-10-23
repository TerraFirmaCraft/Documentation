---
layout: page
title: "Chisel Recipes"
permalink: /1.12.x/crafttweaker/chisel/
---

# Chisel Recipes

```zenscript
// Import the chisel methods into your script
import mods.terrafirmacraft.Chisel;
// Adds a recipe with the given parameters
Chisel.addRecipe(String registryName, IItemStack input, IItemStack output);
// Removes all recipes that have a given output
Chisel.removeRecipe(IItemStack output);
// Removes a single recipe by registry name
Chisel.removeRecipe(String registryName);
```

Note: input and output must be blocks.
