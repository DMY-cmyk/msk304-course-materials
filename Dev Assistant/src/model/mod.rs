pub mod config;

use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Week {
    pub num: u8,
    pub topic_slug: String,
    pub topic_id: String,   // Indonesian title
    pub topic_en: String,   // English title
    #[serde(default)]
    pub tpgs_chapters: Vec<u8>,
    #[serde(default)]
    pub henry_chapters: Vec<u8>,
    #[serde(default)]
    pub articles: Vec<ArticleRef>,
    pub indo_flagship: Company,
    #[serde(default)]
    pub indo_sidebars: Vec<Company>,
    #[serde(default)]
    pub is_article_led: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ArticleRef {
    pub number: u8,
    pub citation: String,
    pub pdf_available: bool,
    pub week_role: String,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Company {
    pub slug: String,
    pub name: String,
    #[serde(default)]
    pub idx_ticker: Option<String>,
    pub concept_anchor: String,
}
