---
layout: page
title: "Firepit Pot Recipes"
permalink: /1.18.x/recipes/pot/
---

# Firepit Pot Recipes

Pot recipes are recipe types which use the ceramic pot, when placed on a firepit. All pot recipes operate in a similar fashion, where a fluid and ingredients must be added, followed by some amount of time spent boiling in which the ingredients can not be removed, and then outputs will be produced. The pot may have output which can be extracted by interacting with the pot, depending on the type of the recipe.

**Note**: the pot can contain up to 1000 mB in the internal tank, and has five slots for ingredients which are restricted to a stack size of one.

TFC adds two types of pot recipe:

- [Fluid Pot](#fluid-pot)
- [Soup Pot](#soup-pot)

<hr>

## Fluid Pot

Fluid pot recipes produce an output fluid directly in the pot. It has the following properties:

- `type`: `tfc:fluid_pot`
- `ingredients`: An array of [Ingredients](../../data/common-types/#ingredients) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Fluid Stack Ingredient](../../data/common-types/#fluid-stack-ingredients) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: An number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".
- `fluid_output`: A [Fluid Stack](../../data/common-types/#fluid-stack) that the pot produces upon completion.

#### Example

```jsonc
// Reference: data/tfc/recipes/pot/black_dye.json
{
    "type": "tfc:pot_fluid",
    "ingredients": [{
        "item": "minecraft:black_dye"
    }],
    "fluid_ingredient": {
        "ingredient": "minecraft:water",
        "amount": 1000
    },
    "duration": 2000,
    "temperature": 600,
    "fluid_output": {
        "fluid": "tfc:black_dye",
        "amount": 1000
    }
}
```

<hr>

## Soup Pot
