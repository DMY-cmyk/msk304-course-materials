use dev_assistant::html_builder;
use dev_assistant::model::config::load_weeks;
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
