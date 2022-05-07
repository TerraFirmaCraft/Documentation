---
layout: page
title: "Item Stack Modifiers"
permalink: /1.18.x/data/item-stack-modifiers/
---

# Item Stack Modifiers

An item stack modifier is a entry in a [Item Stack Provider](../common-types#item-stack-providers). It must contain at least a `type` field which identifies the type of the modifier. Modifiers may also require additional properties based on their type.

TFC adds the following item stack modifier types:

- [Copy Input](#copy-input)
- [Copy Food](#copy-food)
- [Copy Heat](#copy-heat)
- [Reset Food](#reset-food)
- [Empty Bowl](#empty-bowl)
- [Add Trait](#add-trait)
- [Remove Trait](#remove-trait)
- [Add Heat](#add-heat)

## Copy Input

This specifies that the provider should copy the input to the recipe, and ignore the `stack` parameter. The stack defined as the "input" stack will be different depending on the recipe the provider is used in. It has the following fields:

- `type`: `tfc:copy_input`

<hr>

## Copy Food

This specifies that the provider should copy the food properties (expiration date, food traits) from the input stack. It has the following fields:

- `type`: `tfc:copy_food`

<hr>

## Copy Heat

This specifies that the provider should copy the current heat from the input stack. It has the following fields:

- `type`: `tfc:copy_heat`

<hr>

## Reset Food

This specifies that the provider should set the output item to be created at the current time. This might be necessary for recipes that produce item stack outputs that might rot over time. It has the following fields:

- `type`: `tfc:reset_food`

<hr>

## Empty Bowl

This specifies that the output item should be the empty bowl of the input. This is supported for soup items, which return the bowl they were created with. It has the following fields:

- `type`: `tfc:empty_bowl`

<hr>

## Add Trait

This specifies that the provider should add a food trait to the item. It has the following fields:

- `type`: `tfc:add_trait`
- `trait`: A [Food Trait](../common-types/#food-traits) to be added.

<hr>

## Remove Trait

This specifies that the provider should remove a food trait from the item. It has the following fields:

- `type`: `tfc:remove_trait`
- `trait`: A [Food Trait](../common-types/#food-traits) to be removed.

<hr>

## Add Heat

This specifies that the provider should add a specific heat value. Note that adding a heat value where none was previously specified is the same as directly setting the heat. It has the following fields:

- `type`: `tfc:add_trait`
- `temperature`: Integer. An amount in degrees Celsius to be added.
