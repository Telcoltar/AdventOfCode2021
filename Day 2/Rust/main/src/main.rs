use std::fs;

enum Direction {
    Forward,
    Down,
    Up
}

fn string_to_enum_direction(string_direction: &str) -> Direction {
    return match string_direction {
        "forward" => Direction::Forward,
        "down" => Direction::Down,
        "up" => Direction::Up,
        _ => Direction::Down
    }
}

fn get_input_data(filename: &str) -> Vec<(Direction, i32)> {
    let data = fs::read_to_string(filename).unwrap();
    let mut directions = vec![];
    for line in data.lines() {
        let split: Vec<&str> = line.split(" ").collect();
        directions.push((string_to_enum_direction(split[0]),
                         split[1].parse::<i32>().unwrap()))
    }
    return directions;
}

fn solution_part_1(directions: Vec<(Direction, i32)>) -> i32 {
    let mut current_pos = (0, 0);
    for (direction, value) in directions {
        match direction {
            Direction::Forward => current_pos.0 += value,
            Direction::Down => current_pos.1 += value,
            Direction::Up => current_pos.1 -= value
        }
    }
    println!("{:?}", current_pos);
    return current_pos.0 * current_pos.1
}

fn solution_part_2(directions: Vec<(Direction, i32)>) -> i32 {
    let mut current_status = (0, 0, 0);
    for (direction, value) in directions {
        match direction {
            Direction::Forward => {
                current_status.0 += value;
                current_status.1 += current_status.2 * value;
            },
            Direction::Down => current_status.2 += value,
            Direction::Up => current_status.2 -= value,
        }
    }

    return current_status.0 * current_status.1;
}

fn main() {
    println!("{:?}", solution_part_1(get_input_data("../../example.txt")));
    println!("{:?}", solution_part_1(get_input_data("../../input.txt")));
    println!("{:?}", solution_part_2(get_input_data("../../example.txt")));
    println!("{:?}", solution_part_2(get_input_data("../../input.txt")));
}
