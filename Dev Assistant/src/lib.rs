//! Dev Assistant — MST304 course support system pipeline.
//!
//! Pipeline: Markdown fragments → front-matter split → Markdown→HTML →
//! minijinja template → output HTML + copied assets.

pub mod error;
pub mod model;
pub mod content_loader;
pub mod html_builder;

pub use error::{BuildError, Result};
