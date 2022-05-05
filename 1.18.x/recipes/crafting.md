---
layout: page
title: "Crafting Recipes"
permalink: /1.18.x/recipes/crafting/
---

# Crafting Recipes

In addition to custom recipe types, TFC also adds several recipe types that can be used for custom crafting recipes. TFC adds the following crafting recipe types:

- [Damage Inputs](#damage-inputs)
- [Casting](#casting)

## Damage Inputs

These recipes are used for recipes which want to damage tool inputs, such as knives, axes, etc. when crafted, instead of consuming them. There are two different variants for shaped and shapeless recipes.

- `type`: `tfc:damage_inputs_shapeless_crafting` or `tfc:damage_inputs_shaped_crafting`
- `recipe`: The crafting recipe which this applies to. Must be the same shaped/shapeless type as the type of the damage inputs recipe.

#### Example

```jsonc
// Reference: data/tfc/recipes/crafting/rock/marble_brick.json
// This recipe damages the chisel used rather than consuming it
{
    "type": "tfc:damage_inputs_shapeless_crafting",
    "recipe": {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [{
            "item": "tfc:rock/loose/marble"
        }, {
            "tag": "tfc:chisels"
        }],
        "result": {
            "item": "tfc:brick/marble"
        }
    }
}
```

<hr>

## Casting

<hr>