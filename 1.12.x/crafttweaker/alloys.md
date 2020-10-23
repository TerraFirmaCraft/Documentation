---
layout: page
title: "Alloys"
permalink: /1.12.x/crafttweaker/alloys/
---

# Alloy Recipes

For manipulating Alloy recipes a recipe builder is provided:

```zenscript
// Import Alloy methods into your script
import mods.terrafirmacraft.Alloy;
import mods.terrafirmacraft.AlloyRecipeBuilder;

// Gets the recipe builder for the specified metal
AlloyRecipeBuilder builder = Alloy.addAlloy(String metal);
// Removes the alloy recipe from registry
Alloy.removeAlloy(String metal);

// Adds metal content to this alloying recipe
builder.addMetal(String input, double min, double max);
// Finish the recipe, build and register it.
builder.build();
```

Please refer to [Metals](../../metals) for a complete reference on TFC Metals.

Example script:

```zenscript
Alloy.addAlloy("BRONZE").addMetal("COPPER", 0.88, 0.92).addMetal("TIN", 0.08, 0.12).build();
Alloy.addAlloy("BISMUTH_BRONZE").addMetal("COPPER", 0.5, 0.65).addMetal("BISMUTH", 0.1, 0.2).addMetal("zinc", 0.2, 0.3).build();
```
