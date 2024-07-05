---
layout: page
title: "WorldGen Tags"
permalink: /1.18.x/worldgen/tags/
excluded_in_search: true
---

This page details all the world generation tags TFC adds. For generic tags, see [Tags](../../data/tags/).

## Biome Tags

Tag Id | Function
---|---
`tfc:is_lake` | All lake biomes, including underground lakes.
`tfc:is_river` | All river biomes, including underground rivers.
`tfc:is_volcanic` | All volcanic biomes.

## Configured Feature Tags

Tag Id | Function
---|---
`tfc:forest_trees` | A list of all tree entries which are used by the `tfc:forest` feature. These features are not generated directly, rather their configurations are used by the forest feature to determine what trees to actually place.

## Placed Feature Tags

Tag Id | Function
---|---
`tfc:feature/berry_bushes` | All berry bush patch features.
`tfc:feature/boulders` | All boulder features.
`tfc:feature/clay_indicators` | All clay indicator plant features.
`tfc:feature/corals` | All coral features.
`tfc:feature/crops` | All crop patch features.
`tfc:feature/forest_plants` | All plants that are placed within biomes that support forests.
`tfc:feature/fruit_trees` | All fruit tree features.
`tfc:feature/icebergs` | All iceberg features.
`tfc:feature/land_plants` | All plants that are placed within biomes that support any type of land.
`tfc:feature/ocean_decorations` | All features that are ocean specific decoration.
`tfc:feature/ocean_plants` | All plant features that are ocean specific.
`tfc:feature/ore_deposits` | All ore deposits - the smaller gravel ores that are found in rivers and lakes.
`tfc:feature/shore_decorations` | All features that are shore specific decoration.
`tfc:feature/soil_discs` | All standard soil discs, including clay, peat, and powder snow.
`tfc:feature/surface_grasses` | A tag used by the `tfc:surface_grass` feature to select one or two grasses to generate in a given area.
`tfc:feature/volcanoes` | All features generated in volcanic biomes.
`tfc:in_biome/all_lakes` | All lake features, including those in `tfc:in_biome/underground_lakes`.
`tfc:in_biome/erosion` | A tag which just contains the `tfc:erosion` feature.
`tfc:in_biome/strongholds` | Empty.
`tfc:in_biome/surface_structures` | Empty.
`tfc:in_biome/top_layer_modification` | Features placed in the top layer modification step.
`tfc:in_biome/underground_decoration` | Features placed in the underground decoration step.
`tfc:in_biome/underground_lakes` | Only underground lake features.
`tfc:in_biome/underground_structures` | Features placed in the underground structures step.
`tfc:in_biome/veins` | Features placed in the ore veins step.
`tfc:in_biome/large_features/<biome>` | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the large features step.
`tfc:in_biome/soil_discs/<biome>` | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the soil discs step.
`tfc:in_biome/surface_decoration/<biome>` | Where `<biome>` is the registry name of a TFC biome, the features placed in that biome in the surface decoration step.
