---
layout: page
title: "Craft Tweaker Integration"
permalink: /1.12.x/crafttweaker/
---

# Craft Tweaker Integration

For changing recipes, item size/heat/forging capabilities, TerraFirmaCraft adds hooks for CraftTweaker scripts. To do that, you first need to import a recipe manager using `mods.terrafirmacraft.[RecipeType]`. The list of recipe managers currently in TFC is:

* `Alloy` - For adding and removing alloy recipes.
* `Anvil` - For adding anvil working recipes, requiring working temperature and rules.
* `Welding` - For adding recipes to weld two items into one
* `Barrel` - For adding many types of transformations, both fluid and items to barrels.
* `Chisel` - For adding chisel smoothing transformations from block -> block.
* `Loom` - For adding recipes to the loom. Slightly more involved as it requires additional textures or assets for the rendering.
* `Heating` - Anything that can transform at a given heat. Includes pit kiln, forge, fire pit, grill, etc.
* `Quern` - Adds grinding recipes to the quern
* `ClayKnapping` - Adds knapping recipes using clay
* `FireClayKnapping` - Adds knapping recipes using fire clay
* `LeatherKnapping` - Adds knapping recipes using leather
* `StoneKnapping` - Adds knapping recipes using stones. Can respect the rock category (igneous, metamorphic, etc.)

Along with the item registry for Heating, Forging and Size capabilities: 

* `ItemRegistry`
