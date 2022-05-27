---
layout: page
title: "Crafting Recipes"
permalink: /1.18.x/recipes/crafting/
---

# Crafting Recipes

In addition to custom recipe types, TFC also adds several recipe types that can be used for custom crafting recipes. TFC adds the following crafting recipe types:

<!-- Alphabetical Order Please!! -->

- [Advanced Shaped Crafting](#advanced-shaped-crafting)
- [Advanced Shapeless Crafting](#advanced-shapeless-crafting) 
- [Casting](#casting)
- [Damage Inputs](#damage-inputs)
- [Extra Products](#extra-products)
- [Food Combining](#food-combining)

<hr>

## Advanced Shaped Crafting

An advanced shaped crafting recipe is a shaped crafting recipe with some additions to support the output using an [Item Stack Provider](../../data/common-types/#item-stack-providers). It has the following properties:

- `type`: `tfc:advanced_shaped_crafting`
- `group`, `pattern`, `key`, and `conditions` are the same as a usual shaped recipe.
- `result` is an [Item Stack Provider](../../data/common-types/#item-stack-providers), which is the output of the recipe. The "input" stack to the item stack provider is determined by the below `input_row` and `input_column`.
- `input_row` is an integer.
- `input_column` is an integer.

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

An advanced shaped crafting recipe is a shapeless crafting recipe with some additions to support the output using an [Item Stack Provider](../../data/common-types/#item-stack-providers). It has the following properties:

- `type`: `tfc:advanced_shapeless_crafting`
- `group`, `ingredients`, and `conditions` are the same as a usual shapeless recipe.
- `result` is an [Item Stack Provider](../../data/common-types/#item-stack-providers), which is the output of the recipe.
- `primary_ingredient` is an [Ingredient](../data/common-types/#ingredients), which identifies which slot of the recipe is used as the "input" stack for the result.

<hr>

## Casting

This is a crafting recipe which acts as a unified recipe for all [Casting Recipes](../#casting). It is used when placing a filled, solidified mold in the crafting grid. This recipe will then query a casting recipe, and if a valid one is found, it will produce the output of the casting recipe. It has no configurable options by itself.

- `type`: `tfc:casting_crafting`

<hr>

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

## Extra Products

This is a recipe type which wraps a normal crafting recipe, but it's used for producing extra products in addition to the normal recipe products. Any extra products are given directly to the player when they craft the recipe. There are two different variants for shaped and shapeless recipes.

- `type`: `tfc:extra_products_shapeless_crafting` or `tfc:extra_products_shaped_crafting`
- `extra_products`: An Array of [Item Stack](../../data/common-types/#item-stack)s. Each item stack is a single extra product.
- `recipe`: The crafting recipe which this applies to. Must be the same shaped/shapeless type as the type of the damage inputs recipe.

#### Example

```jsonc
// Reference: data/tfc/recipes/crafting/maize_cutting.json
// This recipe uses nested recipe types, both producing extra products (straw) and damaging the knife used
{
    "type": "tfc:extra_products_shapeless_crafting",
    "extra_products": [{
        "item": "tfc:straw"
    }],
    "recipe": {
        "type": "tfc:damage_inputs_shapeless_crafting",
        "recipe": {
            "type": "minecraft:crafting_shapeless",
            "ingredients": [{
                "item": "tfc:food/wheat"
            }, {
                "tag": "tfc:knives"
            }],
            "result": {
                "item": "tfc:food/wheat_grain"
            }
        }
    }
}
```

## Food Combining

This is a crafting recipe which merges foods of the same traits, but with different creation dates. It has no configurable options by itself.

- `type`: `tfc:food_combining`

<hr>
