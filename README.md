# Continuous Integration using GitHub Actions

This repository uses GitHub Actions to automate the build, test, and notifying about the build status.

### Workflow Overview

The workflow is triggered on push or pull request events to the `main` branch. It performs the following steps:
1. Sets up a Python environment.
2. Installs dependencies.
3. Runs tests using `pytest`.
4. Sends notifications about the status of the build.