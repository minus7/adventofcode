use std::path::Path;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
	let f = File::open(Path::new("input")).unwrap();
	let reader = BufReader::new(&f);
	for line in reader.lines() {
		let s = line.unwrap();
		println!("> {}", s);
		let parts: Vec<&str> = s.split(" -> ").collect();
		
	}
}
