---
layout: page
title: "Biomes"
permalink: /1.18.x/worldgen/biomes/
---

# Biomes

In TerraFirmaCraft, biomes determine the overall shape of the land, and the features that are generated. They **do not** determine the temperature, rainfall, or other climate related features. All of TFC's biomes, and their world generation JSON can be found [here](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.18.x/src/main/resources/data/tfc/worldgen/biome).

- Low Altitude Continental Biomes:
  - `tfc:plains`, `tfc:hills`, `tfc:lowlands`, `tfc:low_canyons`
- Mid Altitude Continental Biomes:
  - `tfc:rolling_hills`, `tfc:badlands`, `tfc:plateau`, `tfc:canyons`.
- High Altitude Continental Biomes:
  - `tfc:mountains`, `tfc:old_mountains`, `tfc:oceanic_mountains`, `tfc:volcanic_mountains`, `tfc:volcanic_oceanic_mountains`.
- Oceanic Biomes:
  - `tfc:ocean`, `tfc:ocean_reef`, `tfc:deep_ocean`, `tfc:deep_ocean_trench`
- Technical / Decoration Biomes:
  - `tfc:shore`
  - `tfc:lake`, `tfc:plateau_lake`, `tfc:mountain_lake`, `tfc:old_mountain_lake`, `tfc:oceanic_mountain_lake`, `tfc:volcanic_mountain_lake`, `tfc:volcanic_oceanic_mountain_lake`.
  - `tfc:river`, `tfc:mountain_river`, `tfc:old_mountain_river`, `tfc:volcanic_mountain_river`, `tfc:oceanic_mountain_river`, `tfc:volcanic_oceanic_mountain_river`.


### Tags

All of TFC's biomes use [Placed Feature Tags](../tags/#placed-features) in order to determine what features generate in a given stage. This means it is possible for addons or datapacks to add, remove, or modify specific features by editing these tags, without having to overwrite every single biome. Each TFC biome uses the following tags, where `<biome>` is replaced with the name of the biome in question:

- `tfc:in_biome/erosion`,
- `tfc:in_biome/underground_lakes` or `tfc:in_biome/all_lakes` depending on the biome,
- `tfc:in_biome/soil_discs/<biome>`,
- `tfc:in_biome/underground_structures`,
- `tfc:in_biome/surface_structures`,
- `tfc:in_biome/strongholds`,
- `tfc:in_biome/veins`,
- `tfc:in_biome/underground_decoration`,
- `tfc:in_biome/large_features/<biome>`,
- `tfc:in_biome/surface_decoration/<biome>`,
- `tfc:in_biome/top_layer_modification`

As you can see, apart from three steps, the biome tags used by TFC refer to the same features in every biome.

**Note:** For addon developers, these **do not support `BiomeLoadingEvent` in Forge!**.

### Properties

TFC ignores several properties of biomes in favor of other methods. TFC redirects vanilla methods to call TFC-enhanced methods for functions such as temperature, rainfall, or sky color. These will only apply to biomes which have extensions registered (aka, TFC recognizes them). In these cases, other mods may still use these properties but within TFC and vanilla they will be ignored.

- `temperature`, `temperature_modifier`, and `downfall` and `precipitation` are ignored in the default TFC overworld, or dimensions with custom TFC climate support. All TFC biomes should have `precipitation` set to `rain` or local weather might not work correctly.
- In `effects`, `fog_color`, `sky_color`, `water_color`, and `water_color` are ignored. They are instead queried based off a color map texture file (In `tfc:textures/colormap/*.png`), based off of the actual rainfall and temperature of an area.

### Using Non-TFC Biomes in TFC

In order to use non-TFC biomes in TFC, there are a couple requirements:

- In order to use non-TFC biomes with a TFC biome source, the biomes must have a `BiomeExtension` registered. This object is responsible for integrating with the chunk generator, and includes noise generation and noise blending groups.
- If you want TFC biomes to be *generated* by the TFC biome source, this will very likely require custom hooks based on the sophistication of injections into the biome layer generation. Please consult us on discord with the nature of what you are attempting.
