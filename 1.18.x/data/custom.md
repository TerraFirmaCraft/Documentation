---
layout: page
title: "Custom Data"
permalink: /1.18.x/data/custom/
---

# Custom Data

In addition to recipes, TFC defines and loads a number of completely custom data types. These can also be loaded by datapacks, and all are under the root path `tfc`, meaning that any added data should be located under `/data/<your mod id>/tfc/<subfolder>/...`.

TFC defines the following custom data types:

<!--linky_begin_sort_alphabetical-->

- [Climate Ranges](#climate-ranges)
- [Damage Resistances](#damage-resistances)
- [Drinkables](#drinkables)
- [Fauna](#fauna)
- [Fertilizers](#fertilizers)
- [Food Items](#food-items)
- [Fuels](#fuels)
- [Item Heats](#item-heats)
- [Item Sizes](#item-sizes)
- [Lamp Fuels](#lamp-fuels)
- [Metals](#metals)
- [Supports](#supports)
- [Sluicing](#sluicing)
- [Panning](#panning)

<!--linky_end_sort_alphabetical-->

<hr>

## Climate Ranges

A climate range allows TFC Blocks to reference configurable data related to climate. They specify the range of values that a block can grow in.

**Note:** Climate ranges cannot be added through datapacks, only modified.

A climate range has the following properties:

- `min_hydration` An optional integer [0, 100], by default 0, specifying the minimum hydration.
- `max_hydration`: An optional integer [0, 100], by default 100, specifying the maximum hydration.
- `hydration_wiggle_range`: An optional integer, by default 0, specifying the 'wiggle' range of the block when consulting wiggliness is enabled.
- `min_temperature`: An optional integer, by default -100, specifying the minimum temperature.
- `max_temperature`: An optional integer, by default 100, specifying the maximum temperature.
- `temperature_wiggle_range`: An optional integer, by default 0, specifying the 'wiggle' range of the block when consulting wiggliness is enabled.

#### Examples
```jsonc
// Reference: data/tfc/tfc/climate_ranges/barley
{
  "min_hydration": 18,
  "max_hydration": 75,
  "hydration_wiggle_range": 0,
  "min_temperature": -8,
  "max_temperature": 26,
  "temperature_wiggle_range": 5
}
```

<hr>

## Damage Resistances

Damage Resistances specify extra resistance to certain damage types. They can be applied to either items (which will apply when worn as armor), or to entities (i.e. mobs).

All Damage Resistances have the following properties, each of which specifies either a resistance (positive), or a weakness (negative) to a specific damage type:

- `piercing`: An optional integer (Default: `0`).
- `slashing`: An optional integer (Default: `0`).
- `crushing`: An optional integer (Default: `0`).

Resistance is calculated as a multiplicative factor to the damage dealt. The formula for damage dealt is `damage = base_damage * exp(-0.01 * <sum of all resistance and weaknesses>)`. This means that resistances are additive (i.e. two `+10`s are the same as a single `+20`), and cancel out (a `+10` resistance and `-10` weakness cancel each other out), and have diminishing returns the more resistance you accumulate.

For **entities**, damage resistances are found under the subfolder `entity_damage_resistances`, and must have an additional property:

- `entity`: An Entity Tag, specifying what entities this resistance applies to.

For **armor items**, damage resistances are found under the subfolder `item_damage_resistances`, and must have an additional property:

- `ingredient: An [Ingredient](../ingredients/), specifying what items this resistance applies to.

#### Examples

```jsonc
// Reference: data/tfc/tfc/entity_damage_resistances/skeletons.json
{
  "entity": "tfc:skeletons",
  "piercing": 1000000000, // large number to cause very high resistance
  "slashing": 0,
  "crushing": -50 // negative number to cause weakness
}
```

<hr>

## Drinkables

A drinkable defines that a fluid is directly drinkable. Drinkable fluids can be drank either from an empty hand while right clicking on a source block, or from a container such as the ceramic vessel which allows drinking. The drinkable also defines various effects that the fluid can have on the player when drank. It is located under the subfolder `drinkables`. 

When drinking from a source block, the player consumes 25 mB of the drinkable. Other sources, such as ceramic jugs, consume larger quantities. Note that some drinkable effects are all scaled based on the amount drank.

A drinkable has the following properties:

- `ingredient`: An [Fluid Ingredient](../common-types/#fluid-ingredients), which defines which fluids this drinkable applies to.
- `consume_chance`: An optional number in the range [0, 1] (Default: 0). It represents the chance that, when drank from a source block, the source block is removed.
- `thirst`: An optional integer in the range [0, 100] (Default: 0). It represents an amount of thirst that this drinkable consumes, per 25 mB drank.
- `intoxication`: An optional integer (Default: 0). It represents a number of ticks that the player will be intoxicated for, per 25 mB drank.
- `effects` is a array of custom potion effects that this drinkable can apply. Each entry must be an object with the following properties:
  - `type`: A string, which is the registry ID of a potion effect (i.e. `minecraft:slowness`).
  - `duration`: An optional integer (Default: 20) which is a number of ticks this effect is applied for.
  - `amplifier`: An optional integer (Default: 0) which is the level of the potion effect applied.
  - `chance`: An optional number in the range [0, 1] (Default: 1). This represents the chance that this particular effect will be applied per 25 mB drank.

#### Example:

```jsonc
// Reference: data/tfc/tfc/drinkables/alcohol.json
{
  "ingredient": {
    "tag": "tfc:alcohols"
  },
  "thirst": 10,
  "intoxication": 4000
}
```

<hr>

## Fauna

Fauna allow datapacks to specify some spawning requirements for mobs.

**Note:** Fauna cannot be added with datapacks, only modified.

Fauna have the following properties:

- `chance`: An optional integer, by default 1, of the chance in 1/N chunks that something will spawn. Note that the ratio between mob spawns is better set in the [Biome](../../worldgen/biomes/) json, as those values are baked into the spawn generator.
- `distance_below_sea_level`: An optional integer that sets the distance below sea level something must spawn. This should only be set for underwater creatures.
- `climate`: A [Climate Decorator](../../worldgen/decorators/#climate) configuration for the climate requirements of the fauna.
- `solid_ground`: A boolean. Requires the mob to spawn on a `minecraft:valid_spawn` block tag.
- `max_brightness`: An optional integer specifying the maximum brightness a mob may spawn at.

#### Example

```jsonc
// Reference: data/tfc/tfc/fauna/orca
{
  "chance": 10,
  "distance_below_sea_level": 35,
  "climate": {
    "max_temperature": 19,
    "min_rainfall": 100
  }
}
```

## Fertilizers

A fertilizer defines an item which can be used on farmland or crops to increase the nutrients in the soil (farmland). Nutrients are used and consumed by crops to increase their yield. It is located under the subfolder `fertilizers`. A fertilizer has the following properties:

- `ingredient`: An [Ingredient](../ingredients/), which defines which items this fertilizer applies to.
- `nitrogen`: A number (Default `0.0`). Defines how much <span style="color:#55FFFF">**Nitrogen**</span> nutrient this fertilizer adds.
- `phosphorus`: A number (Default `0.0`). Defines how much <span style="color:#FFAA00">**Phosphorous**</span> nutrient this fertilizer adds.
- `potassium`: A number (Default `0.0`). Defines how much <span style="color:#FF55FF">**Potassium**</span> nutrient this fertilizer adds.

#### Example

```jsonc
// Reference: data/tfc/tfc/fertilizers/bone_meal.json
{
    "ingredient": {
        "item": "minecraft:bone_meal"
    },
    "potassium": 0.1
}
```

<hr>

## Food Items

A food item definition defines a food, and applies TFC style stats to it including decay, hunger, water, and nutrition. It is a file located under the subfolder `food_items`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this food item definition applies to.
- `hunger`: An integer (Default `4`). Defines how much hunger this food restores. The player's full hunger bar is equal to `20`.
- `saturation`: A number (Default `0.0`). Defines how much saturation this food restores. Measured in the same units as hunger.
- `water`: A number (Default `0.0`). Defines how much water this food restores. The player's full water bar is equal to `100`.
- `decay_modifier`: A number (Default `1.0`). Defines how quickly this item decays. Higher values indicate faster decay, and thus shorter expiration times.
- `grain`: A number (Default `0.0`). Defines how much <span style="color:#FFAA00">**Grain**</span> nutrient this food adds.
- `fruit`: A number (Default `0.0`). Defines how much <span style="color:#55FF55">**Fruit**</span> nutrient this food adds.
- `vegetables`: A number (Default `0.0`). Defines how much <span style="color:#00AA00">**Vegetables**</span> nutrient this food adds.
- `protein`: A number (Default `0.0`). Defines how much <span style="color:#FF5555">**Protein**</span> nutrient this food adds.
- `dairy`: A number (Default `0.0`). Defines how much <span style="color:#AA00AA">**Dairy**</span> nutrient this food adds. 

**Note:** Typical values for nutrients are 0-2 for small items (fruits, vegetables), and 1-4 for larger items (breads, meats), and higher for meals. Note that nutrients should also scale with hunger: A 2 nutrient/4 hunger food is the same (nutritionally) as a 4 nutrient/8 hunger food.

<hr>

## Fuels

A fuel defines something that burns, and can be used in a fire pit, forge, or other TFC fuel consuming device. It is a file located under the subfolder `fuels`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this fuel applies to.
- `temperature`: A number. The temperature in degrees Celsius that this fuel burns at.
- `duration`: An integer. The duration in ticks that a single item of this fuel burns for.

#### Example

```jsonc
// Reference: data/tfc/tfc/fuels/coal.json
{
    "ingredient": [
        { "item": "minecraft:coal" },
        { "item": "tfc:ore/bituminous_coal" }
    ],
    "duration": 2200,
    "temperature": 1415
}
```

<hr>

## Item Heats

An item heat definition specifies if an item can be heated, and also properties of the heated item. It is a file located under the subfolder `item_heats`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this item heat definition applies to.
- `heat_capacity`: A number which specifies how fast this item heats up relative to others. This is measured in Energy / °C, meaning higher values indicate it takes more energy (time) to heat up.
- `forging_temperature`: An optional number which specifies the temperature at which this item can be worked, in degrees Celsius. If omitted, this item will not require heat to work.
- `welding_temperature`: An optional number which specifies the temperature at which this item can be worked, in degrees Celsius. If omitted, this item will not require heat to weld.

#### Example

```jsonc
// Reference: data/tfc/tfc/item_heats/metal/bismuth_bronze_ingot.json
{
    "ingredient": {
        "tag": "forge:ingots/bismuth_bronze"
    },
    "heat_capacity": 2.857,
    "forging_temperature": 591.0,
    "welding_temperature": 788.0
}
```

<hr>

## Item Sizes

An item size definition specifies the size and weight of items. Size affects what containers the item can fit in:

- Small vessels can hold items that are `Small` and lower.
- Large vessels can hold items that are `Normal` and lower.
- Chests can hold items that are `Large` and lower.
- Pit Kilns can hold four items that are `Large` and lower, or one item which is `Very Large` or `Huge`

Weight affects the stack size of the item (and TFC will override the stack size where possible):

- `Very Light` items will stack to 64.
- `Light` items will stack to 32.
- `Medium` items will stack to 16.
- `Heavy` items will stack to 4.
- `Very Heavy` items will stack to 1.

Finally, items that are both `Huge` size and `Very Heavy` weight will count towards the player being **Overburdened**. This includes Anvils, Sealed Barrels, and Sealed Large Vessels in TFC. 

 An Item Size Definition is a file located in under the subfolder `item_sizes`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this item size definition applies to.
- `size`: An optional string, which must be one of the following sizes: `tiny`, `very_small`, `small`, `normal`, `large`, `very_large`, or `huge`. Defaults to `normal`.
- `weight`: An optional string, which must be one of the following weights: `very_light`, `light`, `medium`, `heavy`, `very_heavy`. Defaults to `medium`.

Note that TFC will attempt to apply defaults for all items that do not have item sizes. It uses the following rules:

1. If the `Item` or `Block` specifies a custom item size implementation.
2. If a item size definition is found matching the item.
3. If the item is a tool (`instanceof TieredItem`), it will be `Large` and `Medium`.
4. If the item is a piece of armor (`instanceof ArmorItem`), it will be `Large` and `Very Heavy`.
5. If the item is a block (`instanceof BlockItem`), it will be `Small` and `Light`.
6. All other items will be `Very Small` and `Very Light`.

#### Example

```jsonc
// Reference: data/tfc/tfc/item_sizes/straw.json
{
    "ingredient": {
        "item": "tfc:straw"
    },
    "size": "small",
    "weight": "very_light"
}
```

<hr>

## Lamp Fuels

A lamp fuel is a fluid which an be used in a lamp. It will burn over time, consuming mB per tick in order to keep the lamp lit. It has the following properties:

- `fluid`: A [Fluid Ingredient](../common-types/#fluid-ingredients) which determines which fluids this lamp fuel applies to.
- `valid_lamps`: A [Block Ingredient](../common-types/#block-ingredients) which determines what (lamp) blocks are valid for this fuel to be added to.
- `burn_rate` An integer, representing how fast this lamp consumes fuel, in ticks per mB.

#### Example

```jsonc
// Reference: data/tfc/tfc/lamp_fuels/olive_oil.json
{
    "fluid": "tfc:olive_oil",
    "valid_lamps": {
        "type": "tfc:tag",
        "tag": "tfc:lamps"
    },
    "burn_rate": 8000
}
```

<hr>

## Metals

A metal specifies a new metal to be used by TFC. A metal is required in order to melt items into metal fluids, or use metals as ingredients in alloys. Notably, this **does not add new items or blocks** to the game, but only defines a metal to TFC, and how to translate it between fluids and metals. A metal is a file located in under the subfolder `metals`. It has the following properties:

- `tier`: An optional integer, of the tier of the metal. Defaults to `0`.
- `fluid`: The registry name of a fluid which corresponds to this metal.
- `melt_temperature`: A number. The melting temperature of the fluid of this metal.
- `specific_heat_capacity`:  A number which specifies how fast this metal fluid heats up relative to others. This is measured in Energy / (mB x °C), meaning it's scaled relative to a quantity of mB, and that higher values will cause it to require more energy (time) to heat up.
- `ingots`: An [Ingredient](../ingredients/) which defines ingot items that are of this metal. This is used in order to allow other mod ingots to be placed in ingot piles.
- `sheets`: An [Ingredient](../ingredients/) which defines sheet items that are of this metal. This is used in order to allow other mod sheets to be placed in sheet piles.

**Note** There must be a **unique** fluid for every metal. Creating multiple metals that reference the same fluid is liable to cause undefined behavior and may introduce bugs!

#### Example

```jsonc
// Reference: data/tfc/tfc/metals/bismuth_bronze.json
{
    "tier": 2,
    "fluid": "tfc:metal/bismuth_bronze",
    "melt_temperature": 985,
    "specific_heat_capacity": 0.00857,
    "ingots": {
        "tag": "forge:ingots/bismuth_bronze"
    },
    "sheets": {
        "tag": "forge:sheets/bismuth_bronze"
    }
}
```

##### Adding Textures

Each metal references a hardcoded texture location, by the name `<the metal namespace>:block/metal/full/<the metal name>`. This texture is then used to render both ingot piles and sheet piles. 

**Example**

> `tfc:bismuth_bronze` references `tfc:textures/block/metal/full/bismuth_bronze.png`
> `yourmod:yourmetal` would reference `yourmod:textures/block/metal/full/yourmetal.png`

When adding a texture yourself (i.e. via a resource pack), it will also need to be added to the atlas. TFC can do this for you, by adding the texture to `tfc-client.toml`:

```toml
[compatibility]
    # Defines additional metal sheet textures that should be added to the block atlas, as they would be otherwise unused, for use in ingot piles and metal sheet blocks.
    # For Pack Makers: When adding a Metal via a datapack, with a custom texture "domain:block/my_texture", and you get missing textures in ingot piles and sheet blocks, that texture needs to be added here
    additionalMetalSheetTextures = ["<yourmod>:block/metal/full/<yourmetal>"]
```

In summary:

- If your metal is added at `data/yourmod/tfc/metals/yourmetal.json`
- It implicitly has the name `yourmod:yourmetal`,
- A texture must exist in a resource pack by the path `assets/yourmod/textures/block/metal/full/yourmetal.png`
- In `tfc-client.toml`, you must add the entry `"yourmod:block/metal/full/yourmetal"` to the `additionalMetalSheetTextures` list.

<hr>

## Supports

Supports define blocks which prevent collapses from **starting** within a specific radius. They do not prevent collapses that started outside the support radius from causing blocks to collapse within the supported area. A support is a file located in under the subfolder `supports`. It has the following properties:

- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients) which defines what blocks this support applies to.
- `support_up`: Integer (Default `0`). The number of blocks upwards that this block supports.
- `support_down`: Integer (Default `0`). The number of blocks downwards that this block supports.
- `support_horizontal`: Integer (Default `0`). The number of blocks horizontally that this block supports.

#### Example

```jsonc
// Reference: data/tfc/tfc/supports/ash.json
{
    "ingredient": "tfc:wood/horizontal_support/ash",
    "support_up": 1,
    "support_down": 1,
    "support_horizontal": 4
}
```

## Sluicing

Sluices link items to loot tables that it processes those items into. This means that any given item can be configured to drop any loot table, even existing loot tables. The loot table generated by sluices has no required context parameters. See the `minecraft:empty` entry in the [Minecraft Wiki article](https://minecraft.fandom.com/wiki/Loot_table) for loot context types. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) matching the item(s) that will go in the sluice
- `loot_table` The location of a loot table to be dropped for this item.

### Example

```jsonc
// Reference: data/tfc/tfc/sluicing/deposits/cassiterite_andesite.json
{
  "ingredient": {
    "item": "tfc:deposit/cassiterite/andesite"
  },
  "loot_table": "tfc:panning/deposits/cassiterite_andesite"
}

```

## Panning

Panning links blocks to loot tables that it processes those blocks into. This means that any given block can be configured to work in the pan and drop any loot table, even existing loot tables. The loot table generated by sluices has three required context parameters: `origin`, the position of the player, `tool`, the pan itself, and `this` (this entity), the player doing the panning. See the `minecraft:fishing` entry in the [Minecraft Wiki article](https://minecraft.fandom.com/wiki/Loot_table) for loot context types. It has the following properties:

- `ingredient`: A [Block Ingredient](../common-types/#block-ingredients) matching the block(s) that will go in the pan
- `loot_table` The location of a loot table to be dropped for this block after panning.
- `model_stages`: An array of model locations that will be iterated through and rendered as panning progresses. If no panning is in progress, just the first model is rendered. This array must not be empty, but can be any length.

Models defined here *must* be added to the Forge special model registry. This can happen a few ways:
- Addons calling `ForgeModelBakery#addSpecialModel` during `ModelRegistryEvent`
- TFC already registering the model
- Pack makers adding models to the client config (`tfc-client.toml`) option `additionalSpecialModels` to have them registered automatically, but this option is not preferred.

For packmakers using the config option, the model file should be at `domain:assets/models/my/favorite/folder.json` where it implicitly has the name `domain:my/favorite/folder` in the eyes of the game. The implicit name is what should be specified in the config file.

### Example

```jsonc
// Reference: data/tfc/tfc/panning/deposits/native_gold_quartzite.json
{
  "ingredient": "tfc:deposit/native_gold/quartzite",
  "model_stages": [
    "tfc:item/pan/native_gold/quartzite_full",
    "tfc:item/pan/native_gold/quartzite_half",
    "tfc:item/pan/native_gold/result"
  ],
  "loot_table": "tfc:panning/deposits/native_gold_quartzite"
}

```
