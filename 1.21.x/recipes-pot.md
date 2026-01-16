---
layout: page
title: "Firepit Pot Recipes"
permalink: /1.21.x/recipes-pot/
---

# Firepit Pot Recipes

Pot recipes are recipe types which use the ceramic pot, when placed on a firepit. All pot recipes operate in a similar fashion, where a fluid and ingredients must be added, followed by some amount of time spent boiling in which the ingredients can not be removed, and then outputs will be produced. The pot may have output which can be extracted by interacting with the pot, depending on the type of the recipe.

**Note**: the pot can contain up to 1000 mB in the internal tank, and has five slots for ingredients which are restricted to a stack size of one.

TFC adds three types of pot recipe:

<!--linky_begin_sort_alphabetical-->

- [Jam Pot](#jam-pot)
- [Simple Pot](#simple-pot)
- [Soup Pot](#soup-pot)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Jam Pot

Jam pot recipes produce a special output that can be interacted with in the pot. When clicking with an empty jar with lid, items are extracted from the output and given to the player, typically jars of jam. It has the following properties:

- `type`: `tfc:pot_jam`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Sized Fluid Ingredient](../common-types/#sized-fluid-ingredient) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: A number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".
- `unsealed_result`: An [Item Stack](../common-types/#item-stacks). The item given to the player when the pot is clicked with an empty jar (without lid).
- `sealed_result`: An [Item Stack](../common-types/#item-stacks). The item given to the player when the pot is clicked with an empty jar with lid.
- `texture`: A texture location (ResourceLocation) that is rendered in the pot when it is complete and still has output.

#### Example

```json
{
  "type": "tfc:pot_jam",
  "duration": 500,
  "fluid_ingredient": {
    "amount": 100,
    "fluid": "minecraft:water"
  },
  "ingredients": [
    {
      "type": "tfc:and",
      "children": [
        {
          "item": "tfc:food/banana"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    },
    {
      "type": "tfc:and",
      "children": [
        {
          "item": "tfc:food/banana"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    },
    {
      "tag": "tfc:foods/sweeteners"
    }
  ],
  "sealed_result": {
    "count": 2,
    "id": "tfc:jar/banana"
  },
  "temperature": 300.0,
  "texture": "tfc:block/jar/banana",
  "unsealed_result": {
    "count": 2,
    "id": "tfc:jar/banana_unsealed"
  }
}
```

<hr>

## Simple Pot

Simple pot recipes produce an output fluid and/or output items directly in the pot. It has the following properties:

- `type`: `tfc:pot`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Sized Fluid Ingredient](../common-types/#sized-fluid-ingredient) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: A number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".
- `fluid_output`: An optional [Fluid Stack](../common-types/#fluid-stack) that the pot produces upon completion. Defaults to empty.
- `item_output`: An optional array of up to 5 [Item Stack Providers](../common-types/#item-stack-providers) indicating what items should be left in the pot. Defaults to empty.
- `uses_all_fluid`: An optional boolean (Default: `true`). If false, only consumes the fluid ingredient amount and leaves remaining fluid in the pot.

#### Example

```json
{
  "type": "tfc:pot",
  "duration": 2400,
  "fluid_ingredient": {
    "amount": 1000,
    "fluid": "minecraft:water"
  },
  "fluid_output": {
    "amount": 1000,
    "id": "tfc:canola_oil_water"
  },
  "ingredients": [
    {
      "item": "tfc:canola_paste"
    },
    {
      "item": "tfc:canola_paste"
    },
    {
      "item": "tfc:canola_paste"
    },
    {
      "item": "tfc:canola_paste"
    },
    {
      "item": "tfc:canola_paste"
    }
  ],
  "temperature": 300.0
}
```

<hr>

## Soup Pot

Soup pot recipes are used in making soups. When the soup is complete, it will remain in the pot as a special output type, and will have to be right clicked between one and three times with a bowl to extract soup. The type of soup and stats of the soup will be dependent on the input items' food properties. It has the following properties:

- `type`: `tfc:pot_soup`
- `ingredients`: An array of [Ingredients](../ingredients/) that the recipe consumes. Should not be more than five, otherwise the recipe will be impossible.
- `fluid_ingredient`: A [Sized Fluid Ingredient](../common-types/#sized-fluid-ingredient) that the recipe requires.
- `duration`: An integer. The number of ticks that the pot must boil for.
- `temperature`: A number. The minimum temperature in degrees Celsius that the pot must be above to start "boiling".

#### Example

```json
{
  "type": "tfc:pot_soup",
  "duration": 1200,
  "fluid_ingredient": {
    "amount": 100,
    "fluid": "minecraft:water"
  },
  "ingredients": [
    {
      "type": "tfc:and",
      "children": [
        {
          "tag": "tfc:usable_in_soup"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    },
    {
      "type": "tfc:and",
      "children": [
        {
          "tag": "tfc:usable_in_soup"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    },
    {
      "type": "tfc:and",
      "children": [
        {
          "tag": "tfc:usable_in_soup"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    }
  ],
  "temperature": 300.0
}
```

<hr>

<!--linky_end_sort_categories-->
