---
layout: page
title: "Custom Data"
permalink: /1.21.x/custom/
---

# Custom Data

In addition to recipes, TFC defines and loads a number of completely custom data types. These can also be loaded by datapacks, and all are under the root path `tfc`, meaning that any added data should be located under `/data/<your mod id>/tfc/<subfolder>/...`.

TFC defines the following custom data types:

<!--linky_begin_sort_alphabetical-->

- [Climate Ranges](#climate-ranges)
- [Damage Resistances](#damage-resistances)
- [Deposits](#deposits)
- [Drinkables](#drinkables)
- [Fauna](#fauna)
- [Fertilizers](#fertilizers)
- [Fluid Heats](#fluid-heats)
- [Food Items](#food-items)
- [Fuels](#fuels)
- [Item Heats](#item-heats)
- [Item Sizes](#item-sizes)
- [Knapping Types](#knapping-types)
- [Lamp Fuels](#lamp-fuels)
- [Supports](#supports)

<!--linky_end_sort_alphabetical-->
<hr>
<!--linky_begin_sort_categories-->

## Climate Ranges

A climate range allows TFC Blocks to reference configurable data related to climate. They specify the range of values that a block can grow in. It is located under the subfolder `climate_range`.

**Note:** Climate ranges cannot be added through datapacks, only modified.

A climate range has the following properties:

- `min_hydration`: An optional integer [0, 100] (Default: `0`). The minimum hydration.
- `max_hydration`: An optional integer [0, 100] (Default: `100`). The maximum hydration.
- `hydration_wiggle_range`: An optional integer (Default: `0`). The 'wiggle' range for hydration when wiggliness is enabled.
- `min_temperature`: An optional number (Default: no minimum). The minimum temperature in degrees Celsius.
- `max_temperature`: An optional number (Default: no maximum). The maximum temperature in degrees Celsius.
- `temperature_wiggle_range`: An optional number (Default: `0`). The 'wiggle' range for temperature when wiggliness is enabled.

#### Example
```jsonc
// Reference: data/tfc/tfc/climate_range/barley.json
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

- `piercing`: An optional number (Default: `0`).
- `slashing`: An optional number (Default: `0`).
- `crushing`: An optional number (Default: `0`).

Resistance is calculated as a multiplicative factor to the damage dealt. The formula for damage dealt is `damage = base_damage * exp(-0.01 * <sum of all resistance and weaknesses>)`. This means that resistances are additive (i.e. two `+10`s are the same as a single `+20`), and cancel out (a `+10` resistance and `-10` weakness cancel each other out), and have diminishing returns the more resistance you accumulate.

For **entities**, damage resistances are found under the subfolder `entity_damage_resistance`, and must have an additional property:

- `entity`: An Entity Tag, specifying what entities this resistance applies to.

For **armor items**, damage resistances are found under the subfolder `item_damage_resistance`, and must have an additional property:

- `ingredient`: An [Ingredient](../ingredients/), specifying what items this resistance applies to.

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

## Deposits

Deposits link items to loot tables for processing via the pan or sluice. This unified system handles both panning and sluicing. The loot table generated has three context parameters: `origin` (the position of the player), `tool` (the pan or sluice), and `this` (the player). It is located under the subfolder `deposit`. A deposit has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) matching the item(s) that can be processed.
- `loot_table`: The location of a loot table to be dropped after processing.
- `model_stages`: An optional array of model locations used for panning visualization. These are iterated through as panning progresses. If not provided, the deposit can only be used in sluices.

Models defined in `model_stages` must be added to the model registry. This can happen a few ways:
- Addons calling the appropriate model registration during model events
- TFC already registering the model
- Pack makers adding models to the client config (`tfc-client.toml`) option `additionalSpecialModels`

#### Example

```jsonc
// Reference: data/tfc/tfc/deposit/native_gold_quartzite.json
// A deposit that can be panned (has model_stages) or sluiced
{
  "ingredient": {
    "item": "tfc:deposit/native_gold/quartzite"
  },
  "loot_table": "tfc:panning/deposits/native_gold_quartzite",
  "model_stages": [
    "tfc:item/pan/native_gold/quartzite_full",
    "tfc:item/pan/native_gold/quartzite_half",
    "tfc:item/pan/native_gold/result"
  ]
}
```

```jsonc
// A deposit that can only be sluiced (no model_stages)
{
  "ingredient": {
    "item": "tfc:deposit/cassiterite/andesite"
  },
  "loot_table": "tfc:panning/deposits/cassiterite_andesite"
}
```

<hr>

## Drinkables

A drinkable defines that a fluid is directly drinkable. Drinkable fluids can be drank either from an empty hand while right clicking on a source block, or from a container such as the ceramic vessel which allows drinking. The drinkable also defines various effects that the fluid can have on the player when drank. It is located under the subfolder `drinkable`.

When drinking from a source block, the player consumes 25 mB of the drinkable. Other sources, such as ceramic jugs, consume larger quantities. Note that some drinkable effects are all scaled based on the amount drank.

A drinkable has the following properties:

- `ingredient`: A [Fluid Ingredient](../common-types/#fluid-ingredients), which defines which fluids this drinkable applies to.
- `consume_chance`: An optional number in the range [0, 1] (Default: `0`). The chance that, when drank from a source block, the source block is removed.
- `may_drink_when_full`: An optional boolean (Default: `false`). If true, the player can drink this even when their thirst bar is full.
- `hunger`: An optional integer (Default: `0`). The amount of hunger restored per 25 mB drank.
- `saturation`: An optional number (Default: `0`). The amount of saturation restored per 25 mB drank.
- `water`: An optional number (Default: `0`). The amount of thirst restored per 25 mB drank.
- `intoxication`: An optional integer (Default: `0`). The number of ticks the player will be intoxicated for, per 25 mB drank.
- `effects`: An optional array of potion effects that this drinkable can apply. Each entry must be an object with the following properties:
  - `effect`: A string, which is the registry ID of a potion effect (i.e. `minecraft:slowness`).
  - `duration`: An integer, the number of ticks this effect is applied for.
  - `amplifier`: An integer, the level of the potion effect applied.
  - `chance`: A number in the range [0, 1]. The chance that this effect will be applied per 25 mB drank.

#### Example

```jsonc
// Reference: data/tfc/tfc/drinkable/alcohol.json
{
  "ingredient": {
    "tag": "tfc:alcohols"
  },
  "water": 10,
  "intoxication": 4000
}
```

<hr>

## Fauna

Fauna allow datapacks to specify some spawning requirements for mobs. It is located under the subfolder `fauna`.

**Note:** Fauna cannot be added with datapacks, only modified.

Fauna have the following properties:

- `chance`: An optional integer (Default: `1`). The chance in 1/N chunks that something will spawn. Note that the ratio between mob spawns is better set in the [Biome](../worldgen/biomes/) json, as those values are baked into the spawn generator.
- `distance_below_sea_level`: An optional integer (Default: `-1`, disabled). The distance below sea level something must spawn. This should only be set for underwater creatures.
- `climate`: A [Climate Placement](../worldgen/placement-modifiers/#climate) configuration for the climate requirements of the fauna.
- `solid_ground`: An optional boolean (Default: `false`). Requires the mob to spawn on a `minecraft:valid_spawn` block tag.
- `max_brightness`: An optional integer (Default: `-1`, disabled). The maximum brightness a mob may spawn at.
- `months`: An optional list of months (Default: all months). The months during which this fauna can spawn. Valid values are: `january`, `february`, `march`, `april`, `may`, `june`, `july`, `august`, `september`, `october`, `november`, `december`.

#### Example

```jsonc
// Reference: data/tfc/tfc/fauna/orca.json
{
  "chance": 10,
  "distance_below_sea_level": 35,
  "climate": {
    "max_temperature": 19,
    "min_rainfall": 100
  }
}
```

<hr>

## Fertilizers

A fertilizer defines an item which can be used on farmland or crops to increase the nutrients in the soil (farmland). Nutrients are used and consumed by crops to increase their yield. It is located under the subfolder `fertilizer`. A fertilizer has the following properties:

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

## Fluid Heats

A fluid heat definition specifies the heat properties of a fluid, used for melting and alloying. It is a file located under the subfolder `fluid_heat`. It has the following properties:

- `fluid`: The registry name of the fluid this definition applies to.
- `melt_temperature`: A number. The melting temperature of this fluid in degrees Celsius.
- `specific_heat_capacity`: A number which specifies how fast this fluid heats up relative to others. This is measured in Energy / (mB × °C), meaning higher values will cause it to require more energy (time) to heat up.

**Note:** There must be a **unique** fluid heat definition for every fluid used in heating/melting. Creating multiple definitions that reference the same fluid is liable to cause undefined behavior.

#### Example

```jsonc
// Reference: data/tfc/tfc/fluid_heat/metal/bismuth_bronze.json
{
  "fluid": "tfc:metal/bismuth_bronze",
  "melt_temperature": 985,
  "specific_heat_capacity": 0.00857
}
```

<hr>

## Food Items

A food item definition defines a food, and applies TFC style stats to it including decay, hunger, water, and nutrition. It is a file located under the subfolder `food`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this food item definition applies to.
- `edible`: An optional boolean (Default: `true`). If false, the food cannot be eaten directly but still has food properties (used for ingredients).
- `hunger`: An optional integer (Default: `0`). Defines how much hunger this food restores. The player's full hunger bar is equal to `20`.
- `saturation`: An optional number (Default: `0`). Defines how much saturation this food restores. Measured in the same units as hunger.
- `water`: An optional number (Default: `0`). Defines how much water this food restores. The player's full water bar is equal to `100`.
- `decay_modifier`: An optional number (Default: `0`, which means no decay). Defines how quickly this item decays. Higher values indicate faster decay. Use `"infinity"` for items that never decay.
- `grain`: An optional number (Default: `0`). Defines how much <span style="color:#FFAA00">**Grain**</span> nutrient this food adds.
- `fruit`: An optional number (Default: `0`). Defines how much <span style="color:#55FF55">**Fruit**</span> nutrient this food adds.
- `vegetables`: An optional number (Default: `0`). Defines how much <span style="color:#00AA00">**Vegetables**</span> nutrient this food adds.
- `protein`: An optional number (Default: `0`). Defines how much <span style="color:#FF5555">**Protein**</span> nutrient this food adds.
- `dairy`: An optional number (Default: `0`). Defines how much <span style="color:#AA00AA">**Dairy**</span> nutrient this food adds.

**Note:** Typical values for nutrients are 0-2 for small items (fruits, vegetables), and 1-4 for larger items (breads, meats), and higher for meals. Note that nutrients should also scale with hunger: A 2 nutrient/4 hunger food is the same (nutritionally) as a 4 nutrient/8 hunger food.

#### Example

```jsonc
// Reference: data/tfc/tfc/food/apple.json
{
  "ingredient": {
    "item": "tfc:food/apple"
  },
  "hunger": 4,
  "saturation": 0,
  "water": 10,
  "decay_modifier": 3.5,
  "fruit": 0.75
}
```

<hr>

## Fuels

A fuel defines something that burns, and can be used in a fire pit, forge, or other TFC fuel consuming device. It is a file located under the subfolder `fuel`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this fuel applies to.
- `temperature`: A number. The temperature in degrees Celsius that this fuel burns at.
- `duration`: An integer. The duration in ticks that a single item of this fuel burns for.
- `purity`: An optional number (Default: `1.0`). A multiplier for the fuel's effectiveness in the bloomery.

#### Example

```jsonc
// Reference: data/tfc/tfc/fuel/coal.json
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

An item heat definition specifies if an item can be heated, and also properties of the heated item. It is a file located under the subfolder `item_heat`. It has the following properties:

- `ingredient`: An [Ingredient](../ingredients/) to which this item heat definition applies to.
- `heat_capacity`: A number which specifies how fast this item heats up relative to others. This is measured in Energy / °C, meaning higher values indicate it takes more energy (time) to heat up.
- `forging_temperature`: An optional number (Default: `0`). The temperature at which this item can be worked, in degrees Celsius. If `0`, this item will not require heat to work.
- `welding_temperature`: An optional number (Default: `0`). The temperature at which this item can be welded, in degrees Celsius. If `0`, this item will not require heat to weld.

#### Example

```jsonc
// Reference: data/tfc/tfc/item_heat/metal/bismuth_bronze_ingot.json
{
    "ingredient": {
        "tag": "c:ingots/bismuth_bronze"
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

 An Item Size Definition is a file located in under the subfolder `item_size`. It has the following properties:

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
// Reference: data/tfc/tfc/item_size/straw.json
{
    "ingredient": {
        "item": "tfc:straw"
    },
    "size": "small",
    "weight": "very_light"
}
```

<hr>

## Knapping Types

A knapping type specifies a new thing that can be knapped, and how it is knapped. Knapping types are specified as part of [Knapping Recipes](../recipes/#knapping)

Button textures for knapping screens are specified based on the registry name of the item. For example, `minecraft:leather` points to `tfc:textures/gui/knapping/leather`. Note that it is only the path of the item that gets used, and that it always points to the `tfc` namespace to avoid mod conflicts. For a disabled texture, add `_disabled` to the path.

It has the following properties:

- `input`: A [Sized Ingredient](../ingredients/#sized) for what item has to be knapped. These items typically are tagged (for example, `tfc:leather_knapping` for leathers that can be knapped).
- `amount_to_consume`: An Integer. The amount of the item that gets used by the recipe.
- `click_sound`: A registered sound that plays when the knapping occurs.
- `consume_after_complete`: A boolean. If the `amount_to_consume` of your `input` should be consumed as soon as you click one square or when the item is removed from the result slot.
- `has_off_texture`: A boolean. If true, a clicked slot will show a different texture rather than nothing at all.
- `spawns_particles`: A boolean. If true, the screen will spawn small 'particles' when clicking the buttons.
- `icon`: An [Item Stack](../common-types/#item-stacks) that is shown in the automatically generated JEI/EMI category for this knapping type.

#### Example

```jsonc
// Reference: data/tfc/tfc/knapping_types/rock.json
{
  "amount_to_consume": 1,
  "click_sound": "tfc:item.knapping.stone",
  "consume_after_complete": false,
  "has_off_texture": false,
  "icon": {
    "count": 1,
    "id": "tfc:rock/loose/granite"
  },
  "input": {
    "count": 2,
    "tag": "tfc:rock_knapping"
  },
  "spawns_particles": true
}
```

<hr>

## Lamp Fuels

A lamp fuel is a fluid which an be used in a lamp. It will burn over time, consuming mB per tick in order to keep the lamp lit. It has the following properties:

- `fluid`: A [Fluid Ingredient](../common-types/#fluid-ingredients) which determines which fluids this lamp fuel applies to.
- `lamps`: A [Block Ingredient](../common-types/#block-ingredients) which determines what (lamp) blocks are valid for this fuel to be added to.
- `burn_rate` An integer, representing how fast this lamp consumes fuel, in ticks per mB. A burn rate of -1 indicates that it burns forever.

#### Example

```jsonc
// Reference: data/tfc/tfc/lamp_fuel/olive_oil.json
{
  "burn_rate": 8000,
  "fluid": {
    "fluid": "tfc:olive_oil"
  },
  "lamps": "#tfc:lamps"
}
```

<hr>

## Supports

Supports define blocks which prevent collapses from **starting** within a specific radius. They do not prevent collapses that started outside the support radius from causing blocks to collapse within the supported area. A support is a file located under the subfolder `supports`. It has the following properties:

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

<hr>

<!--linky_end_sort_categories-->
