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
