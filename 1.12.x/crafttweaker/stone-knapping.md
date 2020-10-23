---
layout: page
title: "Stone Knapping Recipes"
permalink: /1.12.x/crafttweaker/stone-knapping/
---

# Stone Knapping Recipes

The stone knapping recipe manager works a bit different than the other knapping recipes. It has three methods for recipe manipulation:

```zenscript
// Import the StoneKnapping methods into your script
import mods.terrafirmacraft.StoneKnapping;
// Methods
StoneKnapping.addRecipe(String registryName, IItemStack[] output, String[] rocks, String... pattern)
StoneKnapping.removeRecipe(IItemStack output)
StoneKnapping.removeRecipe(String registryName)
```

Each rock gives different output items depending on which rock you are knapping. By default, this only applied to which rock tool category you get, which translates to how durable the rock tool is. Using this manager, you can add your own output depending on which rock(s) the user knaps.

Rocks in TFC by default are:

* `chalk`
* `granite`
* `diorite`
* `gabbro`
* `shale`
* `claystone`
* `rocksalt`
* `limestone`
* `conglomerate`
* `dolomite`
* `chert`
* `rhyolite`
* `basalt`
* `andesite`
* `dacite`
* `quartzite`
* `slate`
* `phyllite`
* `schist`
* `gneise`
* `marble`

**Examples:**

```zenscript
// Gives a stone hoe in all rocks.
StoneKnapping.addRecipe("testrecipe", [<minecraft:stone_hoe>], ["all"], "     ", "XXXX ");
// Gives a stone hoe only in shale, claystone, rocksalt, limestone.
StoneKnapping.addRecipe("testrecipe2", [<minecraft:stone_hoe>], ["shale", "claystone", "rocksalt", "limestone"], "     ", "XXXX ");
// Gives a stone hoe in claystone, and a pickaxe in limestone.
StoneKnapping.addRecipe("testrecipe3", [<minecraft:stone_hoe>, <minecraft:stone_pickaxe>], ["claystone", "limestone"], "     ", "XXXX ");
// Gives a stone hoe only in basalt and chert.
StoneKnapping.addRecipe("testrecipe4", [<minecraft:stone_hoe>, <minecraft:stone_hoe>], ["basalt", "chert"], "     ", "XXXX ");
```
