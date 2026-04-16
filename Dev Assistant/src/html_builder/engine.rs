use crate::error::Result;
use minijinja::{path_loader, Environment};

pub fn build_env(template_dir: &std::path::Path) -> Result<Environment<'static>> {
    let mut env = Environment::new();
    env.set_loader(path_loader(template_dir));
    Ok(env)
}
