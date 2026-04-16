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
