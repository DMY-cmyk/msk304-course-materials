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
