---
layout: page
title: "Biomes"
permalink: /1.21.x/worldgen/biomes/
---

# Biomes

In TerraFirmaCraft, biomes determine the overall shape of the land, and the features that are generated. They **do not** determine the temperature, rainfall, or other climate related features. All of TFC's biomes, and their world generation JSON can be found [here](https://github.com/TerraFirmaCraft/TerraFirmaCraft/tree/1.21.x/src/main/resources/data/tfc/worldgen/biome).

- Aquatic Biomes:
  - `tfc:ocean`, `tfc:ocean_reef`, `tfc:deep_ocean`, `tfc:deep_ocean_trench`
- Low Altitude Continental Biomes:
  - `tfc:plains`, `tfc:hills`, `tfc:lowlands`, `tfc:salt_marsh`, `tfc:low_canyons`
- Mid Altitude Continental Biomes:
  - `tfc:rolling_hills`, `tfc:highlands`, `tfc:badlands`, `tfc:plateau`, `tfc:plateau_wide`, `tfc:canyons`
- High Altitude Continental Biomes:
  - `tfc:mountains`, `tfc:old_mountains`, `tfc:oceanic_mountains`, `tfc:volcanic_mountains`, `tfc:volcanic_oceanic_mountains`
- Island Biomes:
  - `tfc:guano_island`
- Shore Biomes:
  - `tfc:shore`, `tfc:tidal_flats`, `tfc:sea_stacks`, `tfc:terrace_upper`, `tfc:terrace_lower`, `tfc:setback_cliffs`, `tfc:coastal_dunes`, `tfc:rocky_shores`, `tfc:embayments`
- Water Biomes:
  - `tfc:lake`, `tfc:river`
- Lake Biomes:
  - `tfc:mountain_lake`, `tfc:old_mountain_lake`, `tfc:oceanic_mountain_lake`, `tfc:volcanic_mountain_lake`, `tfc:volcanic_oceanic_mountain_lake`, `tfc:plateau_lake`
- Dry Biomes:
  - `tfc:mud_flats`, `tfc:salt_flats`, `tfc:dune_sea`, `tfc:grassy_dunes`, `tfc:whorled_canyons`, `tfc:stair_step_canyons`, `tfc:mesas`, `tfc:buttes`, `tfc:hoodoos`, `tfc:rocky_plateau`
- Tower Karst Biomes:
  - `tfc:tower_karst_plains`, `tfc:tower_karst_canyons`, `tfc:tower_karst_hills`, `tfc:tower_karst_highlands`, `tfc:tower_karst_lake`, `tfc:tower_karst_bay`
- Karren Karst Biomes:
  - `tfc:burren_plateau`, `tfc:burren_badlands`, `tfc:burren_badlands_tall`, `tfc:burren_plains`, `tfc:burren_roche_moutonee`
- Shilin (Stone Forest) Biomes:
  - `tfc:shilin_plains`, `tfc:shilin_canyons`, `tfc:shilin_hills`, `tfc:shilin_highlands`, `tfc:shilin_plateau`
- Doline Karst Biomes:
  - `tfc:doline_plains`, `tfc:doline_hills`, `tfc:doline_rolling_hills`, `tfc:doline_highlands`, `tfc:doline_plateau`, `tfc:doline_canyons`
- Cenote Biomes:
  - `tfc:cenote_plains`, `tfc:cenote_hills`, `tfc:cenote_rolling_hills`, `tfc:cenote_canyons`, `tfc:cenote_highlands`, `tfc:cenote_plateau`
- Extreme Doline Biomes:
  - `tfc:extreme_doline_plateau`, `tfc:extreme_doline_mountains`
- Shield Volcano Biomes:
  - `tfc:active_shield_volcano`, `tfc:dormant_shield_volcano`, `tfc:extinct_shield_volcano`, `tfc:ancient_shield_volcano`, `tfc:sunken_shield_volcano`, `tfc:shield_volcano_shore`, `tfc:old_shield_volcano_shore`
- Ice Sheet Biomes:
  - `tfc:ice_sheet`, `tfc:ice_sheet_mountains`, `tfc:ice_sheet_oceanic_mountains`, `tfc:ice_sheet_shield_volcano`, `tfc:ice_sheet_tuyas`, `tfc:subglacial_lake`
- Ice Sheet Edge Biomes:
  - `tfc:ice_sheet_edge`, `tfc:ice_sheet_tuyas_edge`, `tfc:ice_sheet_mountains_edge`, `tfc:ice_sheet_oceanic_mountains_edge`, `tfc:meltwater_lake`, `tfc:ice_sheet_oceanic`, `tfc:ice_sheet_shore`
- Glaciated Biomes:
  - `tfc:glaciated_mountains`, `tfc:glaciated_oceanic_mountains`, `tfc:glaciated_shield_volcano`
- Glacially Carved Biomes:
  - `tfc:glacially_carved_mountains`, `tfc:glacially_carved_oceanic_mountains`
- Paleoglacial Biomes:
  - `tfc:drumlins`, `tfc:tuyas`, `tfc:knob_and_kettle`, `tfc:patterned_ground`, `tfc:inverted_patterned_ground`, `tfc:stone_circles`


### Tags

All of TFC's biomes use [Placed Feature Tags](../tags/#placed-feature-tags) in order to determine what features generate in a given stage. This means it is possible for addons or datapacks to add, remove, or modify specific features by editing these tags, without having to overwrite every single biome. Each TFC biome uses the following tags, where `<biome>` is replaced with the name of the biome in question:

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

### Properties

TFC ignores several properties of biomes in favor of other methods. TFC redirects vanilla methods to call TFC-enhanced methods for functions such as temperature, rainfall, or sky color. These will only apply to biomes which have extensions registered (aka, TFC recognizes them). In these cases, other mods may still use these properties but within TFC and vanilla they will be ignored.

- `temperature`, `temperature_modifier`, and `downfall` and `precipitation` are ignored in the default TFC overworld, or dimensions with custom TFC climate support. All TFC biomes should have `precipitation` set to `rain` or local weather might not work correctly.
- In `effects`, `fog_color`, `sky_color`, `water_color`, and `water_color` are ignored. They are instead queried based off a color map texture file (In `tfc:textures/colormap/*.png`), based off of the actual rainfall and temperature of an area.

### Using Non-TFC Biomes in TFC

In order to use non-TFC biomes in TFC, there are a couple requirements:

- In order to use non-TFC biomes with a TFC biome source, the biomes must have a `BiomeExtension` registered. This object is responsible for integrating with the chunk generator, and includes noise generation and noise blending groups.
- If you want TFC biomes to be *generated* by the TFC biome source, this will very likely require custom hooks based on the sophistication of injections into the biome layer generation. Please consult us on Discord with the nature of what you are attempting.
