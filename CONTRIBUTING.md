# Contributing to HalfRand

Thank you for helping improve HalfRand. Bug reports, documentation fixes, tests, and
focused feature proposals are welcome.

## Development setup

1. Fork and clone the repository.
2. Create a virtual environment and install the project:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install --editable .
   ```

3. Run the checks:

   ```bash
   python -m unittest discover -s tests -v
   python -m build
   ```

## Making a change

- Open an issue before implementing a large or breaking change.
- Keep changes focused and preserve backward compatibility when practical.
- Use clear English names, comments, docstrings, commits, and documentation.
- Add tests for new behavior and update the README when public APIs change.
- Do not commit generated distributions, virtual environments, or secrets.

Write commit messages using [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/):

```text
<type>[optional scope]: <description>
```

Common types are `feat`, `fix`, `docs`, `test`, `build`, `ci`, `refactor`, and
`chore`. Use `!` and a `BREAKING CHANGE:` footer when a change is incompatible.
For example: `feat(generator): support bounded sequences`.

## Pull requests

Explain the problem and solution, link related issues, and list the checks you ran.
Maintainers may request changes. By contributing, you agree that your work is licensed
under the project's MIT License and that you will follow the Code of Conduct.

## Releasing

HalfRand follows Semantic Versioning. Before tagging a release:

1. Update the version in `pyproject.toml` and `src/halfrand/__init__.py`.
2. Move relevant changelog entries from **Unreleased** into a dated version section.
3. Run the complete test suite and build the distributions.
4. Merge the release commit into the default branch.
5. Create and push a signed tag matching the package version:

   ```bash
   git tag -s v0.1.0 -m "Release v0.1.0"
   git push origin v0.1.0
   ```

The release workflow verifies that the tag and package versions match, builds and checks
the distributions, publishes them to PyPI through Trusted Publishing, and creates a
GitHub Release. Configure a PyPI Trusted Publisher for this repository and the `release`
GitHub environment before pushing the first release tag.
