---
layout: page
title: "Common Types"
permalink: /1.18.x/data/common-types/
---

# Common Types

Below are a number of common types used by recipes and custom data.

- [Block Ingredients](#block-ingredients)
- [Block State](#block-state)
- [Ingredients](#ingredients)
- [Item Stacks](#item-stacks)
- [Item Stack Ingredients](#item-stack-ingredients)
- [Item Stack Providers](#item-stack-providers)
- [Fluid Ingredients](#fluid-ingredients)
- [Fluid Stack](#fluid-stack)
- [Fluid Stack Ingredients](#fluid-stack-ingredients)
- [Food Traits](#food-traits)

<hr>

## Block Ingredients

This represents a predicate on blocks in the world. It can be any of the following options:

- A String, with the registry name of a single block.
- A JSON object, with a single `block` key, with the registry name of a single block.
- A JSON object, with a single `tag` key, with the name of a block tag to match.
- A JSON object, with a `type` key which specifies a custom block ingredient type to use.
- A JSON array, whose entries are [Block Ingredients](#block-ingredients), which are logically OR'd together.

**Note:** TFC only adds the `tfc:block` and `tfc:tag` types, which are already usable via the above syntaxes for `block` and `tag`, and as a result, are not detailed here. Addons may define other block ingredient types.

<hr>

## Block State

A block state represents an output of a recipe in world. It must be a string which encodes a block. It must contain the registry name of the block, optionally followed by properties with key value pairs separated by `=`, within square brackets. For example:

- `minecraft:dirt` : Just specifying a block name.
- `minecraft:grass[snowy=true]` : Using the `snowy=true` property.
- `minecraft:oak_stairs[facing=north,half=bottom,shape=straight,waterlogged=false]` : Using multiple properties.

<hr>

## Ingredients

This represents a vanilla Minecraft ingredient. It must be a JSON object with one of the following keys:

1. An `item` key with the registry name of an item.
2. A `tag` key with the registry name of an item tag.
3. A `type` key with the name of a custom [Ingredient Type](../ingredients/).

<hr>

## Item Stacks

This represents a vanilla Minecraft item stack. It is a JSON object with the following fields:

- `item`: String. The registry name of the item in the stack.
- `count`: Integer. The count of the item stack.
- `nbt`: An optional object representing NBT data to be added to the item stack.

<hr>

## Item Stack Ingredients

An item stack ingredient is a combination of an ingredient, and a count. It is a JSON object with the following fields:

- `count`: The count of the item.
- `ingredient`: An [Ingredient](#ingredients).

#### Example

```jsonc
// An item stack ingredient which requires 5 x minecraft:apple
{
    "count": 4
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
