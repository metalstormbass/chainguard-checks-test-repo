# chainguard-checks-test-repo

A tiny greeting service used to exercise the reusable checks in
[metalstormbass/chainguard-checks](https://github.com/metalstormbass/chainguard-checks).

```sh
python -m greeter Ada            # Welcome, Ada!
python -m unittest discover -s tests
```

| Check | What it runs against |
| --- | --- |
| `codespell` | every file in the repository |
| `black` | `greeter/` and `tests/` |
| `json-yaml-validate` | `config/greeter.json` against `schemas/greeter.schema.json`, `config/deploy.yaml` against `schemas/deploy.schema.yaml` |
| `replace-tokens` | renders `deploy/greeter.json.tmpl`, then runs the service with the rendered config |
| `dagger` | runs the unit tests in a Chainguard Python container through the Dagger engine |

Each check is a stub from the library, copied into `.chainguard/ci/` and
pinned to a library commit.
