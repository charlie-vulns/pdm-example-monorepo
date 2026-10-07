# PDM Monorepo Example

This is an example of a monorepo managed by [PDM](https://pdm.fming.dev).

## Sub Packages

- `packages/pkg-core`
- `packages/pkg-first`
- `packages/pkg-second`


## Note about `pdm install`


If you change the dependencies in one of the subprojects, the `pdm install` command will not detect that the lock file needs to be re-generated.

You will thus have to run `pdm lock` manually, before running `pdm install`. 

Alternatively, you may for example run `pdm update pkg-first`, if you modified the depedencies of the `pkg-first` sub-project.

## Monorepo code scanning demo

The project map in [`.github/codeql-projects.json`](.github/codeql-projects.json) scans
the three Python packages separately with CodeQL. `pkg-first` and `pkg-second`
include `pkg-core` in their scans because both depend on it. A pull request
changing Python code in `pkg-first` scans only `first`; a change to `pkg-core`
scans all three projects.

The [PR workflow](.github/workflows/codeql-monorepo-pr.yml) scans changed
projects and republishes results for unchanged projects. Before trying that
demo, switch CodeQL from default setup to advanced setup in the repository
settings, then run the [full scan workflow](.github/workflows/codeql-monorepo-full.yml)
on `main` once to establish a result for each project. Run the full scan again
when changing shared top-level configuration, which does not trigger a
project-specific PR scan.
