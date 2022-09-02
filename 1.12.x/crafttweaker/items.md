---
layout: page
title: "Item Capabilities"
permalink: /1.12.x/crafttweaker/items/
excluded_in_search: true
---

# Item Capabilities

This adds TFC capabilities to items outside TFC's realm.

```zenscript
// Imports ItemRegistry methods into your script
import mods.terrafirmacraft.ItemRegistry;

// Register item size and weight. This changes how much a stack can hold.
ItemRegistry.registerItemSize(IIngredient input, String size, String weight);

// Register item heat capability and if this item is forgeable (eg: can be used in anvil).
ItemRegistry.registerItemHeat(IIngredient input, float heatCapacity, float meltTemp, bool forgeable);

// Register item as a metal item. Note that this automatically adds heating and forging capability. 
// If canMelt is false this item won't bear the output directly (like iron ore needs bloomery/blast furnace)
ItemRegistry.registerItemMetal(IIngredient input, String metal, int units, bool canMelt);

// Register item food stats. This takes priority over existing values. Setting Decay to 0 stops decay from happening.
ItemRegistry.registerFood(IIngredient input, int hunger, float water, float saturation, float decay, float grain, float veg, float fruit, float meat, float dairy);

// Register armor stats
ItemRegistry.registerArmor(IIngredient input, float crushingModifier, float piercingModifier, float slashingModifier);

// Register item as a fuel for fire pit or forge
ItemRegistry.registerFuel(IItemStack itemStack, int burnTicks, float temperature, bool forgeFuel, bool bloomeryFuel)
```

Please refer to [Metals](../../metals/) for a complete reference on TFC Metals.

Things to note:

- Sizes [`TINY`, `VERY_SMALL`, `SMALL`, `NORMAL`, `LARGE`, `VERY_LARGE` , `HUGE`]
- Weights [`VERY_LIGHT`, `LIGHT`, `MEDIUM`, `HEAVY`, `VERY_HEAVY`]
- Heat capacity determines how fast an item cools down/heat up. Wrought Iron is 0.35.
- Melt temperature is at which temperature the item is melt. Wrought Iron is 1535 / `Brilliant White` while Bronze is 950 / `Orange`. For more, check the [temperature reference](../../temperatures/)
- Registered metal ingot items aren't automatically registered as a valid input for tools (eg: Steel ingot from other mods registered by `registerMetalItem` method won't be automatically workable to TFC steel pickaxe head)
