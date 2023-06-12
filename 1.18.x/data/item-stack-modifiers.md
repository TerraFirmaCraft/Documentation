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
- [Sandwich](#sandwich)

<!--linky_end_sort_alphabetical-->

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
