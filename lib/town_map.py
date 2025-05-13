from lib.tile_map import TileMap

class TownMap(TileMap):
    def __init__(self, tilesets, tile_size, map_layout):
        super().__init__(tilesets, tile_size)
        self.map_layout = map_layout

    def draw(self, surface):
        for row_index, row in enumerate(self.map_layout):
            for col_index, (tileset_name, tile_index) in enumerate(row):
                tile = self.get_tiles(tileset_name, tile_index)
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                surface.blit(tile, (x,y))