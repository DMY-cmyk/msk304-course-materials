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
    /// Build Master Print Bundle — single-file all-14-weeks course-companion.html (PDF-ready)
    Bundle,
}

const SECTIONS: &[(&str, &str, &str)] = &[
    ("study_guide", "Study Guide - Aid",            "Study Guide / Aid"),
    ("summary",     "Main Summary - Ebook",         "Main Summary / Ebook"),
    ("article",     "Articles",                     "Analisis Artikel Jurnal"),
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
        Command::Bundle => {
            let weeks = load_weeks(&PathBuf::from("configs/week-mapping.toml"))?;
            let out = html_builder::build_master_bundle(&weeks, &content_root, &output_root)?;
            println!("wrote {}", out.display());
            println!("bundle complete.");
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
