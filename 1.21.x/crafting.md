---
layout: page
title: "Crafting Recipes"
permalink: /1.21.x/crafting/
---

# Crafting Recipes

In addition to custom recipe types, TFC also adds several recipe types that can be used for custom crafting recipes. TFC adds the following crafting recipe types:

<!--linky_begin_sort_alphabetical-->

- [Advanced Shaped Crafting](#advanced-shaped-crafting)
- [Advanced Shapeless Crafting](#advanced-shapeless-crafting)
- [Casting](#casting)
- [Food Combining](#food-combining)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Advanced Shaped Crafting

An advanced shaped crafting recipe is a shaped crafting recipe with some additions to support the output and remainder using [Item Stack Providers](../common-types/#item-stack-providers). It has the following properties:

- `type`: `tfc:advanced_shaped_crafting`
- `pattern`: The crafting pattern, same as a vanilla shaped recipe.
- `key`: The key mapping characters to ingredients, same as a vanilla shaped recipe.
- `show_notification`: Optional boolean (Default: `true`). Whether to show a notification when the recipe is unlocked.
- `result`: An [Item Stack Provider](../common-types/#item-stack-providers), which is the output of the recipe. The "input" stack to the item stack provider is determined by the below `input_row` and `input_column`.
- `input_row`: Optional integer (Default: `0`). The row in the pattern to use as the input stack.
- `input_column`: Optional integer (Default: `0`). The column in the pattern to use as the input stack.
- `remainder`: An optional [Item Stack Provider](../common-types/#item-stack-providers), which computes the remaining items after crafting. This can be used for damaging tools or producing extra products.

In a crafting recipe, the `input_row` and `input_column` are zero indexed positions in the *pattern* where the input stack is to be taken from. For example, in the following pattern:

```jsonc
{
    "pattern": [
        "ABC", // Row 0
        "DEF"  // Row 1
    //  0 1 2 Columns
    ],
    // ...
```

In order to use the `F` item as the "input" item stack, the following would be required:

```jsonc
{
    "input_row": 1,
    "input_column": 2
    // ...
```

<hr>

## Advanced Shapeless Crafting

An advanced shapeless crafting recipe is a shapeless crafting recipe with some additions to support the output and remainder using [Item Stack Providers](../common-types/#item-stack-providers). It has the following properties:

- `type`: `tfc:advanced_shapeless_crafting`
- `ingredients`: A list of [Ingredients](../ingredients/), same as a vanilla shapeless recipe.
- `result`: An [Item Stack Provider](../common-types/#item-stack-providers), which is the output of the recipe.
- `primary_ingredient`: An optional [Ingredient](../ingredients/), which identifies which slot of the recipe is used as the "input" stack for the result.
- `remainder`: An optional [Item Stack Provider](../common-types/#item-stack-providers), which computes the remaining items after crafting. This can be used for damaging tools or producing extra products.

#### Example

```jsonc
// A recipe that damages the knife and produces an extra product (straw)
{
  "type": "tfc:advanced_shapeless_crafting",
  "ingredients": [
    {
      "type": "tfc:and",
      "children": [
        {
          "item": "tfc:food/wheat"
        },
        {
          "type": "tfc:not_rotten"
        }
      ]
    },
    {
      "tag": "c:tools/knife"
    }
  ],
  "primary_ingredient": {
    "tag": "c:tools/knife"
  },
  "remainder": {
    "modifiers": [
      {
        "type": "tfc:damage_crafting_remainder"
      },
      {
        "type": "tfc:extra_products",
        "stack": {
          "count": 1,
          "id": "tfc:straw"
        }
      }
    ]
  },
  "result": {
    "modifiers": [
      {
        "type": "tfc:copy_food"
      }
    ],
    "stack": {
      "count": 1,
      "id": "tfc:food/wheat_grain"
    }
  }
}
```

<hr>

## Casting

This is a crafting recipe which acts as a unified recipe for all [Casting Recipes](../recipes/#casting). This has no purpose in terms of the API, as TFC handles everything related to it itself.

- `type`: `tfc:casting_crafting`

<hr>

## Food Combining

This is a crafting recipe which merges foods of the same traits, but with different creation dates. It has no configurable options by itself. This has no purpose in terms of the API, as TFC handles everything related to it itself.

- `type`: `tfc:food_combining`

<hr>

<!--linky_end_sort_categories-->
