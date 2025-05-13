import pygame

class TileMap:
    def __init__(self, tilesets, tile_size):
        self.tilesets = {}
        self.tile_size = tile_size
        for name, path in tilesets.items():
            self.tilesets[name] = self.extract_tiles(path)

    def extract_tiles(self, path):
        tile_sheet = pygame.image.load(path).convert_alpha()
        sheet_width, sheet_height = tile_sheet.get_size()

        print(f"Sheet Size: {sheet_width}x{sheet_height}")
        print(f"Tile Size: {self.tile_size}x{self.tile_size}")

        tiles = []
        for y in range(0, sheet_height, self.tile_size):
            for x in range(0, sheet_width, self.tile_size):
                tile_rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
                tile = tile_sheet.subsurface(tile_rect)
                tiles.append(tile)
        return tiles
    
    def get_tiles(self, tileset_name, index):
        return self.tilesets[tileset_name][index]
    