from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from PIL.ImageFont import FreeTypeFont


SCRIPT_DIR: Path = Path(__file__).parent.resolve()
PROJECT_ROOT: Path = SCRIPT_DIR.parent

RGBA = tuple[int, int, int, int]
Position = tuple[int, int]
PieceSettings = dict[str, Any]

BASE_SETTINGS_SMALL_SENTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_small_sente.png",
    "font_size": 650,
    "text_pos": (420, 260),
}

BASE_SETTINGS_SMALL_GOTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_small_gote.png",
    "font_size": 650,
    "text_pos": (420, 260),
}

BASE_SETTINGS_MEDIUM_SENTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_medium_sente.png",
    "font_size": 680,
    "text_pos": (400, 240),
}

BASE_SETTINGS_MEDIUM_GOTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_medium_gote.png",
    "font_size": 680,
    "text_pos": (400, 240),
}

BASE_SETTINGS_LARGE_SENTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_large_sente.png",
    "font_size": 720,
    "text_pos": (390, 160),
}

BASE_SETTINGS_LARGE_GOTE: dict[str, str | int | Position] = {
    "base_image": "resources/wood_piece_large_gote.png",
    "font_size": 720,
    "text_pos": (390, 160),
}

FONT_PATH: Path = PROJECT_ROOT / "fonts" / "YujiMai-Regular.ttf"
OUTPUT_DIR: Path = PROJECT_ROOT / "build"

ENGRAVE_FILL_COLOR: RGBA = (40, 25, 15, 255)
PROMOTED_FILL_COLOR: RGBA = (200, 30, 30, 255)

SHADOW_OFFSET: Position = (2, 2)
SHADOW_COLOR: RGBA = (0, 0, 0, 255)
SHADOW_BLUR: int = 2

HIGHLIGHT_OFFSET: Position = (-1, -1)
HIGHLIGHT_COLOR: RGBA = (0, 0, 0, 255)
HIGHLIGHT_BLUR: int = 1

SETTINGS = {
    "pawn_sente": {
        **BASE_SETTINGS_SMALL_SENTE,
        "kanji": "歩",
        "promoted": False,
        "rotated": False,
    },
    "pawn_gote": {
        **BASE_SETTINGS_SMALL_GOTE,
        "kanji": "歩",
        "promoted": False,
        "rotated": True,
    },
    "pawn_promoted_sente": {
        **BASE_SETTINGS_SMALL_SENTE,
        "kanji": "と",
        "promoted": True,
        "rotated": False,
    },
    "pawn_promoted_gote": {
        **BASE_SETTINGS_SMALL_GOTE,
        "kanji": "と",
        "promoted": True,
        "rotated": True,
    },
    "lance_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "香",
        "promoted": False,
        "rotated": False,
    },
    "lance_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "香",
        "promoted": False,
        "rotated": True,
    },
    "lance_promoted_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "仝",
        "promoted": True,
        "rotated": False,
    },
    "lance_promoted_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "仝",
        "promoted": True,
        "rotated": True,
    },
    "knight_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "桂",
        "promoted": False,
        "rotated": False,
    },
    "knight_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "桂",
        "promoted": False,
        "rotated": True,
    },
    "knight_promoted_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "今",
        "promoted": True,
        "rotated": False,
    },
    "knight_promoted_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "今",
        "promoted": True,
        "rotated": True,
    },
    "silver_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "銀",
        "promoted": False,
        "rotated": False,
    },
    "silver_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "銀",
        "promoted": False,
        "rotated": True,
    },
    "silver_promoted_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "全",
        "promoted": True,
        "rotated": False,
    },
    "silver_promoted_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "全",
        "promoted": True,
        "rotated": True,
    },
    "gold_sente": {
        **BASE_SETTINGS_MEDIUM_SENTE,
        "kanji": "金",
        "promoted": False,
        "rotated": False,
    },
    "gold_gote": {
        **BASE_SETTINGS_MEDIUM_GOTE,
        "kanji": "金",
        "promoted": False,
        "rotated": True,
    },
    "bishop_sente": {
        **BASE_SETTINGS_LARGE_SENTE,
        "kanji": "角",
        "promoted": False,
        "rotated": False,
    },
    "bishop_gote": {
        **BASE_SETTINGS_LARGE_GOTE,
        "kanji": "角",
        "promoted": False,
        "rotated": True,
    },
    "bishop_promoted_sente": {
        **BASE_SETTINGS_LARGE_SENTE,
        "kanji": "馬",
        "promoted": True,
        "rotated": False,
    },
    "bishop_promoted_gote": {
        **BASE_SETTINGS_LARGE_GOTE,
        "kanji": "馬",
        "promoted": True,
        "rotated": True,
    },
    "rook_sente": {
        **BASE_SETTINGS_LARGE_SENTE,
        "kanji": "飛",
        "promoted": False,
        "rotated": False,
    },
    "rook_gote": {
        **BASE_SETTINGS_LARGE_GOTE,
        "kanji": "飛",
        "promoted": False,
        "rotated": True,
    },
    "rook_promoted_sente": {
        **BASE_SETTINGS_LARGE_SENTE,
        "kanji": "竜",
        "promoted": True,
        "rotated": False,
    },
    "rook_promoted_gote": {
        **BASE_SETTINGS_LARGE_GOTE,
        "kanji": "竜",
        "promoted": True,
        "rotated": True,
    },
    "king_sente": {
        **BASE_SETTINGS_LARGE_SENTE,
        "kanji": "王",
        "promoted": False,
        "rotated": False,
    },
    "king_gote": {
        **BASE_SETTINGS_LARGE_GOTE,
        "kanji": "玉",
        "promoted": False,
        "rotated": True,
    },
}


