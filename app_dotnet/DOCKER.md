## Docker Best Practices

### Using non-root user

As recommended in [Docker Security Best Practices](https://sysdig.com/blog/dockerfile-best-practices/), there is a new user created in the docker image, and no root user is used there for extra security.

### Layer sanity

Copying and installing requirements is a process that can be easily cached. Thus, it is isolated from the other commands.

### Specific version of dotnet is used

More precisely, dotnet/aspnet:8.0 is being used in the image.

### Explicit copies

Each directory is copied explictly with no wildcards.

### Multiple stage docker build