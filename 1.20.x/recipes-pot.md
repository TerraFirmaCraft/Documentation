---
layout: page
title: "Firepit Pot Recipes"
permalink: /1.20.x/recipes-pot/
---

# Firepit Pot Recipes

Pot recipes are recipe types which use the ceramic pot, when placed on a firepit. All pot recipes operate in a similar fashion, where a fluid and ingredients must be added, followed by some amount of time spent boiling in which the ingredients can not be removed, and then outputs will be produced. The pot may have output which can be extracted by interacting with the pot, depending on the type of the recipe.

**Note**: the pot can contain up to 1000 mB in the internal tank, and has five slots for ingredients which are restricted to a stack size of one.

TFC adds two types of pot recipe:

<!--linky_begin_sort_alphabetical-->

- [Jam Pot](#jam-pot)
- [Simple Pot](#simple-pot)
- [Soup Pot](#soup-pot)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Jam Pot

Jam pot recipes produce a special output that can be interacted with in the pot. When clicking with an empty jar with lid, items are extracted from the output and given to the player, typically jars of jam. It ahas the following properties:

- `type`: `tfc:pot_jam`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: An number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".
- `item`: The item given to the player when the pot is clicked with an empty jar. Typically a jar of jam.
- `texture`: A texture location that is rendered in the pot when it is complete and still has output.

#### Example
```jsonc
// References: data/tfc/recipes/pot/jam_banana_2
{
    "type": "tfc:pot_jam",
    "ingredients": [
    {
        "type": "tfc:not_rotten",
        "ingredient": {
            "item": "tfc:food/banana"
        }
    },
    {
        "type": "tfc:not_rotten",
        "ingredient": {
            "item": "tfc:food/banana"
        }
    },
    {
        "tag": "tfc:sweetener"
    }
    ],
    "fluid_ingredient": {
        "ingredient": "minecraft:water",
        "amount": 100
    },
    "duration": 500,
    "temperature": 300,
    "result": {
        "item": "tfc:jar/banana",
        "count": 2
    },
    "texture": "tfc:block/jar/banana"
}
```

<hr>

## Simple Pot

Fluid pot recipes produce an output fluid directly in the pot. It has the following properties:

- `type`: `tfc:pot`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: An number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".
- `fluid_output`: A [Fluid Stack](../common-types/#fluid-stack) that the pot produces upon completion.
- `item_output`: An array of up to 5 [Item Stacks](../common-types/#item-stacks) indicating what items should be left in the pot

#### Example

```jsonc
// Reference: data/tfc/recipes/pot/cooked_rice_2.json
{
  "type": "tfc:pot",
  "ingredients": [
    {
      "type": "tfc:not_rotten",
      "ingredient": {
        "item": "tfc:food/rice_grain"
      }
    },
    {
      "type": "tfc:not_rotten",
      "ingredient": {
        "item": "tfc:food/rice_grain"
      }
    }
  ],
  "fluid_ingredient": {
    "ingredient": "minecraft:water",
    "amount": 100
  },
  "duration": 1000,
  "temperature": 300,
  "item_output": [
    {
      "item": "tfc:food/cooked_rice"
    },
    {
      "item": "tfc:food/cooked_rice"
    }
  ]
}
```

<hr>

## Soup Pot

Soup pot recipes are used in making soups. When the soup is complete, it will remain in the pot as a special output type, and will have to be right clicked between one and three times with a bowl to extract soup. The type of soup and stats of the soup will be dependent on the input items' food properties. It has the following properties:

- `type`: `tfc:soup_pot`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: An number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".

#### Example

```jsonc
// Reference: data/tfc/recipes/pot/soup_3.json
{
    "type": "tfc:pot_soup",
    "ingredients": [{
        "type": "tfc:not_rotten",
        "ingredient": {
            "tag": "tfc:foods/usable_in_soup"
        }
    }, {
        "type": "tfc:not_rotten",
        "ingredient": {
            "tag": "tfc:foods/usable_in_soup"
        }
    }, {
        "type": "tfc:not_rotten",
        "ingredient": {
            "tag": "tfc:foods/usable_in_soup"
        }
    }],
    "fluid_ingredient": {
        "ingredient": "minecraft:water",
        "amount": 1000
    },
    "duration": 1000,
    "temperature": 300
}
```

<hr>

<!--linky_end_sort_categories-->