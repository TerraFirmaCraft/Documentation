---
layout: page
title: "Item Stack Modifiers"
permalink: /1.18.x/data/item-stack-modifiers/
---

# Item Stack Modifiers

An item stack modifier is a entry in a [Item Stack Provider](../common-types/#item-stack-providers). It must contain at least a `type` field which identifies the type of the modifier. Modifiers may also require additional properties based on their type.

Note that some modifiers only function when used in crafting recipes that support the use of an [Item Stack Provider](../common-types/#item-stack-providers), that is, [Advanced Shaped Recipe](../../data/crafting/#advanced-shaped-crafting) and [Advanced Shapeless Recipe](../../data/crafting/#advanced-shapeless-crafting).

TFC adds the following item stack modifier types:

<!--linky_begin_sort_alphabetical-->

- [Meal](#meal)
- [Add Bait to Rod](#add-bait-to-rod)
- [Add Heat](#add-heat)
- [Add Trait](#add-trait)
- [Copy Food](#copy-food)
- [Copy Forging Bonus](#copy-forging-bonus)
- [Copy Heat](#copy-heat)
- [Copy Input](#copy-input)
- [Empty Bowl](#empty-bowl)
- [Remove Trait](#remove-trait)
- [Reset Food](#reset-food)

<!--linky_end_sort_alphabetical-->

<hr>

## Meal

This modifier combines nutrients from various foods in a crafting grid into a single food result item. The resulting food must be a *dynamic food item*, such as sandwiches. You can read about how dynamic foods work [here](../custom/#food-items). It has the following parameters:

- `type`: `tfc:meal`
- `food`: A food data object that describes stats that will always be added to the final food item, specifying all the same parameters for a food's nutrients, decay, water, etc. It follows the same specification as specifying a static food in [a food item json](../custom/#food-items), but without the `ingredient` parameter.
- `portions`: A list of meal portion objects. These objects are checked in order, and the first one to match a food in the crafting grid has its food data added to the result item according to the specification. Note that portions describe how the components of the specified recipe are *used*. They have no bearing on what ingredients are *allowed* in the recipe. A meal portion has the following parameters:
    - `ingredient`: An optional [Ingredient](../ingredients/). If not included, the portion will match all foods. Typically, a meal portion with no ingredient would be specified last in the array of portions, in order to catch all the remaining foods that haven't been used.
    - `nutrient_modifier`: An optional float, default `1.0`, that multiplies the nutrition from the food using this portion.
    - `water_modifier`: An optional float, default `1.0`, that multiplies the water from the food using this portion.
    - `saturation_modifier`: An optional float, default `1.0`, that multiplies the saturation from the food using this portion.

An example for how to specify a meal modifier is below. Note that the `//` comments in the json are for educational purposes and will cause loading to fail in some json specifications.
```jsonc
// Reference: data/tfc/recipes/crafting/oat_sandwich.json
{
    "type": "tfc:meal",
    // this food information is always added to the final sandwich
    "food": {
        "hunger": 4,
        "water": 0.5,
        "saturation": 1,
        "decay_modifier": 4.5
    },
    "portions": [
        {
            // first, we check for sandwich bread
            // anything that matches the sandwich bread tag will get their values multiplied by 0.5 and added to the sandwich
            "ingredient": {
                "tag": "tfc:sandwich_bread"
            },
            "nutrient_modifier": 0.5,
            "saturation_modifier": 0.5,
            "water_modifier": 0.5
        },
        {
            // no ingredient is specified, so any food will match these
            // however, the first portion already 'claimed' the sandwiches, so only the remaining ingredients are used.
            "nutrient_modifier": 0.8,
            "water_modifier": 0.8,
            "saturation_modifier": 0.8
        }
    ]
}
```

**This modifier is only usable in crafting recipes which support item stack providers.**

<hr>

## Add Bait to Rod

This modifier takes as input a fishing rod, and searches elsewhere in the crafting grid for a bait type item, which is then attaches to the fishing rod as the result. It has the following fields:

- `type`: `tfc:add_bait_to_rod`

**This modifier is only usable in crafting recipes which support item stack providers.**

<hr>

## Add Heat

This specifies that the provider should add a specific heat value. Note that adding a heat value where none was previously specified is the same as directly setting the heat. It has the following fields:

- `type`: `tfc:add_heat`
- `temperature`: Integer. An amount in degrees Celsius to be added.

<hr>

## Add Trait

This specifies that the provider should add a food trait to the item. It has the following fields:

- `type`: `tfc:add_trait`
- `trait`: A [Food Trait](../common-types/#food-traits) to be added.

<hr>

## Copy Food

This specifies that the provider should copy the food properties (expiration date, food traits) from the input stack. It has the following fields:

- `type`: `tfc:copy_food`

<hr>

## Copy Forging Bonus

This specifies that the provider should copy the Forging bonus, which is recorded as a NBT tag on the stack, from the input stack. It has the following fields:

- `type`: `tfc:copy_forging_bonus`

<hr>

## Copy Heat

This specifies that the provider should copy the current heat from the input stack. It has the following fields:

- `type`: `tfc:copy_heat`

<hr>

## Copy Input

This specifies that the provider should copy the input to the recipe, and ignore the `stack` parameter. The stack defined as the "input" stack will be different depending on the recipe the provider is used in. It has the following fields:

- `type`: `tfc:copy_input`

<hr>

## Empty Bowl

This specifies that the output item should be the empty bowl of the input. This is supported for soup items, which return the bowl they were created with. It has the following fields:

- `type`: `tfc:empty_bowl`

<hr>

## Remove Trait

This specifies that the provider should remove a food trait from the item. It has the following fields:

- `type`: `tfc:remove_trait`
- `trait`: A [Food Trait](../common-types/#food-traits) to be removed.

<hr>

## Reset Food

This specifies that the provider should set the output item to be created at the current time. This might be necessary for recipes that produce item stack outputs that might rot over time. It has the following fields:

- `type`: `tfc:reset_food`

<hr>

## Sandwich

This modifier constructs a sandwich using the input ingredients present in the recipe.

- `type`: `tfc:sandwich`

**This modifier is only usable in crafting recipes which support item stack providers.**

<hr>
