use std::fs;

fn solution_part_1(input_data: Vec<i32>) -> i32 {
    let mut current_num = input_data[0];
    let mut depth = 0;
    for num in &input_data[1..] {
        if current_num < *num {
            depth += 1;
        }
        current_num = *num;
    }
    return depth;
}

fn solution_part_2(input_data: Vec<i32>) -> i32 {
    let mut parsed = vec![];
    for i in 0..input_data.len() - 2 {
        parsed.push(input_data[i..i+3].iter().sum())
    }
    return solution_part_1(parsed);
}

fn get_input_data(filename: &str) -> Vec<i32> {
    let data = fs::read_to_string(filename).unwrap();
    let mut output = vec![];
    for line in data.lines() {
        output.push(line.parse().unwrap())
    }
    return output;
}

fn main() {
    println!("{}", solution_part_1(get_input_data("../../example.txt")));
    println!("{}", solution_part_1(get_input_data("../../input.txt")));
    println!("{}", solution_part_2(get_input_data("../../example.txt")));
    println!("{}", solution_part_2(get_input_data("../../input.txt")));
}
