# Pyrelvis

Pyrelvis is a simple Python library for visualizing binary relations.

![Example Image3](https://raw.githubusercontent.com/RobinSeidel/pyrelvis/main/docs/img/example3.svg)


## Installation

Pyrelvis depends on [Pycairo](https://github.com/pygobject/pycairo)


Installing Pycairo requires pkg-config and cairo including its headers.

	Ubuntu/Debian: sudo apt install libcairo2-dev pkg-config python3-dev

	macOS/Homebrew: brew install cairo pkg-config

	Arch Linux: sudo pacman -S cairo pkgconf

	Fedora: sudo dnf install cairo-devel pkg-config python3-devel

	openSUSE: sudo zypper install cairo-devel pkg-config python3-devel

After that use pip to install pyrelvis

	pip install pyrelvis 

## Usage

```python
# Simple

from pyrelvis import rel_to_svg

path = "out.svg"

# Relations are expressed as sets of tuples
relation = {(1,2), (2,4), (1,1), (3,2)}

# At least min_nodes nodes are displayed
rel_to_svg(path, relation, min_nodes=4)
```

```python
# With custom configuration

from pyrelvis import RelationPresenter

path = "out.svg"
relation = {(1,2), (2,4), (1,1), (3,2)}

presenter = RelationPresenter(
		path,
		width=700,
		radius=280,
		font_size=28,
		line_width=2,
		arrow_angle=160,
		arrow_length=20
		)

# At least min_nodes are displayed
presenter.print(relation, min_nodes=4)
presenter.close()
```

## Example Output

Using standard settings

![Example Image1](https://raw.githubusercontent.com/RobinSeidel/pyrelvis/main/docs/img/example1.svg)

Using custom settings

![Example Image2](https://raw.githubusercontent.com/RobinSeidel/pyrelvis/main/docs/img/example2.svg)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
