from pathlib import Path

from pyxelate import Pyx
from skimage import io
import tqdm

if __name__ == "__main__":
    factor = 2
    palette = 8
    dither = "none"
    
    src_path = "./avatars/female_original"
    dst_path = f"{src_path}_x{factor}"
    
    Path(dst_path).mkdir(exist_ok=True)
    all_image_paths = list(Path(src_path).glob("*.png"))
    
    for file_path in tqdm.tqdm(all_image_paths):
        image = io.imread(str(file_path))
        
        pixelate = Pyx(factor=factor, palette=palette, dither=dither)
        image_pix = pixelate.fit_transform(image)
        
        save_path = Path(dst_path) / file_path.name
        io.imsave(str(save_path), image_pix)
        