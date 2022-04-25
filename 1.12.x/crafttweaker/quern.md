---
layout: page
title: "Quern Recipes"
permalink: /1.12.x/crafttweaker/quern/
---

# Quern Recipes

```zenscript
// Imports Quern methods into your script
import mods.terrafirmacraft.Quern;
// Adds a recipe with the given parameters
Quern.addRecipe(String registryName, IIngredient input, IItemStack output)
// Removes all recipes that have a given output
Quern.removeRecipe(IItemStack output)
// Removes a single recipe by registry name
Quern.removeRecipe(String registryName)
```

This is a basic input -> output recipe, so, it works like adding a furnace recipe, but without ticks.
