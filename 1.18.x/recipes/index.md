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

<!-- Alphabetical Order Please!! -->

- [Alloy](#alloy)
- [Barrel Instant](#barrel-instant)
- [Barrel Sealed](#barrel-sealed)
- [Bloomery](#bloomery)
- [Casting](#casting)
- [Collapse](#collapse)
- [Heating](#heating)
- [Knapping (Clay, Fire Clay, Leather)](#knapping)
- [Landslide](#landslide)
- [Loom](#loom)
- [Pot](./pot/)
- [Quern](#quern)
- [Rock Knapping](#rock-knapping)
- [Scraping](#scraping)

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

#### Example

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

A sealed barrel recipe is one which requires the barrel to be sealed for a duration of time. The recipe will begin counting time when the barrel is first sealed, and will only complete if the barrel has been consecutively sealed for the required duration (unsealing and re-sealing will interrupt the recipe's progress).

These recipes are declared in their least common ratio form, and the highest multiple of this recipe that is able to be completed, will be. However unlike [Instant Barrel](#barrel-instant) recipes, this recipe **will** void excess fluids, and items, if the ratio does not match the required ratio of the recipe.

**Note**: A barrel recipe must have *at least* one of `input_item` or `input_fluid`.

- `type`: `tfc:barrel_instant`
- `input_item`: An optional [Item Stack Ingredient](../data/common-types/#item-stack-ingredients), representing the input item. Defaults to empty.
- `input_fluid`: A optional [Fluid Stack Ingredient](../data/common-types/#fluid-stack-ingredients), representing the input fluid. Defaults to empty.
- `output_item`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers), representing the output item. Defaults to empty.
- `output_fluid`: A [Fluid Stack](../data/common-types/#fluid-stack), representing the output fluid. Defaults to empty.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.
- `duration`: An Integer, representing a number of ticks that this barrel must be sealed for. A duration of `-1` will render this barrel recipe to be considered **infinite**, meaning it will never complete. Infinite barrel recipes of this form should define either `on_seal` or `on_unseal`.
- `on_seal`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers) which will be applied whenever this barrel is sealed. This can be used to apply special effects to the item in the barrel while sealed.
- `on_unseal`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers) which will be applied whenever this barrel is unsealed. This can be used to remove special effects on the item in the barrel when no longer sealed.

#### Example

```jsonc
// Reference: data/tfc/recipes/barrel/large_prepared_hide.json
{
    "type": "tfc:barrel_sealed",
    "input_item": {
        "ingredient": {
            "item": "tfc:large_scraped_hide"
        }
    },
    "input_fluid": {
        "ingredient": "minecraft:water",
        "amount": 500
    },
    "output_item": {
        "item": "tfc:large_prepared_hide"
    },
    "duration": 8000
}
```

<hr>

## Bloomery

The bloomery follows the following procedure:

1. It consumes two types of input items: primary inputs, and catalysts. These must be consumed in an 1:1 ratio, and the bloomery has a maximum number of items that it can hold.
2. All primary inputs are converted into metal fluid, by finding a matching [Heating Recipe](#heating) for the item.
3. The total output fluid is divided by the input fluid amount - any excess is lost - and then one output item is produced for each full fluid input. (So a 100mB requiring recipe, when given 350 mB of fluid, would produce 3 items)
4. These items are then embedded in the "bloom" block, which can be mined multiple times to obtain the items.

A bloomery recipe has the following properties:

- `type`: `tfc:bloomery`
- `fluid`: A [Fluid Stack Ingredient](../data/common-types/#fluid-stack-ingredients). The fluid that primary inputs must be able to melt into, to be considered primary inputs.
- `catalyst`: An [Ingredient](../data/common-types/#ingredients). The ingredient which catalysts must match.
- `result`: A [Item Stack](../data/common-types/#item-stacks). The result item stack.
- `duration`: An integer, representing the duration in ticks until the bloomery is complete.

#### Example

```jsonc
// Reference: data/tfc/recipes/bloomery/raw_iron_bloom.json
{
    "type": "tfc:bloomery",
    "result": {
        "item": "tfc:raw_iron_bloom"
    },
    "fluid": {
        "ingredient": "tfc:metal/cast_iron",
        "amount": 100
    },
    "catalyst": {
        "item": "minecraft:charcoal"
    },
    "duration": 15000
}
```

<hr>

## Casting

Casting recipes define recipes between filled, solidified molds, and their item counterpart. They are used in two situations:

1. When right clicking on a mold item, the mold will look for a matching casting recipe in order to determine what to produce.
2. The [Casting Crafting Recipe](./crafting/#casting) will internally look for a matching casting recipe to determine the output.

Casting recipes have the following properties:

- `type`: `tfc:casting`
- `mold`: An [Ingredient](../data/common-types/#ingredients). This ingredient is used just to match the mold item itself, not the contents.
- `fluid`: A [Fluid Stack Ingredient](../data/common-types/#fluid-stack-ingredients). This ingredient is used to match the contents of the solidified mold.
- `result`: An [Item Stack](../data/common-types/#item-stacks). This is the output of the recipe.
- `break_chance`: A number between [0, 1]. This is the probability that the mold will break upon completion of this recipe, where a higher number indicates a higher probability.

#### Example

```jsonc
// Reference: data/tfc/recipes/casting/bismuth_bronze_axe_head.json
{
    "type": "tfc:casting",
    "mold": {
        "item": "tfc:ceramic/axe_head_mold"
    },
    "fluid": {
        "ingredient": "tfc:metal/bismuth_bronze",
        "amount": 100
    },
    "result": {
        "item": "tfc:metal/axe_head/bismuth_bronze"
    },
    "break_chance": 1 // A break chance of 1 indicates this recipe breaks the mold every time
}
```

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

## Heating

A heating recipe is used by any device which heats items, such as a firepit, charcoal forge, small vessel, bloomery, or blast furnace. They define what an item transforms into once heated: either converting into another item (such as cooking food), or melting into a liquid (such as melting ores). It has the following properties:

- `type`: `tfc:heating`
- `ingredient`: An [Ingredient](../data/common-types/#ingredients). This defines what items the heating recipe applies to.
- `result_item`: An optional [Item Stack Provider](../data/common-types/#item-stack-providers) (Default: empty). This defines what item the heating recipe may convert to. Note that the "copy heat" functionality of an item stack provider is implicit and always applied when using heating recipes.
- `result_fluid`: An optional [Fluid Stack](../data/common-types/#fluid-stack) (Default: empty). This defines what fluids the heating recipe may create.
- `temperature`: A number, which is the [Temperature](../data/common-types/#temperature) above which this item will convert to it's outputs.

**Note**: A heating recipe may define one, both, or neither of `result_item` and `result_fluid`, depending on what is desired.

#### Example

```jsonc
// Reference: data/tfc/recipes/heating/ore/normal_bismuthinite.json
// This recipe allows normal bismuthinite ore to melt into 25 mB of molten bismuth at 270 C
{
    "type": "tfc:heating",
    "ingredient": {
        "item": "tfc:ore/normal_bismuthinite"
    },
    "result_fluid": {
        "fluid": "tfc:metal/bismuth",
        "amount": 25
    },
    "temperature": 270
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

## Quern

Quern recipes are used for grinding items in the Quern. The handstone slot is special and will accept any item with the tag `tfc:handstone` (See [Item Tags](../tags/#item-tags)). It has the following properties:

- `type`: `tfc:quern`
- `ingredient`: An [Ingredient](../data/common-types/#ingredients). This is the input for the recipe.
- `result`: An [Item Stack](../data/common-types/#item-stacks). The output of the recipe.

#### Example

```jsonc
// Reference: data/tfc/recipes/quern/bone.json
{
    "type": "tfc:quern",
    "ingredient": {
        "item": "minecraft:bone"
    },
    "result": {
        "item": "minecraft:bone_meal",
        "count": 3
    }
}
```

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

<hr>

## Scraping
