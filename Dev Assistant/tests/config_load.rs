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