def resolve_path(relative_path: str) -> Path:
    """Resolve a relative path against the project root."""
    return PROJECT_ROOT / relative_path


def load_base_image(path: str) -> Image.Image | None:
    """Load and convert a base image to RGBA format."""
    try:
        return Image.open(resolve_path(path)).convert("RGBA")
    except (FileNotFoundError, IOError):
        print(f"  Error: Cannot load image '{path}'. Skipping.")
        return None


def load_font(path: Path, size: int) -> FreeTypeFont | None:
    """Load a TrueType font at the specified size."""
    try:
        return ImageFont.truetype(str(path), size)
    except IOError:
        print(f"  Error: Cannot load font '{path}'. Skipping.")
        return None


def get_fill_color(promoted: bool) -> RGBA:
    """Return the appropriate fill color based on promotion status."""
    return PROMOTED_FILL_COLOR if promoted else ENGRAVE_FILL_COLOR


def create_text_mask(
    size: tuple[int, int], text: str, position: Position, font: FreeTypeFont
) -> Image.Image:
    """Create a grayscale mask with the kanji text."""
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.text(position, text, font=font, fill=255)
    return mask


def create_blurred_mask(
    size: tuple[int, int],
    text: str,
    position: Position,
    font: FreeTypeFont,
    blur_radius: int,
) -> Image.Image:
    """Create a blurred grayscale mask for shadow/highlight effects."""
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.text(position, text, font=font, fill=255)
    return mask.filter(ImageFilter.GaussianBlur(blur_radius))


def composite_engraved_text(
    base: Image.Image,
    text: str,
    position: Position,
    font: FreeTypeFont,
    fill_color: RGBA,
) -> Image.Image:
    """Composite shadow, fill, and highlight layers onto the base image."""
    size = base.size
    output = base.copy()

    shadow_pos = (position[0] + SHADOW_OFFSET[0], position[1] + SHADOW_OFFSET[1])
    highlight_pos = (
        position[0] + HIGHLIGHT_OFFSET[0],
        position[1] + HIGHLIGHT_OFFSET[1],
    )

    text_mask = create_text_mask(size, text, position, font)
    shadow_mask = create_blurred_mask(size, text, shadow_pos, font, SHADOW_BLUR)
    highlight_mask = create_blurred_mask(
        size, text, highlight_pos, font, HIGHLIGHT_BLUR
    )

    shadow_layer = Image.new("RGBA", size, SHADOW_COLOR)
    fill_layer = Image.new("RGBA", size, fill_color)
    highlight_layer = Image.new("RGBA", size, HIGHLIGHT_COLOR)

    output = Image.alpha_composite(output, Image.new("RGBA", size, (0, 0, 0, 0)))
    output.paste(shadow_layer, (0, 0), mask=shadow_mask)
    output.paste(fill_layer, (0, 0), mask=text_mask)
    output.paste(highlight_layer, (0, 0), mask=highlight_mask)

    return output


def generate_piece(name: str, params: PieceSettings) -> bool:
    """Generate a single shogi piece image and save it to the output directory."""
    print(f"--- Processing: {name} ---")

    base_image = load_base_image(params["base_image"])
    if base_image is None:
        return False

    font = load_font(FONT_PATH, params["font_size"])
    if font is None:
        return False

    fill_color = get_fill_color(params["promoted"])
    print(
        f"  Using {'Promoted (Red)' if params['promoted'] else 'Standard (Brown)'} color"
    )
    print(
        f"  Drawing '{params['kanji']}' (size {params['font_size']}) at {params['text_pos']}"
    )

    output_image = composite_engraved_text(
        base_image, params["kanji"], params["text_pos"], font, fill_color
    )

    if params["rotated"]:
        print("  Rotating final image 180°")
        output_image = output_image.rotate(180)

    output_path = OUTPUT_DIR / f"{name}.png"
    output_image.save(output_path)
    print(f"  Success! Saved to '{output_path}'")
    return True


def ensure_output_directory() -> None:
    """Create the output directory if it doesn't exist."""
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
        print(f"Created output directory: '{OUTPUT_DIR}'")


def main() -> None:
    """Generate all shogi piece images defined in SETTINGS."""
    print("Starting shogi piece generator...")
    ensure_output_directory()

    for piece_name, params in SETTINGS.items():
        generate_piece(piece_name, params)

    print(f"\n--- All pieces generated successfully in '{OUTPUT_DIR}'! ---")


if __name__ == "__main__":
    main()
