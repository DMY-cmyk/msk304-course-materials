use crate::error::Result;
use crate::model::Week;
use serde::Deserialize;
use std::fs;
use std::path::Path;

#[derive(Debug, Deserialize)]
struct Manifest {
    weeks: Vec<Week>,
}

pub fn load_weeks(path: &Path) -> Result<Vec<Week>> {
    let body = fs::read_to_string(path)?;
    let manifest: Manifest = toml::from_str(&body)?;
    Ok(manifest.weeks)
}
