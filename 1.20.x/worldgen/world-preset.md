---
layout: page
title: "World Preset"
permalink: /1.20.x/worldgen/world-preset/
---

# World Presets

TFC adds a single world preset, which is used to generate a TFC world, and along with that, adds the TFC generator which has a number of important configuration options available. For the generic format of a world preset, see the [Minecraft Wiki](https://minecraft.wiki/w/World_preset_definition), or the [Example](https://github.com/TerraFirmaCraft/TerraFirmaCraft/blob/1.20.x/src/main/resources/data/tfc/worldgen/world_preset/overworld.json). This page is concerned with the `generator` field of the world preset.

The TFC world generator has the following fields:

- `type` must be `"tfc:overworld"`
- `biome_source` must be `{ "type": "tfc:overworld" }`
- `settings` is the name of a [Noise Settings](https://minecraft.wiki/w/Noise_settings) to use. The default is `"minecraft:overworld"`
- `tfc_settings` is an object with various settings that affect TFC world generation. It has the following fields:
  - `flat_bedrock` (Boolean): If the bottom of the world is a single layer of flat bedrock, or random like vanilla
  - `spawn_center_x` (Integer): The center X position around which the spawn position is chosen
  - `spawn_center_z` (Integer): The center Z position around which the spawn position is chosen
  - `spawn_distance` (Integer): The maximum distance from the spawn center the spawn position will be chosen
  - `temperature_scale` (Integer): The distance between two temperature extremes, in blocks. If zero, the temperature will be a constant based on `temperature_constant`
  - `temperature_constant` (Optional Number, Default `0`). A number representing the temperature for an entire world, where `-1.0` is polar and `1.0` is tropical.
  - `rainfall_scale` (Integer): The distance between two rainfall extremes, in blocks. If zero, the rainfall will be a constant based on `rainfall_constant`
  - `rainfall_constant` (Optional Number, Default `0`): A number representing the rainfall for an entire world, where `-1.0` is arid and `1.0` is tropical.
  - `rock_layer_settings` is the [Rock Layer Settings](#rock-layer-settings) for a world.
  - `continentalness` (Number): This is a value between `-1.0` and `1.0` which determines the nature of continents. Smaller values create smaller continents, more islands, whereas larger values create larger, blobbier continents.
  - `grassDensity` (Optional Number, Default `0.5`): This is a number which affects how much grass generates in the world. Higher values indicate more grass coverage. 

### Rock Layer Settings

This describes the rocks that exist in the world, what blocks they use, and how they spawn. It is useful to understand how rock layers generate in TFC:

First, TFC picks the overall **Layer Type** of the area. This may be one of `ocean_floor` (Oceans), `volcanic` (Volcanic islands, and volcanic mountains), `uplift` (Inland mountains), or `land` (All other non-ocean areas). It then looks in the rock layer settings for what [Layer](#rock-layer) correspond to that **Layer Type**.

#### Rock Layer

A **Layer** consists of an object, with two fields:

- `id` (String) The name or ID of the layer
- `layers` (Object) A map of **Rock** IDs to **Layer** IDs

##### Example

```jsonc
// A single "Layer", named "igneous_extrusive", with four rocks (rhyolite, andesite, dacite, and basalt),
// mapped to three layers (felsic, intermediate, and mafic)
{
  "id": "igneous_extrusive",
  "layers": {
    "rhyolite": "felsic",
    "andesite": "intermediate",
    "dacite": "intermediate",
    "basalt": "mafic"
  }
}
```

#### Rock

A **Rock** is a collection of mappings of a name to the resulting blocks that are used for that rock. It can be either, a preset name (these are registered by TFC for ease of use), or an object with the following fields:

- `raw`, `hardened`, `gravel`, `cobble`, `sand`, `sandstone` (String) These are names of blocks that are used for this rock in the respective places in world generation
- `spike`, `mossy`, `mossy_loose` (Optional String) These are names of blocks that are used for this rock in the respective places in world generation, but are optional, and won't generate if not present.

##### Example

```jsonc
// An example "Rock" using default TFC blocks
{
  "raw": "tfc:rock/raw/basalt",
  "hardened": "tfc:rock/hardened/basalt",
  "gravel": "tfc:rock/gravel/basalt",
  "cobble": "tfc:rock/cobble/basalt",
  "sand": "tfc:sand/red",
  "sandstone": "tfc:raw_sandstone/red",
}
```

When considering a layer, TFC will pick a random **Rock** from that layer, and then move onto the following **Layer**, before repeating the process. For example here, TFC could place `basalt`, and then under the basalt, would be a rock from the `mafic` layer.

There is a special **Layer** named `bottom` - This is a layer consisting only of a list of **Rocks**. Once the `bottom` layer is reached, any further rocks underneath it will repeat endlessly from the `bottom` layer (until there are no more Y positions left to generate).

With all that in mind, a **Rock Layer Settings** has the following fields:

- `rocks` is an object which is a map of **Rock** IDs, to [Rock](#rock) objects, or preset names.
- `bottom` is a list of **Rock** IDs, which form the `bottom` layer
- `layers` is a list of all the [Layers](#rock-layer) which exist
- `ocean_floor`, `volcanic`, `uplift`, and `land` are each the default **Layer Types**. They are each a list of the **Layer** IDs which are used for the top rock of each type.

##### Example

```jsonc
// This is the default rock layer settings used by TFC, found at
// data/tfc/worldgen/world_preset/overworld.json
{
  "rocks": {
    "granite": "tfc:granite",
    "diorite": "tfc:diorite",
    "gabbro": "tfc:gabbro",
    "shale": "tfc:shale",
    "claystone": "tfc:claystone",
    "limestone": "tfc:limestone",
    "conglomerate": "tfc:conglomerate",
    "dolomite": "tfc:dolomite",
    "chert": "tfc:chert",
    "chalk": "tfc:chalk",
    "rhyolite": "tfc:rhyolite",
    "basalt": "tfc:basalt",
    "andesite": "tfc:andesite",
    "dacite": "tfc:dacite",
    "quartzite": "tfc:quartzite",
    "slate": "tfc:slate",
    "phyllite": "tfc:phyllite",
    "schist": "tfc:schist",
    "gneiss": "tfc:gneiss",
    "marble": "tfc:marble"
  },
  "bottom": [
    "gneiss",
    "schist",
    "diorite",
    "granite",
    "gabbro"
  ],
  "layers": [{
    "id": "felsic",
    "layers": {
      "granite": "bottom"
    }
  }, {
    "id": "intermediate",
    "layers": {
      "diorite": "bottom"
    }
  }, {
    "id": "mafic",
    "layers": {
      "gabbro": "bottom"
    }
  }, {
    "id": "igneous_extrusive",
    "layers": {
      "rhyolite": "felsic",
      "andesite": "intermediate",
      "dacite": "intermediate",
      "basalt": "mafic"
    }
  }, {
    "id": "igneous_extrusive_x2",
    "layers": {
      "rhyolite": "igneous_extrusive",
      "andesite": "igneous_extrusive",
      "dacite": "igneous_extrusive",
      "basalt": "igneous_extrusive"
    }
  }, {
    "id": "phyllite",
    "layers": {
      "phyllite": "bottom",
      "gneiss": "bottom",
      "schist": "bottom"
    }
  }, {
    "id": "slate",
    "layers": {
      "slate": "bottom",
      "phyllite": "phyllite"
    }
  }, {
    "id": "marble",
    "layers": {
      "marble": "bottom"
    }
  }, {
    "id": "quartzite",
    "layers": {
      "quartzite": "bottom"
    }
  }, {
    "id": "sedimentary",
    "layers": {
      "shale": "slate",
      "claystone": "slate",
      "conglomerate": "slate",
      "limestone": "marble",
      "dolomite": "marble",
      "chalk": "marble",
      "chert": "quartzite"
    }
  }, {
    "id": "uplift",
    "layers": {
      "slate": "phyllite",
      "marble": "bottom",
      "quartzite": "bottom",
      "diorite": "sedimentary",
      "granite": "sedimentary",
      "gabbro": "sedimentary"
    }
  }],
  "ocean_floor": [
    "igneous_extrusive"
  ],
  "volcanic": [
    "igneous_extrusive",
    "igneous_extrusive_x2"
  ],
  "land": [
    "igneous_extrusive",
    "sedimentary"
  ],
  "uplift": [
    "sedimentary",
    "uplift"
  ]
}
```
