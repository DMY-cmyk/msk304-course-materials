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
        "article"     => "week-article.html.j2",
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
        "article" => (
            format!("Analisis Artikel — {}", week.topic_id),
            format!("Kajian mendalam atas artikel empiris minggu ini: pertanyaan riset, metode, temuan, kontribusi teoretis, kritik, dan hubungannya dengan bab TPGS/Henry."),
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
