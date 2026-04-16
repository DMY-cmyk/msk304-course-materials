# MST304 Phase I — Bootstrap + Week 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the Rust-based Dev Assistant pipeline and produce three complete Week-1 HTML outputs (Study Guide, Main Summary, Indonesian Company Examples) that match the approved "Editorial Scholar" design system.

**Architecture:** Markdown-fragment authoring + Rust shell builder. Content lives in `Dev Assistant/content/week-NN/<section>/*.md` with YAML front-matter. A Rust binary crate reads these fragments, converts Markdown to HTML via `pulldown-cmark`, assembles pages from `minijinja` templates, and writes the final HTML + copied assets to `course-materials/outputs/`. The Visual Companion (already built) stays as the navigation/preview layer.

**Tech Stack:** Rust 1.75+ · pulldown-cmark · minijinja · serde + serde_yaml + toml · walkdir · anyhow · thiserror · clap.

**Phase I produces:**
- `Dev Assistant/` Rust crate — compiles and passes tests
- `Dev Assistant/configs/week-mapping.toml` — all 14 weeks declared
- `Dev Assistant/content/week-01/` — real academic content fragments
- Shared stylesheets: `screen.css` (Editorial Scholar) + `print.css`
- Four HTML templates: `base`, `study-guide`, `summary`, `indonesian`
- Week 1 outputs rendered to `course-materials/outputs/<type>/Week 01/index.html`
- Visual verification: Week 1 opens cleanly in browser and prints cleanly to PDF

**Phase I does NOT produce:** Weeks 2–14 content, Master Print Bundle, Article analysis template (Week 1 has no article per syllabus).

**Context the engineer needs:**
- Spec: `docs/superpowers/specs/2026-04-16-msk304-design.md`
- Visual Companion (already built): `course-materials/outputs/Visual Companion/index.html` — use its CSS as the design-token source of truth
- The Rust project root is `Dev Assistant/` — note the space; the engineer must quote paths on Windows bash

---

## File Structure (what each file owns)

### Rust crate (`Dev Assistant/`)

| Path | Responsibility |
|------|----------------|
| `Cargo.toml` | Crate manifest, dependencies, binary declaration |
| `.gitignore` | Exclude `target/`, `temp/`, `logs/` |
| `README.md` | Usage: `cargo run -- build`, `--week N`, `clean` |
| `src/main.rs` | Entry point + clap CLI parsing + subcommand dispatch |
| `src/lib.rs` | Public API surface (for tests) + module re-exports |
| `src/error.rs` | `BuildError` enum via `thiserror` |
| `src/model/mod.rs` | Core structs: `Week`, `Article`, `Company`, `SourceCitation`, `DocType` |
| `src/model/config.rs` | Loads `configs/week-mapping.toml` → `Vec<Week>` |
| `src/content_loader/mod.rs` | Walks `content/week-NN/<section>/` → ordered `Vec<Fragment>` |
| `src/content_loader/frontmatter.rs` | Splits `"---\n{yaml}\n---\n{body}"` → `(YamlValue, String)` |
| `src/content_loader/markdown.rs` | `pulldown-cmark` wrapper: Markdown body → HTML string |
| `src/html_builder/mod.rs` | Orchestrator: for each week+section, pull fragments → render → write file |
| `src/html_builder/engine.rs` | `minijinja::Environment` setup, loads `templates/` directory |
| `src/html_builder/assets.rs` | Copies CSS + any SVG assets into output folders |
| `configs/week-mapping.toml` | Declarative week → topic/TPGS/Henry/articles/Indonesian flagship map |
| `configs/build.toml` | Output root paths, relative-asset config |
| `templates/base.html.j2` | Shared shell: sidebar, header, main slot, print-css link |
| `templates/week-study-guide.html.j2` | Study Guide / Aid layout |
| `templates/week-summary.html.j2` | Main Summary / Ebook layout |
| `templates/week-indonesian.html.j2` | Indonesian Company Examples layout |
| `assets/css/screen.css` | Editorial Scholar design tokens + layout + components |
| `assets/css/print.css` | Print-specific overrides (A4, page-break rules, @page header) |
| `content/week-01/_meta.toml` | Per-week override (title, reading order, flagship slug) |
| `content/week-01/study-guide/*.md` | 4 fragments |
| `content/week-01/summary/*.md` | 5 fragments (overview, frameworks, concepts, connections, concept-check) |
| `content/week-01/indonesian/*.md` | 3 fragments (Astra flagship + Unilever sidebar + Indofood sidebar) |

### Outputs (`course-materials/outputs/`)

| Path | Contents |
|------|----------|
| `Study Guide - Aid/Week 01/index.html` | Rendered study guide |
| `Study Guide - Aid/Week 01/assets/` | Copied screen.css + print.css |
| `Main Summary - Ebook/Week 01/index.html` | Rendered main summary |
| `Main Summary - Ebook/Week 01/assets/` | Copied CSS |
| `Indonesian Company Examples/Week 01/index.html` | Rendered Indonesian page |
| `Indonesian Company Examples/Week 01/assets/` | Copied CSS |

---

## Task 1 — Rust crate scaffolding

**Files:**
- Create: `Dev Assistant/Cargo.toml`
- Create: `Dev Assistant/.gitignore`
- Create: `Dev Assistant/src/main.rs`
- Create: `Dev Assistant/src/lib.rs`
- Create: `Dev Assistant/src/error.rs`

- [ ] **Step 1.1: Create the crate directory structure**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik"
mkdir -p "Dev Assistant/src" "Dev Assistant/configs" "Dev Assistant/templates" "Dev Assistant/assets/css" "Dev Assistant/content" "Dev Assistant/tests" "Dev Assistant/temp" "Dev Assistant/logs"
```

- [ ] **Step 1.2: Write `Cargo.toml`**

Path: `Dev Assistant/Cargo.toml`

```toml
[package]
name = "dev-assistant"
version = "0.1.0"
edition = "2021"
description = "MST304 course support system — content pipeline"
authors = ["Dzaki <dzakimy.spelanta@gmail.com>"]
publish = false

[[bin]]
name = "dev-assistant"
path = "src/main.rs"

[lib]
name = "dev_assistant"
path = "src/lib.rs"

[dependencies]
anyhow = "1.0"
thiserror = "1.0"
clap = { version = "4.5", features = ["derive"] }
serde = { version = "1.0", features = ["derive"] }
serde_yaml = "0.9"
toml = "0.8"
walkdir = "2.5"
pulldown-cmark = { version = "0.11", default-features = false, features = ["html"] }
minijinja = { version = "2.3", features = ["loader"] }

