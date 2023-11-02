---
layout: page
title: "Recipes"
permalink: /1.20.x/data/recipes/
---

# Recipe Types

Recipes can be configured through [datapacks](https://minecraft.wiki/w/Recipe). TFC adds a number of recipe types for its custom crafting operations, and they can be used to add, remove, or modify existing recipes. A complete reference of all of TFC's defined recipes, organized into folders depending on their type can be found in the [TFC Github](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.20.x/src/main/resources/data/tfc/recipes).

TFC adds the following recipe types:

<!--linky_begin_sort_alphabetical-->

- [Alloy](#alloy)
- [Anvil Welding](#anvil-welding)
- [Anvil Working](#anvil-working)
- [Barrel Instant Fluid](#barrel-instant-fluid)
- [Barrel Instant](#barrel-instant)
- [Barrel Sealed](#barrel-sealed)
- [Blast Furnace](#blast-furnace)
- [Bloomery](#bloomery)
- [Casting](#casting)
- [Chiseling](#chiseling)
- [Collapse](#collapse)
- [Glassworking](#glassworking)
- [Heating](#heating)
- [Knapping](#knapping)
- [Landslide](#landslide)
- [Loom](#loom)
- [Pot](../recipes-pot/)
- [Quern](#quern)
- [Scraping](#scraping)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Alloy

Alloy recipes are used in the creation of alloys in small vessels and crucibles. They contain a list of percentages of each other metal which must be satisfied.

**Note:** Only one alloy recipe should be defined for a given output metal. While this is not *required*, some things may not work correctly.

- `type`: `tfc:alloy`
- `result`: A string, representing the registry name of a [Metal](../custom/#metals).
- `contents`: An array of objects, each containing the following properties:
  - `metal`: (String) The registry name of the required [Metal](../custom/#metals).
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

## Anvil Welding

Welding recipes are used to join two items into one. A welding is performed by placing both items in the anvil, plus a single flux, and then shift right clicking the anvil with a hammer. Welding recipes in TFC all require the temperature of the item to be hot enough, however welding recipes do not in general require the item to be heated - only if the item's item temperature defines a `welding_temperature` that is nonzero. Welding recipes have the following properties:

- `type`: `tfc:welding`
- `first_input` and `second_input` are [Ingredients](../ingredients/). They represent both inputs to the recipe. They are not ordered, and so if the two ingredients are different, the recipe will be compared in both orientations to the input items.
- `tier`: An optional integer (Default: -1). The tier of the anvil used must be equal to or greater than the tier of the recipe.
- `result`: An [Item Stack Provider](../common-types/#item-stack-providers) which represents the output of the recipe. Note that the heat of **both** inputs (whichever is higher) is automatically copied to the output.

#### Example

```jsonc
// Reference: data/tfc/recipes/welding/bismuth_bronze_double_ingot.json
{
    "type": "tfc:welding",
    "first_input": {
        "item": "tfc:metal/ingot/bismuth_bronze"
    },
    "second_input": {
        "item": "tfc:metal/ingot/bismuth_bronze"
    },
    "tier": 1, // Tier 1 = Available on copper anvils and above.
    "result": {
        "item": "tfc:metal/double_ingot/bismuth_bronze"
    }
}
```

<hr>

## Anvil Working

Working recipes are used to transform one item into another via the anvil working minigame. Working is performed by placing the item in the anvil, and then using rules to move the pointer until it lines up with the target, and a list of requirements are satisfied by the most recent three rules that were performed.

Rules all follow a specific naming scheme: `[step]_[order]`.

- `[step]` is a type of step that must be performed. It must be one of `hit`, `draw`, `punch`, `bend`, `upset`, `shrink`.
- `[order]` is the order in which the step must be performed, for the rule to be satisfied. It must be one of `any`, `last`, `not_last`, `second_last`, `third_last`.

According to that naming scheme, some valid rules are `hit_last`, `draw_not_last`, `upset_second_last`, or `shrink_any`.

Anvil recipes also can define forging bonuses for certain outputs. The forging bonus is calculated based on the total number of steps used to work the item, and compared to the optimal number of steps possible for that item. The bonus is then compared to a series of thresholds: 1.5x, 2.0x, 5.0x, 10.0x, and a bonus is applied. Forging bonuses consist of the NBT tag `{"tfc:forging_bonus":<value>}`, where `value` is an integer between [1, 4], where a higher number indicates a higher bonus. Tools that have the forging bonus tag have two additional hidden effects, akin to the Unbreaking and Efficiency enchantments in vanilla Minecraft, with their effectiveness based on the higher bonus.

Anvil recipes have the following properties:

- `type`: `tfc:anvil`
- `input`: An [Ingredient](../ingredients/), of the input item. Note that Anvil recipes can have multiple recipes with the same ingredient, and will be selected when the plan is selected for that item.
- `result`: An [Item Stack Provider](../common-types/#item-stack-providers) which represents the output of the recipe. Note that the heat of the input is automatically copied to the output.
- `tier`: An optional integer (Default: -1). The tier of the anvil used must be equal to or greater than the tier of the recipe.
- `rules`: An array of rules. Must have one, two, or three rules. Each rule must be a string following the naming scheme above.
- `apply_forging_bonus`: An optional boolean (Default: `false`). If true, this anvil recipe will automatically apply a forging bonus to the item stack.

#### Example

```jsonc
// Reference: data/tfc/recipes/anvil/bronze_pickaxe_head.json
{
    "type": "tfc:anvil",
    "input": {
        "item": "tfc:metal/ingot/bronze"
    },
    "result": {
        "item": "tfc:metal/pickaxe_head/bronze"
    },
    "tier": 2,
    "rules": [
        "punch_last",
        "bend_not_last",
        "draw_not_last"
    ],
    "apply_forging_bonus": true
}
```

<hr>

## Barrel Instant

An instant barrel recipe is one which takes effect immediately when putting items in a barrel. It can have fluid or item ingredients, and fluid or item outputs, however if it has both fluid and item ingredients, and a fluid output, then the recipe will only activate if there is enough input items to *fully consume* the input fluid.

Like [Sealed Barrel](#barrel-sealed) recipes, these are declared in their lowest common ratio form, and any multiple of this recipe is able to complete at once.

**Note**: A barrel recipe must have *at least* one of `input_item` or `input_fluid`.

- `type`: `tfc:barrel_instant`
- `input_item`: An optional [Item Stack Ingredient](../common-types/#item-stack-ingredients), representing the input item. Defaults to empty.
- `input_fluid`: A optional [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients), representing the input fluid. Defaults to empty.
- `output_item`: An optional [Item Stack Provider](../common-types/#item-stack-providers), representing the output item. Defaults to empty.
- `output_fluid`: A [Fluid Stack](../common-types/#fluid-stack), representing the output fluid. Defaults to empty.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.

#### Example

```jsonc
// Reference: /data/tfc/recipes/barrel/limewater.json
{
    "type": "tfc:barrel_instant",
    "input_item": {
        "ingredient": {
            "item": "tfc:powder/flux"
        }
    },
    "input_fluid": {
        "ingredient": "minecraft:water",
        "amount": 500
    },
    "output_fluid": {
        "fluid": "tfc:limewater",
        "amount": 500
    }
}
```

<hr>

## Barrel Instant Fluid

This is a variant of an instant barrel recipe which involves two fluid inputs. The primary fluid must be in the barrel's liquid tank, and the added fluid must be present in a fluid container item (such as a bucket), and can be added in the item input slot, **or** by placing the item in the fluid input slot. Like a instant barrel recipe, there must be enough fluid in the input item, to fully consume the fluid in the barrel.

Like [Sealed Barrel](#barrel-sealed) recipes, these are declared in their lowest common ratio form, and any multiple of this recipe is able to complete at once.

- `type`: `tfc:barrel_instant_fluid`
- `primary_fluid`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients), representing the input fluid in the barrel.
- `added_fluid`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients), representing the fluid that must be added via a fluid container.
- `output_fluid`: A [Fluid Stack](../common-types/#fluid-stack), representing the output fluid.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.

#### Example

```jsonc
// Reference: /data/tfc/recipes/barrel/brine.json
{
    "type": "tfc:barrel_instant_fluid",
    "primary_fluid": {
        "ingredient": "tfc:salt_water",
        "amount": 9
    },
    "added_fluid": {
        "ingredient": "tfc:vinegar",
        "amount": 1
    },
    "output_fluid": {
        "fluid": "tfc:brine",
        "amount": 10
    }
}
```

<hr>

## Barrel Sealed

A sealed barrel recipe is one which requires the barrel to be sealed for a duration of time. The recipe will begin counting time when the barrel is first sealed, and will only complete if the barrel has been consecutively sealed for the required duration (unsealing and re-sealing will interrupt the recipe's progress).

These recipes are declared in their least common ratio form, and the highest multiple of this recipe that is able to be completed, will be. However unlike [Instant Barrel](#barrel-instant) recipes, this recipe **will** void excess fluids, and items, if the ratio does not match the required ratio of the recipe.

**Note**: A barrel recipe must have *at least* one of `input_item` or `input_fluid`.

- `type`: `tfc:barrel_instant`
- `input_item`: An optional [Item Stack Ingredient](../common-types/#item-stack-ingredients), representing the input item. Defaults to empty.
- `input_fluid`: A optional [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients), representing the input fluid. Defaults to empty.
- `output_item`: An optional [Item Stack Provider](../common-types/#item-stack-providers), representing the output item. Defaults to empty.
- `output_fluid`: A [Fluid Stack](../common-types/#fluid-stack), representing the output fluid. Defaults to empty.
- `sound`: A string, representing the registry name of a sound event, which is played when the recipe finishes. Defaults to `minecraft:block.brewing_stand.brew`.
- `duration`: An Integer, representing a number of ticks that this barrel must be sealed for. A duration of `-1` will render this barrel recipe to be considered **infinite**, meaning it will never complete. Infinite barrel recipes of this form should define either `on_seal` or `on_unseal`.
- `on_seal`: An optional [Item Stack Provider](../common-types/#item-stack-providers) which will be applied whenever this barrel is sealed. This can be used to apply special effects to the item in the barrel while sealed.
- `on_unseal`: An optional [Item Stack Provider](../common-types/#item-stack-providers) which will be applied whenever this barrel is unsealed. This can be used to remove special effects on the item in the barrel when no longer sealed.

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

## Blast Furnace

The blast furnace recipe is used to determine the input and output of a blast furnace. A fluid combined with a catalyst is combined to produce a new fluid.

Blast furnace recipes have the following properties:
- `type`: `tfc:blast_furnace`
- `fluid`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients) for the input fluid.
- `catalyst`: An [Ingredient](../ingredients/) specifying the catalyst item.
- `result`: A [Fluid Stack](../common-types/#fluid-stack) of the output fluid.

#### Example

```jsonc
// Reference: data/tfc/recipes/blast_furnace/pig_iron
{
	"type": "tfc:blast_furnace",
	"fluid": {
		"ingredient": "tfc:metal/cast_iron",
		"amount": 1
	},
	"result": {
		"fluid": "tfc:metal/pig_iron",
		"amount": 1
	},
	"catalyst": {
		"tag": "tfc:flux"
	}
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
- `fluid`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients). The fluid that primary inputs must be able to melt into, to be considered primary inputs.
- `catalyst`: An [Ingredient](../ingredients/). The ingredient which catalysts must match.
- `result`: A [Item Stack](../common-types/#item-stacks). The result item stack.
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
2. The [Casting Crafting Recipe](../crafting/#casting) will internally look for a matching casting recipe to determine the output.

Casting recipes have the following properties:

- `type`: `tfc:casting`
- `mold`: An [Ingredient](../ingredients/). This ingredient is used just to match the mold item itself, not the contents.
- `fluid`: A [Fluid Stack Ingredient](../common-types/#fluid-stack-ingredients). This ingredient is used to match the contents of the solidified mold.
- `result`: An [Item Stack](../common-types/#item-stacks). This is the output of the recipe.
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

## Chiseling

Chiseling recipes define a transformation between blocks when clicked with a chisel. They are used in two situations:

1. When hovering over a block with a chisel to display a preview of the chiseled block
2. When executing a use action with the chisel, to conduct the transformation.

Chisel recipes have the following properties:
- `type`: `tfc:chisel`
- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients) corresponding to the block to be transformed.
- `result`: A [Block State](../common-types/#block-state) that will be placed.
- `mode`: The chisel mode ['smooth', 'stair', 'slab'] that is required.
- `item_ingredient`: An optional [Ingredient](../ingredients/) specifying the chisel. Anything in this ingredient must be in the `tfc:chisels` [Item Tag](../tags/#item-tags)
- `extra_drop`: An optional [Item Stack Provider](../common-types/#item-stack-providers) specifying an item to be dropped on chisel completion.

#### Example
```jsonc
// Reference: data/tfc/recipes/chisel/slab/acacia_wood_slab
{
	"type": "tfc:chisel",
	"ingredient": "tfc:wood/planks/acacia",
	"result": "tfc:wood/planks/acacia_slab",
	"mode": "slab",
	"extra_drop": {
		"item": "tfc:wood/planks/acacia_slab"
	}
}
```

<hr>

## Collapse

A collapse recipe is used for block conversions when a *collapse* occurs, which happens in the following steps:

1. A player mines a block which can *trigger* a collapse (defined by having the `tfc:can_trigger_collapse`) tag.
2. Within a random radius centered on the *trigger* block, blocks that are [unsupported](../custom/#supports) are checked. If one of those blocks can *start* a collapse (defined by having the `tfc:can_start_collapse` tag), a collapse will occur centered on the *start* position.
3. Once a collapse has *started*, within a random radius centered on the *start* position, blocks that can collapse (defined by having both a valid collapse recipe and having the `tfc:can_collapse`), may randomly collapse - apply the recipe and convert to falling blocks.

Collapse recipes are responsible, i.e. from converting raw stone into cobblestone when a collapse occurs.

**Note** The presence of a collapse recipe alone does not make a block able to collapse. It must also be added to the [Can Collapse](../tags/#block-tags) block tag.

A collapse recipe has the following properties:

- `type`: `tfc:collapse`
- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients). The blocks that this recipe applies to.
- `copy_input`: An optional Boolean (Default: `false`). If `true`, the recipe should copy the input block, including properties, as the result, and the `state` property is ignored.
- `result`: A [Block State](../common-types/#block-state). The output state for this recipe. If `copy_input` is `true`, this is not required.

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

## Glassworking

A glassworking recipe is a flexible recipe type that represents a series of *operations* that are performed, most typically on a blowpipe item. When a blowpipe's list of steps on the tooltip matches a recipe, the glass batch is removed from the blowpipe and the result item spawns or is given to the player.

The following operations are possible: `blow`, `roll`, `stretch`, `pinch`, `flatten`, `saw`, `table_pour`, `basin_pour`, `amethyst`, `soda_ash`, `sulfur`, `iron`, `ruby`, `lapis_lazuli`, `pyrite`, `sapphire`, `gold`, `graphite`, `copper`, `nickel`, `tin`, `silver`, `table_pour`, `basin_pour`

A glassworking recipe has the following properties:

- `type`: `tfc:glassworking`
- `operations`: An array of string identifiers for operations, from the list above.
- `batch`: An [Ingredient](../ingredients/) representing the required item that must be attached to the blowpipe. The item should have the `tfc:glass_batches` item tag in order to be able to be added to the blowpipe.
- `result`: An [Item Stack](../common-types/#item-stacks) representing the item result of the recipe.

#### Example

```jsonc
// Reference: data/tfc/recipes/glassworking/lens.json
{
    "type": "tfc:glassworking",
    "operations": [
        "blow",
        "stretch",
        "roll",
        "saw"
    ],
    "batch": {
        "item": "tfc:silica_glass_batch"
    },
    "result": {
        "item": "tfc:lens"
    }
}
```

<hr>

## Heating

A heating recipe is used by any device which heats items, such as a firepit, charcoal forge, small vessel, bloomery, or blast furnace. They define what an item transforms into once heated: either converting into another item (such as cooking food), or melting into a liquid (such as melting ores). Note that this **does not make the item heatable**. Any item used in a heating recipe also needs a [Item Heat](../custom/#item-heats) added for it.

A heating recipe has the following properties:

- `type`: `tfc:heating`
- `ingredient`: An [Ingredient](../ingredients/). This defines what items the heating recipe applies to.
- `result_item`: An optional [Item Stack Provider](../common-types/#item-stack-providers) (Default: empty). This defines what item the heating recipe may convert to. Note that the "copy heat" functionality of an item stack provider is implicit and always applied when using heating recipes.
- `result_fluid`: An optional [Fluid Stack](../common-types/#fluid-stack) (Default: empty). This defines what fluids the heating recipe may create.
- `temperature`: A number, which is the [Temperature](../common-types/#temperature) above which this item will convert to it's outputs.

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

Knapping recipes include all types of knapping. The properties of the knapping recipe are defined by [Knapping Types](../custom/#knapping-types). They define patterns that can be used in the knapping grid. Note that knapping patterns are not automatically rotated or mirrored, and each desired rotation or mirror of a given pattern must be added explicitly. It has the following properties:

- `type`: `tfc:knapping`
- `knapping_type`: An id of a [Knapping Type](../custom/#knapping-types).
- `result`: An [Item Stack](../common-types/#item-stacks). The output of the recipe.
- `ingredient`: An optional [Ingredient] that must match the item clicked. Used to restrict recipes beyond the ingredient in the knapping type, for example how some rock knapping recipes only work for certain rocks. If not provided, there is no restriction beyond that in the knapping type.
- `pattern`: The knapping pattern. Must be an array of strings representing the knapping grid. It can be up to 5 x 5. Spaces are counted as empty space, any other character is treated as a filled spot.
- `outside_slot_required`: Boolean. (Default: `true`) For knapping patterns that are smaller than 5 x 5, this defines if the slots outside that grid are required to be filled, or empty.

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
- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients). The blocks that this recipe applies to.
- `copy_input`: An optional Boolean (Default: `false`). If `true`, the recipe should copy the input block, including properties, as the result, and the `state` property is ignored.
- `result`: A [Block State](../common-types/#block-state). The output state for this recipe. If `copy_input` is `true`, this is not required.

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

Loom recipes are used for producing items with a Loom. Note that loom recipes are unique to their input. This means that you can't have two loom recipes that have the same ingredient. Loom recipes have the following properties:

- `type`: `tfc:loom`
- `ingredient`: An [Item Stack Ingredient](../common-types/#item-stack-ingredients). This is the input for the recipe. Note that this is an Item Stack Ingredient, which means it specifies the count of items required in the ingredient. It is typical for loom recipes to require more than one item.
- `result`: An [Item Stack Provider](../common-types/#item-stack-providers). The result produced by this recipe.
- `steps_required`: An integer, which determines how many steps of the loom's working animation need to be completed to produce one product item.
- `in_progress_texture`: The texture used in the loom rendering when this recipe is in progress.

```jsonc
// Reference: data/tfc/recipes/loom/wool_block.json
{
    "type": "tfc:loom",
    "ingredient": {
       "ingredient": {
           "item": "tfc:wool_cloth"
        },
        "count": 4
    },
    "result": {
        "item": "minecraft:white_wool",
        "count": 8
    },
    "steps_required": 4,
    "in_progress_texture": "minecraft:block/white_wool"
}
```

<hr>

## Quern

Quern recipes are used for grinding items in the Quern. The handstone slot is special and will accept any item with the tag `tfc:handstone` (See [Item Tags](../tags/#item-tags)). It has the following properties:

- `type`: `tfc:quern`
- `ingredient`: An [Ingredient](../ingredients/). This is the input for the recipe.
- `result`: An [Item Stack](../common-types/#item-stacks). The output of the recipe.

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

## Scraping

Scraping recipes are used when any scrapable item - defined as having the `tfc:scrapable` [Item Tag](../tags/#item-tags) is placed on top of a valid scrapable surface - defined by having the `tfc:scraping_surface` [Block Tag](../tags/#block-tags) - and then each of 16 pixel regions are right clicked with a knife in order to transform the recipe from the input to the output. It has the following properties:

- `type`: `tfc:scraping`
- `ingredient`: An [Ingredient](../ingredients/). This is the input for the recipe.
- `result`: An [Item Stack](../common-types/#item-stacks). The output of the recipe.
- `input_texture`: The identifier of the texture displayed on the block for the unfinished item. Must be an existing item/block texture or stitched to the atlas.
- `output_texture`: The identifier of the texture displayed on the block for the finished item. Must be an existing item/block texture or stitched to the atlas.

<hr>

<!--linky_end_sort_categories-->