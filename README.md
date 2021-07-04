# league-ranking-application
A CLI application to calculate rank table on a given league data.

## Requirements

* docker
* docker-compose
  
## Getting Started

To clone this repository, run the following in a terminal.
```bash
git clone https://github.com/ShantanuFadnis/league-ranking-application.git
cd league-ranking-application
```

## Run Tests

This repository contains a Makefile that has few helper commands to run unit and linting tests.

Type the following to see the list of helper commands available.

```
make

bash-in-container              Execute bash in container
black                          Run black tests for the application
blacken                        Format codebase using black
build-image                    Build image for testing
clear                          Remove containers used in tests
lint-all                       Run all linter checks
mypy                           Run mypy tests for the application
pylint                         Run pylint tests for the application
run                            Run application
show-output                    Show output produced after running the application
test-all                       Run all tests
unittest                       Run unit tests for the application
```

### Run all tests together (unittests and linting tests)

This will first download the base python image from docker hub and then build on top of it.

```bash
make test-all
```

### Run unittests

Run python unittests.

```bash
make unittest
```

### Run linting tests

Run linting tests. This application makes use of the following linters - flake8, pylint, mypy, black.

```bash
make lint-all
```

### Run [flake8](https://flake8.pycqa.org/en/latest/)

```bash
make flake8
```

### Run [pylint](https://www.pylint.org/)

```bash
make pylint
```

### Run [black](https://black.readthedocs.io/en/stable/)

```bash
make black
```

### Run blacken (Format your code using black)

```bash
make blacken
```

### Run [mypy](http://mypy-lang.org/)

```bash
make mypy
```

## Run Application

This application accepts a path to a text file as input containing results of game, one per line. See [in.txt](data/in.txt) for details.

Note: The file must be present inside repository's root folder.

Output is produced as text file under `output` directory at root of this repository.

```bash
make run input=<input_file>
```

To see the output produced run the following

```bash
make show-output
```

**Example**:

Run application with `data/in.txt` as input:

```bash
make run input=data/in.txt
```

Check output:
```bash
make show-output
```

Output:

```
cat output/*.txt
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Tech Stack

* PySpark
* Python
* Docker

## Author

Shantanu Fadnis