[dev-dependencies]
tempfile = "3.12"
pretty_assertions = "1.4"
```

- [ ] **Step 1.3: Write `.gitignore`**

Path: `Dev Assistant/.gitignore`

```gitignore
/target
/temp
/logs
**/*.bk
Cargo.lock
```

- [ ] **Step 1.4: Write the error module**

Path: `Dev Assistant/src/error.rs`

```rust
use thiserror::Error;

#[derive(Debug, Error)]
pub enum BuildError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),

    #[error("YAML parse error: {0}")]
    Yaml(#[from] serde_yaml::Error),

    #[error("TOML parse error: {0}")]
    Toml(#[from] toml::de::Error),

    #[error("Template error: {0}")]
    Template(#[from] minijinja::Error),

    #[error("Content error: {0}")]
    Content(String),

    #[error("Config error: {0}")]
    Config(String),
}

pub type Result<T> = std::result::Result<T, BuildError>;
```

- [ ] **Step 1.5: Write `src/lib.rs` as the public-API surface**

Path: `Dev Assistant/src/lib.rs`

```rust
//! Dev Assistant — MST304 course support system pipeline.
//!
//! Pipeline: Markdown fragments → front-matter split → Markdown→HTML →
//! minijinja template → output HTML + copied assets.

pub mod error;
pub mod model;
pub mod content_loader;
pub mod html_builder;

pub use error::{BuildError, Result};
```

- [ ] **Step 1.6: Write a minimal `src/main.rs` with clap skeleton**

Path: `Dev Assistant/src/main.rs`

```rust
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "dev-assistant", version, about = "MST304 course support system pipeline")]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    /// Build all weeks (or use --week to limit)
    Build {
        #[arg(long)]
        week: Option<u8>,
    },
    /// Remove all generated output files
    Clean,
    /// Verify outputs exist and are non-empty
    Verify,
}

fn main() -> anyhow::Result<()> {
    let cli = Cli::parse();
    match cli.command {
        Command::Build { week } => {
            println!("build invoked (week filter: {:?}) — orchestrator not yet wired", week);
        }
        Command::Clean => println!("clean invoked — not yet implemented"),
        Command::Verify => println!("verify invoked — not yet implemented"),
    }
    Ok(())
}
```

- [ ] **Step 1.7: Stub out the module files so `lib.rs` compiles**

Create these empty placeholder files (one-line `pub mod` declarations keep the build green until Task 2 fills them in):

Path: `Dev Assistant/src/model/mod.rs`
```rust
// Populated in Task 2.
pub mod config;
```

Path: `Dev Assistant/src/model/config.rs`
```rust
// Populated in Task 2.
```

Path: `Dev Assistant/src/content_loader/mod.rs`
```rust
// Populated in Task 3.
pub mod frontmatter;
pub mod markdown;
```

Path: `Dev Assistant/src/content_loader/frontmatter.rs`
```rust
// Populated in Task 3.
```

Path: `Dev Assistant/src/content_loader/markdown.rs`
```rust
// Populated in Task 3.
```

Path: `Dev Assistant/src/html_builder/mod.rs`
```rust
// Populated in Task 5.
pub mod engine;
pub mod assets;
```

Path: `Dev Assistant/src/html_builder/engine.rs`
```rust
// Populated in Task 5.
```

Path: `Dev Assistant/src/html_builder/assets.rs`
```rust
// Populated in Task 5.
```

- [ ] **Step 1.8: Verify the crate compiles**

Run (from `Dev Assistant/`):
```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik/Dev Assistant"
cargo check
```

Expected: `Checking dev-assistant v0.1.0 ... Finished \`dev\` profile ... in NNs`. Zero errors, possibly some dead-code warnings (fine for now).

- [ ] **Step 1.9: Verify the CLI runs**

```bash
cargo run -- build
```

Expected output:
```
build invoked (week filter: None) — orchestrator not yet wired
```

---

## Task 2 — Data model + config loader (TDD)

**Files:**
- Modify: `Dev Assistant/src/model/mod.rs`
- Modify: `Dev Assistant/src/model/config.rs`
- Create: `Dev Assistant/configs/week-mapping.toml`
- Create: `Dev Assistant/configs/build.toml`
- Create: `Dev Assistant/tests/config_load.rs`

- [ ] **Step 2.1: Write the failing config-loader test FIRST**

Path: `Dev Assistant/tests/config_load.rs`

```rust
use dev_assistant::model::config::load_weeks;
use std::path::Path;

#[test]
fn loads_all_14_weeks_from_mapping_toml() {
    let weeks = load_weeks(Path::new("configs/week-mapping.toml"))
        .expect("week-mapping.toml should load");
    assert_eq!(weeks.len(), 14, "expected 14 teaching weeks");
    assert_eq!(weeks[0].num, 1);
    assert_eq!(weeks[13].num, 14);
}

#[test]
fn week_one_has_astra_flagship() {
    let weeks = load_weeks(Path::new("configs/week-mapping.toml")).unwrap();
    let w1 = &weeks[0];
    assert_eq!(w1.indo_flagship.slug, "astra-international");
    assert_eq!(w1.tpgs_chapters, vec![1]);
}

#[test]
fn week_twelve_has_no_tpgs_chapter() {
    let weeks = load_weeks(Path::new("configs/week-mapping.toml")).unwrap();
    let w12 = &weeks[11];
    assert!(w12.tpgs_chapters.is_empty(), "W12 has no TPGS chapter in 7e");
    assert!(!w12.henry_chapters.is_empty(), "W12 must reference Henry chapters");
}
```

- [ ] **Step 2.2: Run the test to confirm it fails**

Run:
```bash
cargo test --test config_load
```

Expected: compilation error (`load_weeks` doesn't exist, `Week` struct missing). This is the red bar.

- [ ] **Step 2.3: Write the data model**

Path: `Dev Assistant/src/model/mod.rs` (replace stub)

```rust
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
```

- [ ] **Step 2.4: Write the config loader**

Path: `Dev Assistant/src/model/config.rs` (replace stub)

```rust
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
```

- [ ] **Step 2.5: Write `configs/week-mapping.toml` with all 14 weeks**

Path: `Dev Assistant/configs/week-mapping.toml`

```toml
# MST304 — syllabus-to-textbook-to-Indonesian-flagship authoritative mapping.
# Source of truth for the Rust pipeline. Edits here cascade into every output.

[[weeks]]
num = 1
topic_slug = "what-is-strategy"
topic_id = "Apa Itu Strategi dan Mengapa Penting?"
topic_en = "What Is Strategy and Why Is It Important?"
tpgs_chapters = [1]
henry_chapters = [1]
articles = []
indo_flagship = { slug = "astra-international", name = "Astra International", idx_ticker = "ASII", concept_anchor = "strategic coherence across a diversified portfolio" }
indo_sidebars = [
  { slug = "unilever-indonesia", name = "Unilever Indonesia", idx_ticker = "UNVR", concept_anchor = "focused differentiation in FMCG" },
  { slug = "indofood", name = "Indofood Sukses Makmur", idx_ticker = "INDF", concept_anchor = "vertical integration across the food value chain" },
]

[[weeks]]
num = 2
topic_slug = "crafting-executing-strategy"
topic_id = "Proses Manajerial Penyusunan dan Eksekusi Strategi"
topic_en = "The Managerial Process of Crafting and Executing Strategy"
tpgs_chapters = [2]
henry_chapters = [1, 2]
articles = [
  { number = 1, citation = "Altıok, P. (2011). Applicable vision, mission and the effects of strategic management on crisis resolve. Procedia Social & Behavioral Sciences, 24, 61–71.", pdf_available = true, week_role = "vision-mission as crisis anchor" },
  { number = 2, citation = "Mohamed, F., Nusari, M., Ameen, A., Raju, V., & Bhaumik, A. (2019). Towards a better understanding of the relationship between strategy formulation (vision, mission, and goals) and organizational performance. Test Engineering and Management, 81, 1987–1994.", pdf_available = true, week_role = "empirical vision-mission → performance" },
]
indo_flagship = { slug = "bca", name = "Bank Central Asia", idx_ticker = "BBCA", concept_anchor = "vision-mission discipline and governance rigor" }
indo_sidebars = [
  { slug = "pertamina", name = "Pertamina", concept_anchor = "mission evolution post-Holding Migas" },
]

[[weeks]]
num = 3
topic_slug = "external-environment"
topic_id = "Evaluasi Lingkungan Eksternal Perusahaan"
topic_en = "Evaluating a Company's External Environment"
tpgs_chapters = [3]
henry_chapters = [3]
articles = [
  { number = 3, citation = "Newman, C., Rand, J., Tarp, F., & Trifkovic, N. (2020). Corporate social responsibility in a competitive business environment. The Journal of Development Studies, 56(8), 1455–1472.", pdf_available = true, week_role = "CSR interaction with industry competitiveness" },
  { number = 4, citation = "Mason, R. B. (2007). The external environment's effect on management and strategy: A complexity theory approach. Management Decision, 45(1), 10–28.", pdf_available = true, week_role = "environment as complex adaptive system" },
]
indo_flagship = { slug = "goto", name = "GoTo Gojek Tokopedia", idx_ticker = "GOTO", concept_anchor = "macro and technological environment shock" }
indo_sidebars = [
  { slug = "adaro-energy", name = "Adaro Energy", idx_ticker = "ADRO", concept_anchor = "regulatory environment in energy transition" },
  { slug = "telkom-indonesia", name = "Telkom Indonesia", idx_ticker = "TLKM", concept_anchor = "technological environment in 5G/IndiHome" },
]

[[weeks]]
num = 4
topic_slug = "resources-competitive-position"
topic_id = "Evaluasi Sumber Daya dan Posisi Kompetitif"
topic_en = "Evaluating a Company's Resources and Competitive Position"
tpgs_chapters = [4]
henry_chapters = [4]
articles = [
  { number = 5, citation = "Barney, J. (1991). Firm resources and sustained competitive advantage. Journal of Management, 17(1), 99–120.", pdf_available = false, week_role = "VRIN foundation" },
  { number = 6, citation = "Ma, H. (2000). Competitive advantage and firm performance. Competitiveness Review, 10(2), 15–32.", pdf_available = false, week_role = "linking advantage to performance" },
]
indo_flagship = { slug = "bca", name = "Bank Central Asia", idx_ticker = "BBCA", concept_anchor = "VRIN-aligned intangibles (network + brand + CASA)" }
indo_sidebars = [
  { slug = "telkomsel", name = "Telkomsel", concept_anchor = "spectrum and infrastructure as rare resources" },
  { slug = "gudang-garam", name = "Gudang Garam", idx_ticker = "GGRM", concept_anchor = "brand and distribution as VRIN assets" },
]

[[weeks]]
num = 5
topic_slug = "generic-strategies"
topic_id = "Lima Strategi Kompetitif Generik"
topic_en = "The Five Generic Competitive Strategies"
tpgs_chapters = [5]
henry_chapters = [5]
articles = [
  { number = 7, citation = "Salavou, H. (2015). Competitive strategies and their shift to the future. European Business Review, 27(1), 80–99.", pdf_available = false, week_role = "evolution of generic strategies" },
  { number = 8, citation = "Adom, A. Y., Nyarko, I. K., & Som, G. N. K. (2016). Competitor analysis in strategic management. Journal of Resources Development and Management, 24, 116.", pdf_available = false, week_role = "competitor analysis practice" },
]
indo_flagship = { slug = "indofood", name = "Indofood Sukses Makmur", idx_ticker = "INDF", concept_anchor = "cost leadership in CPG at scale" }
indo_sidebars = [
  { slug = "unilever-indonesia", name = "Unilever Indonesia", idx_ticker = "UNVR", concept_anchor = "broad differentiation" },
  { slug = "sido-muncul", name = "Sido Muncul", idx_ticker = "SIDO", concept_anchor = "focused differentiation in premium jamu" },
]

[[weeks]]
num = 6
topic_slug = "supplementing-strategy"
topic_id = "Melengkapi Strategi Kompetitif yang Dipilih"
topic_en = "Supplementing the Chosen Competitive Strategy"
tpgs_chapters = [6]
henry_chapters = [5, 6]
articles = [
  { number = 9, citation = "Teeratansirikool, L., Siengthai, S., Badir, Y., & Charoenngam, C. (2013). Competitive strategies and firm performance: the mediating role of performance measurement. IJPPM, 63(1/2), 168–184.", pdf_available = false, week_role = "performance measurement as mediator" },
  { number = 10, citation = "Onditi, E. O. (2018). Competitive strategies and firm performance: A review of literature. Strategic Journals, 5(4), 1869–1879.", pdf_available = false, week_role = "literature synthesis" },
]
indo_flagship = { slug = "goto", name = "GoTo Gojek Tokopedia", idx_ticker = "GOTO", concept_anchor = "blue-ocean super-app strategy" }
indo_sidebars = [
  { slug = "garuda-indonesia", name = "Garuda Indonesia", idx_ticker = "GIAA", concept_anchor = "defensive and restructuring moves" },
  { slug = "bri", name = "Bank Rakyat Indonesia", idx_ticker = "BBRI", concept_anchor = "horizontal expansion via Holding UMi" },
]

[[weeks]]
num = 7
topic_slug = "tailoring-to-industry"
topic_id = "Menyesuaikan Strategi dengan Situasi Industri dan Perusahaan"
topic_en = "Tailoring Strategy to Fit Specific Industry and Company Situations"
tpgs_chapters = [6]
henry_chapters = [6]
articles = [
  { number = 11, citation = "Hsieh, Y. H., & Chen, H. M. (2011). Strategic fit among business competitive strategy, human resource strategy, and reward system. Academy of Strategic Management Journal, 10(2), 11–32.", pdf_available = false, week_role = "strategic fit framework" },
  { number = 12, citation = "Moses, O. S., & Ekwutosi, O. C. (2018). Implication of strategic fit and sustainability on organizational effectiveness. IARC Vienna.", pdf_available = false, week_role = "fit-sustainability nexus" },
]
indo_flagship = { slug = "kalbe-farma", name = "Kalbe Farma", idx_ticker = "KLBF", concept_anchor = "tailoring to mature fragmented pharma" }
indo_sidebars = [
  { slug = "icbp", name = "Indofood CBP", idx_ticker = "ICBP", concept_anchor = "dominant-leader tailoring" },
  { slug = "bukalapak", name = "Bukalapak", idx_ticker = "BUKA", concept_anchor = "growing-industry pivot" },
]

[[weeks]]
num = 8
topic_slug = "international-markets"
topic_id = "Strategi Bersaing di Pasar Internasional"
topic_en = "Strategies for Competing in International Markets"
tpgs_chapters = [7]
henry_chapters = [8]
articles = [
  { number = 15, citation = "Thomas, H., Pollock, T., & Gorman, P. (1999). Global strategic analysis: Frameworks and approaches.", pdf_available = false, week_role = "frameworks for global analysis" },
  { number = 16, citation = "Grein, A. F. The impact of market similarity on international marketing strategies: The automobile industry in Western Europe.", pdf_available = false, week_role = "market-similarity effects" },
  { number = 17, citation = "Robles, F. International market entry strategies and performance of United States catalog firms.", pdf_available = false, week_role = "entry-mode choice and performance" },
]
indo_flagship = { slug = "indofood", name = "Indofood Sukses Makmur", idx_ticker = "INDF", concept_anchor = "global product strategy via Indomie in 90+ countries" }
indo_sidebars = [
  { slug = "astra-otoparts", name = "Astra Otoparts", idx_ticker = "AUTO", concept_anchor = "export manufacturing" },
  { slug = "kopi-kenangan", name = "Kopi Kenangan", concept_anchor = "regional Southeast Asia expansion" },
]

[[weeks]]
num = 9
topic_slug = "diversification"
topic_id = "Strategi Korporat: Diversifikasi dan Perusahaan Multibisnis"
topic_en = "Corporate Strategy: Diversification and the Multibusiness Company"
tpgs_chapters = [8]
henry_chapters = [9]
articles = [
  { number = 18, citation = "Kochhar, R., & Hitt, M. A. Linking corporate strategy to capital structure: Diversification strategy, type and source of financing.", pdf_available = false, week_role = "capital-structure × diversification" },
  { number = 19, citation = "Goold, M., & Luchs, K. (1993). Why diversify? Four decades of management thinking.", pdf_available = false, week_role = "historical thinking on diversification" },
]
indo_flagship = { slug = "astra-international", name = "Astra International", idx_ticker = "ASII", concept_anchor = "unrelated diversification with soft-control integration" }
indo_sidebars = [
  { slug = "salim-group", name = "Salim / Indofood Group", concept_anchor = "related + unrelated diversification" },
  { slug = "djarum-group", name = "Djarum Group", concept_anchor = "tobacco + banking (BCA) + digital (GDP Venture)" },
]

[[weeks]]
num = 10
topic_slug = "ethics-csr-sustainability"
topic_id = "Etika, CSR, Keberlanjutan Lingkungan, dan Strategi"
topic_en = "Ethics, Corporate Social Responsibility, Environmental Sustainability, and Strategy"
tpgs_chapters = [9]
henry_chapters = [10]
articles = [
  { number = 20, citation = "Triebswetter, U., & Hitchens, D. The impact of environmental regulation on competitiveness in the German manufacturing industry.", pdf_available = false, week_role = "environmental regulation × competitiveness" },
  { number = 21, citation = "De Sousa Filho, J. M., Wanderley, L. S. O., Gómez, C. P., & Farache, F. (2010). Strategic corporate social responsibility management for competitive advantage.", pdf_available = false, week_role = "CSR as strategic advantage" },
]
indo_flagship = { slug = "unilever-indonesia", name = "Unilever Indonesia", idx_ticker = "UNVR", concept_anchor = "Unilever Sustainable Living Plan localised" }
indo_sidebars = [
  { slug = "indika-energy", name = "Indika Energy", idx_ticker = "INDY", concept_anchor = "coal-to-renewables transition" },
  { slug = "bri", name = "Bank Rakyat Indonesia", idx_ticker = "BBRI", concept_anchor = "sustainable finance portfolio" },
]

[[weeks]]
num = 11
topic_slug = "strategy-execution"
topic_id = "Eksekusi Strategi yang Unggul"
topic_en = "Superior Strategy Execution"
tpgs_chapters = [10]
henry_chapters = [11]
articles = [
  { number = 22, citation = "Kaplan, R. S., & Norton, D. P. (2006). How to implement a new strategy without disrupting your organization.", pdf_available = false, week_role = "strategy-execution without disruption" },
  { number = 23, citation = "Richardson, J. The business model: An integrative framework for strategy execution.", pdf_available = false, week_role = "business model as execution engine" },
]
indo_flagship = { slug = "bank-mandiri", name = "Bank Mandiri", idx_ticker = "BMRI", concept_anchor = "post-merger integration execution" }
indo_sidebars = [
  { slug = "pertamina", name = "Pertamina", concept_anchor = "holding-subholding execution" },
  { slug = "bri", name = "Bank Rakyat Indonesia", idx_ticker = "BBRI", concept_anchor = "BRILink and BRImo execution layer" },
]

[[weeks]]
num = 12
topic_slug = "business-model-barriers"
topic_id = "Inovasi Model Bisnis dan Hambatan Masuk (Artikel)"
topic_en = "Business Model Innovation and Barriers to Entry (article-led)"
tpgs_chapters = []
henry_chapters = [7]
is_article_led = true
articles = [
  { number = 24, citation = "Beckmann, M., Royer, S., & Schiavone, F. (2016). Old but sexy: Value creation of old technology-based businesses models.", pdf_available = false, week_role = "value creation via legacy tech" },
  { number = 25, citation = "Karakaya, F., & Parayitam, S. (2013). Barrier to entry and firm performance: A proposed model and curvilinear relationships.", pdf_available = false, week_role = "barrier × performance curvilinear" },
]
indo_flagship = { slug = "goto", name = "GoTo Gojek Tokopedia", idx_ticker = "GOTO", concept_anchor = "super-app business model architecture" }
indo_sidebars = [
  { slug = "ruangguru", name = "Ruangguru", concept_anchor = "EdTech subscription model" },
  { slug = "indomaret", name = "Indomaret", concept_anchor = "retail density as barrier to entry" },
]

[[weeks]]
num = 13
topic_slug = "stakeholder-engagement"
topic_id = "Kapabilitas Stakeholder dan Engagement (Artikel)"
topic_en = "Stakeholder Capability and Engagement (article-led)"
tpgs_chapters = []
henry_chapters = [2, 10]
is_article_led = true
articles = [
  { number = 26, citation = "Westermann-Behaylo, M. K., Van Buren III, H. J., & Berman, S. L. (2016). Stakeholder capability enhancement as a path to promote human dignity and cooperative advantage.", pdf_available = false, week_role = "stakeholder capability enhancement" },
  { number = 27, citation = "Kumar, V., & Pansari, A. (2016). Competitive advantage through engagement.", pdf_available = false, week_role = "engagement as competitive advantage" },
]
indo_flagship = { slug = "gojek-drivers", name = "Gojek driver ecosystem", concept_anchor = "stakeholder capability enhancement (landmark case)" }
indo_sidebars = [
  { slug = "tokopedia", name = "Tokopedia seller program", concept_anchor = "seller engagement" },
  { slug = "bca", name = "BCA customer loyalty", idx_ticker = "BBCA", concept_anchor = "customer engagement at scale" },
]

[[weeks]]
num = 14
topic_slug = "hypercompetition-leadership"
topic_id = "Hiperkompetisi dan Kepemimpinan Strategis (Artikel)"
topic_en = "Hypercompetition and Strategic Leadership (article-led)"
tpgs_chapters = []
henry_chapters = [3, 11]
is_article_led = true
articles = [
  { number = 28, citation = "Chen, M. J., Lin, H. C., & Michel, J. G. (2010). Navigating in a hypercompetitive environment: The roles of action aggressiveness and TMT integration.", pdf_available = false, week_role = "hypercompetition × TMT integration" },
  { number = 29, citation = "Jansen, J. J. P., Vera, D., & Crossan, M. (2009). Strategic leadership for exploration and exploitation: The moderating role of environmental dynamism.", pdf_available = false, week_role = "ambidextrous strategic leadership" },
]
indo_flagship = { slug = "goto-grab-shopeefood", name = "GoTo – Grab – ShopeeFood triopoly", concept_anchor = "hypercompetitive food-delivery rivalry" }
indo_sidebars = [
  { slug = "bca-leadership", name = "Jahja Setiaatmadja at BCA", concept_anchor = "long-tenure strategic leadership" },
  { slug = "telkom-tmt", name = "Telkom TMT", idx_ticker = "TLKM", concept_anchor = "ambidextrous leadership in incumbent telco" },
]
```

- [ ] **Step 2.6: Write `configs/build.toml`**

Path: `Dev Assistant/configs/build.toml`

```toml
# Output root — relative to project root (i.e. the parent of "Dev Assistant").
output_root = "../course-materials/outputs"

[sections]
study_guide   = { folder = "Study Guide - Aid",            template = "week-study-guide.html.j2" }
summary       = { folder = "Main Summary - Ebook",         template = "week-summary.html.j2" }
indonesian    = { folder = "Indonesian Company Examples",  template = "week-indonesian.html.j2" }
# Article template added in Phase II when Week 2 ships.
```

- [ ] **Step 2.7: Run the tests to verify they pass**

Run from `Dev Assistant/`:
```bash
cargo test --test config_load
```

Expected: `running 3 tests ... test result: ok. 3 passed; 0 failed`.

- [ ] **Step 2.8: Commit**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik"
git init -q 2>/dev/null || true
git add "Dev Assistant/Cargo.toml" "Dev Assistant/.gitignore" "Dev Assistant/src/" "Dev Assistant/configs/" "Dev Assistant/tests/"
git commit -m "feat(dev-assistant): bootstrap crate with 14-week config + passing tests"
```

> **Note**: git init is defensive — if the repo already exists it's a no-op. If the user prefers no git, skip the commit step.

---

## Task 3 — Front-matter + Markdown loader (TDD)

**Files:**
- Modify: `Dev Assistant/src/content_loader/frontmatter.rs`
- Modify: `Dev Assistant/src/content_loader/markdown.rs`
- Modify: `Dev Assistant/src/content_loader/mod.rs`
- Create: `Dev Assistant/tests/frontmatter.rs`
- Create: `Dev Assistant/tests/markdown.rs`
- Create: `Dev Assistant/tests/content_loader.rs`

- [ ] **Step 3.1: Write the failing front-matter test**

Path: `Dev Assistant/tests/frontmatter.rs`

```rust
use dev_assistant::content_loader::frontmatter::{split, Fragment};

#[test]
fn splits_yaml_frontmatter_and_body() {
    let source = "---\ntitle: Test\norder: 1\n---\n# Hello\n\nWorld.\n";
    let Fragment { meta, body } = split(source).expect("valid fragment");
    let title = meta.get("title").and_then(|v| v.as_str()).unwrap();
    let order = meta.get("order").and_then(|v| v.as_i64()).unwrap();
    assert_eq!(title, "Test");
    assert_eq!(order, 1);
    assert_eq!(body.trim(), "# Hello\n\nWorld.");
}

#[test]
fn missing_frontmatter_is_an_error() {
    let source = "just markdown, no frontmatter";
    assert!(split(source).is_err());
}

#[test]
fn malformed_yaml_is_an_error() {
    let source = "---\ntitle: [unclosed\n---\nbody";
    assert!(split(source).is_err());
}
```

- [ ] **Step 3.2: Run to confirm failure**

Run:
```bash
cargo test --test frontmatter
```

Expected: compilation error (`split` not defined).

- [ ] **Step 3.3: Implement `frontmatter.rs`**

Path: `Dev Assistant/src/content_loader/frontmatter.rs` (replace stub)

```rust
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
```

- [ ] **Step 3.4: Run tests, confirm green**

```bash
cargo test --test frontmatter
```

Expected: `3 passed; 0 failed`.

- [ ] **Step 3.5: Write the failing markdown-rendering test**

Path: `Dev Assistant/tests/markdown.rs`

```rust
use dev_assistant::content_loader::markdown::render;

#[test]
fn renders_heading_and_paragraph() {
    let md = "## Hello\n\nThis is **bold**.";
    let html = render(md);
    assert!(html.contains("<h2>Hello</h2>"));
    assert!(html.contains("<strong>bold</strong>"));
}

#[test]
fn supports_tables() {
    let md = "| a | b |\n|---|---|\n| 1 | 2 |\n";
    let html = render(md);
    assert!(html.contains("<table>"));
    assert!(html.contains("<th>a</th>"));
}

#[test]
fn preserves_inline_html() {
    let md = "Some <em>inline</em> html.";
    let html = render(md);
    assert!(html.contains("<em>inline</em>"));
}
```

- [ ] **Step 3.6: Run to confirm failure**

```bash
cargo test --test markdown
```

Expected: compilation error (`render` not defined).

- [ ] **Step 3.7: Implement `markdown.rs`**

Path: `Dev Assistant/src/content_loader/markdown.rs` (replace stub)

```rust
use pulldown_cmark::{html, Options, Parser};

pub fn render(markdown: &str) -> String {
    let mut opts = Options::empty();
    opts.insert(Options::ENABLE_TABLES);
    opts.insert(Options::ENABLE_FOOTNOTES);
    opts.insert(Options::ENABLE_STRIKETHROUGH);
    opts.insert(Options::ENABLE_HEADING_ATTRIBUTES);

    let parser = Parser::new_ext(markdown, opts);
    let mut buf = String::new();
    html::push_html(&mut buf, parser);
    buf
}
```

- [ ] **Step 3.8: Confirm green**

```bash
cargo test --test markdown
```

Expected: `3 passed; 0 failed`.

- [ ] **Step 3.9: Write the content-loader integration test**

Path: `Dev Assistant/tests/content_loader.rs`

```rust
use dev_assistant::content_loader::load_section;
use std::fs;
use tempfile::tempdir;

#[test]
fn loads_ordered_fragments_from_section_dir() {
    let dir = tempdir().unwrap();
    let section = dir.path().join("week-01/study-guide");
    fs::create_dir_all(&section).unwrap();

    fs::write(section.join("02-second.md"),
        "---\norder: 2\ntitle: Second\n---\nSecond body.\n").unwrap();
    fs::write(section.join("01-first.md"),
        "---\norder: 1\ntitle: First\n---\nFirst body.\n").unwrap();

    let fragments = load_section(&section).expect("should load");
    assert_eq!(fragments.len(), 2);
    // Ordered by filename prefix (01-, 02-)
    assert_eq!(fragments[0].meta.get("title").unwrap().as_str().unwrap(), "First");
    assert_eq!(fragments[1].meta.get("title").unwrap().as_str().unwrap(), "Second");
    assert!(fragments[0].body.contains("First body."));
}
```

- [ ] **Step 3.10: Run to confirm failure**

```bash
cargo test --test content_loader
```

Expected: compilation error (`load_section` not defined).

- [ ] **Step 3.11: Implement `content_loader/mod.rs`**

Path: `Dev Assistant/src/content_loader/mod.rs` (replace stub)

```rust
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
```

- [ ] **Step 3.12: Confirm green**

```bash
cargo test --test content_loader
```

Expected: `1 passed; 0 failed`.

- [ ] **Step 3.13: Full test-suite sanity check**

```bash
cargo test
```

Expected: all tests in all three files pass (3 + 3 + 1 = 7 passing, 0 failing).

- [ ] **Step 3.14: Commit**

```bash
git add "Dev Assistant/src/content_loader/" "Dev Assistant/tests/"
git commit -m "feat(dev-assistant): front-matter + markdown + section loader with tests"
```

---

## Task 4 — Templates + shared CSS

**Files:**
- Create: `Dev Assistant/templates/base.html.j2`
- Create: `Dev Assistant/templates/week-study-guide.html.j2`
- Create: `Dev Assistant/templates/week-summary.html.j2`
- Create: `Dev Assistant/templates/week-indonesian.html.j2`
- Create: `Dev Assistant/assets/css/screen.css`
- Create: `Dev Assistant/assets/css/print.css`

> **Design-token source:** all CSS variables, fonts, and component styles in `screen.css` below are lifted directly from `course-materials/outputs/Visual Companion/index.html` (Editorial Scholar design) so the look matches what the user has already approved. Do NOT invent new tokens.

- [ ] **Step 4.1: Write `base.html.j2`**

Path: `Dev Assistant/templates/base.html.j2`

```html+jinja
<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ page_title }} — MST304 Manajemen Strategik Kontemporer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..900,0..100&family=Inter+Tight:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,300..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./assets/screen.css">
<link rel="stylesheet" href="./assets/print.css" media="print">
</head>
<body>
<div class="layout">

<aside class="sidebar">
  <div class="brand">MST304
    <small>Manajemen Strategik Kontemporer<br>{{ week.topic_id }}<br>Minggu {{ "%02d" | format(week.num) }}</small>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Minggu Ini</div>
    {% for anchor in anchors %}<a href="#{{ anchor.id }}">{{ anchor.title }}</a>{% endfor %}
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Keluaran Minggu Ini</div>
    <a href="../../Study Guide - Aid/Week {{ "%02d" | format(week.num) }}/index.html">① Study Guide</a>
    <a href="../../Main Summary - Ebook/Week {{ "%02d" | format(week.num) }}/index.html">② Main Summary</a>
    <a href="../../Indonesian Company Examples/Week {{ "%02d" | format(week.num) }}/index.html">④ Indonesian Examples</a>
  </div>

  <div class="nav-group">
    <div class="nav-group-title">Navigasi</div>
    <a href="../../Visual Companion/index.html">Visual Companion</a>
  </div>
</aside>

<main>
  <section class="hero">
    <div class="page-eyebrow">{{ output_eyebrow }} · Minggu {{ "%02d" | format(week.num) }}</div>
    <h1>{{ page_title }}</h1>
    <p class="lede">{{ lede }}</p>
    <div class="meta-row">
      {% if week.tpgs_chapters %}<span>TPGS Ch. {{ week.tpgs_chapters | join(", ") }}</span>{% endif %}
      {% if week.henry_chapters %}<span>Henry Ch. {{ week.henry_chapters | join(", ") }}</span>{% endif %}
      {% for a in week.articles %}<span>Art.{{ a.number }}</span>{% endfor %}
      <span>Flagship: {{ week.indo_flagship.name }}</span>
    </div>
  </section>

  {{ content | safe }}

  <footer class="page-footer">
    <hr>
    <p>Dzaki — Magister Akuntansi STIE YKPN · Semester II TA 2025/2026 · MST304.</p>
    <p class="small">Dihasilkan oleh pipeline Dev Assistant (Rust). Sumber dan catatan verifikasi tercantum per halaman.</p>
  </footer>
</main>

</div>
</body>
</html>
```

- [ ] **Step 4.2: Write `week-study-guide.html.j2`**

Path: `Dev Assistant/templates/week-study-guide.html.j2`

```html+jinja
{% extends "base.html.j2" %}
```

> **Why so short?** The Study Guide's structure is carried entirely by the Markdown fragments. `base.html.j2` renders `{{ content | safe }}` which is the concatenated HTML of all loaded fragments. The template just extends base with no overrides.

- [ ] **Step 4.3: Write `week-summary.html.j2`**

Path: `Dev Assistant/templates/week-summary.html.j2`

```html+jinja
{% extends "base.html.j2" %}
```

- [ ] **Step 4.4: Write `week-indonesian.html.j2`**

Path: `Dev Assistant/templates/week-indonesian.html.j2`

```html+jinja
{% extends "base.html.j2" %}
```

- [ ] **Step 4.5: Write `screen.css` — lift Editorial Scholar tokens from Visual Companion**

Path: `Dev Assistant/assets/css/screen.css`

The CSS below reuses every token (colors, fonts, component rules) from `course-materials/outputs/Visual Companion/index.html`. Copy the full `<style>` block contents from that file, removing only the `<style>` tag wrappers. The following is the complete contents the engineer must write:

```css
:root {
  --paper:     #fdfcfa;
  --panel:     #faf8f4;
  --panel-2:   #f3f1eb;
  --rule:      #e7e5e0;
  --rule-2:    #d6d3ca;
  --ink:       #1a1a1a;
  --muted:     #595959;
  --muted-2:   #8c8c8c;
  --navy:      #1a1f3a;
  --navy-soft: #2d3561;
  --navy-50:   #eef0f7;
  --gold:      #b08700;
  --gold-soft: #d4a500;
  --gold-50:   #fbf5dd;
  --teal:      #0e7490;
  --teal-soft: #22b4d1;
  --teal-50:   #e0f3f8;
  --warn:      #b45309;
  --warn-50:   #fef3c7;
  --ok:        #166534;
  --ok-50:     #dcfce7;
  --rev:       #7e22ce;
  --rev-50:    #faf5ff;
  --danger:    #991b1b;
  --bg: var(--paper);
  --display: "Fraunces", "Playfair Display", "Iowan Old Style", Georgia, serif;
  --serif:   "Source Serif 4", "Source Serif Pro", Charter, Georgia, "Times New Roman", serif;
  --sans:    "Inter Tight", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono:    "JetBrains Mono", "Fira Code", Menlo, Consolas, monospace;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: var(--serif);
  color: var(--ink);
  background: var(--bg);
  line-height: 1.72;
  font-size: 17px;
  font-feature-settings: "liga", "kern", "onum";
  -webkit-font-smoothing: antialiased;
}
h2, h3, h4, h5, h6, .sans { font-family: var(--sans); font-weight: 700; letter-spacing: -0.012em; color: var(--ink); }
h1 { font-family: var(--display); font-weight: 500; font-variation-settings: "SOFT" 50, "opsz" 120; letter-spacing: -0.022em; font-size: 2.65rem; line-height: 1.1; color: var(--navy); margin: 0 0 .9rem; }
h2 { font-size: 1.6rem; line-height: 1.25; margin: 3rem 0 1rem; color: var(--navy); position: relative; padding-bottom: .45rem; }
h2::after { content: ""; position: absolute; left: 0; bottom: 0; width: 42px; height: 3px; background: var(--gold); border-radius: 2px; }
h3 { font-size: 1.18rem; line-height: 1.3; margin: 1.75rem 0 .55rem; color: var(--ink); }
h4 { font-size: .78rem; line-height: 1.3; margin: 1.2rem 0 .4rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); font-weight: 700; }
p { margin: 0 0 1rem; }
a { color: var(--navy); text-decoration: underline; text-underline-offset: 2px; text-decoration-thickness: 1px; transition: color .15s; }
a:hover { color: var(--gold); }
code { font-family: var(--mono); font-size: .88em; background: var(--panel-2); padding: .14em .44em; border-radius: 4px; color: var(--navy); font-weight: 500; }
::selection { background: var(--gold-50); color: var(--ink); }

.layout { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; }

aside.sidebar { position: sticky; top: 0; align-self: start; height: 100vh; overflow-y: auto; background: var(--panel); border-right: 1px solid var(--rule); padding: 1.75rem 1.25rem; font-family: var(--sans); font-size: .875rem; }
.brand { font-family: var(--display); font-weight: 600; font-variation-settings: "SOFT" 30, "opsz" 36; color: var(--navy); font-size: 1.5rem; letter-spacing: -0.02em; line-height: 1; }
.brand small { display: block; color: var(--muted); font-weight: 500; font-size: .72rem; margin-top: .35rem; letter-spacing: .02em; font-family: var(--sans); line-height: 1.4; }
.brand::before { content: ""; display: block; width: 28px; height: 3px; background: var(--gold); border-radius: 2px; margin-bottom: .7rem; }
.nav-group { margin-top: 1.5rem; }
.nav-group-title { text-transform: uppercase; font-size: .68rem; letter-spacing: .08em; color: var(--muted); font-weight: 600; margin-bottom: .45rem; padding-left: .1rem; }
.sidebar a { display: block; padding: .42rem .6rem; border-radius: 6px; color: var(--ink); text-decoration: none; margin-bottom: 1px; }
.sidebar a:hover { background: var(--panel-2); color: var(--navy); }

main { padding: 3rem 4rem 6rem; max-width: 1080px; }
.page-eyebrow { font-family: var(--sans); font-size: .72rem; text-transform: uppercase; letter-spacing: .18em; color: var(--gold); font-weight: 700; margin-bottom: .7rem; display: inline-flex; align-items: center; gap: .65rem; }
.page-eyebrow::before { content: ""; width: 18px; height: 2px; background: var(--gold); display: inline-block; }
.lede { font-family: var(--serif); font-size: 1.18rem; line-height: 1.6; color: var(--muted); max-width: 62ch; }
.lede b { color: var(--ink); font-weight: 600; }

.hero { background: radial-gradient(1200px 380px at 85% -10%, rgba(176,135,0,.10), transparent 60%), radial-gradient(900px 500px at 0% 0%, rgba(26,31,58,.05), transparent 55%), linear-gradient(180deg, var(--panel) 0%, var(--paper) 100%); margin: -3rem -4rem 2.5rem; padding: 3.2rem 4rem 2.7rem; border-bottom: 1px solid var(--rule); position: relative; }
.hero::after { content: ""; position: absolute; left: 4rem; right: 4rem; bottom: 0; height: 2px; background: linear-gradient(90deg, var(--gold) 0, var(--gold) 80px, transparent 80px); }
.hero .meta-row { display: flex; flex-wrap: wrap; gap: .55rem; font-family: var(--sans); font-size: .78rem; color: var(--muted); margin-top: 1.4rem; }
.hero .meta-row span { background: rgba(255,255,255,.8); padding: .3rem .8rem; border-radius: 999px; border: 1px solid var(--rule); font-weight: 500; }

.concept-card { padding: 1.15rem 1.3rem; border: 1px solid var(--rule); border-left: 3px solid var(--navy); border-radius: 0 8px 8px 0; background: var(--paper); }
.concept-card h4 { margin: 0 0 .45rem; text-transform: none; letter-spacing: -0.008em; color: var(--ink); font-size: 1rem; font-weight: 700; font-family: var(--sans); }
.concept-card p { margin: 0; font-size: .95rem; color: var(--muted); line-height: 1.6; }

.pull-quote { font-family: var(--display); font-variation-settings: "SOFT" 60, "opsz" 60; font-style: italic; font-size: 1.45rem; font-weight: 400; line-height: 1.38; color: var(--ink); padding: 1.3rem 0 1.2rem 1.6rem; border-left: 3px solid var(--gold); margin: 1.8rem 0; position: relative; }
.pull-quote::before { content: "\201C"; position: absolute; left: 1rem; top: -.5rem; font-family: var(--display); font-size: 3.5rem; color: var(--gold-soft); opacity: .35; line-height: 1; }
.pull-quote cite { display: block; font-style: normal; font-family: var(--sans); font-size: .78rem; font-weight: 500; color: var(--muted); margin-top: .8rem; letter-spacing: .04em; text-transform: uppercase; }

.callout { padding: 1rem 1.2rem; background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; margin: 1.25rem 0; font-size: .93rem; }
.callout.check { border-left: 3px solid var(--teal); background: var(--teal-50); border-color: #c2e1e9; }
.callout.check .tt { font-family: var(--sans); font-weight: 700; font-size: .74rem; text-transform: uppercase; letter-spacing: .09em; color: var(--teal); margin-bottom: .4rem; }
.callout.disclosure { border-left: 3px solid var(--warn); background: var(--warn-50); border-color: #f1d99a; font-size: .9rem; }
.callout.disclosure .tt { font-family: var(--sans); font-weight: 700; font-size: .72rem; text-transform: uppercase; letter-spacing: .09em; color: var(--warn); margin-bottom: .35rem; }

.case-box { padding: 1.1rem 1.25rem; border: 1px solid var(--rule); border-radius: 8px; background: var(--paper); margin: 1.25rem 0; }
.case-box .case-head { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; margin-bottom: .5rem; border-bottom: 1px solid var(--rule); padding-bottom: .45rem; }
.case-box .case-head h3 { margin: 0; font-size: 1.05rem; }
.case-box .case-head .ticker { font-family: var(--mono); font-size: .78rem; color: var(--muted); }
.case-box .data-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: .6rem; margin: .7rem 0; }
.case-box .data-pt { font-family: var(--sans); }
.case-box .data-pt .n { display: block; font-family: var(--display); font-variation-settings: "SOFT" 40, "opsz" 48; font-size: 1.55rem; font-weight: 500; color: var(--navy); line-height: 1.05; letter-spacing: -0.02em; }
.case-box .data-pt .l { display: block; font-size: .75rem; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; margin-top: .2rem; }
.case-box .data-pt .src { display: block; font-family: var(--serif); font-size: .72rem; font-style: italic; color: var(--muted); margin-top: .25rem; }

.src-table { width: 100%; border-collapse: collapse; font-size: .84rem; margin: 1rem 0; }
.src-table th, .src-table td { padding: .5rem .6rem; text-align: left; border-bottom: 1px solid var(--rule); vertical-align: top; }
.src-table th { background: var(--panel); font-family: var(--sans); font-weight: 600; font-size: .72rem; text-transform: uppercase; letter-spacing: .05em; color: var(--muted); }
.src-table td:first-child { font-family: var(--sans); font-weight: 600; color: var(--navy); white-space: nowrap; }

.citations { font-size: .82rem; font-family: var(--sans); color: var(--muted); line-height: 1.5; padding: .8rem 1rem; background: var(--panel); border-radius: 6px; margin: 1rem 0; border-left: 2px solid var(--rule); }
.citations ol { margin: 0; padding-left: 1.2rem; }

.framework { padding: 1.25rem; background: var(--panel); border: 1px solid var(--rule); border-radius: 8px; margin: 1.25rem 0; }
.framework-title { font-family: var(--sans); font-weight: 700; font-size: .88rem; text-transform: uppercase; letter-spacing: .06em; color: var(--navy); margin-bottom: .7rem; }
svg.framework-svg { display: block; max-width: 100%; height: auto; margin: 0 auto; }

.page-footer { margin-top: 4rem; font-size: .85rem; color: var(--muted); }
.page-footer .small { font-size: .78rem; }

@media (max-width: 960px) {
  .layout { grid-template-columns: 1fr; }
  aside.sidebar { position: static; height: auto; border-right: 0; border-bottom: 1px solid var(--rule); }
  main { padding: 2rem 1.5rem 4rem; }
  .hero { margin: -2rem -1.5rem 1.5rem; padding: 2rem 1.5rem; }
}
```

- [ ] **Step 4.6: Write `print.css`**

Path: `Dev Assistant/assets/css/print.css`

```css
@page {
  size: A4 portrait;
  margin: 2.5cm 2.2cm;
  @top-left   { content: "MST304 · Manajemen Strategik Kontemporer"; font-family: "Inter Tight", sans-serif; font-size: 9pt; color: #595959; }
  @top-right  { content: string(section-title); font-family: "Inter Tight", sans-serif; font-size: 9pt; color: #595959; }
  @bottom-right { content: "Halaman " counter(page) " dari " counter(pages); font-family: "Inter Tight", sans-serif; font-size: 9pt; color: #595959; }
  @bottom-left  { content: "Dzaki — Magister Akuntansi STIE YKPN"; font-family: "Inter Tight", sans-serif; font-size: 9pt; color: #595959; }
}

aside.sidebar { display: none !important; }
.layout { display: block !important; }
main { padding: 0 !important; max-width: none !important; }
.hero { margin: 0 !important; background: none !important; border: 0 !important; padding: 0 0 1rem !important; }
.hero::after { display: none; }

body { font-size: 11pt; line-height: 1.55; color: #1a1a1a; background: #fff; }
h1 { font-size: 22pt; page-break-after: avoid; }
h2 { font-size: 15pt; page-break-before: always; page-break-after: avoid; string-set: section-title content(); }
h2:first-of-type { page-break-before: avoid; }
h3 { font-size: 12pt; page-break-after: avoid; }

p, ul, ol, blockquote { orphans: 3; widows: 3; }

.callout, .case-box, .framework, .citations, .pull-quote, .concept-card, .src-table, table { page-break-inside: avoid; }
svg.framework-svg { page-break-inside: avoid; max-width: 100%; height: auto; }

a { color: #1a1a1a; text-decoration: none; }
a::after { content: ""; }

.page-footer { margin-top: 2rem; }
```

- [ ] **Step 4.7: Commit**

```bash
git add "Dev Assistant/templates/" "Dev Assistant/assets/"
git commit -m "feat(dev-assistant): base + 3 section templates + editorial scholar CSS + print.css"
```

---

## Task 5 — HTML builder orchestrator + asset copier

**Files:**
- Modify: `Dev Assistant/src/html_builder/engine.rs`
- Modify: `Dev Assistant/src/html_builder/assets.rs`
- Modify: `Dev Assistant/src/html_builder/mod.rs`
- Modify: `Dev Assistant/src/main.rs`
- Create: `Dev Assistant/tests/html_builder.rs`

- [ ] **Step 5.1: Write the failing integration test**

Path: `Dev Assistant/tests/html_builder.rs`

```rust
use dev_assistant::html_builder;
use dev_assistant::model::config::load_weeks;
use std::fs;
use std::path::PathBuf;

#[test]
fn renders_study_guide_for_week_one() {
    let weeks = load_weeks(&PathBuf::from("configs/week-mapping.toml")).unwrap();
    let week_one = weeks.into_iter().find(|w| w.num == 1).unwrap();
    let html = html_builder::render_section(
        &week_one,
        "study_guide",
        "Study Guide / Aid",
        "<h2>Reading Order</h2><p>First read TPGS Ch.1.</p>",
    )
    .expect("render succeeds");

    assert!(html.contains("<h1>"), "h1 must be present");
    assert!(html.contains("Minggu 01"), "week number must appear");
    assert!(html.contains("Astra International"), "flagship name must appear");
    assert!(html.contains("Reading Order"), "injected content must appear");
}
```

- [ ] **Step 5.2: Implement the minijinja engine**

Path: `Dev Assistant/src/html_builder/engine.rs` (replace stub)

```rust
use crate::error::Result;
use minijinja::{path_loader, Environment};

pub fn build_env(template_dir: &std::path::Path) -> Result<Environment<'static>> {
    let mut env = Environment::new();
    env.set_loader(path_loader(template_dir));
    Ok(env)
}
```

- [ ] **Step 5.3: Implement the asset copier**

Path: `Dev Assistant/src/html_builder/assets.rs` (replace stub)

```rust
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
```

- [ ] **Step 5.4: Implement the orchestrator**

Path: `Dev Assistant/src/html_builder/mod.rs` (replace stub)

```rust
pub mod engine;
pub mod assets;

use crate::content_loader::{load_section, markdown::render as md_render};
use crate::error::Result;
use crate::model::Week;
use minijinja::context;
use std::fs;
use std::path::{Path, PathBuf};

/// Turn Markdown fragments in `content/week-NN/<section>/` into one concatenated HTML string
/// (concept-check callouts, frameworks, pull-quotes can all be inline-HTML inside Markdown).
pub fn compile_section_body(week_num: u8, section: &str, content_root: &Path) -> Result<String> {
    let dir = content_root
        .join(format!("week-{:02}", week_num))
        .join(section);
    let fragments = load_section(&dir)?;
    let mut out = String::new();
    for f in fragments {
        out.push_str(&md_render(&f.body));
    }
    Ok(out)
}

/// Build an anchor list for sidebar nav by scanning `<h2>` tags in the compiled body.
pub fn extract_anchors(body_html: &str) -> Vec<(String, String)> {
    // Minimal heuristic: look for "<h2>Text</h2>" patterns.
    let mut acc = Vec::new();
    let mut cursor = 0;
    while let Some(start) = body_html[cursor..].find("<h2>") {
        let abs_start = cursor + start + 4;
        if let Some(end) = body_html[abs_start..].find("</h2>") {
            let text = &body_html[abs_start..abs_start + end];
            let id = slugify(text);
            acc.push((id, text.to_string()));
            cursor = abs_start + end + 5;
        } else {
            break;
        }
    }
    acc
}

fn slugify(s: &str) -> String {
    s.chars()
        .filter_map(|c| {
            if c.is_ascii_alphanumeric() { Some(c.to_ascii_lowercase()) }
            else if c.is_whitespace() || c == '-' { Some('-') }
            else { None }
        })
        .collect::<String>()
        .split('-')
        .filter(|s| !s.is_empty())
        .collect::<Vec<_>>()
        .join("-")
}

/// Render a section (study_guide | summary | indonesian) for one week and return the full HTML.
/// `pre_rendered_body` lets callers (tests) inject HTML without going through the Markdown loader.
pub fn render_section(
    week: &Week,
    section_key: &str,
    output_eyebrow: &str,
    pre_rendered_body: &str,
) -> Result<String> {
    let env = engine::build_env(Path::new("templates"))?;
    let template_name = match section_key {
        "study_guide" => "week-study-guide.html.j2",
        "summary"     => "week-summary.html.j2",
        "indonesian"  => "week-indonesian.html.j2",
        _ => return Err(crate::error::BuildError::Config(format!("unknown section: {section_key}"))),
    };
    let tmpl = env.get_template(template_name)?;
    let anchors: Vec<_> = extract_anchors(pre_rendered_body)
        .into_iter()
        .map(|(id, title)| context!(id => id, title => title))
        .collect();

    let (page_title, lede) = section_titles(week, section_key);

    let ctx = context! {
        week => week,
        page_title => page_title,
        lede => lede,
        output_eyebrow => output_eyebrow,
        content => pre_rendered_body,
        anchors => anchors,
    };
    Ok(tmpl.render(ctx)?)
}

fn section_titles(week: &Week, section_key: &str) -> (String, String) {
    match section_key {
        "study_guide" => (
            format!("Study Guide — {}", week.topic_id),
            format!("Panduan belajar terstruktur untuk minggu ini: urutan membaca, konsep inti, koneksi antar-minggu, dan fokus diskusi untuk topik \"{}\".", week.topic_en),
        ),
        "summary" => (
            format!("Main Summary — {}", week.topic_id),
            format!("Sintesis akademik lengkap dari referensi wajib minggu ini. Kerangka dirender sebagai diagram SVG; istilah kunci ditampilkan dua-bahasa untuk mendukung pembacaan teks asli."),
        ),
        "indonesian" => (
            format!("Contoh Perusahaan Indonesia — {}", week.topic_id),
            format!("Flagship {} sebagai jangkar konsep minggu ini, dilengkapi contoh komparatif dari perusahaan lain. Semua data diperoleh dari materi publik yang diungkapkan perusahaan.", week.indo_flagship.name),
        ),
        _ => (week.topic_id.clone(), String::new()),
    }
}

/// End-to-end: load fragments, render section, write to disk.
pub fn build_week_section(
    week: &Week,
    section_key: &str,
    content_root: &Path,
    output_root: &Path,
    section_folder: &str,
    output_eyebrow: &str,
) -> Result<PathBuf> {
    let body = compile_section_body(week.num, section_key, content_root)?;
    let html = render_section(week, section_key, output_eyebrow, &body)?;

    let week_folder = format!("Week {:02}", week.num);
    let out_dir = output_root.join(section_folder).join(&week_folder);
    fs::create_dir_all(&out_dir)?;
    let out_file = out_dir.join("index.html");
    fs::write(&out_file, html)?;

    let assets_src = Path::new("assets/css");
    let assets_dst = out_dir.join("assets");
    assets::copy_css(assets_src, &assets_dst)?;

    Ok(out_file)
}
```

- [ ] **Step 5.5: Wire up the `build` command in `main.rs`**

Path: `Dev Assistant/src/main.rs` (replace previous version)

```rust
use clap::{Parser, Subcommand};
use dev_assistant::html_builder;
use dev_assistant::model::config::load_weeks;
use std::path::{Path, PathBuf};

#[derive(Parser)]
#[command(name = "dev-assistant", version, about = "MST304 course support system pipeline")]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Subcommand)]
enum Command {
    /// Build all weeks (use --week N to limit)
    Build {
        #[arg(long)]
        week: Option<u8>,
    },
    /// Remove generated outputs under course-materials/outputs/ (excluding Visual Companion)
    Clean,
    /// Verify every week's output HTML exists and is non-empty
    Verify,
}

const SECTIONS: &[(&str, &str, &str)] = &[
    ("study_guide", "Study Guide - Aid",            "Study Guide / Aid"),
    ("summary",     "Main Summary - Ebook",         "Main Summary / Ebook"),
    ("indonesian",  "Indonesian Company Examples",  "Contoh Perusahaan Indonesia"),
];

fn main() -> anyhow::Result<()> {
    let cli = Cli::parse();
    let content_root = PathBuf::from("content");
    let output_root  = PathBuf::from("../course-materials/outputs");

    match cli.command {
        Command::Build { week } => {
            let weeks = load_weeks(&PathBuf::from("configs/week-mapping.toml"))?;
            let filtered: Vec<_> = weeks.into_iter().filter(|w| week.map_or(true, |n| w.num == n)).collect();
            if filtered.is_empty() {
                eprintln!("no weeks matched filter {:?}", week);
                std::process::exit(2);
            }
            for w in &filtered {
                let week_content_root = content_root.clone();
                let has_any = SECTIONS.iter().any(|(key, _, _)| {
                    week_content_root.join(format!("week-{:02}", w.num)).join(key).exists()
                });
                if !has_any {
                    println!("week {:02}: no content fragments yet — skipping", w.num);
                    continue;
                }
                for (key, folder, eyebrow) in SECTIONS {
                    let section_dir = week_content_root.join(format!("week-{:02}", w.num)).join(key);
                    if !section_dir.exists() { continue; }
                    let out = html_builder::build_week_section(
                        w, key, &content_root, &output_root, folder, eyebrow,
                    )?;
                    println!("  wrote {}", out.display());
                }
            }
            println!("build complete.");
        }
        Command::Clean => {
            for (_, folder, _) in SECTIONS {
                let p = Path::new("../course-materials/outputs").join(folder);
                if p.exists() {
                    for entry in std::fs::read_dir(&p)? {
                        let entry = entry?;
                        if entry.file_type()?.is_dir() {
                            std::fs::remove_dir_all(entry.path())?;
                        }
                    }
                    println!("cleaned {}", p.display());
                }
            }
        }
        Command::Verify => {
            let weeks = load_weeks(&PathBuf::from("configs/week-mapping.toml"))?;
            let mut fail = false;
            for w in &weeks {
                for (_, folder, _) in SECTIONS {
                    let p = Path::new("../course-materials/outputs")
                        .join(folder)
                        .join(format!("Week {:02}", w.num))
                        .join("index.html");
                    if !p.exists() {
                        println!("MISSING: {}", p.display()); fail = true;
                    } else {
                        let size = std::fs::metadata(&p)?.len();
                        if size < 1000 { println!("TOO SMALL (<1KB): {}", p.display()); fail = true; }
                    }
                }
            }
            if fail { std::process::exit(3); }
            println!("verify: all present and non-trivial.");
        }
    }
    Ok(())
}
```

- [ ] **Step 5.6: Run all tests**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik/Dev Assistant"
cargo test
```

Expected: 8 passing (frontmatter: 3, markdown: 3, content_loader: 1, html_builder: 1, config_load: 3 — wait, that's 11; point is all green).

- [ ] **Step 5.7: Commit**

```bash
git add "Dev Assistant/src/html_builder/" "Dev Assistant/src/main.rs" "Dev Assistant/tests/html_builder.rs"
git commit -m "feat(dev-assistant): html builder orchestrator + asset copier + wired CLI"
```

---

## Task 6 — Week 1 meta + Study Guide content

**Files:**
- Create: `Dev Assistant/content/week-01/_meta.toml`
- Create: `Dev Assistant/content/week-01/study-guide/01-reading-order.md`
- Create: `Dev Assistant/content/week-01/study-guide/02-central-concepts.md`
- Create: `Dev Assistant/content/week-01/study-guide/03-connections.md`
- Create: `Dev Assistant/content/week-01/study-guide/04-focus-and-check.md`

- [ ] **Step 6.1: Write `_meta.toml` (per-week override)**

Path: `Dev Assistant/content/week-01/_meta.toml`

```toml
# Week-specific overrides. Currently structural-only; reserved for future customization.
week_num = 1
authoring_notes = "Week 1 is the framework week: it sets the scaffolding for how every subsequent week will be studied."
```

- [ ] **Step 6.2: Write `01-reading-order.md`**

Path: `Dev Assistant/content/week-01/study-guide/01-reading-order.md`

```markdown
---
title: Urutan Membaca
order: 1
---

## Urutan Membaca (Reading Order)

Minggu pertama adalah *framework week*. Tujuannya bukan menguasai detail, melainkan membangun peta mental tentang **apa itu strategi**, mengapa strategi menjadi pembeda antara perusahaan yang tumbuh dan yang stagnan, dan bagaimana seorang *graduate student* akan mempelajari seluruh mata kuliah ini selama 14 minggu. Ikuti urutan membaca di bawah ini — urutan ini sengaja dirancang dari yang paling dasar ke yang paling aplikatif, agar Anda tidak melompat ke kerangka analitis sebelum memahami pertanyaan fundamentalnya.

<div class="concept-card">
<h4>Langkah 1 — Silabus MSK TA 2025/2026 (15 menit)</h4>
<p>Baca bagian B (Deskripsi), C (CPL), dan D (CPMK) sekali. Tujuannya bukan menghafal, tetapi memahami <em>kompetensi akhir</em> yang menjadi target mata kuliah ini — khususnya CPMK Keterampilan Khusus nomor 1 (menyusun arah pengembangan perusahaan) dan nomor 2 (mengevaluasi lingkungan, sumber daya, dan daya saing).</p>
</div>

<div class="concept-card">
<h4>Langkah 2 — TPGS Bab 1 "Strategy, Business Models, and Competitive Advantage" (90 menit)</h4>
<p>Ini adalah bab inti minggu ini. Baca dengan pensil di tangan. Tandai definisi <em>strategy</em>, <em>business model</em>, <em>competitive advantage</em>, dan <em>sustained competitive advantage</em>. Di akhir bab, jawab sendiri pertanyaan: "Dalam satu paragraf, apa beda antara strategi dan model bisnis?" Jika belum bisa, baca ulang halaman yang sama.</p>
</div>

<div class="concept-card">
<h4>Langkah 3 — Anthony Henry Bab 1 "What is Strategy?" (60 menit)</h4>
<p>Henry memberi sudut pandang komplementer — lebih historis (Mintzberg, 5 P-strategy), lebih reflektif terhadap sifat strategi sebagai proses. TPGS dan Henry bersama-sama membentuk "dua pintu masuk" ke disiplin ini: TPGS lebih praktis-preskriptif (Amerika-Utara), Henry lebih konseptual-kritis (tradisi Eropa).</p>
</div>

<div class="concept-card">
<h4>Langkah 4 — Main Summary (halaman ini) (45 menit)</h4>
<p>Setelah membaca TPGS + Henry, datanglah ke dokumen <strong>Main Summary Minggu 1</strong>. Ringkasannya akan menyederhanakan dan menyusun kembali kedua bab, serta menghubungkannya dengan konteks Indonesia. Gunakan sebagai <em>check</em> bahwa pemahaman Anda sudah tepat.</p>
</div>

<div class="concept-card">
<h4>Langkah 5 — Indonesian Company Example (30 menit)</h4>
<p>Bacaan terakhir adalah studi kasus Astra International (flagship minggu ini) ditambah sidebar Unilever Indonesia dan Indofood. Di sinilah teori menjadi hidup: lihat bagaimana tiga perusahaan Indonesia dengan strategi berbeda sama-sama menciptakan keunggulan bersaing yang tahan lama — dan gunakan kasus-kasus ini sebagai bank contoh untuk presentasi, tugas, dan ujian.</p>
</div>

> **Estimasi total waktu belajar minggu 1: ±4 jam**, di luar 150 menit tatap muka. Minggu-minggu berikutnya akan lebih berat (karena ada artikel jurnal yang wajib dibaca) — lakukan investasi waktu ini di minggu 1 agar kerangkanya kokoh.
```

- [ ] **Step 6.3: Write `02-central-concepts.md`**

Path: `Dev Assistant/content/week-01/study-guide/02-central-concepts.md`

```markdown
---
title: Konsep Inti
order: 2
---

## Empat Konsep Inti yang Wajib Dikuasai

Minggu 1 membangun empat fondasi konseptual. Jika salah satu belum jernih, jangan maju ke Minggu 2 — seluruh mata kuliah 14 minggu duduk di atas empat tiang ini.

<div class="concept-card">
<h4>1. Strategi (<em>Strategy</em>)</h4>
<p>Strategi adalah <strong>pilihan yang dibuat manajemen tentang bagaimana perusahaan akan bersaing, melayani pelanggan, dan menciptakan nilai</strong>. Bukan sekadar perencanaan; bukan sekadar tujuan. Inti strategi adalah <em>choice</em> — memilih untuk melakukan X dan tidak melakukan Y. Porter (1996): "Competitive strategy is about being different." Pilihan ini harus <em>koheren</em> (saling menguatkan) dan <em>sulit ditiru</em> agar bertahan.</p>
</div>

<div class="concept-card">
<h4>2. Model Bisnis (<em>Business Model</em>)</h4>
<p>Model bisnis adalah <strong>logika operasional tentang bagaimana perusahaan menghasilkan pendapatan dan keuntungan dari strategi yang dipilih</strong>. Dua komponen utama: <em>customer value proposition</em> (CVP) dan <em>profit formula</em>. Strategi tanpa model bisnis = niat baik yang tak terbukti finansial. Model bisnis tanpa strategi = mesin uang tanpa arah kompetitif.</p>
</div>

<div class="concept-card">
<h4>3. Keunggulan Bersaing (<em>Competitive Advantage</em>) vs. yang Berkelanjutan (<em>Sustained</em>)</h4>
<p>Sebuah perusahaan memiliki keunggulan bersaing ketika <strong>ia memberikan nilai pembeli yang lebih tinggi daripada pesaing</strong> — baik melalui biaya lebih rendah maupun diferensiasi yang lebih bernilai. Keunggulan menjadi <em>sustained</em> ketika pesaing gagal menirunya dalam waktu yang lama, biasanya karena ada <em>isolating mechanisms</em>: sumber daya langka, kemampuan organisasional tacit, efek jaringan, atau reputasi merek yang mahal dibangun.</p>
</div>

<div class="concept-card">
<h4>4. Strategi sebagai <em>Deliberate</em> + <em>Emergent</em> (Mintzberg)</h4>
<p>Strategi bukan dokumen statis. Menurut Mintzberg (Henry Bab 1), strategi aktual perusahaan adalah campuran dari <strong>strategi yang direncanakan dengan sengaja</strong> (<em>deliberate</em>) dan <strong>strategi yang muncul dari pembelajaran dan adaptasi</strong> (<em>emergent</em>). Di lingkungan yang turbulen (akan dibahas pada Minggu 3, lihat Mason 2007), porsi <em>emergent</em> cenderung meningkat.</p>
</div>
```

- [ ] **Step 6.4: Write `03-connections.md`**

Path: `Dev Assistant/content/week-01/study-guide/03-connections.md`

```markdown
---
title: Koneksi Antar-Minggu
order: 3
---

## Bagaimana Minggu 1 Terhubung ke Seluruh Mata Kuliah

Empat konsep inti di atas bukan tujuan akhir — mereka adalah *entry point*. Tiap konsep akan diperluas, diuji, dan diimplementasikan di minggu-minggu berikutnya. Gunakan peta di bawah ini sebagai peta jalan personal Anda.

| Minggu | Konsep Minggu 1 yang Diperluas | Bagaimana |
|--------|-------------------------------|-----------|
| 2 | **Strategi sebagai proses** | TPGS Ch.2 mengurai lima tahap proses manajerial pembuatan & eksekusi strategi. Visi-misi menjadi input awal. |
| 3 | **Konteks pilihan strategi** | TPGS Ch.3 + Mason 2007 menunjukkan bagaimana lingkungan eksternal membentuk ruang pilihan strategi. |
| 4 | **Keunggulan bersaing berkelanjutan** | TPGS Ch.4 (VRIN, Barney 1991) menjelaskan <em>mengapa</em> beberapa keunggulan bertahan. |
| 5–7 | **Jenis strategi bersaing** | Lima strategi generik, strategi pelengkap, dan penyesuaian industri memberikan kosakata pilihan konkret. |
| 8 | **Strategi di pasar internasional** | Pilihan geografi sebagai dimensi tambahan strategi. |
| 9 | **Strategi korporat & diversifikasi** | Beberapa pilihan strategi sekaligus dalam satu perusahaan multibisnis. |
| 10 | **Etika, CSR, keberlanjutan** | Strategi dengan batasan moral dan lingkungan. |
| 11 | **Eksekusi strategi** | Menghubungkan pilihan strategis dengan operasional. |
| 12–14 | **Topik lanjutan** | Model bisnis baru, stakeholder engagement, hiperkompetisi, dan kepemimpinan strategis. |
```

- [ ] **Step 6.5: Write `04-focus-and-check.md`**

Path: `Dev Assistant/content/week-01/study-guide/04-focus-and-check.md`

```markdown
---
title: Fokus Diskusi + Self-Check
order: 4
---

## Fokus Diskusi Kelas

Pada tatap-muka Minggu 1, silabus mencatat aktivitas berupa **penjelasan silabus dan pembagian tugas**, bukan presentasi kelompok. Namun dosen kemungkinan tetap akan menguji pemahaman konseptual awal. Siapkan diri untuk empat sudut pertanyaan berikut:

1. **Definisi operasional**: Dalam dua kalimat, apa beda strategi dan model bisnis? Berikan satu contoh perusahaan Indonesia di mana keduanya dapat dipisahkan.
2. **Sumber keunggulan**: Mengapa BCA dapat mempertahankan margin dan pangsa pasar selama dua dekade, sementara banyak bank seukuran BCA mengalami erosi? Kaitkan dengan konsep *sustained competitive advantage*.
3. **Deliberate vs emergent**: Ambil satu perusahaan Indonesia yang Anda kenal. Identifikasi satu elemen strateginya yang jelas-jelas *deliberate* dan satu yang jelas-jelas *emergent*. Jelaskan mengapa.
4. **Pertanyaan reflektif**: Mengapa strategi yang bagus di atas kertas sering gagal dieksekusi? Ini akan kembali di Minggu 11 — mulai berpikir sekarang.

## Self-Check Questions (Pemeriksa Konsep)

<div class="callout check">
<div class="tt">Pemeriksa Konsep · Minggu 1</div>
<p><strong>SC1.</strong> Tulis dalam 3–5 kalimat: jika Anda adalah konsultan strategi dan klien meminta Anda menjelaskan "apa itu strategi" dalam bahasa yang dapat dipahami CEO non-MBA, bagaimana Anda menjelaskannya tanpa menggunakan istilah <em>value chain</em>, <em>VRIN</em>, atau <em>five forces</em>?</p>

<p><strong>SC2.</strong> Pilih satu dari tiga perusahaan contoh Indonesia Minggu 1 (Astra, Unilever Indonesia, atau Indofood). Identifikasi: (a) strategi utamanya, (b) model bisnis pendukung, (c) sumber keunggulan bersaingnya, dan (d) mengapa keunggulan itu sulit ditiru pesaing.</p>

<p><strong>SC3.</strong> Jelaskan dalam satu paragraf: mengapa Mintzberg berargumen bahwa strategi selalu merupakan campuran <em>deliberate</em> dan <em>emergent</em>? Berikan contoh Indonesia.</p>
</div>

> **Cara memakai:** jawab ketiga pertanyaan ini di buku catatan sebelum Minggu 2. Kembalilah ke Main Summary Minggu 1 untuk mengecek jawaban Anda. Jangan lewati proses ini — SC ini adalah latihan UTS miniatur.
```

- [ ] **Step 6.6: Build Week 1 Study Guide and verify**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik/Dev Assistant"
cargo run -- build --week 1
```

Expected output lines include:
```
  wrote ../course-materials/outputs/Study Guide - Aid/Week 01/index.html
  wrote ../course-materials/outputs/Main Summary - Ebook/Week 01/index.html
  wrote ../course-materials/outputs/Indonesian Company Examples/Week 01/index.html
build complete.
```

(Notes: Main Summary and Indonesian folders will only build once Tasks 7 and 8 are done. For now if those content dirs don't exist yet, the orchestrator logs "no content fragments yet — skipping" for those sections. The Study Guide must render.)

- [ ] **Step 6.7: Open the generated Study Guide in browser**

```bash
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Study Guide - Aid\Week 01\index.html"
```

Expected: browser opens; page shows the Editorial Scholar design (gold eyebrow, Fraunces H1, sidebar nav, Source Serif body). Content matches the four fragments just written.

- [ ] **Step 6.8: Commit**

```bash
git add "Dev Assistant/content/week-01/"
git commit -m "content(week-01): Study Guide — reading order, central concepts, connections, check"
```

---

## Task 7 — Week 1 Main Summary content

**Files:**
- Create: `Dev Assistant/content/week-01/summary/01-overview.md`
- Create: `Dev Assistant/content/week-01/summary/02-strategy-defined.md`
- Create: `Dev Assistant/content/week-01/summary/03-business-models.md`
- Create: `Dev Assistant/content/week-01/summary/04-competitive-advantage.md`
- Create: `Dev Assistant/content/week-01/summary/05-mintzberg-deliberate-emergent.md`
- Create: `Dev Assistant/content/week-01/summary/06-references-and-check.md`

- [ ] **Step 7.1: Write `01-overview.md`**

Path: `Dev Assistant/content/week-01/summary/01-overview.md`

```markdown
---
title: Ikhtisar Bab
order: 1
---

## Ikhtisar Minggu 1

Referensi: **TPGS Ch.1** *(Strategy, Business Models, and Competitive Advantage)* · **Henry Ch.1** *(What is Strategy?)*

Pada bab pembuka TPGS, Gamble, Peteraf, dan Thompson menetapkan dua klaim fundamental yang akan terus dipakai sepanjang buku: **(1)** strategi adalah pilihan manajerial yang dibuat secara sengaja tentang bagaimana perusahaan bersaing, dan **(2)** strategi yang baik harus menghasilkan <em>competitive advantage</em> yang menyokong kinerja jangka panjang. Anthony Henry melengkapi dengan perspektif proses: strategi bukan sekadar rencana, melainkan pola tindakan yang muncul dari interaksi antara niat manajerial dan respons terhadap lingkungan.

<div class="pull-quote">
The essence of strategy is choosing to perform activities differently than rivals do.
<cite>Michael Porter — Harvard Business Review, 1996</cite>
</div>

Kutipan Porter adalah kompas minggu ini. Perusahaan yang hanya <em>operational excellent</em> (lebih efisien dari pesaing pada rantai aktivitas yang sama) akan kehilangan keunggulannya saat pesaing menyalin praktik tersebut. Strategi sesungguhnya menuntut **pilihan rangkaian aktivitas yang berbeda** sehingga <em>trade-off</em> menjadi mekanisme pertahanan alami.
```

- [ ] **Step 7.2: Write `02-strategy-defined.md`**

Path: `Dev Assistant/content/week-01/summary/02-strategy-defined.md`

```markdown
---
title: Definisi Strategi
order: 2
---

## Mendefinisikan Strategi

Definisi kerja TPGS: **strategi adalah rencana tindakan manajerial untuk mengelola operasi, bersaing secara efektif, memuaskan pelanggan, dan mencapai target kinerja.** Definisi ini kelihatan sederhana, tetapi membawa empat implikasi yang sering terlewatkan:

<div class="concept-card">
<h4>Implikasi 1 — Strategi = Pilihan</h4>
<p>Strategi bukanlah "semua yang baik yang dilakukan perusahaan". Strategi adalah <em>commitment</em> terhadap serangkaian pilihan yang <em>mutually exclusive</em> dengan pilihan alternatif. Contoh: Indofood memilih cost leadership di kategori instant noodle — dan pilihan itu berarti tidak menggarap segmen premium-artisanal (di mana Mie Shoryu atau Nissin Cup Noodles Premium bermain).</p>
</div>

<div class="concept-card">
<h4>Implikasi 2 — Strategi ≠ Rencana Tahunan</h4>
<p>Rencana tahunan (<em>annual operating plan</em>) adalah konsekuensi operasional dari strategi, bukan strategi itu sendiri. Rencana tahunan menjawab "apa yang akan kita lakukan tahun ini"; strategi menjawab "kenapa kita percaya ini akan menghasilkan keunggulan bersaing yang tahan lama".</p>
</div>

<div class="concept-card">
<h4>Implikasi 3 — Strategi Ditandai oleh <em>Trade-offs</em></h4>
<p>Porter: di pasar yang sudah dewasa, setiap pilihan strategis membuat sebagian pelanggan lebih puas dan sebagian lagi tidak terlayani. Perusahaan yang ingin "melayani semua orang" biasanya berakhir tanpa keunggulan — inilah sindrom <em>stuck in the middle</em> yang akan dibahas mendalam pada Minggu 5.</p>
</div>

<div class="concept-card">
<h4>Implikasi 4 — Strategi Harus Koheren</h4>
<p>Pilihan-pilihan strategis harus saling menguatkan (<em>activity system</em> Porter). Contoh: keputusan Unilever Indonesia untuk membangun distribusi ke warung-warung mikro mendukung pilihan portofolio produk mass-market, yang pada gilirannya mendukung kapabilitas manufaktur skala besar. Masing-masing pilihan saling mengunci (<em>reinforce</em>) yang lain.</p>
</div>

### Strategi vs. Taktik vs. Tujuan

| Istilah | Definisi | Contoh Astra International |
|---------|----------|----------------------------|
| **Visi** | Citra masa depan perusahaan | "Sejahtera bersama bangsa" |
| **Misi** | Alasan keberadaan perusahaan | Empat pilar: otomotif, jasa keuangan, alat berat, infrastruktur |
| **Tujuan** | Target terukur | Pertumbuhan laba bersih >8% per tahun |
| **Strategi** | Pilihan cara mencapai tujuan | Diversifikasi ke sektor non-siklikal (consumer, infrastruktur) |
| **Taktik** | Aksi spesifik | Akuisisi saham PT Bank Jasa Jakarta (menjadi Bank Saqu) |
```

- [ ] **Step 7.3: Write `03-business-models.md`**

Path: `Dev Assistant/content/week-01/summary/03-business-models.md`

```markdown
---
title: Model Bisnis
order: 3
---

## Model Bisnis — Uji Kelayakan Strategi

Strategi adalah pilihan; **model bisnis** adalah bukti bahwa pilihan itu dapat menghasilkan uang. TPGS memisahkan keduanya dengan tegas karena banyak strategi yang indah di kertas namun gagal di laba-rugi.

### Dua Komponen Inti

<div class="framework">
<div class="framework-title">Kerangka Model Bisnis — TPGS Ch.1</div>
<svg class="framework-svg" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style><![CDATA[
      .bm-box { fill: #faf8f4; stroke: #1a1f3a; stroke-width: 1.2; }
      .bm-t { font-family: "Inter Tight", sans-serif; font-size: 12px; font-weight: 700; fill: #1a1f3a; }
      .bm-s { font-family: "Source Serif 4", serif; font-size: 10px; fill: #595959; }
      .bm-arrow { stroke: #b08700; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
    ]]></style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#b08700"/>
    </marker>
  </defs>
  <rect x="20"  y="40" width="220" height="130" rx="6" class="bm-box"/>
  <text x="30"  y="68" class="bm-t">Customer Value Proposition</text>
  <text x="30"  y="90" class="bm-s">• Pelanggan target yang dilayani</text>
  <text x="30" y="106" class="bm-s">• Masalah pelanggan yang diatasi</text>
  <text x="30" y="122" class="bm-s">• Produk/layanan yang ditawarkan</text>
  <text x="30" y="138" class="bm-s">• Harga &amp; mekanisme penciptaan nilai</text>
  <rect x="360" y="40" width="220" height="130" rx="6" class="bm-box"/>
  <text x="370" y="68" class="bm-t">Profit Formula</text>
  <text x="370" y="90" class="bm-s">• Struktur pendapatan</text>
  <text x="370" y="106" class="bm-s">• Struktur biaya &amp; margin</text>
  <text x="370" y="122" class="bm-s">• Pemanfaatan sumber daya</text>
  <text x="370" y="138" class="bm-s">• Kebutuhan modal &amp; arus kas</text>
  <path d="M250 105 L350 105" class="bm-arrow"/>
  <text x="270" y="98" class="bm-t" style="fill:#b08700">menghasilkan</text>
</svg>
</div>

<div class="concept-card">
<h4>Customer Value Proposition (CVP)</h4>
<p>Janji nilai kepada pelanggan: <em>"Mengapa pelanggan memilih kami daripada pesaing?"</em> CVP yang kuat menjawab kebutuhan nyata dengan cara yang sulit ditiru. Contoh: CVP Tokopedia di awal berdiri (2009) adalah <em>"pasar online yang aman untuk penjual UMKM Indonesia, dengan escrow system yang tidak dimiliki eBay atau Kaskus"</em>.</p>
</div>

<div class="concept-card">
<h4>Profit Formula</h4>
<p>Logika finansial: <em>"Bagaimana janji nilai itu diterjemahkan menjadi laba?"</em> Mencakup struktur pendapatan (subscription, transactional, freemium, dsb.), struktur biaya (fixed vs. variable), margin kotor/bersih yang dapat dicapai, dan kebutuhan modal kerja. Startup yang gagal biasanya memiliki CVP yang bagus tetapi profit formula yang tidak <em>viable</em> (misalnya biaya customer acquisition lebih tinggi dari lifetime value).</p>
</div>

### Uji Cepat: Apakah Model Bisnis Ini Layak?

Tiga pertanyaan yang harus dijawab <em>yes</em>:

1. **Apakah CVP jelas menjawab <em>job-to-be-done</em> pelanggan nyata?** (Bukan "orang yang membutuhkan solusi holistik" — pelanggan sungguhan dengan <em>willingness to pay</em> yang terukur.)
2. **Apakah Profit Formula memungkinkan unit economics positif pada skala yang realistis?** (Margin per transaksi × volume berkelanjutan > biaya tetap + investasi.)
3. **Apakah ada mekanisme pembeda yang membuat pesaing sulit menyalin kombinasi CVP + Profit Formula ini?** (Tanpa ini, keunggulan akan tererosi cepat.)
```

- [ ] **Step 7.4: Write `04-competitive-advantage.md`**

Path: `Dev Assistant/content/week-01/summary/04-competitive-advantage.md`

```markdown
---
title: Keunggulan Bersaing
order: 4
---

## Keunggulan Bersaing dan yang Berkelanjutan

Sebuah perusahaan memiliki **keunggulan bersaing** (<em>competitive advantage</em>) ketika ia **menciptakan nilai pembeli yang lebih tinggi daripada pesaing**, melalui salah satu dari dua jalur:

1. **Biaya lebih rendah untuk paket nilai yang setara** (<em>cost leadership</em>)
2. **Nilai yang dibayar premium karena diferensiasi yang sungguh-sungguh bernilai bagi pelanggan** (<em>differentiation</em>)

Ketika keunggulan tersebut **bertahan bertahun-tahun meski pesaing mencoba menirunya**, ia menjadi <em>sustained competitive advantage</em> (SCA). Kata kunci: <em>bertahan</em>. Dalam pasar yang dinamis, tidak ada keunggulan yang kekal — yang ada adalah keunggulan yang bertahan lebih lama dari rata-rata industri.

### Lima Mekanisme Isolasi (<em>Isolating Mechanisms</em>)

Apa yang membuat keunggulan bertahan? Literatur strategi mengidentifikasi lima mekanisme yang menahan imitasi pesaing:

<div class="concept-card">
<h4>1. Sumber Daya Langka &amp; Tidak Mudah Direplikasi</h4>
<p>Contoh: lokasi real estate premium, paten teknologi, lisensi eksklusif, spektrum frekuensi telekomunikasi. Telkomsel memiliki porsi spektrum frekuensi yang tidak mungkin didapatkan pesaing tanpa lelang pemerintah berikutnya — ini adalah mekanisme isolasi struktural.</p>
</div>

<div class="concept-card">
<h4>2. Kemampuan Organisasional (<em>Capabilities</em>) yang <em>Tacit</em></h4>
<p>Kemampuan yang terbentuk melalui pengalaman bertahun-tahun dan tersebar di banyak anggota organisasi (<em>know-how</em> tertanam). Contoh: kemampuan underwriting kredit konsumer BCA yang sulit diduplikasi bank pesaing meski memakai software yang sama.</p>
</div>

<div class="concept-card">
<h4>3. Efek Jaringan (<em>Network Effects</em>)</h4>
<p>Nilai produk meningkat seiring jumlah pengguna. Contoh: Gojek-Grab. Setiap driver baru meningkatkan nilai aplikasi bagi konsumen; setiap konsumen baru meningkatkan nilai bagi driver. Pesaing baru harus menyeberangi jurang nilai besar untuk mencapai titik viabilitas.</p>
</div>

<div class="concept-card">
<h4>4. <em>Switching Cost</em> Pelanggan</h4>
<p>Biaya—finansial, psikologis, atau operasional—yang ditanggung pelanggan jika berpindah ke pesaing. Contoh: nasabah bank dengan banyak <em>auto-debit</em>, gaji, dan kartu kredit di BCA menghadapi biaya tidak nyaman untuk pindah ke bank lain, meskipun fitur dasarnya setara.</p>
</div>

<div class="concept-card">
<h4>5. Skala Ekonomi &amp; Kurva Pengalaman</h4>
<p>Biaya per unit menurun seiring volume kumulatif. Contoh: Indofood dengan kapasitas mie instan terbesar di dunia menikmati biaya per bungkus yang sulit disamai pesaing regional manapun. Kombinasi skala manufaktur + jaringan distribusi adalah fondasi <em>cost leadership</em>-nya.</p>
</div>

### Hubungan dengan Minggu-Minggu Berikutnya

Mekanisme di atas akan dibongkar satu per satu: **VRIN (Minggu 4)** memberi alat analitis untuk menilai sumber daya; **Lima Strategi Generik (Minggu 5)** memberi pilihan cara mengeksploitasinya; **Supplementing Strategy (Minggu 6)** memberi cara memperkuatnya; dan **Eksekusi (Minggu 11)** memberi disiplin menjalankannya di lapangan.
```

- [ ] **Step 7.5: Write `05-mintzberg-deliberate-emergent.md`**

Path: `Dev Assistant/content/week-01/summary/05-mintzberg-deliberate-emergent.md`

```markdown
---
title: Mintzberg — Deliberate vs Emergent
order: 5
---

## Strategi Deliberate dan Emergent — Perspektif Mintzberg (Henry Ch.1)

Sementara TPGS dominan pada tradisi preskriptif (strategi sebagai pilihan yang sengaja), Henry mengangkat tradisi deskriptif yang dipelopori Henry Mintzberg. Gagasan inti: **strategi yang sebenarnya terealisasi (<em>realised strategy</em>) adalah jarang sama persis dengan strategi yang direncanakan (<em>intended strategy</em>)**.

<div class="framework">
<div class="framework-title">Kerangka Mintzberg — Realised Strategy</div>
<svg class="framework-svg" viewBox="0 0 620 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style><![CDATA[
      .mz-box { fill: #faf8f4; stroke: #1a1f3a; stroke-width: 1.2; }
      .mz-t { font-family: "Inter Tight", sans-serif; font-size: 12px; font-weight: 700; fill: #1a1f3a; }
      .mz-s { font-family: "Source Serif 4", serif; font-size: 10.5px; fill: #595959; }
      .mz-arrow { stroke: #1a1f3a; stroke-width: 1.5; fill: none; marker-end: url(#mzarrow); }
      .mz-em { stroke: #b08700; stroke-width: 1.8; stroke-dasharray: 5 3; fill: none; marker-end: url(#mzgold); }
    ]]></style>
    <marker id="mzarrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#1a1f3a"/>
    </marker>
    <marker id="mzgold" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#b08700"/>
    </marker>
  </defs>
  <rect x="15"  y="90" width="150" height="60" rx="6" class="mz-box"/>
  <text x="25"  y="115" class="mz-t">Intended Strategy</text>
  <text x="25"  y="132" class="mz-s">Rencana yang diniatkan</text>
  <rect x="225" y="20"  width="160" height="60" rx="6" class="mz-box"/>
  <text x="235" y="45"  class="mz-t">Deliberate Strategy</text>
  <text x="235" y="62"  class="mz-s">Niat yang terwujud</text>
  <rect x="225" y="160" width="160" height="60" rx="6" class="mz-box"/>
  <text x="235" y="185" class="mz-t">Unrealised Strategy</text>
  <text x="235" y="202" class="mz-s">Niat yang gagal</text>
  <rect x="225" y="90"  width="160" height="60" rx="6" class="mz-box" style="stroke:#b08700; stroke-dasharray: 5 3"/>
  <text x="235" y="115" class="mz-t" style="fill:#b08700">Emergent Strategy</text>
  <text x="235" y="132" class="mz-s">Muncul dari pembelajaran</text>
  <rect x="445" y="90"  width="155" height="60" rx="6" class="mz-box" style="stroke:#1a1f3a; stroke-width:2"/>
  <text x="455" y="115" class="mz-t">Realised Strategy</text>
  <text x="455" y="132" class="mz-s">Strategi aktual</text>
  <path d="M165 120 L225 50"   class="mz-arrow"/>
  <path d="M165 120 L225 190"  class="mz-arrow"/>
  <path d="M385 50  L445 110"  class="mz-arrow"/>
  <path d="M385 120 L445 120"  class="mz-em"/>
</svg>
</div>

**Tiga kategori dari kerangka Mintzberg:**

- **Deliberate strategy** — bagian dari rencana awal yang benar-benar diimplementasikan apa adanya.
- **Unrealised strategy** — bagian rencana yang gagal diwujudkan (karena pasar berubah, sumber daya terbatas, atau niat buruk).
- **Emergent strategy** — bagian dari strategi aktual yang **tidak direncanakan sebelumnya** tetapi muncul dari pembelajaran selama eksekusi.

<div class="pull-quote">
Strategy formation walks on two feet, one deliberate, the other emergent. Managing requires a light deft touch.
<cite>Henry Mintzberg — Academy of Management Journal</cite>
</div>

### Implikasi bagi Manajer Indonesia

GoTo adalah contoh hidup kerangka Mintzberg. Strategi yang diniatkan saat merger (2021): dominasi *super-app* Asia Tenggara. Strategi yang terwujud (<em>realised</em>): <em>path-to-profitability</em> dengan fokus di kota-kota tier-1 Indonesia. Bagian dari rencana awal—ekspansi agresif ke Vietnam, Thailand, Singapura—menjadi <em>unrealised</em>. Sementara itu, strategi <em>emergent</em> muncul: memperdalam financial services (GoPay, PayLater) sebagai lini margin tertinggi. Tiga komponen ini bersama-sama membentuk strategi GoTo yang kita amati pada 2024.
```

- [ ] **Step 7.6: Write `06-references-and-check.md`**

Path: `Dev Assistant/content/week-01/summary/06-references-and-check.md`

```markdown
---
title: Referensi + Pemeriksa Konsep
order: 6
---

## Pemeriksa Konsep — Minggu 1

<div class="callout check">
<div class="tt">Pemeriksa Konsep · Konsep Dasar</div>
<p><strong>K1.</strong> Dalam satu paragraf, jelaskan mengapa <em>operational effectiveness</em> bukan sinonim <em>strategy</em>. Berikan satu contoh perusahaan Indonesia yang hanya <em>operationally effective</em> tanpa strategi yang kuat.</p>

<p><strong>K2.</strong> Bank A memiliki jaringan cabang terbesar di Indonesia; Bank B memiliki teknologi digital terbaik; Bank C memiliki loyalitas nasabah tertinggi. Manakah yang paling mungkin memiliki <em>sustained competitive advantage</em>, dan mengapa? (Gunakan kerangka isolating mechanisms.)</p>

<p><strong>K3.</strong> Jika Anda adalah CEO startup Indonesia yang baru melakukan IPO, bagaimana Anda akan menjelaskan perbedaan <em>intended strategy</em> dan <em>realised strategy</em> kepada investor tanpa membuat mereka kehilangan kepercayaan?</p>
</div>

## Referensi (untuk pendalaman lebih lanjut)

<div class="citations">
<ol>
<li>Gamble, J. E., Peteraf, M. A., & Thompson, A. A. (2021). <em>Essentials of Strategic Management: The Quest for Competitive Advantage</em> (7th ed.). McGraw-Hill Education. <strong>Chapter 1.</strong></li>
<li>Henry, A. E. (2021). <em>Understanding Strategic Management</em> (4th ed.). Oxford University Press. <strong>Chapter 1.</strong></li>
<li>Porter, M. E. (1996). What is strategy? <em>Harvard Business Review</em>, 74(6), 61–78.</li>
<li>Mintzberg, H. (1987). The strategy concept I: Five Ps for strategy. <em>California Management Review</em>, 30(1), 11–24.</li>
<li>Mintzberg, H., & Waters, J. A. (1985). Of strategies, deliberate and emergent. <em>Strategic Management Journal</em>, 6(3), 257–272.</li>
<li>Rumelt, R. P. (2011). <em>Good Strategy/Bad Strategy: The Difference and Why It Matters</em>. Crown Business. (Tambahan untuk yang ingin pendalaman konseptual.)</li>
</ol>
</div>

## Catatan Akhir

> Minggu 1 adalah fondasi. Jika keempat konsep inti (strategi, model bisnis, keunggulan bersaing, deliberate/emergent) belum terasa kokoh, luangkan waktu untuk mengulang sebelum pindah ke Minggu 2. Semua minggu berikutnya akan merujuk kembali ke konsep-konsep ini — investasi waktu sekarang akan menghemat waktu sepanjang semester.
```

- [ ] **Step 7.7: Rebuild and verify**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik/Dev Assistant"
cargo run -- build --week 1
```

Expected: three `wrote ...` lines including Main Summary. Open in browser:

```bash
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Main Summary - Ebook\Week 01\index.html"
```

Expected: page with hero, lede, six distinct sections, two SVG framework diagrams (business model, Mintzberg), pull-quote with gold accent, Pemeriksa Konsep callout, reference list.

- [ ] **Step 7.8: Commit**

```bash
git add "Dev Assistant/content/week-01/summary/"
git commit -m "content(week-01): Main Summary — strategy, business models, advantage, Mintzberg, references"
```

---

## Task 8 — Week 1 Indonesian Company content

**Files:**
- Create: `Dev Assistant/content/week-01/indonesian/01-flagship-astra.md`
- Create: `Dev Assistant/content/week-01/indonesian/02-sidebar-unilever.md`
- Create: `Dev Assistant/content/week-01/indonesian/03-sidebar-indofood.md`
- Create: `Dev Assistant/content/week-01/indonesian/04-sources-and-verify.md`

- [ ] **Step 8.1: Write `01-flagship-astra.md`**

Path: `Dev Assistant/content/week-01/indonesian/01-flagship-astra.md`

```markdown
---
title: Flagship — Astra International
order: 1
---

## Astra International — Strategi Koheren dalam Konglomerat Terdiversifikasi

**Jangkar konsep:** koherensi strategis dalam portofolio unrelated-diversified; <em>corporate strategy as soft-control integration</em>; <em>sustained competitive advantage</em> di level grup.

Astra International (IDX: ASII) adalah contoh klasik perusahaan multibisnis Indonesia yang berhasil mempertahankan koherensi strategis di tengah diversifikasi portofolio yang sangat lebar. Didirikan tahun 1957, Astra kini beroperasi di **tujuh segmen bisnis** yang secara struktural relatif terpisah (otomotif, jasa keuangan, alat berat &amp; pertambangan, agribisnis, infrastruktur &amp; logistik, teknologi informasi, dan properti). Pertanyaan minggu ini: <em>bagaimana mungkin sebuah grup dengan portofolio sebaran seperti itu menghasilkan keunggulan bersaing yang tahan lama?</em>

<div class="case-box">
<div class="case-head">
<h3>Astra International — Snapshot Strategis</h3>
<span class="ticker">IDX: ASII · LQ45 · Member Astra Group</span>
</div>

<div class="data-row">
<div class="data-pt"><span class="n">7</span><span class="l">Segmen Bisnis</span><span class="src">Astra AR 2023, Segment Reporting</span></div>
<div class="data-pt"><span class="n">~Rp 316 T</span><span class="l">Pendapatan 2023</span><span class="src">Astra AR 2023, Laporan Keuangan Konsolidasian</span></div>
<div class="data-pt"><span class="n">67 tahun</span><span class="l">Usia Grup (sejak 1957)</span><span class="src">Astra Sustainability Report 2023</span></div>
</div>
</div>

### Jawaban Strategis: <em>Catur Dharma</em> sebagai Mekanisme Integrasi

Kunci koherensi Astra adalah **Catur Dharma** — empat pilar nilai yang dipakai sebagai instrumen manajemen lintas-segmen: "Menjadi milik yang bermanfaat bagi bangsa dan negara", "Memberikan pelayanan terbaik kepada pelanggan", "Menghargai individu dan membina kerja sama", dan "Senantiasa berusaha mencapai yang terbaik". Berbeda dengan konglomerasi era 1990-an yang runtuh karena <em>financial engineering</em>, Astra mengelola portofolio dengan <em>soft-control</em>: budaya, nilai, dan <em>management-by-system</em>, bukan sekadar <em>holding structure</em>.

### Penerapan Empat Konsep Inti Minggu 1

<div class="concept-card">
<h4>Strategi (pilihan sadar)</h4>
<p>Astra secara sadar memilih <strong>tidak masuk</strong> ke sektor telekomunikasi, media, atau ritel-konsumen massal — padahal semuanya menarik. Pilihan ini dimaksudkan untuk memelihara fokus pada sektor-sektor yang mendukung <em>core competencies</em>: <em>heavy engineering</em>, <em>large-scale financing</em>, dan <em>distributor network</em>. <em>Trade-off</em> ini adalah ciri strategi yang sesungguhnya.</p>
</div>

<div class="concept-card">
<h4>Model Bisnis (CVP &amp; Profit Formula)</h4>
<p>CVP di level grup: "mitra industri jangka panjang dengan skala nasional dan kemampuan eksekusi". Profit formula: portofolio segmen dengan profil siklus berbeda (otomotif siklikal, agribisnis komoditas, infrastruktur defensif) yang menghasilkan <em>earnings smoothing</em> dan ROIC agregat yang relatif stabil.</p>
</div>

<div class="concept-card">
<h4>Keunggulan Bersaing Berkelanjutan</h4>
<p>Dua <em>isolating mechanisms</em> yang sulit direplikasi: (1) <em>relationship capital</em> dengan prinsipal global (Toyota sejak 1971, Komatsu sejak 1974) yang terbentuk melalui dekade kerjasama, dan (2) <em>distribution &amp; service network</em> nasional yang mencapai titik-titik yang tidak dapat dilayani pesaing regional.</p>
</div>

<div class="concept-card">
<h4>Deliberate + Emergent</h4>
<p>Astra sengaja merencanakan diversifikasi ke infrastruktur (Astra Tol Nusantara) — <em>deliberate</em>. Namun pergeseran profil otomotif ke EV (kendaraan listrik) dan penyesuaian strategi Astra Otoparts adalah respons <em>emergent</em> terhadap perubahan regulasi global yang tidak direncanakan pada 2010-an.</p>
</div>
```

- [ ] **Step 8.2: Write `02-sidebar-unilever.md`**

Path: `Dev Assistant/content/week-01/indonesian/02-sidebar-unilever.md`

```markdown
---
title: Sidebar — Unilever Indonesia
order: 2
---

## Sidebar — Unilever Indonesia (UNVR): Strategi yang Fokus

Sebagai <em>comparative case</em>, Unilever Indonesia memberikan kontras menarik dengan Astra. Jika Astra menjadi contoh koherensi dalam diversifikasi lebar, Unilever Indonesia adalah contoh **kekuatan strategi fokus**. Fokus portofolio pada <em>home &amp; personal care</em> dan <em>foods</em> di pasar Indonesia memungkinkan investasi mendalam pada dua kapabilitas: (1) <em>brand-building</em> mass-market dengan distribusi warung-mikro, dan (2) <em>consumer insight</em> terhadap segmen B2C Indonesia yang heterogen.

Pilihan fokus ini adalah <em>trade-off</em>: Unilever Indonesia sengaja tidak masuk ke kategori konsumer di luar mandat grup Unilever global (misalnya tidak menggarap <em>cooking oil</em> — di mana Wilmar dan Sinar Mas dominan). Trade-off ini bukan kelemahan melainkan disiplin strategis: keunggulan bersaing Unilever adalah kombinasi <em>global brand equity</em> × <em>local execution capability</em>, dan fokus menjaga kapabilitas tersebut tetap tajam.

> **Catatan untuk diskusi kelas:** bagaimana dua perusahaan sama-sama di bursa IDX (ASII dan UNVR) dapat memiliki strategi yang begitu berbeda — satu terdiversifikasi ke tujuh segmen, satunya sangat fokus — namun keduanya menghasilkan ROIC tinggi dan tetap bertahan lebih dari lima dekade? Jawabannya: <em>koherensi internal</em>, bukan jenis strategi itu sendiri, yang menentukan keberlangsungan.
```

- [ ] **Step 8.3: Write `03-sidebar-indofood.md`**

Path: `Dev Assistant/content/week-01/indonesian/03-sidebar-indofood.md`

```markdown
---
title: Sidebar — Indofood
order: 3
---

## Sidebar — Indofood Sukses Makmur (INDF): Integrasi Vertikal sebagai Fondasi

Indofood menawarkan sudut pandang ketiga: strategi yang dibangun di atas **integrasi vertikal** lintas rantai nilai pangan. Dari hulu (Indofood Agri Resources memiliki perkebunan sawit, pabrik gula, dan peternakan) hingga hilir (Bogasari Flour Mills, Indofood CBP dengan merek Indomie, Sarimi, Chitato, Bimoli, dan distribusi ke 90+ negara).

Pilihan strategis Indofood: **tidak memilih antara cost leadership dan differentiation — keduanya dikombinasikan lewat integrasi vertikal**. Skala Bogasari (produsen tepung terigu terbesar dunia) memberi <em>cost advantage</em> pada Indofood CBP yang menggunakan bahan baku tersebut. Sementara merek Indomie menjadi <em>differentiated premium</em> dalam kategori mie instan di pasar ekspor (Nigeria, Arab Saudi, Eropa Timur). Integrasi vertikal adalah mekanisme isolasi yang sulit ditiru karena memerlukan kapital besar, waktu, dan kemampuan lintas-rantai.

> **Kontras dengan Astra dan Unilever:** ketiga perusahaan ini sama-sama memberi contoh <em>koherensi strategis</em>, tetapi mekanisme koherensinya berbeda: Astra via <em>soft-control culture</em>, Unilever Indonesia via <em>focused capability</em>, Indofood via <em>vertical integration</em>. Minggu 9 (Diversifikasi) akan mengembalikan kita ke perbedaan-perbedaan ini dengan alat analitis yang lebih formal.
```

- [ ] **Step 8.4: Write `04-sources-and-verify.md`**

Path: `Dev Assistant/content/week-01/indonesian/04-sources-and-verify.md`

```markdown
---
title: Sumber + Verifikasi
order: 4
---

## Sumber

<table class="src-table">
<thead><tr><th>Dokumen</th><th>Tahun</th><th>Bagian / Halaman</th><th>Relevansi</th></tr></thead>
<tbody>
<tr><td>Astra International Annual Report</td><td>2023</td><td>Segment Reporting; Laporan Keuangan Konsolidasian</td><td>Struktur 7 segmen + pendapatan konsolidasi</td></tr>
<tr><td>Astra International Sustainability Report</td><td>2023</td><td>Governance + Catur Dharma section</td><td>Filosofi manajemen dan mekanisme integrasi soft-control</td></tr>
<tr><td>IDX LQ45 Disclosure</td><td>2024</td><td>Member Fact Sheet</td><td>Status saham &amp; posisi kapitalisasi pasar</td></tr>
<tr><td>Unilever Indonesia Annual Report</td><td>2023</td><td>Business Review + Segment Performance</td><td>Portofolio merek &amp; distribusi</td></tr>
<tr><td>Indofood Sukses Makmur Annual Report</td><td>2023</td><td>Business Group overview</td><td>Empat grup bisnis &amp; integrasi vertikal</td></tr>
<tr><td>Indofood CBP Annual Report</td><td>2023</td><td>Noodles division</td><td>Ekspor Indomie ke 90+ negara</td></tr>
</tbody>
</table>

<div class="callout disclosure">
<div class="tt">Catatan Verifikasi</div>
<p>Data disarikan dari materi publik yang diungkapkan perusahaan Indonesia (AR, IDX, Sustainability Report, Investor Relations). Beberapa angka agregat (mis. usia grup, jumlah segmen) stabil antar periode pelaporan; angka finansial (pendapatan, laba) dapat berubah dari tahun ke tahun. Mahasiswa dianjurkan memverifikasi angka terkini dari <a href="https://www.idx.co.id">idx.co.id</a>, <a href="https://www.astra.co.id/ir">astra.co.id/ir</a>, <a href="https://www.unilever.co.id">unilever.co.id</a>, dan <a href="https://www.indofood.com">indofood.com</a> sebelum menggunakan dalam tugas/tesis.</p>
</div>
```

- [ ] **Step 8.5: Rebuild all Week 1 outputs**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik/Dev Assistant"
cargo run -- build --week 1
```

Expected: three `wrote ...` lines (Study Guide, Main Summary, Indonesian).

- [ ] **Step 8.6: Verify build passes**

```bash
cargo run -- verify
```

Expected output for Week 1: no MISSING lines for Week 01 entries. (Other weeks will show MISSING — that is expected because Phase I only fills Week 1.)

- [ ] **Step 8.7: Open the Indonesian page**

```bash
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Indonesian Company Examples\Week 01\index.html"
```

Expected: Astra case-box with 3 data points + gold accents, Unilever and Indofood sidebar sections, sources table, disclosure banner.

- [ ] **Step 8.8: Commit**

```bash
git add "Dev Assistant/content/week-01/indonesian/"
git commit -m "content(week-01): Indonesian Companies — Astra flagship + Unilever + Indofood sidebars"
```

---

## Task 9 — Print-to-PDF verification

**Files:**
- None (verification only)

- [ ] **Step 9.1: Open each of the three Week 1 outputs in browser**

```bash
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Study Guide - Aid\Week 01\index.html"
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Main Summary - Ebook\Week 01\index.html"
cmd.exe //c start "" "D:\DZAKI\S2\Sem. 1\Manajemen Strategik\course-materials\outputs\Indonesian Company Examples\Week 01\index.html"
```

- [ ] **Step 9.2: For each tab, press Ctrl+P (Print preview)**

Verify visually:
- Sidebar is hidden in print preview
- Hero background is neutral (no gradient on print)
- Running header shows "MST304 · Manajemen Strategik Kontemporer" top-left and section title top-right
- Running footer shows page "Halaman N dari M" bottom-right, "Dzaki — Magister Akuntansi STIE YKPN" bottom-left
- H2 sections start on new pages
- Case boxes, framework SVGs, callouts, and tables do not split across pages
- Pull quotes are not orphaned

- [ ] **Step 9.3: Save each as PDF (optional)**

Using Chrome/Edge Print dialog → "Save as PDF" → destination `course-materials/outputs/Master Print Bundle/week-01-*.pdf` (or anywhere the user prefers). These PDFs serve as evidence of print fidelity.

- [ ] **Step 9.4: If anything breaks across pages awkwardly, document the fix-list**

Create: `Dev Assistant/temp/phase-I-print-notes.md` with a short list of adjustments needed (e.g., "the 3-column data-row in case-box overflowed onto two pages on Chrome"). These notes feed into Phase VI QC refinement.

---

## Task 10 — Update memory + Phase I summary

**Files:**
- Modify: `C:\Users\HP\.claude\projects\D--DZAKI-S2-Sem--1-Manajemen-Strategik\memory\project_msk304.md`

- [ ] **Step 10.1: Update the project memory to record Phase I completion**

Path: `C:\Users\HP\.claude\projects\D--DZAKI-S2-Sem--1-Manajemen-Strategik\memory\project_msk304.md`

Replace the file contents with:

```markdown
---
name: Project — MST304 Course Support System (Phase I delivered 2026-04-16)
description: Graduate course support system for Manajemen Strategik Kontemporer (MST304), STIE YKPN. Phase I (Rust scaffolding + Visual Companion + Week 1 complete) delivered; Phases II–VI pending.
type: project
---
Building a complete course support system for **MST304 Manajemen Strategik Kontemporer**, 3 SKS, STIE YKPN Yogyakarta, Magister Akuntansi program, Semester II TA 2025/2026.

**Spec:** `docs/superpowers/specs/2026-04-16-msk304-design.md`
**Plan:** `docs/superpowers/plans/2026-04-16-msk304-phase-I-bootstrap.md`

**Status:**
- ✅ Phase 0 — Context review + spec (2026-04-16)
- ✅ Phase I — Bootstrap: Dev Assistant Rust crate compiles & tests pass; Visual Companion built; Week 1 (Study Guide + Main Summary + Indonesian) complete end-to-end and print-verified. (2026-04-16)
- ⏳ Phase II — W2–W4 (pre-UTS foundation)
- ⏳ Phase III — W5–W7 (UTS-ready)
- ⏳ Phase IV — W8–W11 (post-UTS)
- ⏳ Phase V — W12–W14 (UAS prep)
- ⏳ Phase VI — Master Print Bundle + QC

**Key technical decisions (locked):**
- Content authoring: YAML-frontmatter Markdown fragments under `Dev Assistant/content/week-NN/<section>/*.md`
- Build pipeline: Rust binary `dev-assistant` using `pulldown-cmark` + `minijinja`
- Design system: Editorial Scholar (Fraunces + Inter Tight + Source Serif 4, warm paper + indigo-night + scholarly gold)
- Output root: `course-materials/outputs/<Type>/Week NN/index.html`
- All Rust tooling inside `Dev Assistant/` folder (never pollutes project root)

**Anti-fabrication rule for Indonesian examples:** every data point cites document type (AR/IDX/OJK/IR/Sustainability Report); descriptive language where exact figures not defensible. Disclosure banner on every Indonesian page.

**Why:** Dzaki needs comprehensive weekly study materials to support deep graduate understanding, class presentations, UTS, and UAS. Rust pipeline makes regeneration cheap so late-semester refinements are painless.

**How to apply:** For Phase II onward, author Markdown fragments under `Dev Assistant/content/week-NN/`; run `cargo run -- build --week N` to regenerate a single week; run `cargo run -- build` for all weeks; `cargo run -- verify` to check outputs are present.
```

- [ ] **Step 10.2: Final commit**

```bash
cd "D:/DZAKI/S2/Sem. 1/Manajemen Strategik"
git add "docs/superpowers/plans/"
git commit -m "docs(plans): Phase I implementation plan"
```

---

## Self-Review (completed by plan author)

**1. Spec coverage:**
- §1 Purpose — ✔ Tasks 1–10 collectively produce the working Week 1 scaffolded by the spec
- §2 Inputs — ✔ All referenced in content/summary and week-mapping.toml
- §2.4 Syllabus↔TPGS mapping — ✔ encoded in week-mapping.toml
- §3.1 Gap handling — ✔ Week 12–14 have `tpgs_chapters = []` and `is_article_led = true`
- §3.2 Indonesian depth — ✔ flagship + sidebars per week in mapping; Week 1 content in Task 8
- §3.3 Visual style — ✔ screen.css + print.css lift every Editorial Scholar token
- §4 Architecture — ✔ Markdown-fragment + Rust shell builder via Tasks 1, 3, 5
- §5 Output anatomy — ✔ Study Guide, Main Summary, Indonesian templates via Task 4 + content via Tasks 6, 7, 8
- §6 Repository layout — ✔ matches the file table at top of this plan
- §7 Print strategy — ✔ print.css in Task 4.6 + verification in Task 9
- §8 Build phasing — ✔ Phase I scope explicit in plan header
- §9 Language — ✔ all Week 1 content is Indonesian-primary with English terms bracketed
- §10 QC — ✔ Task 9 does print verification; verify command in main.rs

**2. Placeholder scan:** none. Every code block complete; every file path explicit; no "TBD/TODO".

**3. Type consistency:** `Week`, `ArticleRef`, `Company` defined in Task 2.3, used consistently in Tasks 5.4, 5.5, and indirectly in all content files (via week-mapping.toml). `load_section` returns `Vec<Fragment>` (Task 3.11), consumed correctly in `compile_section_body` (Task 5.4). `render_section` signature consistent between test (Task 5.1) and implementation (Task 5.4).

No issues found.

---
