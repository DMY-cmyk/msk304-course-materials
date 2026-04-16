use crate::error::{BuildError, Result};
use serde_yaml::Value;

#[derive(Debug)]
pub struct Fragment {
    pub meta: Value,
    pub body: String,
}

pub fn split(source: &str) -> Result<Fragment> {
    let trimmed = source.trim_start();
    if !trimmed.starts_with("---") {
        return Err(BuildError::Content(
            "fragment missing YAML front-matter opener '---'".into(),
        ));
    }
    let after_open = &trimmed[3..];
    // Skip optional newline right after opener
    let after_open = after_open.strip_prefix('\n').unwrap_or(after_open);

    let close_idx = after_open
        .find("\n---")
        .ok_or_else(|| BuildError::Content("missing closing '---' for front-matter".into()))?;

    let yaml_block = &after_open[..close_idx];
    let meta: Value = serde_yaml::from_str(yaml_block)?;

    // Body starts after the closing '\n---' (plus optional trailing '\n')
    let after_close = &after_open[close_idx + 4..];
    let body = after_close.strip_prefix('\n').unwrap_or(after_close).to_string();

    Ok(Fragment { meta, body })
}
