pub mod frontmatter;
pub mod markdown;

use crate::error::Result;
use crate::content_loader::frontmatter::{split, Fragment};
use std::fs;
use std::path::Path;

/// Loads every `*.md` file in `section_dir`, splits front-matter,
/// and returns them ordered by filename (which is how the authoring
/// convention `01-`, `02-`, `03-` enforces order).
pub fn load_section(section_dir: &Path) -> Result<Vec<Fragment>> {
    if !section_dir.exists() {
        return Ok(vec![]);
    }
    let mut entries: Vec<_> = fs::read_dir(section_dir)?
        .filter_map(|e| e.ok())
        .filter(|e| {
            e.path()
                .extension()
                .and_then(|s| s.to_str())
                .map_or(false, |ext| ext.eq_ignore_ascii_case("md"))
        })
        .collect();
    entries.sort_by_key(|e| e.file_name());

    let mut out = Vec::new();
    for entry in entries {
        let src = fs::read_to_string(entry.path())?;
        out.push(split(&src)?);
    }
    Ok(out)
}
