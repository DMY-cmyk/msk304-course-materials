use crate::error::Result;
use std::fs;
use std::path::Path;

pub fn copy_css(asset_src: &Path, out_assets: &Path) -> Result<()> {
    fs::create_dir_all(out_assets)?;
    for name in ["screen.css", "print.css"] {
        let src = asset_src.join(name);
        let dst = out_assets.join(name);
        fs::copy(&src, &dst)?;
    }
    Ok(())
}
