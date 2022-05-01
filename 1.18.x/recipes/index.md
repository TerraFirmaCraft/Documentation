---
layout: page
title: "Recipes"
permalink: /1.18.x/recipes/
---

<!--
Note to self: consider separating this page out into multiple pages as it might get really long.
One page per recipe type would be decent, all under recipes/
This is generally considering that recipes are more complex than i.e. the types in common-types or data (although the latter also may want to be broken out into their own pages)
 -->

# Recipe Types

Recipes can be configured through [datapacks](https://minecraft.fandom.com/wiki/Recipe). TFC adds a number of recipe types for its custom crafting operations, and they can be used to add, remove, or modify existing recipes. A complete reference of all of TFC's defined recipes, organized into folders depending on their type can be found in the [TFC Github](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.18.x/src/main/resources/data/tfc/recipes).

TFC adds the following recipe types:

- [Alloy](#alloy)
- [Barrel Instant](#barrel-instant)
- [Barrel Sealed](#barrel-sealed)
- [Bloomery](#bloomery)
- [Casting](#casting)
- [Collapse](#collapse)
- [Knapping (Clay, Fire Clay, Leather)](#knapping)
- [Landslide](#landslide)
- [Loom](#loom)
- [Pot](#pot)
- [Quern](#quern)
- [Rock Knapping](#rock-knapping)

<hr>

## Alloy

Alloy recipes are used in the creation of alloys in small vessels and crucibles. They contain a list of percentages of each other metal which must be satisfied.

**Note:** Only one alloy recipe should be defined for a given output metal. While this is not *required*, some things may not work correctly.

- `type`: `tfc:alloy`
- `result`: A string, representing the registry name of a [Metal](../data/#metals).
- `contents`: An array of objects, each containing the following properties:
  - `metal`: (String) The registry name of the required [Metal](../data/#metals).
  - `min`: The minimum proportion needed in the mixture, in the range [0, 1].
  - `max`: The maximum proportion needed, larger than `min` and in the range [0, 1].

### Example

```json
{
  "type": "tfc:alloy",
  "result": "tfc:bismuth_bronze",
  "contents": [
    {
      "metal": "tfc:copper",
      "min": 0.2,
      "max": 0.3
    },
    {
      "metal": "cool_addon:another_metal",
      "min": 0.5,
      "max": 0.65
    }
  ]
}
```

<hr>

## Barrel Instant

An instant barrel recipe is one which takes effect immediately when putting items in a barrel. It can have fluid or item ingredients, and fluid or item outputs, however if it has both fluid and item ingredients, and a fluid output, then the recipe will only activate if there is enough input items to *fully consume* the input fluid.

Like [Sealed Barrel](#barrel-sealed) recipes, these are declared in their lowest common ratio form, and any multiple of this recipe is able to complete at once.

**Note**: A barrel recipe must have *at least* one of `input_item` or `input_fluid`.

- `type`: `tfc:barrel_instant`
- `input_item`: An optional [Item Stack Ingredient](../data/common-types/#item-stack-ingredients), representing the input item. Defaults to empty.
- `input_fluid`: A optional [Fluid Stack Ingredient](../data/common-types/#fluid-stack-ingredients), representing the input fluid. Defaults to empty.
- `output_item`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers), representing the output item. Defaults to empty.
- `output_fluid`: A [Fluid Stack](../data/common-types/#fluid-stack), representing the output fluid. Defaults to empty.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.

<hr>

## Barrel Sealed

<hr>

## Bloomery

<hr>

## Casting

<hr>

## Collapse

A collapse recipe is used for block conversions when a *collapse* occurs, which happens in the following steps:

1. A player mines a block which can *trigger* a collapse (defined by having the `tfc:can_trigger_collapse`) tag.
2. Within a random radius centered on the *trigger* block, blocks that are [unsupported](../data/#supports) are checked. If one of those blocks can *start* a collapse (defined by having the `tfc:can_start_collapse` tag), a collapse will occur centered on the *start* position.
3. Once a collapse has *started*, within a random radius centered on the *start* position, blocks that can collapse (defined by having both a valid collapse recipe and having the `tfc:can_collapse`), may randomly collapse - apply the recipe and convert to falling blocks.

Collapse recipes are responsible, i.e. from converting raw stone into cobblestone when a collapse occurs.

**Note** The presence of a collapse recipe alone does not make a block able to collapse. It must also be added to the [Can Collapse](../tags/#block-tags) block tag.

A collapse recipe has the following properties:

- `type`: `tfc:collapse`
- `ingredient`: A [Block Ingredient](../data/common-types/#block-ingredients). The blocks that this recipe applies to.
- `copy_input`: An optional Boolean (Default: `false`). If `true`, the recipe should copy the input block, including properties, as the result, and the `state` property is ignored.
- `result`: A [Block State](../data/common-types/#block-state). The output state for this recipe. If `copy_input` is `true`, this is not required.

#### Example

```jsonc
// Reference: data/tfc/recipes/collapse/andesite_spike.json
{
    "type": "tfc:collapse",
    "ingredient": "tfc:rock/spike/andesite",
    "copy_input": true,
    // Note that no 'result' field is required, as 'copy_input' is true.
}
```

<hr>

## Knapping

Knapping recipes include clay knapping, fire clay knapping, and leather knapping. They define patterns that can be used in the knapping grid. Note that knapping patterns are not automatically rotated or mirrored, and each desired rotation or mirror of a given pattern must be added explicitly. It has the following properties:

- `type`: `tfc:clay_knapping`, `tfc:fire_clay_knapping`, or `tfc:leather_knapping`
- `result`: An [Item Stack](../data/common-types/#item-stacks). The output of the recipe.
- `pattern`: The knapping pattern. Must be an array of strings representing the knapping grid. It can be up to 5 x 5. Spaces are counted as empty space, any other character is treated as a filled spot.
- `outside_slot_required`: Boolean. (Default: `true`) For knapping patterns that are smaller than 5 x 5, this defines if the slots outside that grid are required to be filled, or empty.

**Note** For rock knapping, see [Rock Knapping](#rock-knapping)

#### Example

```jsonc
// Reference: data/tfc/recipes/clay_knapping/pickaxe_head_mold.json
{
    "type": "tfc:clay_knapping",
    "outside_slot_required": true,
    "pattern": [
        "XXXXX",
        "X   X",
        " XXX ",
        "XXXXX"
      ],
    "result": {
        "item": "tfc:ceramic/unfired_pickaxe_head_mold"
    }
}
```

<hr>

## Landslide

A landslide recipe is used for block conversions when a certain block *landslides*. A *landslide* is what occurs when a block update causes adjacent blocks to check if they are affected by gravity, and either fall directly downwards, or to adjacent blocks and downwards. It is responsible, i.e. from converting grass to dirt when landsliding.

**Note** The presence of a landslide recipe alone does not make a block able to landslide. It must also be added to the [Can Landslide](../tags/#block-tags) block tag.

A landslide recipe has the following properties:

- `type`: `tfc:landslide`
- `ingredient`: A [Block Ingredient](../data/common-types/#block-ingredients). The blocks that this recipe applies to.
- `copy_input`: An optional Boolean (Default: `false`). If `true`, the recipe should copy the input block, including properties, as the result, and the `state` property is ignored.
- `result`: A [Block State](../data/common-types/#block-state). The output state for this recipe. If `copy_input` is `true`, this is not required.

#### Example

```jsonc
// Reference: data/tfc/recipes/landslide/black_sand.json
{
    "type": "tfc:landslide",
    "ingredient": "tfc:sand/black",
    "result": "tfc:sand/black"
}
```

<hr>

## Loom

<hr>

## Pot

<hr>

## Quern

<hr>

## Rock Knapping

Rock knapping recipes can be used when knapping loose rocks. They define patterns that can be used in the knapping grid. Note that knapping patterns are not automatically rotated or mirrored, and each desired rotation or mirror of a given pattern must be added explicitly. It has the following properties:

- `type`: `tfc:rock_knapping`
- `ingredient`: An [Ingredient](../data/common-types/#ingredients). This defines what loose rock items this recipe applies to.
- `result`: An [Item Stack](../data/common-types/#item-stacks). The output of the recipe.
- `pattern`: The knapping pattern. Must be an array of strings representing the knapping grid. It can be up to 5 x 5. Spaces are counted as empty space, any other character is treated as a filled spot.
- `outside_slot_required`: Boolean. (Default: `true`) For knapping patterns that are smaller than 5 x 5, this defines if the slots outside that grid are required to be filled, or empty.

**Note** For other types of knapping, see [Knapping](#knapping)

#### Example

```jsonc
// Reference: data/tfc/recipes/rock_knapping/axe_head_sedimentary.json
{
    "type": "tfc:rock_knapping",
    "outside_slot_required": false,
    "pattern": [
        " X   ",
        "XXXX ",
        "XXXXX",
        "XXXX ",
        " X   "
    ],
    "result": {
        "item": "tfc:stone/axe_head/sedimentary"
    },
    "ingredient": {
        "tag": "tfc:sedimentary_rock"
    }
}
```
