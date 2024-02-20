# Github CI best practices

## 1. Set timeouts for each jobs

In order to prevent endless jobs that can be caused by misconfiguration,
deadlocks, etc.

## 2. Use actions with fixed versions

To improve stability & security of the pipeline

## 3. Use Github Secrets with limited scopes

It's obvious that secrets must not be exposed. Moreover, it's generally more
secure to use minimal required access rights as well

## 4. Trigger workflow only in case when files are changed in a specific path

Obviously, there is no need to re-run the workflow if somebody changes markdown
file in other folder (`app_java`) or something that does not affect project
functionality.

## 5. Job dependencies

Yet another obvious thing. In case, for example, tests are failed - there is no
need to push broken image onto Dockerhub. Let the workflow fail faster

## 6. Use caches

It's used for example, in `build_push` job in order to optimize future pipelines
