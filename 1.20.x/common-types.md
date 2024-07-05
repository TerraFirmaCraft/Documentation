---
layout: page
title: "Common Types"
permalink: /1.20.x/common-types/
---

# Common Types

Below are a number of common types used by recipes and custom data.

<!--linky_begin_sort_alphabetical-->

- [Block Ingredients](#block-ingredients)
- [Block State](#block-state)
- [Fluid Ingredients](#fluid-ingredients)
- [Fluid Stack Ingredients](#fluid-stack-ingredients)
- [Fluid Stack](#fluid-stack)
- [Food Traits](#food-traits)
- [Item Stack Ingredients](#item-stack-ingredients)
- [Item Stack Providers](#item-stack-providers)
- [Item Stacks](#item-stacks)
- [Temperature](#temperature)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Block Ingredients

This represents a predicate on blocks in the world. It can be any of the following options:

- A String, with the registry name of a single block.
- A JSON object, with a single `block` key, with the registry name of a single block.
- A JSON object, with a single `tag` key, with the name of a block tag to match.
- A JSON array, whose entries are [Block Ingredients](#block-ingredients), which are logically OR'd together.

<hr>

## Block State

A block state represents an output of a recipe in world. It must be a string which encodes a block. It must contain the registry name of the block, optionally followed by properties with key value pairs separated by `=`, within square brackets. For example:

- `minecraft:dirt` : Just specifying a block name.
- `minecraft:grass_block[snowy=true]` : Using the `snowy=true` property.
- `minecraft:oak_stairs[facing=north,half=bottom,shape=straight,waterlogged=false]` : Using multiple properties.

<hr>

## Fluid Ingredients

A fluid ingredient represents a predicate of fluids. It can be any of the following options:

- A String, with the registry name of a single fluid.
- A JSON object, with a single `fluid` key, with the registry name of a single fluid.
- A JSON object, with a single `tag` key, with the name of a fluid tag to match.
- A JSon array, whose entries are [Fluid Ingredients](#fluid-ingredients), which are logically OR'd together.

<hr>

## Fluid Stack

A fluid stack is used to represent a combination of a single fluid with an amount. It is a JSON object which has the following fields:

- `fluid`: String. The registry name of a Fluid.
- `amount`: Integer. The amount of the fluid stack, in mB.

#### Example

```jsonc
// A fluid stack representing a bucket of water
{
    "fluid": "minecraft:water",
    "amount": 1000
}
```

<hr>

## Fluid Stack Ingredients

A fluid stack ingredient is a combination of a fluid ingredient with an amount. It is a JSON object which has the following fields:

- `ingredient`: A [Fluid Ingredient](#fluid-ingredients)
- `amount`: Integer. An amount in mB for this ingredient. Defaults to 1000 mB.

#### Example

```jsonc
// A fluid stack ingredient which matches a bucket of water
{
    "ingredient": { "fluid": "minecraft:water" },
    "amount": 1000
}
```

<hr>

## Food Traits

A food trait is a String, which must be one of the following options. Note addons may add other food traits not in this list:

- `tfc:salted`, `tfc:pickled`, `tfc:brined`, `tfc:preserved`, `tfc:vinegar`, `tfc:charcoal_grilled`, `tfc:wood_grilled`, `tfc:burnt_to_a_crisp`

<hr>

## Item Stack Ingredients

An item stack ingredient is a combination of an ingredient, and a count. It is a JSON object with the following fields:

- `count`: An optional integer (Default: 1) The count of the item.
- `ingredient`: An [Ingredient](../ingredients/).

#### Example

```jsonc
// An item stack ingredient which requires 5 x minecraft:apple
{
    "count": 5,
    "ingredient": {
        "item": "minecraft:apple"
    }
}
```

<hr>

## Item Stack Providers

An item stack provider represents an output of a recipe, an item stack with any number of transformations applied to it at recipe completion. These transformations are applied sequentially, starting with the provided stack. It is a JSON object with the following fields:

- `stack`: An [Item Stack](#item-stacks) This represents the starting stack before transformations are applied.
- `modifiers`: An array of [Item Stack Modifiers](../item-stack-modifiers/). Each modifier is applied sequentially to the output stack, and at the end, the final result is used as the output of the item stack provider.

**Note:** Any [Item Stack](#item-stacks) will be accepted as a valid item stack provider with no modifiers, if neither the `stack` or `modifiers` keys are present.

#### Example

```jsonc
// An item stack provider which produces a minecraft:steak,
// but copies the food traits and expiration date from the input, and sets the temperature to 400 C
{
    "stack": {
        "item": "minecraft:steak",
        "count": 1
    },
    "modifiers": [
        { "type": "tfc:copy_food" },
        {
            "type": "tfc:add_heat",
            "temperature": 400
        }
    ]
}
```

<hr>

## Item Stacks

This represents a vanilla Minecraft item stack. It is a JSON object with the following fields:

- `item`: String. The registry name of the item in the stack.
- `count`: Integer. The count of the item stack.
- `nbt`: An optional object representing NBT data to be added to the item stack.

#### Example

```jsonc
// An item stack of 3 x minecraft:apple
{
    "item": "minecraft:apple",
    "count": 3
}
```

<hr>

## Temperature

A temperature is a number, which corresponds to a value in degrees Celsius (&deg;C). In-game, the tooltip displays the color based on the internal temperature value:

Temperature Range (&deg;C) | Color
---|---
1 - 80 | <span style="color:#555555">**Warming**</span>
80 - 210 | <span style="color:#555555">**Hot**</span>
210 - 480 | <span style="color:#555555">**Very Hot**</span>
480 - 580 | <span style="color:#AA0000">**Faint Red**</span>
580 - 730 | <span style="color:#AA0000">**Dark Red**</span>
730 - 930 | <span style="color:#FF5555">**Bright Red**</span>
930 - 1100 | <span style="color:#FFAA00">**Orange**</span>
1100 - 1300 | <span style="color:#FFFF55">**Yellow**</span>
1300 - 1400 | <span style="color:#FFFF55">**Yellow-White**</span>
1400 - 1500 | <span style="color:#FFFFFF;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;">**White**</span>
> 1500 | <span style="color:#FFFFFF;text-shadow: 1px 0 0 #000, 0 -1px 0 #000, 0 1px 0 #000, -1px 0 0 #000;">**Brilliant White**</span>

<hr>

<!--linky_end_sort_categories-->