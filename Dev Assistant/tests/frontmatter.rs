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
